const random_append = () => Math.round( Math.random() * 9 );
// console.log('random_append() :>> ', random_append());

data = [];
[1,2,3,4].forEach( ( v ) => {
  data.push(random_append())
} )
// console.log('data :>> ', data);

data.forEach( ( value, index, array ) => {
  d3.select("#append-numeric")
    .append("span")
    .classed(`countup led-xl text-light text-nowrap part${index}`, true)
    .html(+value)
    .attr("cup-start", 0)
    .attr("data-number", +value)
    .attr("cup-end", +value)
    .attr("cup-prepend", "");

})
