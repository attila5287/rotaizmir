// $nick = d3.select("#nickname_on_air");
d3.json("/nicknames/api", function (err, data) {
  const n = Object.keys(data).length;

  let genRandID = ( n_samples ) => Math.floor( Math.random() * n_samples );
  const first_random = genRandID( n );
  
  yearSelectEnd(first_random);  
  d3.select("#yearEnd")
    .attr("min", 0)
    .attr( "max", Object.keys(data).length )
    .attr( "value", 0 )
    ;
  
} );

function yearSelectEnd(def_index) {
  // const defIndex = 2020;
  // console.log('yr end  :>> ', defIndex);

  let $yearEnd = d3.select("#yearEnd");
  $yearEnd.attr("value", def_index);
  // console.log( 'userInput :>> ', defIndex );
  let parseTime = d3.timeParse("%Y"); // display only year

  let width = $("#nickname-generator").width();
  let height = $("#nickname-generator").height();

  let svg = d3
    .select("#nickname-generator")
    .append("svg")
    .attr("width", width)
    .attr("height", height);

  let plotGroup = svg.append("g").classed("plot", true);

  let scale = d3
    .scaleTime()
    .domain([def_index - 1, def_index + 1])
    .range([0, height]);

  let axis = d3
    .axisRight(scale)
    .ticks(3)
    .tickFormat(function (d, i) {
      return "Year" + d; //"Year1 Year2, etc depending on the tick value - 0,1,2,3,4"
    });
    ;

  let axisGroup = plotGroup.append("g").classed("jackpot", true);

  function jackpotRight(userInput, axG, parseTime, height) {
    let scale = d3
      .scaleLinear()
      .domain([userInput - 1, userInput + 1])
      .range([height, 0]);

    let axis = d3.axisRight( scale )
      .ticks( 3 ).tickFormat( d3.format( "," ) );
    
    axG
      .transition()
      .ease(d3.easeElastic)
      .duration(1500)
      .call(axis);
  }

  jackpotRight( def_index, axisGroup, parseTime, height );
  
  d3.select( "#yearEnd" ).on( "change", function () {
    let new_index = +this.value;

    jackpotRight( +this.value, axisGroup, parseTime, height );
    
  });
}

