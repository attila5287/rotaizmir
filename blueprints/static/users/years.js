
function yearSelectEnd(defIndex) {
  
  // const defIndex = 2020;
  // console.log('yr end  :>> ', defIndex);
      
  let $yearEnd = d3.select( '#yearEnd' );
  $yearEnd.attr( 'value', defIndex );
  // console.log( 'userInput :>> ', defIndex );
  let parseTime = d3.timeParse( "%Y" ); // display only year

  let width = $( `#jackpotYrEnd` ).width();
  let height = $( `#jackpotYrEnd` ).height();

  let svg = d3.select( '#jackpotYrEnd' )
    .append( 'svg' )
    .attr( 'width', width )
    .attr( 'height', height );

  let plotGroup = svg.append( 'g' )
    .classed( 'plot', true );

  let scale = d3.scaleTime()
    .domain( [ parseTime(defIndex-1), parseTime(defIndex+1) ] )
    .range( [ 0, height ] );

  let axis = d3
    .axisRight( scale )
    .ticks( d3.timeYear.every( 1 ) )
    .tickFormat( d3.timeFormat( "%Y" ) );

  let axisGroup = plotGroup.append( 'g' )
    .classed( 'jackpot', true );

  function jackpotRight( userInput, axG,  parseTime, height ) {
    let scale = d3.scaleTime()
      .domain( [ parseTime(userInput-1), parseTime(userInput+1) ] )
      .range( [ height , 0 ] );

    let axis = d3
      .axisRight( scale )
      .ticks( d3.timeYear.every( 1 ) )
      .tickFormat( d3.timeFormat( "%Y" ) );

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
yearSelectEnd(2020);
