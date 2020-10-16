d3.json("/nicknames/api", function (err, data) {
  const n = Object.keys(data).length;

  let genRandID = (n_samples) => Math.floor(Math.random() * n_samples);
  const first_random = genRandID(n);
  d3.select("#slider-nn")
    .attr("min", 0)
    .attr("max", Object.keys(data).length - 1)
    .attr("value", 0);

  yearSelectEnd(first_random);

  function yearSelectEnd(def_index) {
    let $yearEnd = d3.select("#slider-nn");
    $yearEnd.attr("value", def_index);

    let width = $("#nickname-generator").width();
    let height = $("#nickname-generator").height();

    let svg = d3
      .select("#nickname-generator")
      .append("svg")
      .attr("width", width)
      .attr("height", height);

    let plotGroup = svg
      .append("g")
      .classed("plot", true);
      ;
    const keys = Object.keys( data ).map( ( k ) => data[ k ] );  
    const first_dom = [
      keys[ def_index - 1 ],
      keys[ def_index ],
      keys[ def_index + 1 ],
    ];
    let scale = d3
      .scaleBand()
      .domain(first_dom)
      .range([0, height])
      ;
    
    let axis = d3
      .axisRight(scale)
      .tickSizeInner(width * 0.15)
      .tickSizeOuter(width * 0.15)
      .tickPadding( 3 )
      ;
    
    let axisGroup = plotGroup
      .append( "g" )
      .classed( "jackpot", true );
    
    jackpotRight( def_index, axisGroup, height, keys, width );
    
    function jackpotRight(index, axG, chartHeight, keysList, chartWidth) {
      let new_domain = [
        keysList[index-1],
        keysList[index],
        keysList[index+1],
      ];
      let scale = d3
        .scaleBand()
        .domain(new_domain)
        .range([0, chartHeight])
        ;
      let axis = d3
        .axisRight(scale)
        .tickSizeInner(chartWidth * 0.25)
        .tickSizeOuter(width * 0.15)
        .tickPadding(3);
        ;
      
      axG.transition().ease( d3.easeElastic ).duration( 1500 ).call( axis );
    }
    
    d3.select("#slider-nn").on("change", function () {
      let new_index = +this.value;

      jackpotRight(+this.value, axisGroup, height, keys, width);
    });
    d3.selectAll( '.nickname-buttons' )
      .on( "click", function ( event ) {
        // d3.event.preventDefault();
        let selected = d3.event.target.id.trim();
        let actions = {
          "up-icon-nn" : 1,
          "up-nn" : 1,
          "down-nn" : -1,
          "down-icon-nn" : -1,
        };

        let this_val = d3.select( "#slider-nn" ).attr( "value" );
        
        d3.select( "#slider-nn" ).attr( "value", +this_val + actions[ selected ] );
        
        jackpotRight(+this_val, axisGroup, height, keys, width);        
      } )
  }
});


