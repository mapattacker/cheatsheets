// New version from network_update
// using canvas instead of svg to improve the loading speed


// define variables
// random min & max for video recording
min1 = 2
max1 = 4

// figure out network graph bootstrap grid size width
if ($(window).width() < 768) {
    width = 768/4*3 // recalculated based on bootstrap 3/4 sizing of network graph
}
else if ($(window).width() >= 768 &&  $(window).width() <= 992) {
    width = 768/4*3
}
else if ($(window).width() > 992 &&  $(window).width() <= 1200) {
    width = 992/4*3
}
else  {
    width = 1200/4*3
}


var width = width-50, 
    height = $(window).height()-200,


// add random parameter to json file to force refresh cached json
nocache_init = 'mongo.json?nocache=' + (new Date()).getTime();


var canvas = d3.select("#network").append("canvas")
                .attr("width", width)
                .attr("height", height);

var context = canvas.node().getContext("2d");


// refresh to get new json file
window.onload = function(){
    $.ajax({
        url: '/cmongo',
        type: 'POST',
        processData: false,
        contentType: 'application/json',
        data: JSON.stringify(
        {
            "Password": "$imda",
        }),
        dataType: 'json',

        success: function (res) {
        console.log(res)
        // add random parameter to json file to force refresh cached json
        },
        error: function (err) {
        console.log('Error:', err)
        }
    })
}

// delay to allow ajax to communicate to node.js to send new mongo.json file
sleep(100)


// get total nodes in json for dynamic forcelayout of gravity and charge adjustments
var nodecount;
$.ajax({
    dataType: "json",
    url: nocache_init,
    async: false,
    success: function(data){
        nodecount = data[0].nodes.length
        linkcount = data[0].links.length
    }
})
console.log("total nodes: " + nodecount + ", total links: " + linkcount)


//initialise the force layout object here
var force = d3.layout.force()
    .size([width, height])
    .charge(chargeadjust(nodecount))
    // .charge(-25)
    .linkDistance(30)
    .linkStrength(linksadjust(linkcount))
    .gravity(gravityadjust(nodecount))
    .on("tick", tick);

// set node fill & border colors, and font sizes
// var top5fill = d3.rgb(173, 211, 35); // legacy fill
// var top5fill = d3.rgb(144, 95, 171); // purple fill
// var top5fill = d3.rgb(0, 139, 41); // wee siong fill
var top5fill = d3.rgb(0, 75, 22); 
var top5stroke = d3.rgb(0, 0, 0);
var othersfill = d3.rgb(150, 150, 150);
var othersstroke = d3.rgb(50, 50, 50);
var linkcolor = d3.rgb(95, 95, 95);
var font = 15;



// update function for resizing nodes
var update = function(){
    // console.log(graphData)

    // calculate max token size, for dynamic node size -----------------------
    maxsize = max(graphData[0].nodes)
    minsize = min(graphData[0].nodes)
    maxtopn = maxtopN(graphData[0].nodes)
    mintopn = mintopN(graphData[0].nodes)
    // calculate max links, for dynamic link thickness -----------------------
    maxlink = graphData[0].links.length
    // console.log("minsize: " + minsize)
    // console.log("maxsize: " + maxsize)
    // console.log("maxtopN: " + maxtopn)
    // console.log("mintopN: " + mintopn)
    // console.log("maxlink: " + maxlink)
    // console.log("link thickness: " + linksizing(maxlink))


    // update token counter
    countdown = 8000 - maxtokens(graphData[0].nodes)
    // if tokens ever hit less than 0, stay at 0
    if (countdown < 0){
        countdown = '0'
    } else {countdown = (countdown).toString()}


    if (countdown.length == 3){
        countdown = '0' + countdown
    } else if (countdown.length == 2){
        countdown = '00' + countdown
    } else if (countdown.length == 1){
        countdown = '000' + countdown
    } else countdown
    document.getElementById('one').innerHTML = countdown


    force.nodes(graphData[0].nodes);
    force.links(graphData[0].links);

    // update node & link counts for charge, linkstrength & gravity
    nodecount = graphData[0].nodes.length
    linkcount = graphData[0].links.length

    // console.log('nodecount: ' + nodecount)
    // console.log('linkcount: ' + linkcount)

    // RESET ALPHA FOR CONTINUOUS DRIFT -----------------------------------
    // setInterval(function(){force.resume();}, 5000);
    setInterval(function(){force.alpha(0.4);}, 40);

    // console.log(graphData[0].nodes)
    // console.log(graphData[0].links)

}


// initial json
d3.json(nocache_init, function(error, json) {
  if (error) throw error;


  // get the latest time for most recent update
  context.font="bold 14px Arial";
  latestnodetime = d3.max(json[0].nodes, function(d){return d.nodeUpdatetime})
  latestlinktime = d3.max(json[0].links, function(d){return d.timestamp})

//   console.log(latestnodetime)

  // using id as source-target instead of array sequential count ---------------------------
  // basically have to rebuild the link json from string into numerical arrays
  edges = [];
  json[0].links.forEach(function(e) { // iterate each link
      // filter node array that matches with link target & source names
      var sourceNode = json[0].nodes.filter(function(n) { //
          return n.emailid === e.source;
          })[0],
          targetNode = json[0].nodes.filter(function(n) {
              return n.emailid === e.target;
          })[0];
      edges.push({
          source: sourceNode,
          target: targetNode,
          value: e.value
      });
  });
  
  graphData = json;
  graphData[0].links = edges

  update()

  force.start();

  // store previous topn nodes
  storetopn = graphData[0].nodes.filter(function(d){
      if (d.topn != null){
          return d
      }
  })
  barchart(storetopn)

});


// tick function
function tick() {
    // clear screen so can repopulate canvas again for each loop
    context.clearRect(0, 0, width, height);


    // draw links
    context.strokeStyle = linkcolor
    context.beginPath();
    graphData[0].links.forEach(function(d) {
      context.moveTo(d.source.x, d.source.y);
      context.lineTo(d.target.x, d.target.y);
    });
    context.stroke();


    // draw nodes
    graphData[0].nodes.forEach(function(d) {
        context.beginPath();
        // draw circle centre
        context.moveTo(d.x, d.y);
        // centreX, centreY, radius, circumference  
        context.arc(d.x, d.y, nodefixed(d.totaltokens, maxsize, minsize, d.topn, maxtopn, mintopn), 0, 2 * Math.PI);
        // circle border
        // stroke has to be drawn before fill
        if (d.topn != null) {context.strokeStyle = top5stroke} else {context.strokeStyle = othersstroke};
        context.stroke();
        // circle fill
        if (d.topn != null) {context.fillStyle = top5fill} else {context.fillStyle = othersfill};
        context.fill();
    });


    // draw labels
    graphData[0].nodes.forEach(function(d) {
        context.beginPath();
        context.moveTo(d.x, d.y);

        
        var newsize = newtopnsize(d.totaltokens, maxtopn, mintopn)
        var adjust = adjustleft(newsize)
        if (d.topn != null) {
            context.font="bold " + newsize + "px " + "Arial";}
        // context.font="bold " + newsize + "px " + "Arial";
        context.fillStyle="white";
        if (d.topn != null) {context.fillText(d.topn, d.x+adjust, d.y+5);}
    });
   
}


setInterval(function(){

    // print out time
    var currentdate = new Date(); 
    var currenttime = currentdate.getHours() + ":"  
                + currentdate.getMinutes() + ":" 
                + currentdate.getSeconds();

    // call node.js to tell mongodb query and export json to front-end
    $.ajax({
         url: '/xxx',
         type: 'POST',
         processData: false,
         contentType: 'application/json',
         data: JSON.stringify(
           {
             "Password": "xxx",
           }),
         dataType: 'json',
 
         success: function (res) {
            console.log(currenttime + ' ' + 'success!')

            // delay function so ajax have time to communicate to node and update mongo.json
            sleep(1000)

            // add random parameter to json file to force refresh cached json
            nocache_update = 'mongo.json?nocache=' + (new Date()).getTime();

            d3.json(nocache_update, function(error, update2){
                if (error) throw error;

                // PREPARE BEFORE APPENDING / UPDATING GRAPHDATA ARRAY ----------------
                // store previous topn nodes
                storetopn = graphData[0].nodes.filter(function(d){
                            if (d.topn != null){
                                return d
                            }
                        })
                // set topn in original graphData array to all null
                graphData[0].nodes.forEach(function(i){
                            i.topn = null
                        })
                // extract topn only
                topn = update2[0].nodes.filter(function(d){
                            if (d.topn != null){
                                return d
                            }
                        })
                // extract only UPDATED NODES based on last updated time
                update2[0].nodesize = update2[0].nodes.filter(function(d){
                            if (d.nodeUpdatetime > latestnodetime && d.nodeUpdatetime != null){
                                return d;
                            }
                        })
                // extract only NEW NODES created based on node-ids comparison
                var existingid = graphData[0].nodes.map(function(i){return i.emailid;}) // array of existing ids
                update2[0].nodes = update2[0].nodes.filter(function(d){
                            if ($.inArray(d.emailid, existingid) == -1){
                                return d;
                            }
                        })
                // extract only UPDATED LINKS based on last updated time
                update2[0].links = update2[0].links.filter(function(d){
                            if (d.timestamp > latestlinktime){
                                return d;
                            }
                        })


                // concat to initial dataset of nodes so can do link matching
                // not required later as it will be a single json
                nodesall = graphData[0].nodes.concat(update2[0].nodes) 
                
                // allow source target to be names instead of array sequence numbers
                edges2 = [];
                update2[0].links.forEach(function(e) {
                    var sourceNode = nodesall.filter(function(n) {
                            return n.emailid === e.source;
                            })[0],
                        targetNode = nodesall.filter(function(n) {
                            return n.emailid === e.target;
                            })[0];
                        edges2.push({
                            source: sourceNode,
                            target: targetNode,
                            value: e.value
                        });
                    });


                // have to iterate or it will prompt datatype error
                // UPDATED NEW NODES ----------------
                update2[0].nodes.forEach(function(i){
                    graphData[0].nodes.push(i);
                })
                // UPDATE NEW LINKS ----------------
                edges2.forEach(function(i){
                    graphData[0].links.push(i);
                })
                // UPDATE TOKEN SIZE ----------------
                graphData[0].nodes.forEach(function(i){
                    update2[0].nodesize.forEach(function(ii){
                        if (i.emailid == ii.emailid){
                            i.totaltokens = ii.totaltokens
                            // console.log(ii.totaltokens)
                        }
                    })
                })
                // PUT NEW TOPN INTO GRAPHDATA ARRAY ----------------
                graphData[0].nodes.forEach(function(i){
                    topn.forEach(function(ii){
                        if (i.emailid == ii.emailid){
                            i.topn = ii.topn
                            // i.totaltokens = i.totaltokens + getRandomInt(min1,max1)
                            // console.log(i.topn)
                        }
                    })
                })

                update()
                force.start()
                        
                // replace previous topn based on current topn
                storetopn = topn

                // update barchart
                add(storetopn)
                // replace the latest time for most recent update
                latestnodetime = latestNtime(update2[0].nodes, latestnodetime)
                latestlinktime = latestLtime(update2[0].links, latestlinktime)

                // console.log(latestnodetime)

            })
        
        },
        error: function (err) {
            console.log('Error:', err)
            // add in a refresh if error
        }
        })
}, 10000);


// UPDATE NETWORK GRAPH BASED ON LATEST TIME ------------------------------------------------------
// setInterval(function(){
// // d3.select("#update1").on("click", function() {
    

//     // add random parameter to json file to force refresh cached json
//     nocache_update = 'mongo.json?nocache=' + (new Date()).getTime();

//     d3.json(nocache_update, function(error, update2){
//         if (error) throw error;

//         // PREPARE BEFORE APPENDING / UPDATING GRAPHDATA ARRAY ----------------
//         // store previous topn nodes
//         storetopn = graphData[0].nodes.filter(function(d){
//                     if (d.topn != null){
//                         return d
//                     }
//                 })
//         // set topn in original graphData array to all null
//         graphData[0].nodes.forEach(function(i){
//                     i.topn = null
//                 })
//         // extract topn only
//         topn = update2[0].nodes.filter(function(d){
//                     if (d.topn != null){
//                         return d
//                     }
//                 })
//         // extract only UPDATED NODES based on last updated time
//         update2[0].nodesize = update2[0].nodes.filter(function(d){
//                     if (d.nodeUpdatetime > latestnodetime && d.nodeUpdatetime != null){
//                         return d;
//                     }
//                 })
//         // extract only NEW NODES created based on node-ids comparison
//         var existingid = graphData[0].nodes.map(function(i){return i.emailid;}) // array of existing ids
//         update2[0].nodes = update2[0].nodes.filter(function(d){
//                     if ($.inArray(d.emailid, existingid) == -1){
//                         return d;
//                     }
//                 })
//         // extract only UPDATED LINKS based on last updated time
//         update2[0].links = update2[0].links.filter(function(d){
//                     if (d.timestamp > latestlinktime){
//                         return d;
//                     }
//                 })


//         // concat to initial dataset of nodes so can do link matching
//         // not required later as it will be a single json
//         nodesall = graphData[0].nodes.concat(update2[0].nodes) 
        
//         // allow source target to be names instead of array sequence numbers
//         edges2 = [];
//         update2[0].links.forEach(function(e) {
//             var sourceNode = nodesall.filter(function(n) {
//                     return n.emailid === e.source;
//                     })[0],
//                 targetNode = nodesall.filter(function(n) {
//                     return n.emailid === e.target;
//                     })[0];
//                 edges2.push({
//                     source: sourceNode,
//                     target: targetNode,
//                     value: e.value
//                 });
//             });


//         // have to iterate or it will prompt datatype error
//         // UPDATED NEW NODES ----------------
//         update2[0].nodes.forEach(function(i){
//             graphData[0].nodes.push(i);
//         })
//         // UPDATE NEW LINKS ----------------
//         edges2.forEach(function(i){
//             graphData[0].links.push(i);
//         })
//         // UPDATE TOKEN SIZE ----------------
//         graphData[0].nodes.forEach(function(i){
//             update2[0].nodesize.forEach(function(ii){
//                 if (i.emailid == ii.emailid){
//                     i.totaltokens = ii.totaltokens
//                     // console.log(ii.totaltokens)
//                 }
//             })
//         })
//         // PUT NEW TOPN INTO GRAPHDATA ARRAY ----------------
//         graphData[0].nodes.forEach(function(i){
//             topn.forEach(function(ii){
//                 if (i.emailid == ii.emailid){
//                     i.topn = ii.topn
//                     // i.totaltokens = i.totaltokens + getRandomInt(min1,max1)
//                     // console.log(i.topn)
//                 }
//             })
//         })

//         update()
//         force.start()
                
//         // replace previous topn based on current topn
//         storetopn = topn

//         console.log()
//         // update barchart
//         add(storetopn)
//         // replace the latest time for most recent update
//         latestnodetime = latestNtime(update2[0].nodes, latestnodetime)
//         latestlinktime = latestLtime(update2[0].links, latestlinktime)

//         // console.log(latestnodetime)

//     })
// }, 8000);
// });






// MISCELLANEOUS CODES ----------------------------

// title casing
function title(str) {
    return str.replace(/\b\S/g, function(t) { return t.toUpperCase() });
  }

// sleep function
function sleep(milliseconds) {
    var start = new Date().getTime();
    for (var i = 0; i < 1e7; i++) {
      if ((new Date().getTime() - start) > milliseconds){
        break;
      }
    }
  }

// for recording video demo purposes, a random number generator
function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
}

// get topn function
function gettopn(graph){
    JSON.parse(JSON.stringify(graph.nodes))
        .sort((a, b) => b.totaltokens - a.totaltokens || a.nodeUpdatetime - b.nodeUpdatetime)
        .slice(0, 5)
}

// get total tokens, for token count down
function maxtokens(graph){
    var totalcount = 0
    graph.forEach(function(i){
        totalcount = totalcount + i.totaltokens
    })
    return totalcount
}

// get max node size
function max(graph){
    // remove top5 token size as they already have a fixed node size
    var graph = graph.filter(function(i){ if(i.topn == null){return i}})
    return Math.max.apply(Math, graph.map(function(i){ return i.totaltokens;}))
}

// get min node size
function min(graph){
    return Math.min.apply(Math, graph.map(function(i){return i.totaltokens;}))
}

// get max node size between topn
function maxtopN(graph){
    // remove top5 token size as they already have a fixed node size
    var graph = graph.filter(function(i){ if(i.topn != null){return i}})
    return Math.max.apply(Math, graph.map(function(i){ return i.totaltokens;}))
}

// get min node size between topn
function mintopN(graph){
    var graph = graph.filter(function(i){ if(i.topn != null){return i}})
    return Math.min.apply(Math, graph.map(function(i){return i.totaltokens;}))
}

// get lastest node time
function latestNtime(graph, latestlinktime){
    if (d3.max(graph, function(d){return d.nodeUpdatetime})==null){
        return latestnodetime
    } else {
        return d3.max(graph, function(d){return d.nodeUpdatetime})
    }
}

// get latest link time
function latestLtime(graph, latestlinktime){
    if (d3.max(graph, function(d){return d.timestamp})==null){
        return latestnodetime
    } else {
        return d3.max(graph, function(d){return d.timestamp})
    }
}

// dynamic node sizing so that it won't get too big and cover whole screen
// size = token size, maxsize = total nodes, topn = top 5 by token count
// use the below formula from https://gamedev.stackexchange.com/questions/33441/how-to-convert-a-number-from-one-min-max-set-to-another-min-max-set
// ((Input - InputLow) / (InputHigh - InputLow)) * (OutputHigh - OutputLow) + OutputLow;

// start from min 2 to max 8 as 1 is too small and >=9 is too large
function nodefixed(size, maxsize, minsize, topn, maxtopn, mintopn){
    var newsize
    if (minsize == maxsize){
        newsize = 2
    } else {
        newsize = (((size-minsize) / (maxsize-minsize)) * (0.8 - 0.2) + 0.2).toFixed(1) * 10 // fixed to 1 decimal, then *10 to get an integer btw 2-8
    }
    
    if (topn != null) { // top 5 nodes
        var newtopnsize = (((size-mintopn) / (maxtopn-mintopn)) * (0.16 - 0.12) + 0.12).toFixed(2) * 100 // fixed to 1 decimal, then *10 to get an integer btw 2-8
        return newtopnsize
    } else {
        return newsize
    }
}

function newtopnsize(size, maxtopn, mintopn){
    return (((size-mintopn) / (maxtopn-mintopn)) * (0.16 - 0.12) + 0.12).toFixed(2) * 100 // fixed to 1 decimal, then *10 to get an integer btw 2-8
}

// dynamic link sizing to reduce link thickness when there are lots of them
function linksizing(maxlink){
    if (maxlink < 100) {
        return 1.25
    } else if (maxlink < 500){
        return 1.1
    } else if (maxlink < 1000) {
        return 1
    } else if (maxlink < 2500) {
        return 0.8
    } else if (maxlink < 10000) {
        return 0.6
    } else if (maxlink < 15000) {
        return 0.25
    } else {
        return 0.1
    }
}

// dynamic gravity adjustment based on node size
function gravityadjust(size){
    if (size < 50){
        return 0.1
    } else if (size < 100){
        return 0.12
    } else if (size < 300){
        return 0.14
    } else if (size < 500){
        return 0.16
    } else {
        return 0.18
    }
}

// dynamic charge adjustment based on node size
function chargeadjust(size){
    if (size < 50){
        return -100
    } else if (size < 100){
        return -80
    } else if (size < 200){
        return -60
    } else if (size < 300){
        return -50
    } else if (size >= 400){
        return -40
    } else if (size >= 500){
        return -30
    } else if (size >= 600){
        return -1
    }
}

// dynamic link strength adjustment based on no. links
function linksadjust(size){
    if (size < 1000){
        return 0.1
    } else if (size < 5000){
        return 0.08
    } else if (size < 10000){
        return 0.06
    } else if (size < 15000){
        return 0.04
    } else if (size < 20000){
        return 0.02
    } else if (size >= 20000){
        return 0.005
    }
}

// adjust topn font size based on node size
function fontsize(nodesize){
    if (nodesize <= 12){
        return "14"
    } else if (nodesize <= 14) {
        return "24.5"
    } else if (nodesize <= 16) {
        return "25"
    } else if (nodesize >= 16) {
        return "26"
    } else 0
}

// dynamic node y coordinate adjustment of node label
function adjustleft(fsize){
    if (fsize <= "20"){
        return -4
    } else if (fsize <= "24.5"){
        return -5
    } else if (fsize <= "25"){
        return -6
    } else if (fsize <= "30"){
        return -6
    } else return -8
}



// CHARTJS BARCHART ------------------------------------------------------
function barchart(topn){
    // split topn dataset into two arrays, labels & data from initial dataset
    topn = topn.sort((a, b) => a.topn - b.topn)
    // barlabel = topn.map(a => a.name + '|' + a.company + ' - ' + a.totaltokens + ' tokens' )
    barlabel = topn.map(a => a.name + '|' + a.totaltokens + ' tokens' )
    bardata = topn.map(a => a.totaltokens)

    

    var ctx = document.getElementById('barchart').getContext('2d');
    chart = new Chart(ctx, {
        type: 'horizontalBar',
        data: {
            labels: barlabel,
            datasets: [{
                label: "Top 5",
                backgroundColor: top5fill,
                borderColor: 'rgb(0, 0, 0)',
                data: bardata
            }]
        },
        options: {
            tooltips: {enabled: false},
            legend: {display: false},
            responsive: true, 
            maintainAspectRatio: false, // set as false so that height can be fixed while width is responsive
            scales: {
                xAxes: [{ticks: {autoSkip: false,
                                 display: false,
                                 min: 0},
                        gridLines: {display:false}}],
                yAxes: [{ticks: {display: false,
                                 fontSize: 14,
                                 fontStyle: "bold"},
                        gridLines: {display:false},
                        categoryPercentage: 0.96,
                        barPercentage: 0.96}]
                    },
                layout: {
                    padding: { left: 16
                    }
                },
            animation: { // overcome mirror labels which hide behind the bar chart
                onProgress () {
                    const chartInstance = this.chart;
                    const ctx = chartInstance.ctx;
                    const dataset = this.data.datasets[0];
                    const meta = chartInstance.controller.getDatasetMeta(0);
                    
                    // ranking label
                    // Chart.helpers.each(meta.data.forEach((bar, index) => {
                    //     const label = this.data.labels[index];
                    //     const rank = [index+1];
                    //     const labelPositionX = 10;
                    //     const labelWidth = ctx.measureText(label).width + labelPositionX;
                        
                    //     // canvas properties
                    //     ctx.textBaseline = 'middle';
                    //     ctx.textAlign = 'left';
                    //     ctx.fillStyle = 'rgb(100, 100, 100)';
                    //     ctx.font = "bold 14px Arial";
                    //     ctx.fillText(rank, labelPositionX, bar._model.y);
                    // }));
                    
                    // name label
                    Chart.helpers.each(meta.data.forEach((bar, index) => {
                        const label = this.data.labels[index];
                        const label1 = title(label.split("|")[0]); // name
                        const rank = barlabel[index];
                        const labelPositionX = 35;
                        const labelWidth = ctx.measureText(label).width + labelPositionX;
                        
                        // canvas properties
                        ctx.textBaseline = 'middle';
                        ctx.textAlign = 'left';
                        ctx.fillStyle = '#FFF';
                        ctx.font = "bold 16px Arial";
                        ctx.fillText(label1, labelPositionX, bar._model.y-5);
                        // ctx.fillText(label2, labelPositionX, bar._model.y+10)
                    }));

                    // company & token label
                    Chart.helpers.each(meta.data.forEach((bar, index) => {
                        const label = this.data.labels[index];
                        const label2 = label.split("|")[1];
                        const rank = barlabel[index];
                        const labelPositionX = 35;
                        const labelWidth = ctx.measureText(label).width + labelPositionX;
                        
                        // canvas properties
                        ctx.textBaseline = 'middle';
                        ctx.textAlign = 'left';
                        ctx.fillStyle = '#FFF';
                        ctx.font = "10px Arial";
                        // ctx.fillText(label1, labelPositionX, bar._model.y-10);
                        ctx.fillText(label2, labelPositionX, bar._model.y+14)
                    }));
                }
            }
        },
        // enable labelling for new line
        plugins: [{
            beforeInit: function (chart) {
            chart.data.labels.forEach(function (e, i, a) {
                if (/\n/.test(e)) {
                a[i] = e.split(/\n/)
                }
            })
            }
        }]
    });
}

// change topn data in barchart upon each update
function add(newtopn){

    topn = newtopn.sort((a, b) => a.topn - b.topn)
    // newlabel = topn.map(a => a.name + '|' + a.company + ' - ' + a.totaltokens + ' tokens' )
    newlabel = topn.map(a => a.name + '|' + a.totaltokens + ' tokens' )
    newdata = topn.map(a => a.totaltokens)

    // add new data
    var data = chart.data.datasets[0].data;
    data[0] = newdata[0]
    data[1] = newdata[1]
    data[2] = newdata[2]
    data[3] = newdata[3]
    data[4] = newdata[4]

    // add new label
    var label = chart.data.labels;
    label[0] = newlabel[0]
    label[1] = newlabel[1]
    label[2] = newlabel[2]
    label[3] = newlabel[3]
    label[4] = newlabel[4]

    // update barchart with new data & labels
    chart.update();
}