console.log('content')
let status_icons = {
  "declined": "gavel",
  "approved": "stamp",
  "pending": "balance-scale",
};
let status_styles = {
  "declined": "secondary",
  "approved": "primary",
  "pending": "info",
};
let auto_messages = {
  declined: [
    "Feel free to appeal by sending another request.",
    "Don't hesitate to send another request if feels fair.",
    "Unfortunately, denied but could always send a new one. ",
    "Bad news, request denied. Re-send if it doesn't feel right",
  ],
  approved: [
    "Congrats, now check unlocked features of app!",
    "Good news, approved! Enjoy more features! ",
    "Moving up the ladder of auth.levels, approved!",
    "Approved, more features to explore- finally!",
  ],
  pending: [
    "A little patient appreciated, still in review...",
    "Stuck in review, we are only human after all...",
    "Pending, yet not denied-half of the...",
    "Reviewing auth. request, patient is a virtue...",
  ],
};

d3.selectAll( ".select_status" )
  .on( 'change', () => { 
    // pivot variable, pre-req for most----------
    let selected_value = d3.event.target.value;
    let n_pool = auto_messages[ selected_value ].length;
    if (n_pool) {
      n_pool = n_pool - 1;
      
    } 
    let random_index = Math.round(Math.random() * n_pool);
    
    console.log("random_index :>> ", random_index);

    let selected_icon = status_icons[selected_value];
    let selected_style = status_styles[selected_value];
    let search_term = d3.event.target.dataset.search_term;
    
    console.log( "search_term :>> ", search_term );
    
    let panel = d3.select( `#panel_${search_term}` );
    panel.classed(
        `bg-${selected_style} text-light`,
        true
      );
      
    let panel_icon = d3.select( `#panel_iconbox_${search_term}` );
    let panel_header = d3.select( `#panel_header_${search_term}` );

    independent_updates();

    
    d3.selectAll(".change_value").attr(
      "value",
      auto_messages[selected_value][random_index]
    );


    d3.selectAll( ".change_text" ).classed( "text-uppercase", true ).text( selected_value );
    d3.selectAll(".change_btn").attr("class",
      "change_shadow change_btn btn btn-light text-bold text-"+selected_style + " btn-block shadow"
    );
    
    panel
      .attr(
        "class",
        `panel panel-asym shadow-lg pb-4 mb-5 px-0 bg-${selected_style}`
      );
    
    panel_icon.selectAll( 'img' ).remove();
    panel_icon.selectAll( 'i' ).remove();
    

    panel_header.attr(
      "class",
      `panel-header panel-header-${selected_style} panel-header-icon`
    );
    
    // .attr( 'class', 'background-color', )
    panel_icon
      .append("i")
      .attr(
        "class",
        `txt-shd text-light fas fa-${selected_icon} ${selected_style}` );
    
  } );

function independent_updates () {// independent of selection
  d3.selectAll( ".change_border" ).classed( "border-light", true );
  d3.selectAll( ".change_shadow" ).classed( "shadow", false );
  d3.selectAll( ".change_shadow" ).classed( "shd-lite", true );
  d3.selectAll( ".highlight_bg" ).classed( "bg-light rnd-lg px-2 pt-0 pb-2", true );
  d3.selectAll( ".highlight_text" ).classed(
    "text-light",
    true
  );
}
  