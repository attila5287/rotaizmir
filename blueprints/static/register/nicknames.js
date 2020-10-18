d3.json( "/nicknames/api", function ( err, data ) {
  const n = Object.keys( data ).length;

  let genRandID = ( n_samples ) => Math.floor( Math.random() * n_samples );
  const first_random = genRandID( n );
  d3.select( "#slider-nn" )
    .attr( "min", 0 )
    .attr( "max", Object.keys( data ).length - 1 )
    .attr( "value", 0 );

  yearSelectEnd( first_random, data );


  function yearSelectEnd ( def_index, data ) {
    // console.log('data :>> ', data);
    let $sliderNN = d3.select( "#slider-nn" );
    $sliderNN.attr( "value", def_index );

    let width = $( "#nickname-generator" ).width();
    let height = $("#nickname-generator").width() * 0.4;

    let svg = d3
      .select("#nickname-generator")
      .append("svg")
      .attr("class", "bg-glass")
      .attr("width", width)
      .attr("height", height);

    let plotGroup = svg
      .append( "g" )
      .classed( "plot", true );
    
    const flat_paired_arr = Object.keys( data ).map( ( k ) => data[ k ] );

    let axisGroup = plotGroup
      .append( "g" )
      .classed( "jackpot", true )
      ;
    
    
    function jackpotRight(index, svg, chartHeight, data, chartWidth) {
      const $input = d3.select("#input-nickname").select("input");

      if (!$input.empty()) {
        $input.remove();
      }
      d3.select("#input-nickname")
        .append("input")
        .classed("rdonly text-lite form-control bg-transparent border-0", true)
        .attr("value", data[index]);

      let new_domain = [
        data[index - 2],
        data[index - 1],
        data[index],
        data[index + 1],
        data[index + 2],
      ];

      let scale = d3.scaleBand().domain(new_domain).range([0, chartHeight]);
      let axis = d3
        .axisRight(scale)
        .ticks(5)
        .tickSizeInner(chartWidth * 0.10)
        .tickPadding(1);
        ;
      
      svg.transition().ease(d3.easeElastic).duration(1500).call(axis);
    }
    
    jackpotRight(def_index, axisGroup, height, flat_paired_arr, width);
    
    
    d3.select( "#slider-nn" ).on( "change", function () {
      jackpotRight(+this.value, axisGroup, height, flat_paired_arr, width);
    } );

    d3.selectAll( '.nickname-buttons' )
      .on( "click", function () {
        let selected = d3.event.target.id.trim();
        let actions = {
          "up-icon-nn": 1,
          "up-btn-nn": 1,
          "down-btn-nn": -1,
          "down-icon-nn": -1,
        };

        let this_val = d3.select( "#slider-nn" ).attr( "value" );

        d3.select( "#slider-nn" ).attr( "value", +this_val + actions[ selected ] );

        jackpotRight(+this_val, axisGroup, height, flat_paired_arr, width);
      } )
  }
} );
