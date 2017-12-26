<template>
  <div class="portfolio-modal modal fade" id="portfolioModal1" tabindex="-1" role="dialog" aria-hidden="true" style="background-image: url('./img/agency/backgrounds/Horizon.jpg');height:1000px;width:1000px; margin : auto">
    <div class="modal-dialog" style="margin : auto">
      <div class="modal-content">
        <div class="close-modal" data-dismiss="modal">
          <i class="fa fa-times fa-3x" style="color:black"></i>
        </div>
        <div class="modal-body">
          <div class="container">
            <div class="row">
              <div class="col-md-12">
                <span id="svg_chart" class="chart" style="text-align=center"></span>
              </div>
            <div class="col-md-12">    
              <table v-if="check==0" class="type10">
                <thead>
                  <tr>
                    <th>회차</th>
                    <th><label for="ex1" data-toggle="tooltip" data-placement="top" title="상환금=만기상환이자">상환금</label></th>
                    <th>납부이자</th>
                    <th>납부원금</th>
                    <th>잔금</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="test in calc">
                  <td>{{test.month}}</td>
                  <td>{{Math.round(test.상환금) | currency }}</td>
                  <td>{{Math.round(test.납부이자) | currency }}</td>
                  <td>{{test.납부원금 | currency }}</td>
                  <td>{{test.잔금 | currency }}</td>
                  </tr>
                </tbody>
              </table>
              <table v-else class="type10">
                <thead>
                  <tr>
                    <th>회차</th>
                    <th><label for="ex1" data-toggle="tooltip" data-placement="top" title="상환금=만기상환이자+원리금상환이자+원리금상환원금납입액">상환금</label></th>
                    <th>만기상환<br>이자</th>
                    <th>만기상환<br>잔금</th>
                    <th>원리금상환<br>이자</th>
                    <th>원리금상환<br>원금납입액</th>
                    <th>원리금상환<br>잔금</th>
                  </tr>
                </thead>
                <tbody>
                    <tr v-for="test in calc">
                    <td>{{test.month}}</td>
                    <td>{{Math.round(test.상환금) | currency }}</td>
                    <td>{{Math.round(test.만기상환이자) | currency }}</td>
                    <td>{{Math.round(test.만기상환잔금) | currency }}</td>
                    <td>{{Math.round(test.원리금상환이자) | currency }}</td>
                    <td>{{Math.round(test.원리금상환원금) | currency }}</td>
                    <td>{{Math.round(test.원리금상환잔금) | currency }}</td>
                  </tr>
                </tbody>
              </table>     
            </div>
          </div>
          <div class=".col-md-6 .col-md-offset-3">
            <br><br>
            <button type="button" class="btn btn-primary" data-dismiss="modal" style="color:black">
              <i class="fa fa-times" style></i>
              Close</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>
<script>
$("#svg_chart").empty();
import {bus} from '../bus.js'

export default {
  data () {
    return {
      calc:[],
      test:[],
      check:''
    }
  },
  methods : {
    calculate:function(){
      var margin = {top: 20, right: 200, bottom: 35, left: 80};
      var width = 860 - margin.left - margin.right,
      height = 460 - margin.top - margin.bottom;
      var svg = d3.select(".chart")
      .append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
      .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

      /* Data in strings like it would be if imported from a csv */

      console.log('넣을 test : '+this.test);
      var data = this.test;
      console.log('********************************************');
      console.log('받아온 계산값 : ' +data);

      // Transpose the data into layers
      var dataset = d3.layout.stack()(["만기상환이자", "원리금상환이자", "원리금상환원금"].map(function(fruit) {
        return data.map(function(d) {
          return {x: parseInt(d.month), y: +d[fruit]};
        });
      }));

      // Set x, y and colors
      var x = d3.scale.ordinal()
      .domain(dataset[0].map(function(d) { return d.x; }))
      .rangeRoundBands([10, width-10], 0.02);

      var y = d3.scale.linear()
      .domain([0, d3.max(dataset, function(d) {  return d3.max(d, function(d) { return d.y0 + d.y; });  })])
      .range([height, 0]);

      var colors = ["b33040", "#d25c4d", "#f2b447"];
      // "#d9d574"

      // Define and draw axes
      var yAxis = d3.svg.axis()
      .scale(y)
      .orient("left")
      .ticks(5)
      .tickSize(-width, 0, 0)
      .tickFormat( function(d) { return d/10000 +" 만원"} );

      var xAxis = d3.svg.axis()
      .scale(x)
      .orient("bottom")
      //.tickFormat(d3.time.format("%Y"));

      svg.append("g")
      .attr("class", "y axis")
      .style("color", "white")
      .call(yAxis);

      svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .style("color", "white")
      .call(xAxis);


      // Create groups for each series, rects for each segment 
      var groups = svg.selectAll("g.cost")
      .data(dataset)
      .enter().append("g")
      .attr("class", "cost")
      .style("color", "white")
      .style("fill", function(d, i) { return colors[i]; });

      var rect = groups.selectAll("rect")
      .data(function(d) { return d; })
      .enter()
      .append("rect")
      .attr("x", function(d) { return x(d.x); })
      .attr("y", function(d) { return y(d.y0 + d.y); })
      .attr("height", function(d) { return y(d.y0) - y(d.y0 + d.y); })
      .attr("width", 18)
      .style("color", "white")
      //.attr("width", x.rangeBand())
      .on("mouseover", function() { tooltip.style("display", null); })
      .on("mouseout", function() { tooltip.style("display", "none"); })
      .on("mousemove", function(d) {
      var xPosition = d3.mouse(this)[0] -15;
      var yPosition = d3.mouse(this)[1] -25;
      // var xPosition = d3.mouse(this)[0] - 100;
      // var yPosition = d3.mouse(this)[1] - 200;

      tooltip.attr("transform", "translate(" + xPosition + "," + yPosition + ")");
      console.log('x 표시'+xPosition);
      console.log('y 표시'+yPosition);
      tooltip.select("text").text(d.y);
      });


      // Draw legend
      var legend = svg.selectAll(".legend")
      .data(colors)
      .enter().append("g")
      .attr("class", "legend")
      .style("color", "white")
      .attr("transform", function(d, i) { return "translate(30," + i * 19 + ")"; });
    

      legend.append("rect")
      .attr("x", width - 18)
      .attr("width", 18)
      .attr("height", 18)
      .style("color", "white")
      .style("fill", function(d, i) {return colors.slice().reverse()[i];});

      legend.append("text")
      .attr("x", width + 5)
      .attr("y", 9)
      .attr("dy", ".35em")
      .style("text-anchor", "start")
      .style("color", "white")
      .text(function(d, i) { 
          switch (i) {
                      case 0: return "원리금균등 상환원금";
                      case 1: return "원리금균등 이자";
                      case 2: return "만기이자";
          }
        });

      // Prep the tooltip bits, initial display is hidden
      var tooltip = svg.append("g")
      .attr("class", "tooltip")
      .style("color", "white")
      .style("display", "none");

      tooltip.append("rect")
      .attr("width", 30)
      .attr("height", 20)
      .attr("fill", "white")
      .style("color", "white")
      .style("opacity", 0.5);

      tooltip.append("text")
      .attr("x", 15)
      .attr("dy", "1.2em")
      .style("text-anchor", "middle")
      .style("color", "white")
      .attr("font-size", "12px")
      .attr("font-weight", "bold");
    },
    modal:function(result){
      this.calc = []
      this.test = []
      this.empt();
      console.log('modal data'+result);
      console.log(result[0].repayment);
      this.check = result[0].repayment;
      for(var i=0;i<result.length;i++){
        if(result[0].repayment == 0){
            console.log(result[i].month);
            console.log(result[i].상환금);
            console.log(result[i].납부이자);
            console.log(result[i].납부원금);
            console.log(result[i].잔금);
          this.calc.push(
          {
            month: result[i].month,
            상환금: result[i].상환금,
            납부이자: result[i].납부이자,
            납부원금: result[i].납부원금,
            잔금: result[i].잔금
          }
        )
          this.test.push(
        {
          month: (result[i].month),
          만기상환이자: (result[i].납부이자),
          원리금상환이자: (result[i].원리금상환이자),
          원리금상환원금: (result[i].원리금상환원금)
        })
        }else{
              console.log(result[i].month);
              console.log(result[i].상환금);
              console.log(result[i].만기상환이자);
              console.log(result[i].만기상환잔금);
              console.log(result[i].원리금상환이자);
              console.log(result[i].원리금상환원금);
              console.log(result[i].원리금상환잔금);
        this.calc.push(
          {
            month: result[i].month,
            상환금: result[i].상환금,
            만기상환이자: result[i].만기상환이자,
            만기상환잔금: result[i].만기상환잔금,
            원리금상환이자: result[i].원리금상환이자,
            원리금상환원금: result[i].원리금상환원금,
            원리금상환잔금: result[i].원리금상환잔금
          }
        )
        this.test.push(
          {  
            month: (result[i].month),
            만기상환이자: (result[i].만기상환이자),
            원리금상환이자: (result[i].원리금상환이자),
            원리금상환원금: (result[i].원리금상환원금)
          }
        )}
      }
      this.calculate();
    },
    empt:function(){
      $("#svg_chart").empty();
    }
  },
  created(){
    bus.$on('modal', this.modal)
  }
}
</script>

<style>
table.type10 {
    border-collapse: collapse;
    text-align: left;
    line-height: 1.5;
    border-top: 1px solid #ccc;
    border-bottom: 1px solid #ccc;
    margin: 20px 10px;
}
table.type10 thead th {
    width: 150px;
    padding: 10px;
    font-weight: bold;
    vertical-align: top;
    color: #fff;
    background: #e7708d;
    margin: 20px 10px;
}
table.type10 tbody th {
    width: 150px;
    padding: 10px;
    color:black;
}
table.type10 td {
    width: 350px;
    padding: 10px;
    vertical-align: top;
    color:black;
}
table.type10 .even {
    background: #fdf3f5;
}
.btn-primary{
  color:black;
     border: 1px solid black;
    background-color: transparent;
}
.close {
  color: red;
}
</style>