// $nick = d3.select("#nickname_on_air");
d3.json("/nicknames/api", function (err, data) {
  const n = Object.keys(data).length;

  let genRandID = ( n_samples ) => Math.floor( Math.random() * n_samples );
  const first_random = genRandID( n );

yearSelectEnd(first_random);  
// d3.select("#yearEnd")
//   .attr("min", 0)
//   .attr( "max", Object.keys(data).length )
//   .attr( "value", 0 )
//   ;
  
});





function yearSelectEnd(defIndex) {
  
  // const defIndex = 2020;
  // console.log('yr end  :>> ', defIndex);
      
  let $yearEnd = d3.select( '#yearEnd' );
  $yearEnd.attr( 'value', defIndex );
  // console.log( 'userInput :>> ', defIndex );
  let parseTime = d3.timeParse( "%Y" ); // display only year

  let width = $( "#nickname-generator" ).width();
  let height = $( "#nickname-generator" ).height();

  let svg = d3.select( '#nickname-generator' )
    .append( 'svg' )
    .attr( 'width', width )
    .attr( 'height', height );

  let plotGroup = svg.append( 'g' )
    .classed( 'plot', true );

  let scale = d3.scaleTime()
    .domain( [ defIndex-1, defIndex+1 ] )
    .range( [ 0, height ] );

  let axis = d3
    .axisRight( scale )
    // .ticks( d3.timeYear.every( 1 ) )
    .tickFormat( d3.timeFormat( "%Y" ) );

  let axisGroup = plotGroup.append( 'g' )
    .classed( 'jackpot', true );

  function jackpotRight( userInput, axG,  parseTime, height ) {
    let scale = d3.scaleLinear()
      .domain( [ userInput-1, userInput+1 ] )
      .range( [ height , 0 ] );

    let axis = d3
      .axisRight( scale )
      // .ticks( d3.timeYear )
      .tickFormat( d3.format( "," ) )
      ;

    axG
     .transition()
    //  .ease( d3.easeBounce )
     .ease( d3.easeElastic )
     .duration( 1500 )
     .call( axis );
    }
    
    jackpotRight( defIndex, axisGroup, parseTime, height );
    d3.select( '#yearEnd' )
      .on( 'change', function () {
        jackpotRight( +this.value, axisGroup,  parseTime, height );
        

    } )

}

