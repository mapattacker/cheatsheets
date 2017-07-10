//////////////////// introduction ////////////////////
// https://github.com/d3/d3/blob/master/API.md
// there are gigantic differences btw version 3 & version 4. See more https://iros.github.io/d3-v4-whats-new/#9


// source
<script src="https://d3js.org/d3.v4.js"></script>
<script src="https://d3js.org/d3-selection.v1.min.js"></script>


//////////////////// SELECTION ////////////////////
  // select will grab the first selection it encounters
  // selectAll will grab all selection
d3.select(".main-title") //select class
d3.select("#header") // select id
d3.select("h1") // select tag
d3.select("img").attr("src") // select an attribute eg., <img src="./assets/udacity.svg">

  // nested selection
      // select parent id=header, and then followed by the child tag <img>. Need not be direct child
d3.select("#header img") 


//////////////////// SWAP ////////////////////
  // change text
d3.select(".main-title").text("I changed the title");
  // change attribute content
      // select parent class navbar, child img tag, and change image link
d3.select('.navbar img').attr('src', './assets/udacity_white.png'); 

//////////////////// REMOVE ////////////////////
d3.select('.main').remove
d3.select('.main').html(null) // or undefined, or empty string ''

//////////////////// SCALE ////////////////////
// note that for y-axis, 0 starts from top down
.domain //refers to actual range
.range //refers to d3 scale range

// remove html tags under .main
var svg = d3.select('.main').html(null).append('svg');
svg.attr('width', 600).attr('height', 300)
  // output as <svg width="600" height="300"></svg>
d3.scale.linear.domain([15,90]).range([250,0])


