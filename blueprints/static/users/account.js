const $btn = d3.select("#set-as-profile-pic");
let generated_randint = Math.floor( Math.random() * 70 );
const web =
  "https://raw.githubusercontent.com/attila5287/regropoly-img/master/avatars/";

const ext = ".png";
d3.select("#img_url").attr("data", generated_randint);

d3.select( '#img_url' ).on( 'change', function () {
  console.log("<<:img_url test :>> ");
  
  d3.select( "#img_on_air" )
    .select( "img" )
    .attr( "class", "card-img bg-transparent border-0" )
    .attr( "src", `${web}${this.value}${ext}` );
} );

d3.select( "#img_on_air" ).on( "click", function () {
  d3.event.preventDefault();
  generated_randint = Math.floor( Math.random() * 70 );

  d3.select( "#img_url" )
    .attr( "data", generated_randint );

  d3.select( "#img_on_air" )
    .select( "img" )
    .attr( "class", "card-img bg-transparent border-0" )
    .attr( "src", `${web}${generated_randint}${ext}` );

  d3.select( "#img_url_index" )
    .selectAll( ".index" )
    .remove();

  $index = d3.select( '#img_url_index' )
    .selectAll( '.index' )
    .data( [ generated_randint ] );

  $index
    .enter()
    .append( "div" )
    .transition()
    .ease( d3.easeElastic )
    .duration( 500 )
    .attr( "class", "index" )
    .text( ( d ) => {
      console.log( "d :>> ", d );
      return d;
    } );
  
  


  console.log('$btn :>> ', $btn.attr("data-title") ); 
  
  $btn.attr("href", `${$btn.attr("data-title")}${generated_randint}`);
  
  
} );


$btn.attr("href", `${$btn.attr("data-title")}${generated_randint}`);
