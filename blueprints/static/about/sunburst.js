$( document ).ready( () => {
  
  console.log( 'test :>> ' );
  sunBurnMeUp();
  
  function sunBurnMeUp () {
    var labels = ['Guest', 'User', 'Member', 'admin'];
    var parents = ["", "Guest", "User", "Member", "admin"];
    var data = [{
      type: "sunburst",
      labels: labels,
      parents: parents,
      values: [54, 24, 12, 12, 6, 6],
      outsidetextfont: {
        size: 12,
        color: "#377eb8"
      },
      leaf: {
        opacity: 0.4
      },
      marker: {
        line: {
          width: 2
        }
      },
    } ];
      
    var layout = {
      plot_bgcolor: "rgb(255,255,255,0)",
      paper_bgcolor: "rgb(255,255,255,0)",
      responsive: true,
      margin: {
        l: 0,
        r: 0,
        b: 0,
        t: 0,
      },
      padding: {
        l: 0,
        r: 0,
        b: 0,
        t: 0,
      },
      sunburstcolorway: [
        "#78c2ad",
        "#00ddc9",
        "#B58900",
        "#636efa",
        "#EF553B",
        "#6610f2",
        "#6f42c1",
      ],
      extendsunburstcolorway: true,
    };
    Plotly.newPlot('sunburst', data, layout);
  }
  
});
