// generate random id within n_population boundaries



d3.json( '/nicknames/api', function ( err, data ) {

  const n = Object.keys( data ).length;

  let genRandID = ( n_samples ) => Math.floor( Math.random() * n_samples );
  
  $nick = d3.select( '#nickname_on_air' );
    

  d3.select( "#generator-btn" ).on( "click", () => {

    d3.select( "#username" ).attr( "data", genRandID( n ) );
    
  });

});
