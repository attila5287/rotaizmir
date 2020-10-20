
// d3.selectAll( '.custrange-vertical' )
//   .each( () => {
//     console.log( 'object :>> ' );
//     d3.select( this )
//       .on( "input", function ( event ) {
//         let val = d3.event.target.value;
//         console.log( 'val :>> ', val );
//         let val2 = d3.select("#input-color")
//           .attr( "value" );
        
//         console.log('val2 :>> ', val2);
//   } )
//   } )
//   ;
  
// d3.selectAll( '.evt-clk' )
//   .each( function () {
//     console.log( 'test evl sel :>> ' );
//     d3.select( this ).on( "click", function ( event ) {
//       let btn_id = d3.event.target.id;
//       console.log('btn_id :>> ', btn_id);
//     } );
//   } );
// d3.select('#input-color')
// d3.select('#lucky-number')

render_signup();

function render_signup () {
  val_nn = d3.select( "#input-nickname" )
    .select( "input" )
    .attr( "value" );
  val_color = '' + d3.select( "#input-color" )
    .select( "input" )
    .attr( "value" );

  let append_numeric = '';

  d3.select( "#append-numeric" ).selectAll( "span" ).each( function () {
    append_numeric = append_numeric + d3.select( this ).attr( "data-number" );
  } );

  const $signup = d3.select( "#sign_up_as" ).select( "a" );
  if (!$signup.empty()) {
    $signup.remove();
  }

  $join = d3.select( "#sign_up_as" ) // CREATE FORM BUTTON
  .selectAll( '.signup-button' )
  .data( [ `${val_nn}${val_color}${append_numeric}` ] );
  
  $join.exit().remove();
  $join
    .enter()
    .append("div")
    .attr("class", "row")
    .append("div")
    .attr("class", "col-10 offset-1")

    .append("a")
    .transition()
    .duration(5000)
    .attr(
      "class",
      "btn btn-outline-info btn-block text-xl text-light border-0 bg-themy rnd-2xl pt-1 pb-2"
    )
    .attr("type", "button")
    .text((d) => `Sign Up As: ${d}`)
    .attr( "href", ( d ) => `/reg/post/public/${d}` )
    ;
    
    
    $form = d3.select( "#regpub-form" )
    .data( [ `${val_nn}${val_color}${append_numeric}` ] );
    $form
    .attr( "action", ( d ) => `/reg/post/public/${d}` );
}

