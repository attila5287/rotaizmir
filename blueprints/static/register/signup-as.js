// d3.select('#input-color')
// d3.select('#lucky-number')
val_nn = d3.select( "#input-nickname" )
  .select( "input" )
  .attr("value")
  ;
val_color = '-'+d3.select( "#input-color" )
  .select( "input" )
  .attr("value")
  ;

let append_numeric = '-';
 d3.select( "#append-numeric" ).selectAll( "span" ).each( function () {
   append_numeric = append_numeric + d3.select(this).attr("data-number");
 } );

d3.selectAll( '.evt-clk' )
  .on( "click", function ( ) {
    console.log('test :>> ');
  } );

 

 
 
 
 
 let img_index = 0;
d3.select( "#sign_up_as" ) // CREATE FORM BUTTON
  .text( `Sign Up As: ${val_nn}${val_color}` )
  .attr( "href", `/reg/post/${val_nn}${val_color}${append_numeric}/${img_index}` );



