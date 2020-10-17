// d3.select('#input-color')
// d3.select('#lucky-number')
$input_nn = d3.select( "#input-nickname" )
  .select( "input" )
  .attr("value")
  ;
$input_clr = d3.select( "#input-color" )
  .select( "input" )
  .attr("value")
  ;
$append_num = d3.select( "#append-numeric" ).selectAll( "span" ).each( function () {
  console.log("d.value :>> ", this["cup-end"]);
} );

console.log('inp :>> ', $input_nn);
console.log( 'inp :>> ', $input_clr );
d3.select( "#sign_up_as" )
  .text( `Sign Up As: ${$input_nn}${$input_clr}` )
  .attr("href", `/add/member/${$input_nn}${$input_clr}${$append_num}`);

    console.log('d3.event.target :>> ', this.value());
  })
