
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
      "text-md text-center text-italic text-light mb-0"
      )
    .text((d) => `How about ${d} for temporary username?`)
    ;
    
    
    $form = d3.select( "#regpub-form" )
    .data( [ `${val_nn}${val_color}${append_numeric}` ] );
    $form
    .attr( "action", ( d ) => `/reg/post/public/${d}` );
}

