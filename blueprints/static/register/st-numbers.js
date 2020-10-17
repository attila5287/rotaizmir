
function prepStateDemo( state ) { // data prep for demographic
  const fPerct = d3.format( ".4" );
  const fComma = d3.format( "," );

  const selected = { // numeric columns
    'whitePerc':diversityPart1[state].white,
    'minTotal':diversityPart1[ state ].minTotal+1,
    'hispPerc':diversityPart1[ state ].hisp,
    'blackPerc': diversityPart2[ state ].black,
    'asianPerc': diversityPart2[ state ].asian,
    'nativePerc': diversityPart2[ state ].native,
  };
  
  const numcols = [ // numeric columns
    'whitePerc',
    'minTotal',
    'hispPerc',
    'blackPerc',
    'asianPerc',
    'nativePerc',
  ];

  const labels = { // numeric labels
    'whitePerc': 'White',
    'minTotal': 'Minority Total',
    'hispPerc': 'Hispanic',
    'blackPerc': 'African-American',
    'asianPerc': 'Asian',
    'nativePerc': 'Native',
  };

  const prepends = { // before the animated part
    'whitePerc': '',
    'minTotal': '',
    'hispPerc': '',
    'blackPerc': '',
    'asianPerc': '',
    'nativePerc': '',
  };

  const appends = { // after the animated part
    'whitePerc': ' %',
    'minTotal': ' %',
    'hispPerc': ' %',
    'blackPerc': ' %',
    'asianPerc': ' %',
    'nativePerc': ' %',
  };

  let result = [];

  numcols.forEach( d => {
    let obj = {};
    obj[ 'label' ] = labels[ d ];
    obj[ 'value' ] = +selected[ d ];
    obj[ 'prepend' ] = prepends[ d ];
    obj[ 'append' ] = appends[ d ];

    result.push( obj );
  } );

  // console.log( 'result :>> ', result[ 3 ] );
  
  // console.log( 'result :>> ', result );
  return result;
}

function prepStateMain( state ) { // data prep array of objs
  const fPerct = d3.format( ".4" );
  const fComma = d3.format( "," );

  const compiled = {
    'numOfSeat' : +seatsByState[ state ], 
    'over18Perc': +over18PercBySt[ state ],
    'medHHI' : Math.floor(+medianHHIbySt[ state ]/1000), 
    'medAge': +medAgeBySt[ state ], 
    'minWage': +minWageBySt[ state ], 
  };

  const numcols = [ // st numeric columns
    'numOfSeat',
    'over18Perc',
    'medHHI',
    'medAge',
    'minWage',
  ];

  const labels = { // labels 
    'numOfSeat': 'Num House Seats',
    'over18Perc': 'Pop.Over18',
    'medHHI': 'Mdn.Household Income',
    'medAge': 'Median Age',
    'minWage': 'Minimum Wage',
  };

  const prepends = { //before countup not animated 
    'numOfSeat': '',
    'over18Perc': '',
    'medHHI': '$ ',
    'medAge': '',
    'minWage': '$ ',
  };

  const appends = { // after the countup not animated
    'numOfSeat': '',
    'over18Perc': ' %',
    'medHHI': afterThousands(+medianHHIbySt[ state ]),
    'medAge': ' yrs.',
    'minWage': ' /hr',
  };

  function afterThousands(number) {
    const comma = ", ";
    const zero = "0";
    
    if(number%1000 == +number%10){
      return comma+zero+zero+number%1000;
    }
    
    if(number%1000 == +number%100){
      return comma+zero+number%1000;
    }
    return ", "+number%1000;
  };


  let result = [];
  numcols.forEach( d => {
    let obj = {};
    obj[ 'value' ] = +compiled[ d ];
    obj[ 'label' ] = labels[ d ];
    obj[ 'prepend' ] = prepends[ d ];
    obj[ 'append' ] = appends[ d ];

    result.push( obj );
  } );
  // console.log( 'result :>> ', result[ 3 ] );
  // console.log( 'result :>> ', result );
  return result;
}

// renderStateMain( prepStateMain( "Colorado" ) );
// renderStateDemo( prepStateDemo( "Colorado" ) );

function renderStateDemo ( dataReady ) { // countup st demographic
  // console.log('dataReady :>> ', dataReady);
  d3.select("#hldr-diversity").selectAll("li").selectAll("span").remove();
  d3.select("#hldr-diversity").selectAll("li").remove();

  dataReady.forEach(d => {
    // console.log('d :>> ', d);
    var li = d3.select("#hldr-diversity").append("li").classed('nav-item bg-transparent text-sm py-0 text-break',true);
    li.text(d.label)
    .classed( 'text-light text-break', true )
      ;
    li.append( "span" )
      .classed( 'countup led-sm text-primary', true )
      .html(d.value + " %")
      .attr( 'cup-start', 0 )
      .attr( 'cup-end', d.value )
      .attr( 'cup-prepend', d.prepend )
      .attr( 'cup-append', d.append )
      ;
  });

} 

function renderStateMain ( dataReady ) { // countup st main numbers
  // console.log('dataReady :>> ', dataReady);
  d3.select("#hlder-main").selectAll("li").selectAll("span").remove();
  d3.select("#hlder-main").selectAll("li").remove();
  dataReady.forEach(d => {
    // console.log('d :>> ', d);
    var li = d3.select("#hlder-main").append("li").classed('list-group-item bg-transparent text-right text-sm py-0',true);
    li.text(d.label)
    .classed( 'text-light', true )
      ;
    li.append( "span" )
      .classed( 'countup led-md text-primary text-nowrap', true )
      .html(d.value )
      .attr( 'cup-start', 0 )
      .attr( 'cup-end', d.value )
      .attr( 'cup-prepend', d.prepend )
      .attr( 'cup-append', d.append )
      ;

    
  });

} 
