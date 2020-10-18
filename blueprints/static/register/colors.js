d3.json("/colors/api", function (err, data) {
  const n = Object.keys(data).length;

  let genRandID = ( n_samples ) => Math.floor( Math.random() * n_samples );
  
  const first_random = genRandID( n );
  
  d3.select("#input-color")
    .attr("data-name", data[first_random].color)
    .attr("data-number", data[first_random].colorcode)
    .attr("value", data[first_random].color)
    .style("fill", data[first_random].colorcode);
  
  d3.select( "#slider-clr" )
    .attr("min", 0)
    .attr("max", Object.keys(data).length - 1)
    .attr("value", 0);

  yearSelectEnd(first_random);

  function yearSelectEnd(def_index) {
    d3.select( "#slider-clr" )
      .attr( "value", def_index );

    let width = $("#color-generator").width();
    let height = $("#color-generator").width()*.4;

    let svg = d3
      .select("#color-generator")
      .append( "svg" )
      .attr("class", "bg-glass")
      .attr("width", width)
      .attr("height", height);

    let plotGroup = svg
      .append("g")
      .classed( "plot", true )
      ;
    let axisGroup = plotGroup
      .append( "g" )
      .classed( "jackpot", true )
    ;
    
    jackpotRight( def_index, axisGroup, height, data, width );
    
    function jackpotRight ( index, axG, chartHeight, data, chartWidth ) {
      const $input = d3.select("#input-color").select("input");

      if (!$input.empty()) {
        $input.remove();
      }
      d3.select("#input-color")
        .style("border-color", data[index].colorcode)
        .style("fill", data[index].colorcode)
        .style("background-color", data[index].colorcode)
        .append("input")
        .classed(
          "rdonly text-outlined text-center text-3xl form-control bg-transparent",
          true
        )
        .attr("value", data[index].color);
      
      let new_domain = [
        data[index - 2].color,
        data[index - 1].color,
        data[index].color,
        data[index + 1 ].color,
        data[index + 2 ].color,
      ];
      let scale = d3
        .scaleBand()
        .domain(new_domain)
        .range([0, chartHeight])
        ;
      let axis = d3
        .axisRight(scale)
        .ticks(5)
        .tickSizeInner(chartWidth * 0.25)
        ;
      
      axG.transition().ease( d3.easeElastic ).duration( 1500 ).call( axis );
    }
    
    d3.select("#slider-clr").on("change", function () {
      let new_index = +this.value;

      jackpotRight(+this.value, axisGroup, height, data, width);
    });
    d3.selectAll( '.color-buttons' )
      .on( "click", function (  ) {
        // d3.event.preventDefault();
        let selected = d3.event.target.id.trim();
        let actions = {
          "up-btn-clr": 1,
          "up-icon-clr": 1,
          "down-btn-clr": -1,
          "down-icon-clr": -1,
        };

        let this_val = d3.select( "#slider-clr" ).attr( "value" );
        
        d3.select( "#slider-clr" ).attr( "value", +this_val + actions[ selected ] );
        d3.select( "#read-only-username" )
          .style(
          "background-color",
          data[first_random + actions[selected]].colorcode
        );
        
        d3.select("#input-color")
          .attr("data-name", data[first_random].color)
          .attr("data-number", data[first_random].colorcode)
          .attr("value", data[first_random].color)
          
          ;
        
        jackpotRight(+this_val, axisGroup, height, data, width);        
      } )
  }
});


