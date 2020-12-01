const msg = "welcome";
console.log( 'msg :>> ', msg );

let filtered = {
  a: "admin",
  m: "member",
  p: "prez",
};
let categories = [
  'm',
  'a',
  'p',
];
let styles = {
  a: "secondary",
  m: "primary",
  p: "info",
};


d3.selectAll( ".filter_btn" )
  .on( 'click', () => {
    generate_filter_btn();
  } );

function generate_filter_btn() {
  let selected = d3.event.target.dataset.category;
  let selected_name = d3.event.target.dataset.name;
  let selected_box = d3.select( `#filter_box_${selected}` );
  let selected_icon = d3.select( `#filter_icon_${selected}` );
  console.log( 'selected :>> ', selected );

  categories.forEach( ( category ) => {

    if ( category == selected ) {
      selected_box.selectAll( `.filter_btn` ).remove();

      if ( filtered[ category ] == null ) {

        console.log( "filter in" );
        filtered[ category ] = selected_name;

        selected_box
          .append( "div" )
          .attr( "data-category", selected )
          .attr( "data-name", selected_name )
          .attr(
            "class",
            `filter_btn filter_btn_${selected} btn btn-block btn-${styles[ category ]}`
          )
          .text( 'filter out' );

        selected_icon
          .attr( "class", "mb-0 opac-100" );

      } else {
        console.log( "filter out" );
        selected_box
          .append( "div" )
          .attr( "data-category", selected )
          .attr( "data-name", selected_name )
          .attr(
            "class",
            `filter_btn filter_btn_${selected} btn btn-block btn-outline-${styles[ category ]}`
          )
          .text( "filter in" );
        selected_icon.attr( "class", "mb-0 opac-40" );

        delete filtered[ category ];
      }

      selected_box.select( '.filter_btn' ).on( 'click', () => generate_filter_btn() );

    } else {
      // console.log( 'not selected' );
    }

    let new_categories = Object.keys( filtered ).join( "" );
    let new_catnames = Object.keys( filtered )
      .map( ( k ) => filtered[ k ] )
      .join( ", " );

    console.log( 'new_cat :>> ', new_categories );
    d3.select( "#filter_submit_box" )
      .selectAll( ".filter_submit_btn" )
      .remove();

    if ( new_categories != '' ) {
      console.log( 'if no cats selected' )
      d3.select( "#filter_submit_box" )
        .append( "a" )
        .attr(
          "class",
          "filter_submit_btn btn btn-primary btn-block text-lg text-comfo shadow mt-1"
        )
        .attr( "id", "filter_submit_btn" )
        .attr( "href", `/admin/${new_categories}/requests` )
        .text( new_catnames );

      const default_msg = 'included categories';

      d3.select( "#filtered_categories" )
        .attr( "class", "text-italic text-center mb-1 mt-2" )
        .text( default_msg );

    } else {

      const warning_msg = "No Categories Included!";

      d3.select( "#filtered_categories" )
        .attr( 'class', 'text-secondary mb-1 mt-2' )
        .text( warning_msg );

      let warning_button = d3.select( "#filter_submit_box" )
        .append( "a" )
        .attr(
          "class",
          "filter_submit_btn btn btn-secondary btn-block text-lg text-comfo shadow mt-1 disabled"
        );


      warning_button
        .append( "i" )
        .attr( "class", "fab fa-github text-2xl mr-2" );

      warning_button
        .append( "i" )
        .attr( "class", "text-xl" )
        .text( "need some cats!" );
    }
  } );
}
// icon_box_
