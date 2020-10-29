  render_signup();
  
  function render_signup () {
    val_nn = d3
      .select("#input-nickname")
      .select("input")
      .classed(
        "shadow rdonly text-3xl text-secondary text-monts form-control form-control-dark form-control-lg bg-transparent border-0 text-center",
        true
      )
      .attr("readonly", true)
      .attr("value");
    
    val_color = '' + d3.select( "#input-color" )
      .select( "input" )
      .attr( "value" );
  
    let append_numeric = '';
  
    d3.select( "#append-numeric" ).selectAll( "span" ).each( function () {
      append_numeric = append_numeric + d3.select( this ).attr( "data-number" );
    } );
  
    const $signup = d3.select( "#sign_up_as" ).select( "p" );
    if (!$signup.empty()) {
      $signup.remove();
    }
  
    $join = d3.select( "#sign_up_as" ) // CREATE FORM BUTTON
    .selectAll( '.signup-button' )
    .data( [ `${val_nn}${val_color}${append_numeric}` ] );
    
    $join.exit().remove();
    $join
      .enter()
      .append("p")
      .attr(
        "class",
        "text-md text-center text-italic mb-0"
        )
      .text((d) => `How about ${d} for temporary username?`)
      ;
      
      
      $form = d3.select( "#regpub-form" )
      .data( [ `${val_nn}${val_color}${append_numeric}` ] );
      $form
      .attr( "action", ( d ) => `/reg/post/public/${d}` );
  }
