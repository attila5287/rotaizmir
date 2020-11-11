d3.json("/colors/api", function (err, data) {
  const n = Object.keys(data).length;

  let genRandID = ( n_samples ) => Math.floor( Math.random() * n_samples );
  
  const defIndex = genRandID( n );
  
  d3.select("#input-color")
    .attr("data-name", data[defIndex].color)
    .attr("data-number", data[defIndex].colorcode)
    .attr("value", data[defIndex].color)
    .style("fill", data[defIndex].colorcode);
  
  d3.select( "#slider-clr" )
    .attr("min", 0)
    .attr("max", Object.keys(data).length - 1)
    .attr("value", 0);

  yearSelectEnd(defIndex);

  function yearSelectEnd(def_index) {
    d3.select( "#slider-clr" )
      .attr( "value", def_index );

    let width = $("#color-generator").width();
    let height = $("#color-generator").height();

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
        const create_doma1n = (d, i) => {
          const arr = Object.keys( d ).map( ( k ) => d[ k ] );
          
          if (i == 0) {
            return ["turquoise", "aqua", arr.slice(i, i + 3).map(d=>d.color)].flat();
          } else if (i == 1) {
            return [
              "turqoise",
              arr.slice(i - 1, i + 3).map((d) => d.color),
            ].flat();
          } else {
            return arr.slice(i - 2, i + 3).map((d) => d.color);
          }
        };
      const get_colcodes = (d, i) => {
        const arr = Object.keys(d).map((k) => d[k]);

        if (i == 0) {
          return [
            "#40E0D0",
            "#00FFFF",
            arr.slice(i, i + 3).map((d) => d.colorcode),
          ].flat();
        } else if (i == 1) {
          return [
            "#40E0D0",
            arr.slice(i - 1, i + 3).map((d) => d.colorcode),
          ].flat();
        } else {
          return arr.slice(i - 2, i + 3).map((d) => d.colorcode);
        }
      };

      
      let now_displaying = create_doma1n( data, index );
      let now_colcodes = get_colcodes( data, index );
      
      
      // console.log('now_displaying :>> ', now_displaying);
      // console.log('now_displaying  cc:>> ', now_colcodes);
      $cc = d3.selectAll( '.color-squares' )
        .data( now_colcodes )
        .transition()
        .duration(500)
        .style( "background-color", d => d );

      let color_on_air = data[ index ].color;
      
      d3.select("#input-color")
        .style("border-color", color_on_air)
        .style("fill", color_on_air)
        .style("background-color", color_on_air)
        .style("border-radius", "6px")
        .append("input")
        .classed(
          "rdonly text-outlined border-0 text-center text-3xl form-control bg-transparent",
          true
        )
        .attr( "id", "input-clr")
        .attr( "value", `-${color_on_air}-` )
        ;
      
        
      
      let scale = d3
        .scaleBand()
        .domain(now_displaying)
        .range( [ 0, chartHeight ] );
      
      let axis = d3
        .axisRight(scale)
        .ticks(5)
        .tickSizeInner( chartWidth * 0.30 );
      
      
      
      axG.transition().ease( d3.easeElastic ).duration( 1500 ).call( axis );
      render_signup();
    }
    
    d3.select("#slider-clr").on("change", function () {
      let new_index = +this.value;

      jackpotRight(new_index, axisGroup, height, data, width);
    } );
    
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
          data[defIndex + actions[selected]].colorcode
        );
        
        d3.select("#input-color")
          .attr("data-name", data[defIndex].color)
          .attr("data-number", data[defIndex].colorcode)
          .attr("value", data[defIndex].color)
          
          ;
        
        jackpotRight(+this_val, axisGroup, height, data, width);        
      } )
  }
});


