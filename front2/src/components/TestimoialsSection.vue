<template>
	<!-- 통계 - 전체기간 중 가장인기있는 상품 -->
<section class="page-section testimonials bg-light" id="go_stat">
<div class="text-center wow fadeIn">
      <h2>통계 보기</h2>
      <hr class="colored">
</div>
<hr/>
<h3>전체 기간 선호 상품</h3>
<hr/>
<span>
<div >1위</div>
<svg id="fillgauge2" width="100%" height="200"></svg>
<div style="color: #FF4444">
	{{Data_name[0]}}
</div>
</span>
<span>
<div>2위</div>
<svg id="fillgauge3" width="100%" height="200"></svg>
<div style="color: #553300">
	{{Data_name[1]}}
</div>
</span>
<span>
<div>3위</div>
<svg id="fillgauge5" width="100%" height="200"></svg>
<div style="color: #555500">
	{{Data_name[2]}}
	</div>
</span>

<!-- 통계 - 최근 6개월간 가장 인기있는 상품-->
<hr/>
<h3>
	최근 6개월 선호 상품
</h3>
<hr/>
<span>
<div>1위</div>
<svg id="fillgauge22" width="100%" height="200"></svg>
<div style="color: #FF4444">
	{{Data_name[3]}}
</div>
</span>
<span>
<div>2위</div>
<svg id="fillgauge33" width="100%" height="200"></svg>
<div style="color: #553300">
	{{Data_name[4]}}
</div>
</span>
<span>
<div>3위</div>
<svg id="fillgauge55" width="100%" height="200"></svg>
<div style="color: #555500">
	{{Data_name[5]}}
</div>
</span>
<hr/>
</section>
</template>

<script>
import axios from 'axios'
export default{
	data(){
		return{ 
			Data_name : []
			}
	},
	methods:{

	},
	mounted:function(){
		var Data_name = this.Data_name;
		axios({
			method:'get',
			url:'http://localhost:3000/api/process/list_statistic'
		   
		})
		.then(function(response){
			console.log('응답받음');
			var Data = {
				fi: response.data.data1[0].m1_num / response.data.data1[0].total,
				se: response.data.data1[0].m2_num / response.data.data1[0].total,
				th: response.data.data1[0].m3_num / response.data.data1[0].total,
				fi2: response.data.data1[1].m1_num / response.data.data1[1].total,
				se2: response.data.data1[1].m2_num / response.data.data1[1].total,
				th2: response.data.data1[1].m3_num / response.data.data1[1].total
			};
			console.log(response.data.data1);
			for(var i = 0; i<response.data.data2.length; i++){
			  if(response.data.data2[i].loan_good_num == response.data.data1[0].m1_loan_good_num ){
				Data_name.push(response.data.data2[i].loan_good_name);
			  }
			}

			for(var i = 0; i<response.data.data2.length; i++){
			  if(response.data.data2[i].loan_good_num == response.data.data1[0].m2_loan_good_num ){
				Data_name.push(response.data.data2[i].loan_good_name);
			  }
			}

			for(var i = 0; i<response.data.data2.length; i++){
			  if(response.data.data2[i].loan_good_num == response.data.data1[0].m3_loan_good_num ){
				Data_name.push(response.data.data2[i].loan_good_name);
			  }
			}

			for(var i = 0; i<response.data.data2.length; i++){
			  if(response.data.data2[i].loan_good_num == response.data.data1[1].m1_loan_good_num ){
				Data_name.push(response.data.data2[i].loan_good_name);
			  }
			}

			for(var i = 0; i<response.data.data2.length; i++){
			  if(response.data.data2[i].loan_good_num == response.data.data1[1].m2_loan_good_num ){
				Data_name.push(response.data.data2[i].loan_good_name);
			  }
			}

			for(var i = 0; i<response.data.data2.length; i++){
			  if(response.data.data2[i].loan_good_num == response.data.data1[1].m3_loan_good_num ){
				Data_name.push(response.data.data2[i].loan_good_name);
			  }
			}





			function liquidFillGaugeDefaultSettings() {
			return {
				minValue: 0, // The gauge minimum value.
				maxValue: 100, // The gauge maximum value.
				circleThickness: 0.05, // The outer circle thickness as a percentage of it's radius.
				circleFillGap: 0.05, // The size of the gap between the outer circle and wave circle as a percentage of the outer circles radius.
				circleColor: "#178BCA", // The color of the outer circle.
				waveHeight: 0.05, // The wave height as a percentage of the radius of the wave circle.
				waveCount: 1, // The number of full waves per width of the wave circle.
				waveRiseTime: 1000, // The amount of time in milliseconds for the wave to rise from 0 to it's final height.
				waveAnimateTime: 18000, // The amount of time in milliseconds for a full wave to enter the wave circle.
				waveRise: true, // Control if the wave should rise from 0 to it's full height, or start at it's full height.
				waveHeightScaling: true, // Controls wave size scaling at low and high fill percentages. When true, wave height reaches it's maximum at 50% fill, and minimum at 0% and 100% fill. This helps to prevent the wave from making the wave circle from appear totally full or empty when near it's minimum or maximum fill.
				waveAnimate: true, // Controls if the wave scrolls or is static.
				waveColor: "#178BCA", // The color of the fill wave.
				waveOffset: 0, // The amount to initially offset the wave. 0 = no offset. 1 = offset of one full wave.
				textVertPosition: .5, // The height at which to display the percentage text withing the wave circle. 0 = bottom, 1 = top.
				textSize: 1, // The relative height of the text to display in the wave circle. 1 = 50%
				valueCountUp: true, // If true, the displayed value counts up from 0 to it's final value upon loading. If false, the final value is displayed.
				displayPercent: true, // If true, a % symbol is displayed after the value.
				textColor: "#045681", // The color of the value text when the wave does not overlap it.
				waveTextColor: "#A4DBf8" // The color of the value text when the wave overlaps it.
			};
		}

		function loadLiquidFillGauge(elementId, value, config, t) {
			if (config == null) config = liquidFillGaugeDefaultSettings();

			var gauge = d3.select("#" + elementId);
			var radius = Math.min(parseInt(gauge.style("width")), parseInt(gauge.style("height"))) / 2;
			var locationX = parseInt(gauge.style("width")) / 2 - radius;
			var locationY = parseInt(gauge.style("height")) / 2 - radius;
			var fillPercent = Math.max(config.minValue, Math.min(config.maxValue, value)) / config.maxValue;

			var waveHeightScale;
			if (config.waveHeightScaling) {
				waveHeightScale = d3.scale.linear()
					.range([0, config.waveHeight, 0])
					.domain([0, 50, 100]);
			} else {
				waveHeightScale = d3.scale.linear()
					.range([config.waveHeight, config.waveHeight])
					.domain([0, 100]);
			}

			var textPixels = (config.textSize * radius / 2);
			var textFinalValue = parseFloat(value).toFixed(2);
			var textStartValue = config.valueCountUp ? config.minValue : textFinalValue;
			var percentText = config.displayPercent ? "%" : "";
			var circleThickness = config.circleThickness * radius;
			var circleFillGap = config.circleFillGap * radius;
			var fillCircleMargin = circleThickness + circleFillGap;
			var fillCircleRadius = radius - fillCircleMargin;
			var waveHeight = fillCircleRadius * waveHeightScale(fillPercent * 100);

			var waveLength = fillCircleRadius * 2 / config.waveCount;
			var waveClipCount = 1 + config.waveCount;
			var waveClipWidth = waveLength * waveClipCount;

			// Rounding functions so that the correct number of decimal places is always displayed as the value counts up.
			var textRounder = function(value) {
				return Math.round(value);
			};
			if (parseFloat(textFinalValue) != parseFloat(textRounder(textFinalValue))) {
				textRounder = function(value) {
					return parseFloat(value).toFixed(1);
				};
			}
			if (parseFloat(textFinalValue) != parseFloat(textRounder(textFinalValue))) {
				textRounder = function(value) {
					return parseFloat(value).toFixed(2);
				};
			}

			// Data for building the clip wave area.
			var data = [];
			for (var i = 0; i <= 40 * waveClipCount; i++) {
				data.push({
					x: i / (40 * waveClipCount),
					y: (i / (40))
				});
			}

			// Scales for drawing the outer circle.
			var gaugeCircleX = d3.scale.linear().range([0, 2 * Math.PI]).domain([0, 1]);
			var gaugeCircleY = d3.scale.linear().range([0, radius]).domain([0, radius]);

			// Scales for controlling the size of the clipping path.
			var waveScaleX = d3.scale.linear().range([0, waveClipWidth]).domain([0, 1]);
			var waveScaleY = d3.scale.linear().range([0, waveHeight]).domain([0, 1]);

			// Scales for controlling the position of the clipping path.
			var waveRiseScale = d3.scale.linear()
				// The clipping area size is the height of the fill circle + the wave height, so we position the clip wave
				// such that the it will overlap the fill circle at all when at 0%, and will totally cover the fill
				// circle at 100%.
				.range([(fillCircleMargin + fillCircleRadius * 2 + waveHeight), (fillCircleMargin - waveHeight)])
				.domain([0, 1]);
			var waveAnimateScale = d3.scale.linear()
				.range([0, waveClipWidth - fillCircleRadius * 2]) // Push the clip area one full wave then snap back.
				.domain([0, 1]);

			// Scale for controlling the position of the text within the gauge.
			var textRiseScaleY = d3.scale.linear()
				.range([fillCircleMargin + fillCircleRadius * 2, (fillCircleMargin + textPixels * 0.7)])
				.domain([0, 1]);

			// Center the gauge within the parent SVG.
			var gaugeGroup = gauge.append("g")
				.attr('transform', 'translate(' + locationX + ',' + locationY + ')');

			// Draw the outer circle.
			var gaugeCircleArc = d3.svg.arc()
				.startAngle(gaugeCircleX(0))
				.endAngle(gaugeCircleX(1))
				.outerRadius(gaugeCircleY(radius))
				.innerRadius(gaugeCircleY(radius - circleThickness));
			gaugeGroup.append("path")
				.attr("d", gaugeCircleArc)
				.style("fill", config.circleColor)
				.attr('transform', 'translate(' + radius + ',' + radius + ')');

			// Text where the wave does not overlap.
			var text1 = gaugeGroup.append("text")
				.text(textRounder(textStartValue) + percentText)
				.attr("class", "liquidFillGaugeText")
				.attr("text-anchor", "middle")
				.attr("font-size", textPixels + "px")
				.style("fill", config.textColor)
				.attr('transform', 'translate(' + radius + ',' + textRiseScaleY(config.textVertPosition) + ')');

			// The clipping wave area.
			var clipArea = d3.svg.area()
				.x(function(d) {
					return waveScaleX(d.x);
				})
				.y0(function(d) {
					return waveScaleY(Math.sin(Math.PI * 2 * config.waveOffset * -1 + Math.PI * 2 * (1 - config.waveCount) + d.y * 2 * Math.PI));
				})
				.y1(function(d) {
					return (fillCircleRadius * 2 + waveHeight);
				});
			var waveGroup = gaugeGroup.append("defs")
				.append("clipPath")
				.attr("id", "clipWave" + elementId);
			var wave = waveGroup.append("path")
				.datum(data)
				.attr("d", clipArea)
				.attr("T", 0);

			// The inner circle with the clipping wave attached.
			var fillCircleGroup = gaugeGroup.append("g")
				.attr("clip-path", "url(#clipWave" + elementId + ")");
			fillCircleGroup.append("circle")
				.attr("cx", radius)
				.attr("cy", radius)
				.attr("r", fillCircleRadius)
				.style("fill", config.waveColor);

			// Text where the wave does overlap.
			var text2 = fillCircleGroup.append("text")
				.text(textRounder(textStartValue) + percentText)
				.attr("class", "liquidFillGaugeText")
				.attr("text-anchor", "middle")
				.attr("font-size", textPixels + "px")
				.style("fill", config.waveTextColor)
				.attr('transform', 'translate(' + radius + ',' + textRiseScaleY(config.textVertPosition) + ')');

			// Make the value count up.
			if (config.valueCountUp) {
				var textTween = function() {
					var i = d3.interpolate(this.textContent, textFinalValue);
					return function(t) {
						this.textContent = textRounder(i(t)) + percentText;
					}
				};
				text1.transition()
					.duration(config.waveRiseTime)
					.tween("text", textTween);
				text2.transition()
					.duration(config.waveRiseTime)
					.tween("text", textTween);
			}
			// Make the wave rise. wave and waveGroup are separate so that horizontal and vertical movement can be controlled independently.
			var waveGroupXPosition = fillCircleMargin + fillCircleRadius * 2 - waveClipWidth;
			if (config.waveRise) {
				waveGroup.attr('transform', 'translate(' + waveGroupXPosition + ',' + waveRiseScale(0) + ')')
					.transition()
					.duration(config.waveRiseTime)
					.attr('transform', 'translate(' + waveGroupXPosition + ',' + waveRiseScale(fillPercent) + ')')
					.each("start", function() {
						wave.attr('transform', 'translate(1,0)');
					}); // This transform is necessary to get the clip wave positioned correctly when waveRise=true and waveAnimate=false. The wave will not position correctly without this, but it's not clear why this is actually necessary.
			} else {
				waveGroup.attr('transform', 'translate(' + waveGroupXPosition + ',' + waveRiseScale(fillPercent) + ')');
			}
			if (config.waveAnimate) animateWave();
			function animateWave() {
				wave.attr('transform', 'translate(' + waveAnimateScale(wave.attr('T')) + ',0)');
				wave.transition()
					.duration(config.waveAnimateTime * (1 - wave.attr('T')))
					.ease('linear')
					.attr('transform', 'translate(' + waveAnimateScale(1) + ',0)')
					.attr('T', 1)
					.each('end', function() {
						wave.attr('T', 0);
						animateWave(config.waveAnimateTime);
					});
			}
		}
		function dashboard_list(Data) {
			var config1 = liquidFillGaugeDefaultSettings();
			config1.circleColor = "#FF7777";
			config1.textColor = "#FF4444";
			config1.waveTextColor = "#FFAAAA";
			config1.waveColor = "#FFDDDD";
			config1.circleThickness = 0.2;
			config1.textVertPosition = 0.8;
			config1.waveHeight = 0.05;
			config1.waveAnimateTime = 1000;
			var gauge2 = loadLiquidFillGauge("fillgauge2", Data.fi * 100, config1);
			var config2 = liquidFillGaugeDefaultSettings();
			config2.circleColor = "#D4AB6A";
			config2.textColor = "#553300";
			config2.waveTextColor = "#805615";
			config2.waveColor = "#AA7D39";
			config2.circleThickness = 0.1;
			config2.circleFillGap = 0.2;
			config2.textVertPosition = 0.8;
			config2.waveAnimateTime = 2000;
			config2.waveHeight = 0.05;
			config2.waveCount = 1;
			var gauge3 = loadLiquidFillGauge("fillgauge3", Data.se * 100, config2);
			var config4 = liquidFillGaugeDefaultSettings();
			config4.circleThickness = 0.15;
			config4.circleColor = "#808015";
			config4.textColor = "#555500";
			config4.waveTextColor = "#FFFFAA";
			config4.waveColor = "#AAAA39";
			config4.textVertPosition = 0.8;
			config4.waveAnimateTime = 1000;
			config4.waveHeight = 0.05;
			config4.waveAnimate = true;
			config4.waveRise = false;
			config4.waveHeightScaling = false;
			config4.waveOffset = 0.25;
			config4.textSize = 0.75;
			config4.waveCount = 3;
			var gauge5 = loadLiquidFillGauge("fillgauge5", Data.th * 100, config4);

			var config11 = liquidFillGaugeDefaultSettings();
			config11.circleColor = "#FF7777";
			config11.textColor = "#FF4444";
			config11.waveTextColor = "#FFAAAA";
			config11.waveColor = "#FFDDDD";
			config11.circleThickness = 0.2;
			config11.textVertPosition = 0.8;
			config11.waveHeight = 0.05;
			config11.waveAnimateTime = 1000;
			var gauge22 = loadLiquidFillGauge("fillgauge22", Data.fi2 * 100, config11);
			var config22 = liquidFillGaugeDefaultSettings();
			config22.circleColor = "#D4AB6A";
			config22.textColor = "#553300";
			config22.waveTextColor = "#805615";
			config22.waveColor = "#AA7D39";
			config22.circleThickness = 0.1;
			config22.circleFillGap = 0.2;
			config22.textVertPosition = 0.8;
			config22.waveAnimateTime = 2000;
			config22.waveHeight = 0.05;
			config22.waveCount = 1;
			var gauge33 = loadLiquidFillGauge("fillgauge33", Data.se2 * 100, config22);
			var config44 = liquidFillGaugeDefaultSettings();
			config44.circleThickness = 0.15;
			config44.circleColor = "#808015";
			config44.textColor = "#555500";
			config44.waveTextColor = "#FFFFAA";
			config44.waveColor = "#AAAA39";
			config44.textVertPosition = 0.8;
			config44.waveAnimateTime = 1000;
			config44.waveHeight = 0.05;
			config44.waveAnimate = true;
			config44.waveRise = false;
			config44.waveHeightScaling = false;
			config44.waveOffset = 0.25;
			config44.textSize = 0.75;
			config44.waveCount = 3;
			var gauge55 = loadLiquidFillGauge("fillgauge55", Data.th2 * 100, config44);
		}
		dashboard_list(Data);
		})
	}
}
</script>

<style>
		.liquidFillGaugeText {
			font-family: Helvetica;
			font-weight: bold;
			align-content: center;
		}

		span {
			display: inline-block;
		}

		div {
			font-family: Helvetica;
			font-weight: bold;
			text-align: center;
		}
		
		p {
			text-align: center;
			font-family: Helvetica;
			font-weight: bold;
			align-content: center;
		}
	</style>