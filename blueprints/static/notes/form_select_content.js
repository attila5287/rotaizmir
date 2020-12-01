console.log('content')
let status_styles = {
  "declined": "secondary",
  "approved": "primary",
  "pending": "info",
};
d3.selectAll( ".select_status" )
  .on('change', () => {
    let selected_value = d3.event.target.value;
    let search_term = d3.event.target.dataset.search_term;

    d3.select(`#panel_${search_term}`).classed(
      `bg-${status_styles[selected_value]} text-light`,
      true
    );
    let panel_icon = d3.select( `#panelicon_${search_term}` );
    panel_icon.select( 'img' ).remove();
    panel_icon
      .append( 'i' )
      .attr('fas fa-stamp')
    ;
    
      panel_icon.classed(
        `bg-${status_styles[selected_value]} text-light`,
        true
      );


  }

  );
