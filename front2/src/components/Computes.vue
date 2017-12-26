<template>
<!-- 전세추천 계산시 나오는 추천 및 분석 페이지 -->
<section id="nav_computing">
<article class="page-section" id="computing">
<br><br><br><br>
<h2 style="font-size: 40px"> 계산 결과 </h2>
<hr class="colored">
	<div class = "container"> 
		<div class="row" style="text-align : center;" >
			<!-- 나의정보, 상품정보 출력 창 -->    
			<div class="col-sm-5">
				<table class="type09">
					<tr>
						<th scope="row" class="even">거래은행</th>
						<td class="even">{{bank_name}}</td>
					</tr>
					<tr>
						<th scope="row">대출상품명</th>
						<td> {{loan_good_name}}</td>
					</tr>
					<tr>
						<th scope="row" class="even">연봉</th>
						<td class="even">{{cus_salary | currency}}</td>
					</tr>
						<tr>
						<th scope="row">임차보증금</th>
						<td >{{leasing_mortgage | currency}}</td>
					</tr>
						<tr>
						<th scope="row" class="even">대출금액</th>
						<td class="even">{{cus_loan| currency}}</td>
					</tr>
						<tr>
						<th scope="row" >상환방법</th>
						<td>{{repayment_word}}</td>
					</tr>
						<tr>
						<th scope="row" class="even">만기상환 대출금액</th>
						<td class="even">{{repayment_money_s| currency}}</td>
					</tr>
						<tr v-show="repayment===1">
						<th scope="row" >원리금상환 대출금액</th>
						<td>{{repayment_money| currency}}</td>
					</tr>
						<tr>
							<th scope="row" id="go_detail">대출기간</th>
						<td >{{month_loan_period}}</td>
					</tr>
						<tr>
						<th class="even" scope="row">평균금리</th>
						<td class="even">{{avg_int_rat}}</td>
					</tr>
				</table>
			</div>

<!-- 상환분석 창 --> 
			<div v-if="repayment===1" class="col-sm-7">
				<div class="container">
					<table class="type09">
						<thead>
							<tr>
								<th style="text-align:center">상환방식</th>
								<th style="text-align:center">대출금액</th>
								<th style="text-align:center">월 납입액</th>
							</tr>
						</thead>
						<tbody>
							<tr>
								<td>만기상환</td>
								<td>{{repayment_money_s | currency}}</td>
								<td>{{Math.round(s_m_repay_atm) | currency}}(①)</td>
							</tr>
							<tr>
								<td>원리금상환</td>
								<td>{{repayment_money| currency}}</td>
								<td>{{Math.round(p_m_repay_atm)| currency}}</td>
							</tr>
						</tbody>
						<tfoot>
							<tr>
								<td>합산</td>
								<td>{{cus_loan| currency}}</td>
								<td> {{Math.round(s_m_repay_atm+p_m_repay_atm)| currency}}</td>
							</tr>
						</tfoot>
					</table>
					<br>
					<p style="text-align:left">  {{ cus_loan | currency }}을 대출 받았을 때 월 납입 금액은 <span style="color: red">{{ Math.round(s_m_repay_atm+p_m_repay_atm) | currency }}</span>입니다.</p>
					<br>
					<a @click="modalStart" href="#portfolioModal1" data-toggle="modal" class="btn btn-primary" style="color : #EF4035; border-color : #EF4035">월 납입액 자세히보기</a>
					<div style="height : 50px"></div>
					<p> 고객님의 예상 수익률을 입력하시면 월세보증금과 월세를 계산해드립니다.<br><br>고객님의 예상 수익률은?<input v-model.number="i_rate" class="col-sm-2 control-label form-control">% </p>
				</div>
			</div>

			<div v-else class="col-sm-7">
				<table class="type09">
					<thead>
						<tr>
							<th style="text-align:center">상환방식</th>
							<th style="text-align:center">대출금액</th>
							<th style="text-align:center">월 납입액</th>
						</tr>
					</thead>
					<tbody>
						<tr>
							<td>만기상환</td>
							<td>{{repayment_money_s | currency}}</td>
							<td> {{Math.round(s_m_repay_atm) | currency}}(①)</td>
						</tr>		   
					</tbody>
					<tfoot>
						<tr>
							<td>합산</td>
							<td>{{repayment_money_s | currency}}</td>
							<td> {{Math.round(s_m_repay_atm) | currency}}</td>
						</tr>
					</tfoot>
				</table>
				<br>
				<p style="text-align:left">만기 일시 상환방식으로 {{repayment_money_s | currency}}을 대출 받았을 때 <br>월 납입 이자는 <span style="color: red">{{Math.round(s_m_repay_atm) | currency}}</span>입니다.</p>
				<br>
				<a @click="modalStart" href="#portfolioModal1" data-toggle="modal" class="btn btn-primary" style="color : #EF4035; border-color : #EF4035">월 납입액 자세히보기</a>
				<div style="height : 50px"></div>
			</div>
		</div>

	<!-- 전세 vs 월세 화면 -->        
		<div class="col-md-12">		
			<div v-if="repayment===1">
				<div style="border : 1px solid; margin: 0px">		
					<p style="font-size:38px; background-color : #212529; color : white; ">전세 vs 월세</p><br>
					<p v-if="i_rate>0" style="margin: 0px">만약 고객님이 {{month_loan_period}}개월 동안 <span style="color: blue">{{i_rate}}%</span> 수익률을 낼 수 있다면<br>전세보증금 {{leasing_mortgage | currency}} 중 {{cus_loan | currency}}을 대출 받는것은<br>대출없이 보유하고 있는 돈으로 월세 보증금 <span style="color: red">{{Math.round(deposit) | currency}}</span>을 내고<br> 월세 <span style="color: red">{{Math.round(rent) | currency}}</span>에 사는 것과 가치가 동등합니다. </p>
					<p v-else>수익률을 입력하여 주세요</p><br>
				</div><br>
				<a @click="toggleTrue" id = "go_detail2" class="btn btn-xl" style="background : transparent; border : 1px solid" href="#go_detail2">자세히보기</a>  
				<div v-show="toggle==true">
					<div class="container">
						<div class="row">
							<div class="row container" style="margin-top : 30px">
								<div class="col-sm-5">
									<table class="type09" style="height:0%">
										<thead>
											<tr>
												<th style="text-align:center">금액</th>
												<th style="text-align:center">현재가치</th>
											</tr>
										</thead>
											<tr>
												<td style="width:65%">현재 {{repayment_money_s| currency}}</td>
												<td> {{repayment_money_s| currency}}</td>
											</tr>
											<tr>
												<td>{{month_loan_period}}개월 후 {{repayment_money_s| currency}}</td>
												<td>  {{Math.round((cus_loan - repayment_money) *(Math.pow(1 + (n_rate / 100) / 12, -month_loan_period)))| currency}}</td>
											</tr>
											<tr>
												<td>차액</td>
												<td> {{Math.round( (cus_loan - repayment_money) *(1- Math.pow(1 + (n_rate / 100) / 12, -month_loan_period)))| currency}}</td>
											</tr>
										</table>
									</div>
									<div class="col-sm-2" style="margin : auto">
										<i class="fa fa-angle-right fa-4x"></i>
									</div>
									<div class="col-sm-5" style="margin-top : 30px; margin : auto">
										<p style="text-align:left">{{repayment_money_s | currency}}에 대해 떨어지는 가치차액 <br>{{Math.round( (cus_loan - repayment_money) *(1- Math.pow(1 + (this.n_rate / 100) / 12, -month_loan_period))) | currency}}을
											{{month_loan_period}}개월로 분할했을 경우 <br>{{s_m_rent-s_m_repay_atm | currency}}(②)이 나옵니다. <br>
											그러므로 고객님은 {{repayment_money_s | currency}}을 대출 받지 <br>않을 경우 월 납부 이자액 {{Math.round(s_m_repay_atm)| currency}}(①)과 가치차액 월세액 {{s_m_rent-s_m_repay_atm | currency}}(②)을 합한 금액 <span style="color: red">{{s_m_rent-s_m_repay_atm+Math.round(s_m_repay_atm)|currency}}</span> 월세에 투자할 수 있습니다. </p>
									</div>
								</div>
								<div class="row container" style="margin-top : 30px">
									<div class="col-sm-5">
										<table class="type09" style="margin-top : 50px">
											<thead>
												<tr>
													<th style="text-align:center">유형</th>
													<th style="text-align:center">매월 납부액</th>
												</tr>
											</thead>
												<tr>
													<td style="width:65%">원리금상환 대출 <br>{{repayment_money| currency}}</td>
													<td> {{p_m_repay_atm| currency}}</td>
												</tr>
												<tr>
													<td>{{month_loan_period}}개월 후에 {{i_rate}}% 수익률로 {{repayment_money| currency}}만들기 </td>
													<td> {{this.p_loan_atm_i | currency}} </td>
												</tr>
												<tr>
													<td>차액</td>
													<td> {{p_m_repay_atm-p_loan_atm_i | currency}}</td>
												</tr>
											</table>
										</div>
										<div class="col-sm-2" style="margin : auto">
										<i class="fa fa-angle-right fa-4x"></i>
									</div>
									<div class="col-sm-5" style="margin-top : 30px; margin : auto;">
									<p style="text-align:left">고객님이 {{repayment_money| currency}}을 원리금 상환으로 <br>대출받았을 경우 {{p_m_repay_atm| currency}}을 납부하게 되지만
										<br>연 {{i_rate}}%의 수익률을 낼 수 있다면 {{repayment_money| currency}}을 모으기 위해 매월 {{this.p_loan_atm_i | currency}}을 납부하게 됩니다.
										그러므로 {{repayment_money| currency}}을 대출 받지 않았을 경우 둘의 차액 <span style="color: red"> {{p_m_repay_atm-p_loan_atm_i | currency}}(③)</span>을 월세에 투자할 수 있습니다. </p>
								</div>
							</div>
							<div class="row container" style="margin-top : 30px">
								<div class="col-sm-5">
									<table class="type09" style="margin-top : 50px">
										<tr>
											<td style="color : green"><i class="fa fa-plus-circle"></i> 대출시 월 이자액(①)</td>
											<td>{{Math.round(s_m_repay_atm)| currency}}</td>
										</tr>	
										<tr>
											<td style="color : green; width:65%"><i class="fa fa-plus-circle"></i> 현재가치 추가월세(②)</td>
											<td>{{s_m_rent-s_m_repay_atm| currency}}</td>
										</tr>
										<tr>
											<td style="color : green"><i class="fa fa-plus-circle"></i> 수익률 추가 월세(③)</td>
											<td>{{Math.round(this.p_m_repay_atm-this.p_loan_atm_i )| currency}}</td>
										</tr>
										<tr>
											<td style="color : red">= 합계 월세</td>
											<td>{{Math.round(s_m_rent-s_m_repay_atm+s_m_repay_atm+this.p_m_repay_atm-this.p_loan_atm_i)| currency}}</td>
										</tr>
									</table>
								</div>
								<div class="col-sm-2" style="margin : auto">
									<i class="fa fa-angle-right fa-4x"></i>
								</div>
								<div class="col-sm-5" style="margin : auto">
									<p style="text-align:left">고객님의 적정 월세가격은 <br>+ ①에 대한 금액<br> + ②에 대한 금액<br>+ ③에 대한 금액을 합한 {{Math.round(rent)| currency}}입니다.<br>
										따라서 전세보증금 {{leasing_mortgage | currency}} 중 <br>{{cus_loan | currency}}을 대출 받는 것은 보유하고 있는<br> 돈으로 월세 보증금 <span style="color: red">{{deposit| currency}}</span>을 내고 월세 <span style="color: red">{{Math.round(rent)| currency}}</span>에 사는것과 가치가 동등합니다. </p>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div v-else>
				<div style="border : 1px solid; margin-top : 30px">
					<p style="font-size:38px; background-color : black; color : white;">전세 vs 월세</p><br>
					<p style="font-size:23px;">전세보증금 {{leasing_mortgage | currency}} 중 {{repayment_money_s | currency}}을 대출 받는것은<br> 대출없이 보유하고 있는 돈으로 월세 보증금 <span style="color: red">{{deposit| currency}}</span>을 내고<br> 월세 <span style="color: red">{{Math.round(rent)| currency}}</span>에 사는 것과 가치가 동등합니다. </p><br>
				</div>
				<br>
				<div class="container">
					<a @click="toggleTrue" class="btn btn-xl" style="background : transparent; border : 1px solid" href="#go_detail">자세히보기</a>
				</div>

				<div v-show="toggle==true">
					<div class="row">
						<div class="row container" style="margin-top : 70px">
							<div class="col-sm-5">
								<table class="type09">
									<thead>
										<tr>
											<th>금액</th>
											<th>현재가치</th>
										</tr>
									</thead>
									<tr>
										<td style="width:65%">현재 {{repayment_money_s | currency}}</td>
										<td> {{repayment_money_s | currency}}</td>
									</tr>
										<tr>
											<td>{{month_loan_period}}개월 후 {{repayment_money_s | currency}}</td>
											<td>  {{Math.round((cus_loan - repayment_money) *(Math.pow(1 + (this.n_rate / 100) / 12, -month_loan_period))) | currency}}</td>
									</tr>
									<tr>
										<td>차액</td>
										<td> {{Math.round( (cus_loan - repayment_money) *(1- Math.pow(1 + (this.n_rate / 100) / 12, -month_loan_period))) | currency}}</td>
									</tr>
								</table>
							</div>
							<div class="col-sm-2" style="margin : auto">
								<i class="fa fa-angle-right fa-4x"></i>
							</div>
							<div class="col-sm-5" style="margin : auto">
								<p style="text-align:left"> {{repayment_money_s | currency}}에 대해 떨어지는 가치차액 {{Math.round( (cus_loan - repayment_money) *(1- Math.pow(1 + (this.n_rate / 100) / 12, -month_loan_period))) | currency}}을
								{{month_loan_period}}개월로 분할할 경우 {{s_m_rent-s_m_repay_atm | currency}}이 나옵니다.<br>
							    그러므로 고객님은 {{repayment_money_s | currency}}을 대출 받지 않을<br> 경우 매월 <span style="color: red">{{s_m_rent-s_m_repay_atm | currency}}(②)</span>을 월세에 투자할 수 있습니다.</p>
							</div>
						</div>
						<div class="row container" style="margin-top : 50px">
							<div class="col-sm-5">  
								<table class="type09">
									<tr>
										<td style="color : green;"><i class="fa fa-plus-circle"></i> 대출시 월 이자액(①)</td>
										<td>{{Math.round(s_m_repay_atm) | currency}}</td>
									</tr>
									<tr>
										<td style="color : green; width:65%"><i class="fa fa-plus-circle"></i> 현재가치 고려 추가 월세(②)</td>
										<td>{{s_m_rent-s_m_repay_atm | currency}}</td>
									</tr>
									<tr>
										<td style="color : red;">= 합계 월세</td>
										<td>{{Math.round(s_m_rent-s_m_repay_atm+s_m_repay_atm) | currency}}</td>
									</tr>

								</table>
							</div>
							<div class="col-sm-2" style="margin : auto">
								<i class="fa fa-angle-right fa-4x"></i>
							</div>
							<div class="col-sm-5" style="margin : auto">
								<p style="text-align:left">고객님의 적정 월세가격은<br>①에 대한 금액 + ②에 대한 금액을 <br>합한 {{Math.round(rent)| currency}}입니다.
								<br>따라서 전세보증금 {{leasing_mortgage | currency}}중 <br>{{repayment_money_s | currency}}을 대출 받아서 사는 것은 <br>대출 없이 현재 보유하고 있는 돈으로 <br>월세 보증금 <span style="color: red">{{deposit | currency}}</span>을 내고 <br>월세 <span style="color: red">{{Math.round(rent)| currency}}</span>에 사는 것과 가치가 동등합니다.</p>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>

			<!-- 모달 창 -->        
 		<div v-show="showDetail" class="modal is-active">
			<div class="modal-background">
			</div>
			<div class="modal-content">
				<div class="box">
					<h3>this is modal </h3>
					<span></span> 
					<table v-if="repayment==0" class="bluetop">
						<tr>
							<th>회차</th><th><label for="ex1" data-toggle="tooltip" data-placement="top" title="상환금=만기상환이자">상환금</label></th><th>납부이자</th><th>납부원금</th><th>잔금</th>
						</tr>
						<tr v-for="test in tests">
							<td>{{test.month}}</td>
							<td>{{Math.round(test.상환금)}}</td>
							<td>{{Math.round(test.납부이자)}}</td>
							<td>{{test.납부원금}}</td>
							<td>{{test.잔금}}</td>
						</tr>
					</table>
					<table v-else class="bluetop">
						<tr>
							<th>회차</th><th><label for="ex1" data-toggle="tooltip" data-placement="top" title="상환금=만기상환이자+원리금상환이자+원리금상환원금납입액">상환금</label></th><th>만기상환이자</th><th>만기상환잔금</th><th>원리금상환이자</th><th>원리금상환납입원금납입액</th><th>원리금상환잔금</th>
						</tr>
						<tr v-for="test in tests">
							<td>{{test.month}}</td>
							<td>{{Math.round(test.상환금)}}</td>
							<td>{{Math.round(test.만기상환이자)}}</td>
							<td>{{Math.round(test.만기상환잔금)}}</td>
							<td>{{Math.round(test.원리금상환이자)}}</td>
							<td>{{Math.round(test.원리금상환원금)}}</td>
							<td>{{Math.round(test.원리금상환잔금)}}</td>
						</tr>
					</table>
				</div>
			</div>
			<button class="modal-close" aria-label="close"></button>
		</div>
	</div>

</article>
</section>
</template>

<!-- compute #2 -->        
<script>
import{bus} from '../bus.js'
import axios from'axios'
export default{    
	data(){
		return {
			cus_imform:[], //받아온 고객 정보 넣기
			cus_num:{},
			i_rate:0, //수익률 결정
			deposit:'',//보증금계산
			toggle:false,
			tests:[], //차트 데이터 넣을 곳
			repayment_money_s : '', // 만기상환 대출금액
			s_m_repay_atm : '', //만기상환 대출금액 월 납입액(이자액)
			p_m_repay_atm : '', //원리금상환 대출금액 월 납입액
			s_m_rent : '',//만기상환 경우 월세값 계산
			n_rate : '', //국고채 금리
			repayment_word : '',// 만기상환 , 만기&부분상환 용어
			repayment: '' ,  //상환방식
			repayment_money: '', //원리금 상환 대출금액
			cus_salary:'',  //고객연봉
			cus_loan:'', //대출금액
			leasing_mortgage:'' , //임차보증금 
			month_loan_period:'' , //상환기간
			bank_name:'', //은행이름
			loan_good_name:'' , //대출상품명
			avg_int_rat:'', //평균금리
		}
	},
   methods:{
	   //자세히 보기 버튼 클릭시
		toggleTrue:function(){
			this.toggle=!this.toggle;
		},
		modalStart:function(){
			console.log('modal bus 시작');
			bus.$emit('modal', this.tests);
			console.log('modal bus 끝');
		},
		//계산하기
		calculate:function(){
			console.log('계산하기 실행됨??')
			console.log('계산하기 실행됨');
			this.tests = [];
			if(this.repayment==0){
				for(var i=1;i<=this.month_loan_period;i++){
					this.tests.push({
						repayment: 0,
						month:i.toString(),
						상환금:this.s_m_repay_atm.toString(),
						납부이자:this.s_m_repay_atm.toString(),
						납부원금:0,
						잔금:this.repayment_money_s.toString()
					}); 
				}
			}else{
			var d_m_int; //원리금 상환 매월 이자 계산
			var d_m_or_atm; //원리금 상환 
			var d_m_balance; //원리금 상환시 원금 잔액 계산
			var d_bf_balance; //원리금 상환시 잔액 계산
			 for (var i = 1; i <= this.month_loan_period; i++) {
					if (i == 1) { 
						d_m_int = this.repayment_money * (this.avg_int_rat / 100) / 12; //이자
						d_m_or_atm = this.p_m_repay_atm - d_m_int; //원금
						d_m_balance = this.repayment_money - d_m_or_atm; // 잔금
						this.tests.push({
							repayment: 1,
							month: i.toString(),
							상환금:(this.s_m_repay_atm+d_m_int+d_m_or_atm).toString(),
							만기상환이자: this.s_m_repay_atm.toString(),
							만기상환잔금:this.repayment_money_s.toString(),
							원리금상환이자: d_m_int.toString(),
							원리금상환원금: d_m_or_atm.toString(),
							원리금상환잔금:d_m_balance.toString()
							}); //상환할 이자, 원금 : 차트사용하기 위해 데이터 넣기 (원리금 상환 이자,원금 납부 변화 그래프사용하기 위해)
					} else {
						d_m_int = d_bf_balance * (this.avg_int_rat/ 100) / 12; //이자
						d_m_or_atm = this.p_m_repay_atm - d_m_int; //원금
						d_m_balance = d_bf_balance - d_m_or_atm; //잔금
						console.log('이자 :' +d_m_int+'원금: '+d_m_or_atm+'잔금 : '+d_m_balance);
						this.tests.push({
							repayment: 1,
							month: i.toString(),
							상환금:(this.s_m_repay_atm+d_m_int+d_m_or_atm).toString(),
							만기상환이자: this.s_m_repay_atm.toString(),
							만기상환잔금:this.repayment_money_s.toString(),
							원리금상환이자: d_m_int.toString(),
							원리금상환원금: d_m_or_atm.toString(),
							원리금상환잔금:d_m_balance.toString()
						}); //상환할 이자, 원금 //차트 사용하기 위해 데이터 넣기 (원리금 상환 이자,원금 납부 변화 그래프사용하기 위해)
					}
					d_bf_balance = d_m_balance; // 잔금 계산
			 	}
			}
		},
		resetInform:function(){
			console.log("emit실행됨(resetInform)")
			axios({
				method:'get',
				url:'http://localhost:3000/api/process/getuser',
				data : {
					cus_num : this.cus_num
				}
			})
			.then((response) => {
				this.repayment = ''; 
				this.repayment_money = '';
				this.cus_salary = '';
				this.cus_loan = '';
				this.leasing_mortgage = '';
				this.month_loan_period = '';
				this.bank_name  = '';
				this.loan_good_name = '';  
				this.avg_int_rat = '';
				this.cus_imform.push(response.data);

				//불러온 데이터 입력
				this.repayment = response.data[0].repayment; 
				this.repayment_money = response.data[0].repayment_money; 
				this.cus_salary = response.data[0].cus_salary; 
				this.cus_loan = response.data[0].cus_loan;
				this.leasing_mortgage = response.data[0].leasing_mortgage;
				this.month_loan_period = response.data[0].month_loan_period; 
				this.bank_name  = response.data[0].bank_name ;
				this.loan_good_name = response.data[0].loan_good_name; 
				this.avg_int_rat = response.data[0].avg_int_rat ;
				
				//만기상환대출금액 계산
				this.repayment_money_s=this.cus_loan - this.repayment_money; 
				
				//만기상환 대출금액 월 이자 납입액
				this.s_m_repay_atm = (this.repayment_money_s) * (this.avg_int_rat / 100) / 12;
				
				//원리금상환 대출금액 월 납입액
				this.p_m_repay_atm = (this.repayment_money) * (this.avg_int_rat / 100) / 12 / (1 - Math.pow(1 + (this.avg_int_rat / 100) / 12, -this.month_loan_period));
				
				//국고채 금리 2년이하 2% 아니면 3%으로 계산
				 if(this.month_loan_period>=12&this.month_loan_period<=24){
					 this.n_rate = 2;
					}else{
					this.n_rate = 3;
					}
		
				//만기상환 대출 받은 금액 현재가치 차액 변수
				var s_loan_atm_diff; 
				 s_loan_atm_diff = (this.repayment_money_s) *(1- Math.pow(1 + (this.n_rate / 100) / 12, -this.month_loan_period));
				//만기상환 대출에 대한 월세 환산
				this.s_m_rent = this.s_m_repay_atm + s_loan_atm_diff * (this.n_rate / 100) / 12 / (1 - Math.pow(1 + (this.n_rate / 100) / 12, -this.month_loan_period));
			  
			  //보증금 계산
				this.deposit = response.data[0].leasing_mortgage-response.data[0].cus_loan;
	 
			 //용어 바꿔주기
				if(this.repayment===0){
				this.repayment_word = '만기일시상환';
				}else{
					this.repayment_word = '만기&원리금상환';
				}
				 this.calculate();
			 })
		},
		send:function(text){
			 console.log(text);
			this.cus_num = text;
			console.log(this.cus_num); 
		}
	},
	created(){
			bus.$on('resetInform',this.resetInform);        
			bus.$on('send', this.send); 

	},
	computed:{
	 p_loan_atm_i:function(){
		 return (this.repayment_money) * (this.i_rate / 100) / 12 / (Math.pow(1 + (this.i_rate / 100) / 12, this.month_loan_period) - 1);
	 },
	 p_m_rent:function(){
		 if(this.repayment===0){
			 return 0;
		 }else{
			 return this.p_m_repay_atm-this.p_loan_atm_i;
		 }
	 },
	 rent:function(){
		 return this.s_m_rent+this.p_m_rent; 
	 }
	}
}

</script>
<style>
	.axis .domain {
		display: none;
	}
	th,td{
		font-size: 18px;
	}
	table.type06 {
	border-collapse: collapse;
	/* text-align: left; */
	line-height: 1.5;
	border-top: 1px solid #ccc;
	border-bottom: 1px solid #ccc;
	margin: 20px 10px;
}
table.type06 th {
	text-align:center;
	width: 200px;
	padding: 10px;
	font-weight: bold;
	vertical-align: top;
}  
table.type06 td {
	width: 250px;
	padding: 10px;
	vertical-align: top;
}
table.type06 .even {
	background: #efefef;
}
</style>