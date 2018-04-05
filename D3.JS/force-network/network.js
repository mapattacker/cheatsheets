
// define initial variables
var width = $(window).width()-40,
    height = $(window).height()-80,
    radius = 10;

// put SVG canvas into DOM tag
var svg = d3.select("#network").append("svg")
    .attr("width", width)
    .attr("height", height);

// main force script
var force = d3.layout.force()
    // .gravity(.05)
    .charge(-240) // repel-attract strength
    .linkDistance(50)
    .size([width, height]);

// set colors to 20 categorical colors
var fill = d3.scale.category10();

// Define the div for the tooltipvar arr = new Array();

var div = d3.select("#network").append("div")	
    .attr("class", "tooltip")				
    .style("opacity", 0);


// main script to define nodes & lines
d3.json("miserables.json", function(error, json) {
    if (error) throw error;
    
    // for using id as source-target instead of array sequential count
    // basically have to rebuild the link json from string into numerical arrays
    var edges = [];
    json.links.forEach(function(e) {
        var sourceNode = json.nodes.filter(function(n) {
            return n.id === e.source;
            })[0],
            targetNode = json.nodes.filter(function(n) {
                return n.id === e.target;
            })[0];

        edges.push({
            source: sourceNode,
            target: targetNode,
            value: e.value
        });
    });
    console.log(edges);

    // top N connections
    // note for duplicates
    // filter the top N results by connection
    var topNnodes = JSON.parse(JSON.stringify(json.nodes))
                        .sort( function(a, b) { return b.connect - a.connect; })
                        .slice(0, 5)
                        .map(n => n.name);
    // add a new Boolean key called topN to filter on when calling labels
    json.nodes = json.nodes.map(function(d) {
                    if (topNnodes.indexOf(d.name) > -1) d.topN = true;
                        return d;
                    });
    // print top N names
    // document.getElementById('topN').innerText = topNnodes;

    // main force script
    force
        .nodes(json.nodes)
        .links(edges) // replace json.links into edges for id linkage
        .start() // cooling parameter alpha will slowly decrease to zero
    
    // reset alpha every 0.1 sec so that it will not decay to zero
    // continuous drift, force.resume same as force.alpha(0.1)
    // setInterval(function(){force.resume();}, 100);


    // define links from data source
    var link = svg.append("g").selectAll(".link")
        .data(edges)
        .enter().append("line")
        .attr("class", "link"); // css class

    // define node from data source
    // group "g" all nodes tog else new nodes will appear below links?
    var node = svg.append("g").selectAll(".node")
        .data(json.nodes)
        .enter().append("g")
        .attr("class", "node") // css class
        .on("mouseover", mouseover) // expand circle
        .on("mouseout", mouseout)
        .call(force.drag); // force drag node

    // console.log(node.on("mouseout", mouseout))
    
    // add circle to each node
    node.append("circle")
        .attr("r", function(d) { return d.connect*3; }) // node size
        .style("fill", function(d) { return fill(d.company); })
        .style("stroke", function(d) { return d3.rgb(fill(d.company)).darker(); })
        // hover-over tooltip
        .on("mouseover", function(d) {		
            div.transition()		
                .duration(200)		
                .style("opacity", 1);		
            div.html(d.name + ' ' + '<span style="text-transform: uppercase; font-style: italic;"><strong>' 
                        +d.company + '</strong></span>')	
                .style("left", (d3.event.pageX + 40) + "px")		
                .style("top", (d3.event.pageY - 28) + "px");	
            })					
        .on("mouseout", function(d) {		
            div.transition()		
                .duration(500)		
                .style("opacity", 0);	
        });

    // label halo top 10
    // node.filter( function(d) { return d.topN; }).append("text")
    //     .attr("dx", -20)
    //     .attr("dy", ".35em")
    //     .attr("class", "shadow")
    //     .text(function(d) { return d.name });

    // label top 10
    node.filter( function(d) { return d.topN; }).append("text")
        .attr("dx", -20)
        .attr("dy", ".35em")
        .text(function(d) { return d.name });

    // draw circle & lines coordinates
    // allows force.drag function
    force.on("tick", function() {

        link.attr("x1", function(d) { return d.source.x; })
            .attr("y1", function(d) { return d.source.y; })
            .attr("x2", function(d) { return d.target.x; })
            .attr("y2", function(d) { return d.target.y; });

        node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });
        
        // code to keep within svg bounding box
        node.attr("cx", function(d) { return d.x = Math.max(radius, Math.min(width - radius, d.x)); })
            .attr("cy", function(d) { return d.y = Math.max(radius, Math.min(height - radius, d.y)); });

    });


    // expand circle
    function mouseover() {
        d3.select(this).select("circle").transition()
            .duration(750)
            .attr("r", 30);
        }
    // reduce circle back to original on mouseout
    function mouseout() {
        d3.select(this).select("circle").transition()
            .duration(750)
            .attr("r", function(d) { return d.connect*3; });
        }

    // generate array for all names in search box
    var optArray = [];
    for (var i = 0; i < json.nodes.length; i++) {
        optArray.push(json.nodes[i].name);
    }
    optArray = optArray.sort();
    // send array to search id-tag using JQuery autocomplete
    $(function () {
        $("#search").autocomplete({
            source: optArray
        });
    });
    console.log(optArray);
});

// grab search result
// animation effects after entering search button
function searchNode() {
    //find the node
    var selectedVal = document.getElementById('search').value;
    var node = svg.selectAll(".node");
    if (selectedVal == "none") {
        node.style("stroke", "white").style("stroke-width", "1");
    } else {
        var selected = node.filter(function (d, i) {
            return d.name != selectedVal;
        });
    selecteatyle("opacity", 1);
    }
}

