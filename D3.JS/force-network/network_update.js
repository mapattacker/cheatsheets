// network graph with update of new data feature
// include a barchart to show top 5 connections
// search box to show name of person in the network
// label of top 5



//Variables to set up SVG container
var width = ($(window).width()-40)/4 * 3 - 80,
    height = $(window).height()-80,
    radius = 20; // specify radius of node so that it won't be truncated at the border of bounding box
    

//We initialise the force layout object here
var force = d3.layout.force()
    .size([width, height])
    .charge(-200)
    .linkDistance(30)
    .gravity(0.1)
    .on("tick", tick);

// create svg element for force-directed graph
var svg = d3.select("#network").append("svg")
            .attr("width", width)
            .attr("height", height);

// barchart
var barwidth = 235,
    barHeight = 40,
    x = d3.scale.linear().range([0, barwidth]),
    chart = d3.select(".chart")
              .attr("barwidth", barwidth);



//Create a "g" container elements and create selections to reference throughout
var link = svg.append("g").selectAll(".link");
var node = svg.append("g").selectAll(".node");

// set colors to N categorical colors
var fill = d3.scale.category20();

// Define the div for the tooltip
var div = d3.select("body").append("div")	
            .attr("class", "tooltip")				
            .style("opacity", 0);


// update new links
var update = function(){

    // top N connections ------------------------------------------------------
    // filter the top N results by connection
    // var topNnodes = JSON.parse(JSON.stringify(graphData.nodes))
    //                     .sort( function(a, b) { return b.connect - a.connect; })
    //                     // .slice(0, 5)
    //                     // .map(n => n.id);
    
    // if (topNnodes.slice(4,5)[0].connect != topNnodes.slice(5,6)[0].connect ) {
    //     var last = 5;
    // } else if (topNnodes.slice(4,5)[0].connect != topNnodes.slice(6,7)[0].connect ) {
    //     var last = 6;
    // } else if (topNnodes.slice(4,5)[0].connect != topNnodes.slice(7,8)[0].connect ) {
    //     var last = 7;
    // } else if (topNnodes.slice(4,5)[0].connect != topNnodes.slice(8,9)[0].connect ) {
    //     var last = 8;
    // } else if (topNnodes.slice(4,5)[0].connect != topNnodes.slice(9,10)[0].connect ) {
    //     var last = 9;
    // }

    // var topNnodes = topNnodes.slice(0, last)
    //                          .map(n => n.id)

    // or if need to sort by connection & earliest time instead, use this: 
    // https://stackoverflow.com/questions/6129952/javascript-sort-array-by-two-fields
    topNnodes = JSON.parse(JSON.stringify(graphData.nodes))
                    .sort((a, b) => b.connect - a.connect || a.time - b.time)
                    .slice(0, 5)
                    .map(n => n.id);
    // console.log(topNnodes)

    topNnodes2 = JSON.parse(JSON.stringify(graphData.nodes))
                    .sort((a, b) => b.connect - a.connect || a.time - b.time)
                    .slice(0, 5);

    // CREATE TOP N LISTING ------------------------------------------------------
    
    // toplist = d3.select("#topN").selectAll('div').data(topNnodes2)
    // toplist.enter()
    //         .append("div")
    //         .text(function(a, i){return (i+1) + ". " + a.name + " (" + a.connect + ")"})


    // BARCHART ------------------------------------------------------
    x.domain([0, d3.max(topNnodes2, function(d) { return d.connect; })]);

    chart.attr("height", barHeight * topNnodes2.length);

    bar = chart.selectAll("g")
        .data(topNnodes2)
        .enter().append("g")
        
    // transition: https://codepen.io/netkuy/pen/KzPaBe
    bar.append("rect")
        .attr("width", function(d) { return x(d.connect); })
        .attr("height", barHeight - 1)
        .transition()
        .duration(500)
        .ease("quad")
            .attr("transform", function(d, i) { return "translate(0," + i * barHeight + ")"; });
        

    bar.append("text")
        .attr("x", function(d) { return x(d.connect) - 10; })
        .attr("y", barHeight / 2)
        .attr("dy", ".35em")
        .text(function(d) { return d.name +  " (" + d.connect + ")"; })
        .transition()
        .duration(500)
        .ease("quad")
            .attr("transform", function(d, i) { return "translate(0," + i * barHeight + ")"; });
            


    // CREATE LINK ------------------------------------------------------
    //Create an UPDATE selection by joining data with "link" element selection
    link = link.data(graphData.links);

    link.enter().append("line")
        .attr("class", "link");

    link.exit().remove();


    // CREATE NODE ------------------------------------------------------
    //same update pattern for nodes
    node = node.data(graphData.nodes) // bind nodes data
            
    // APPEND CIRCLE TAG WITHIN "G" TAG
    node.enter().append("circle") // create svg tag called circle
        .attr("class", "node")
        // circle fill & border
        .style("fill", function(d) { return fill(d.company); })
        // .style("stroke", function(d) { return d3.rgb(fill(d.company)).darker(); })
        // circle size
        .attr("r", function(d) { return nodefixed(d.connect)*3; })
        // expand circle when hover over
        .on("mouseenter", mouseover)
        .on("mouseleave", mouseout)
        // popup label
        .on("mouseover", function(d) {
            div.transition()
                .duration(200)
                .style("opacity", 1);
            div.html(d.name + ' (' + d.connect + ')' + '<span style="text-transform: uppercase; font-size: 14px;"><strong>'
                        + '<br>'
                        + d.company + '</strong></span>')
                .style("left", (d3.event.pageX + 40) + "px")
                .style("top", (d3.event.pageY - 28) + "px");
            })					
        .on("mouseout", function(d) {
            div.transition()		
               .duration(500)		
               .style("opacity", 0);	
        })

    node.call(force.drag);
    node.exit().remove();



    // CREATE LABEL ------------------------------------------------------
    label = svg.append("g").selectAll(".label");
    label = label.data(graphData.nodes)

    // // cannot chain with previous or 
    // // exit-remove will not be able to work
    // // adding new nodes will not work too
    label.enter().append("text")
         .attr("class", "labels")
         .style("font-size", function(d){return fontsize(nodefixed(d.connect)) + "px"})
         .attr("dx", function(d){return adjustleft(fontsize(nodefixed(d.connect)))})
         .attr("dy", ".35em")
         .text(function(d) {  // only label topN, else empty label
            console.log(d.name)
            if ($.inArray(d.id, topNnodes) > -1){
                    return $.inArray(d.id, topNnodes) + 1} // label by ranking
         })

    label.exit().remove();
    force.start();


    // RESET ALPHA ------------------------------------------------------
    setInterval(function(){force.resume();}, 100);


    // JQUERY AUTOCOMPLETE SEARCHBOX ------------------------------------------------------
    var optArray = [];
    for (var i = 0; i < graphData.nodes.length; i++) {
        optArray.push(graphData.nodes[i].name);
    }
    optArray = optArray.sort();
    // send array to search id-tag using JQuery autocomplete
    $(function () {
        $("#search").autocomplete({
            source: optArray
        });
    });
};



// RENDER XY  ------------------------------------------------------
function tick() {
    link.attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });

    // transform-translate is essential for bounding labels
    // node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

    // code to keep within svg bounding box
    node.attr("cx", function(d) { return d.x = Math.max(radius, Math.min(width - radius, d.x)); })
        .attr("cy", function(d) { return d.y = Math.max(radius, Math.min(height - radius, d.y)); });

    label.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });
}
    

// add random parameter to json file to force refresh cached json
nocache_init = 'miserables.json?nocache=' + (new Date()).getTime();

// INPUT INITIAL JSON ------------------------------------------------------
d3.json(nocache_init, function(error, json){
    if (error) throw error;

    // get the latest time for most recent update
    latesttime = d3.max(json.nodes, function(d){return d.time})

    // using id as source-target instead of array sequential count ---------------------------
    // basically have to rebuild the link json from string into numerical arrays
    edges = [];
    json.links.forEach(function(e) { // iterate each link
        // filter node array that matches with link target & source names
        var sourceNode = json.nodes.filter(function(n) { //
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
    
    graphData = json;
    graphData.links = edges

    drag = force.drag()

    force.links(graphData.links);
    force.nodes(graphData.nodes);

    update()

})


// UPDATE NETWORK GRAPH BASED ON LATEST TIME ------------------------------------------------------
// https://stackoverflow.com/questions/9539294/adding-new-nodes-to-force-directed-layout
// https://stackoverflow.com/questions/46467114/d3-v3-force-layout-gracefully-add-remove-nodes-without-refresh
// intervalupdate = function(){

d3.select("#update1").on("click", function() {

    // add random parameter to json file to force refresh cached json
    nocache_update = 'update.json?nocache=' + (new Date()).getTime();
    console.log(nocache_update)

    d3.json(nocache_update, function(error, update2){
        if (error) throw error;

        // extract only updated nodes based on last updated time
        update2.nodesize = update2.nodes.filter(function(d){
                                if (d.time > latesttime & d.node_update == 1){
                                    return d;
                                }
                            })
        // extract only new nodes based on last updated time
        update2.nodes = update2.nodes.filter(function(d){
                                if (d.time > latesttime & d.node_update != 1){
                                    return d;
                                }
                            })
        // extract only updated links based on last updated time
        update2.links = update2.links.filter(function(d){
                                if (d.time > latesttime){
                                    return d;
                                }
                            })

        // concat to initial dataset so can do link matching
        // not required later as it will be a single json
        nodesall = graphData.nodes.concat(update2.nodes) 
        
        edges2 = [];
        update2.links.forEach(function(e) {
            var sourceNode = nodesall.filter(function(n) {
                    return n.id === e.source;
                    })[0],
                targetNode = nodesall.filter(function(n) {
                    return n.id === e.target;
                    })[0];
                edges2.push({
                    source: sourceNode,
                    target: targetNode,
                    value: e.value
                });
            });
        
        // have to iterate or it will prompt datatype error
        // update new nodes
        update2.nodes.forEach(function(i){
            graphData.nodes.push(i);
        })
        // update new links
        edges2.forEach(function(i){
            graphData.links.push(i);
        })
        // replace node size in graphData array
        graphData.nodes.forEach(function(i){
            update2.nodesize.forEach(function(ii){
                if (i.id == ii.id){
                    i.connect = ii.connect
                }
            })
        })
        // update node size
        update2.nodesize.forEach(function(i){
            var selectedVal = i.id
            // select all tags with node class
            var node = svg.selectAll(".node");
            // identify the circle with node size needed to be updated
            var selected = node.filter(function (d, i) {
                return d.id == selectedVal;
                });
            // update the new size
            selected.attr("r", function(d) { return nodefixed(i.connect)*3; })
        })

        // remove labels & barcharts so that latest can be updated
        label.remove();
        bar.remove();


        update()


        // replace the latest time for most recent update
        latesttime = d3.max(update2.nodes, function(d){return d.time})
    })
});
// };

// SEARCH RESULT TRANSITION ------------------------------------------------------
// animation effects after entering search button
function searchNode() {
    //get node name from search box
    var selectedVal = document.getElementById('search').value;

    // select all tags with node class
    var node = svg.selectAll(".node");

    if (selectedVal == "none") {
        node.style("stroke", "white").style("stroke-width", "1");
        } 
    // if selection > 0, return all node names NOT same as selection name
    else {
        var selected = node.filter(function (d, i) {
            return d.name != selectedVal;
            });

        // change unselected to opacity to 0
        selected.style("opacity", "0")

        // get the link tag and change unselected opacity to 0 too
        var link = svg.selectAll(".link")
        link.style("opacity", "0");
        // get the text tag and change unselected opacity to 0 too
        var label = svg.selectAll("text")
        label.style("opacity", "0");
        
        // transition back to full opaque
        d3.selectAll(".node, .link, text").transition()
            .duration(3000)
            .style("opacity", 1)
    }
}


// N SECONDS RELOAD TO UPDATE NETWORK GRAPH
// https://stackoverflow.com/questions/8779845/javascript-setinterval-not-working
// will only capture changed data
// setInterval("intervalupdate()", 20000);



// dynamic node size label ranking
// 15: -3, 20: -5, 25: -7, 30: 
function fontsize(connection){
    if (connection < 5){
        return "15"
    } else if (connection < 10) {
        return "20"
    } else if (connection < 20) {
        return "25"
    } else if (connection >= 20) {
        return "30"
    }
}

// need to fixed node size so that it won't get too big
// and cover whole screen
function nodefixed(size){
    if (size == 1){
        return 1
    } else if (size < 5){
        return 2
    } else if (size < 10){
        return 3
    } else if (size < 15){
        return 4
    } else if (size < 20){
        return 5
    } else if (size < 30){
        return 6
    } else if (size < 40){
        return 7
    } else if (size >= 40){
        return 8
    }
}

// dynamic node y coordinate adjustment of node label
function adjustleft(fsize){
    if (fsize == "15"){
        return -4
    } else if (fsize == "20"){
        return -5
    } else if (fsize == "25"){
        return -7
    } else if (fsize == "30"){
        return -8
    }
}

function topN(top5nodes){
    JSON.parse(JSON.stringify(top5nodes))
        .sort((a, b) => b.connect - a.connect || a.time - b.time)
        .slice(0, 5)
        .map(n => n.id);
}

// EXPAND CIRCLE ------------------------------------------------------
function mouseover() {
    d3.select(this)
        .transition()
        .duration(750)
        .attr("r", 30);
    };

// reduce circle back to original on mouseout
function mouseout() {
    d3.select(this)
        .transition()
        .duration(750)
        // issue, size return to initial size
        .attr("r", function(d) { return nodefixed(d.connect)*3; });
    };