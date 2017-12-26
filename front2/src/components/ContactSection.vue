<template>
<!-- 계산기 페이지 -->
<section class="page-section" id="contact">

<div class="container">
  <div style="text-align:left; margin-left:35px; margin-bottom:30px">
    <h6 style="color : #2c3e50;">원하는 계산기의 버튼을 클릭하여 주세요</h6>
    <button class="btn btn-primary" style="color : #EF4035; border-color : #EF4035" @click="change_calc1">대출 상환 계산기</button><button class="btn btn-primary" style="color : #EF4035; border-color : #EF4035" @click="change_calc2">적정주택가격 계산기</button>
  </div>
</div>

<div class="container">
  <div v-if="check_cal===0" class="row">
    <div class="container wow fadeIn col-sm-5">
      <div class="text-center" id="calculate">
        <h2 style="font-size:45px">대출 상환 계산기</h2>
        <hr class="colored">
        <p>간단한 정보를 입력하시면 고객님께서 받으신 대출을<br> 매월 얼마씩 갚아나가야 모두 상환할 수 있는지 월별로 보여드립니다.</p>
      </div>
      <div class="row mt-4">
        <div class="col-lg-10 mx-auto">
          <form name="sentMessage" id="contactForm" novalidate>
            <div class="row control-group">
              <div class="form-group col-12 floating-label-form-group controls" style="padding:0px">
                <select  class="form-control-lg" v-model="selected" style="margin-top : 20px; width:300px; height:50px" >
                  <option>상환방법선택</option><option>만기일시상환</option><option>원리금균등상환</option><option>원금균등상환</option>
                </select>
                <button class="btn btn-primary" style="border:0px" data-toggle="tooltip" data-placement="right" data-html="true" title="※ 대출 상환 방법 <br>
                    원리금균등상환 - 가장 일반적인 방법으로, 원금과 이자를 합한 상환금액이 매달 동일합니다.<br>
                    원금균등상환 - 매달 원금을 동일하게 상환하므로, 이자는 매달 줄어들게 됩니다.<br> 단, 매달 이자가 다르므로 원금과 이자를 합한 상환금액도 매달 달라집니다.<br>
                    원금만기일시상환 - 대출기간동안 매달 이자만 상환하하고, 대출 만기일에 원금을 일시상환 합니다.<br><br>
                    ※ 거치기간<br>
                    거치기간동안 이자만 납부하고, 거치기간이 끝나면 원금+이자를 납부하게 됩니다. <br>따라서 원리금/원금 균등상환에만 적용됩니다.<br><br>

                  ※ 오차 가능성 안내<br>
                    본 대출금 상환 계산기는 월 단위로 계산 한 것이므로, <br>실제 대출 시작 일자에 일할 계산에 따른 약간의 차이는 있을 수 있습니다.">
                <i class="fa fa-question fa-2x"></i></button>
                <p class="help-block text-danger"></p>
              </div>
            </div>
            <div class="row control-group">
              <div class="form-group col-12 floating-label-form-group controls" style="padding:0px">
                <label>대출금액</label>
                <vue-numeric type="text" style="text-align : center" v-model.number="loan_atm" currency="￦" separator=","  class="form-control" placeholder="대출금액" required data-validation-required-message="대출금액을 입력하여 주세요"></vue-numeric>
                <p class="help-block text-danger"></p>
              </div>
            </div>
            <div class="row control-group">
              <div class="form-group col-12 floating-label-form-group controls" style="padding:0px">
                <label>대출금리</label>
                <vue-numeric type="text" style="text-align : center" v-model.number="d_rate" class="form-control" v-bind:precision = "1" placeholder="대출금리" currency="%" currency-symbol-position="suffix" required data-validation-required-message="대출금리를 입력하여 주세요"></vue-numeric>
                <p class="help-block text-danger"></p>
              </div>
            </div>
            <div class="row control-group">
              <div class="form-group col-12 floating-label-form-group controls" style="padding:0px">
                <label>대출기간</label>
                <vue-numeric type="text" style="text-align : center" v-model.number="i_term" class="form-control" placeholder="대출기간" id="message" currency="개월" currency-symbol-position="suffix" required data-validation-required-message="대출기간을 입력하여 주세요"></vue-numeric>
                <p class="help-block text-danger"></p>
              </div>
            </div><br>
            <div id="success">
            </div>
            <div class="row">
              <div class="form-group col-12">
                <button type="submit" @click.prevent="calculate" class="btn btn-primary">계산하기</button>
                <button type="submit" @click.prevent="calculate_reset" class="btn btn-primary">화면닫기</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div> 

    <div class="col-sm-2" style="margin : auto">
        <i class="fa fa-angle-right fa-4x"></i>
    </div>

    <div class="container wow fadeIn col-sm-5" style="padding:0px">
      <p>월별상환금</p>
      <table class="type04" style="margin:0px">
        <tr>
          <th style="font-size:14px">회차</th>
          <th style="font-size:14px">상환금</th>
          <th style="font-size:14px">납부이자</th>
          <th style="font-size:14px">납부원금</th>
          <th style="font-size:14px">잔금</th>
        </tr>
        <tr v-for="test in tests">
        <td style="font-size:13px">{{test.month}}</td>
        <td style="font-size:13px">{{Math.round(test.상환금) | currency }}</td>
        <td style="font-size:13px">{{Math.round(test.납부이자) | currency}}</td>
        <td style="font-size:13px">{{Math.round(test.납부원금) | currency}}</td>
        <td style="font-size:13px">{{Math.round(test.잔금) | currency}}</td>
        </tr>
      </table>  
    </div>
  </div>

  <div v-else class="row">
    <div class="container wow fadeIn col-sm-5">
      <div class="text-center">
        <h2 style="font-size:45px">적정 주택가격 계산기</h2>
        <hr class="colored">
        <p>간단한 정보를 입력하시면 <br>자신의 적정한 주택의 가격을 보여드립니다</p>
      </div>
      <div class="row mt-4">
        <div class="col-lg-10 mx-auto">
          <form name="sentMessage" id="contactForm" novalidate>
            <div class="row control-group">
              <div class="form-group col-12 floating-label-form-group controls" style="padding:0px">
                <select class="form-control-lg" v-model="selected2" style="margin-top : 20px; width:300px; height:50px">
                 <option>상환방법선택</option><option>만기일시상환</option><option>원리금균등상환</option>
                </select>
                <button id="tooltip_calc" class="btn btn-primary" style="border:0px;" data-toggle="tooltip" data-placement="right" data-html="true" title="※ 대출 상환 방법 <br>
                    원리금균등상환 - 가장 일반적인 방법으로, 원금과 이자를 합한 상환금액이 매달 동일합니다.<br>
                    원금균등상환 - 매달 원금을 동일하게 상환하므로, 이자는 매달 줄어들게 됩니다.<br> 단, 매달 이자가 다르므로 원금과 이자를 합한 상환금액도 매달 달라집니다.<br>
                    원금만기일시상환 - 대출기간동안 매달 이자만 상환하하고, 대출 만기일에 원금을 일시상환 합니다.<br><br>

                  ※원금균등상환은 매월 상환금액이 다르기 때문에 주택적정가격을 계산하기 어렵습니다.<br> 이 계산기는 원리금균등상환과 원금만기일시상환할 경우에만 이용할 수 있습니다.<br><br>

                  ※ 오차 가능성 안내<br>
                    본 대출금 상환 계산기는 월 단위로 계산 한 것이므로, <br>실제 대출 시작 일자에 일할 계산에 따른 약간의 차이는 있을 수 있습니다.<br>"><i class="fa fa-question fa-2x"></i></button>
                <p class="help-block text-danger"></p>
              </div>
            </div>
            <div class="row control-group">
              <div class="form-group col-12 floating-label-form-group controls" style="padding:0px">
                <label>보유금액</label>
                <vue-numeric type="text" class="form-control"  style="text-align : center"  v-model.number="money" currency="￦" separator="," placeholder="보유금액" required data-validation-required-message="보유금액을 입력하여 주세요"></vue-numeric>
                <p class="help-block text-danger"></p>
              </div>
            </div>
            <div class="row control-group">
              <div class="form-group col-12 floating-label-form-group controls" style="padding:0px">
                <label>월 희망 상환금액</label>
                <vue-numeric type="text" class="form-control"  style="text-align : center" placeholder="월 희망 상환금액" v-model.number="repay" currency="￦" separator="," required data-validation-required-message="월 희망 상환금액을 입력하여 주세요"></vue-numeric>
                <p class="help-block text-danger"></p>
              </div>
            </div>
            <div class="row control-group">
              <div class="form-group col-12 floating-label-form-group controls" style="padding:0px">
                <label>대출금리</label>
                <vue-numeric type="text" style="text-align : center" v-model.number="d_rate2" class="form-control" v-bind:precision = "1" placeholder="대출금리" currency="%" currency-symbol-position="suffix" required data-validation-required-message="대출금리를 입력하여 주세요"></vue-numeric>
                <p class="help-block text-danger"></p>
              </div>
            </div>
            <div class="row control-group">
              <div class="form-group col-12 floating-label-form-group controls" style="padding:0px">
                <label>상환기간</label>
                <vue-numeric type="text" style="text-align : center" v-model.number="i_term2" class="form-control" placeholder="상환기간" id="message" currency="개월" currency-symbol-position="suffix" required data-validation-required-message="대출기간을 입력하여 주세요"></vue-numeric>
                <p class="help-block text-danger"></p>
              </div>
            </div>
            <br>
            <div id="success"></div>
            <div class="row">
              <div class="form-group col-12">
                <button type="submit" class="btn btn-secondary" @click.prevent="calculate2">계산하기</button>
                <button type="submit" @click.prevent="calculate_reset2" class="btn btn-primary">다시계산</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>

    <div class="col-sm-2" style="margin : auto">
      <i class="fa fa-angle-right fa-4x"></i>
    </div>
    
    <div class="container wow fadeIn col-sm-5" style="margin : auto">
      <h3>계산결과
      고객님은 {{Math.round(loan_atm2)|currency}}을 대출 받으실 수 있습니다.<br><br>
      고객님의 적정 주택 구입가격은 <span style="color:red">{{Math.round(this.money+loan_atm2)|currency}}</span>입니다.</h3>
    </div>
  </div>
</div>
</section>
</template>

<script>
import{bus} from '../bus.js'
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
});
var check_cal = 0

export default{
  data(){
    return {
      selected: "상환방법선택",
      loan_atm: "", //대출금액
      tests: [],
      i_term: "", //대출기간
      l_term: "", //거치기간
      d_rate: "", //대출금리
      s_m_repay_atm: null, //만기일시 상환금 월 이자액
      p_m_repay_atm: null, //원리금균등 월 상환액(이자+원금)

      selected2: "상환방법선택",
      money:"",
      repay:"",
      d_rate2:"",
      i_term2:"",
      loan_atm2:"",

      check_cal: 0


      }
  },

  methods:{
    calculate: function() {
      this.tests = []
      if (this.selected == '만기일시상환') {
        this.s_m_repay_atm = (this.loan_atm) * (this.d_rate / 100) / 12; //만기일시 상환금 월 이자액
        for (var i = 1; i <= this.i_term; i++) {
          this.tests.push({
              month: i,
              상환금: Math.round(this.s_m_repay_atm),
              납부이자: Math.round(this.s_m_repay_atm),
              납부원금: 0,
              잔금: Math.round(this.loan_atm)
          })
        }
      } else if (this.selected == '원리금균등상환') {
        this.p_m_repay_atm = (this.loan_atm) * (this.d_rate / 100) / 12 / (1 - Math.pow(1 + (this.d_rate / 100) / 12, -(this.i_term - this.l_term))); //월납부액
        this.s_m_repay_atm = (this.loan_atm) * (this.d_rate / 100) / 12; //거치기간동안 월 이자액
        var d_m_int;
        var d_m_or_atm;
        var d_m_balance;
        var d_bf_balance;
        for (var i = 1; i <= this.l_term; i++) {
          this.tests.push({
              month: i,
              상환금: Math.round(this.s_m_repay_atm),
              납부이자: Math.round(this.s_m_repay_atm),
              납부원금: 0,
              잔금: Math.round(this.loan_atm)
          })
        }
        for (var i = (this.l_term + 1); i <= this.i_term; i++) {
          if (i == (this.l_term + 1)) {
              d_m_int = this.loan_atm * (this.d_rate / 100) / 12; //이자
              d_m_or_atm = this.p_m_repay_atm - d_m_int; //원금
              d_m_balance = this.loan_atm - d_m_or_atm; // 잔금
              this.tests.push({
                  month: i,
                  상환금: Math.round(d_m_int + d_m_or_atm),
                  납부이자: Math.round(d_m_int),
                  납부원금: Math.round(d_m_or_atm),
                  잔금: Math.round(d_m_balance)
              }); //상환할 이자, 원금
          } else {
              d_m_int = d_bf_balance * (this.d_rate / 100) / 12; //이자
              d_m_or_atm = this.p_m_repay_atm - d_m_int; //원금
              d_m_balance = d_bf_balance - d_m_or_atm; //잔금
              this.tests.push({
                month: i,
                상환금: Math.round(d_m_int + d_m_or_atm),
                납부이자: Math.round(d_m_int),
                납부원금: Math.round(d_m_or_atm),
                잔금: Math.round(d_m_balance)
              }); //상환할 이자, 원금
          }
              d_bf_balance = d_m_balance;
        }
      } else {
        var d_or_rt_amt = this.loan_atm / (this.i_term - this.l_term);
        this.s_m_repay_atm = (this.loan_atm) * (this.d_rate / 100) / 12; //거치기간동안 월 이자액  
        var d_m_int;
        var d_m_or_atm;
        var d_m_balance;
        var d_bf_balance;
        for (var i = 1; i <= this.l_term; i++) {
          this.tests.push({
            month: i,
            상환금: this.s_m_repay_atm,
            납부이자: this.s_m_repay_atm,
            납부원금: 0,
            잔금: this.loan_atm
          })
        }
        for (var i = (this.l_term + 1); i <= this.i_term; i++) {
          if (i == (this.l_term + 1)) {
              d_m_int = this.loan_atm * (this.d_rate / 100) / 12; //이자
              d_m_or_atm = d_or_rt_amt; //원금
              d_m_balance = this.loan_atm - d_m_or_atm; // 잔금
              this.tests.push({
                month: i,
                상환금: d_m_int + d_m_or_atm,
                납부이자: d_m_int,
                납부원금: d_m_or_atm,
                잔금: d_m_balance
              }); //상환할 이자, 원금
          } else {
            d_m_int = d_bf_balance * (this.d_rate / 100) / 12; //이자
            d_m_or_atm = d_or_rt_amt; //원금
            d_m_balance = d_bf_balance - d_m_or_atm; //잔금
            this.tests.push({
                month: i,
                상환금: d_m_int + d_m_or_atm,
                납부이자: d_m_int,
                납부원금: d_m_or_atm,
                잔금: d_m_balance
            }); //상환할 이자, 원금
          }
          d_bf_balance = d_m_balance;
        }
      }
    },
    calculate2: function() {
      if (this.selected2 == '만기일시상환') {
          // this.s_m_repay_atm = (this.loan_atm) * (this.d_rate / 100) / 12; //만기일시 상환금 월 이자액
        this.loan_atm2= (this.repay)/((this.d_rate2 / 100) / 12);
      } else{
          this.loan_atm2= (this.repay)/( (this.d_rate2 / 100) / 12 / (1 - Math.pow(1 + (this.d_rate2 / 100) / 12, -this.i_term2)));
      }
    },
    calculate_reset: function() {
      this.selected =  "상환방법선택",
      this.loan_atm = "", //대출금액
      this.tests = [],
      this.i_term = "", //대출기간
      this.l_term = "", //거치기간
      this.d_rate = "", //대출금리
      this.s_m_repay_atm = null, //만기일시 상환금 월 이자액
      this.p_m_repay_atm = null //원리금균등 월 상환액(이자+원금)
    },
    calculate_reset2: function() {
      this.selected2 = "상환방법선택",
      this.money = "",
      this.repay = "",
      this.d_rate2 = "",
      this.i_term2 = "",
      this.loan_atm2 = ""
    },
    change_calc1: function(){
      check_cal = '';
      this.check_cal = 0
    },
    change_calc2: function(){
      check_cal = '';
      this.check_cal = 1
    }
  }
}
</script>
<style>
.tooltip-inner {
  max-width: 750px;
  width: 750px; 
} 
table.type04 td {
	padding: 5px;

}
</style>
