<template id="template">
<!-- 전세대출 상품추천 페이지 -->
<section class="page-section" id="services"> 
  <div class="container">
    <div class="text-center wow fadeIn">
      <h2>전세대출 상품 추천</h2>
      <hr class="colored">
      <p class="mb-0">전세대출과 관련된 정보를 입력해주시기 바랍니다.</p>
    </div>
    <div class="row" style="background-color=black">  
      <div class="col-md-12" style =" text-align: center"><br> 
        <table class="type04 col-md-12">
          <tr>
            <th>
              <label class="customerlabel" for="cus_age" data-toggle="tooltip" data-placement="top" title="고객님의 나이입니다">나이</label>
            </th>
            <th>
              <vue-numeric class="form-control" type="text" name="cus_age" placeholder="나이" currency="세" currency-symbol-position="suffix" v-model="cus_age" style="width:55%"></vue-numeric>
            </th>
          </tr>
          <tr>
            <th>
              <label class="customerlabel" for="cus_sex" data-toggle="tooltip" data-placement="top" title="고객님의 성별입니다">성별</label>
            </th>
            <th>
              <select class="form-control" name="cus_sex" onchange="seletedBox(this)" v-model="cus_sex" id="selectbox" style="width:55%">
              <option value="0">남자</option>
              <option value="1">여자</option>
              </select>
            </th>
          </tr>
          <tr>
            <th><label class="customerlabel" for="ex1" data-toggle="tooltip" data-placement="top" title="고객님의 연봉을 써주세요. ex) 24000000">고객연봉</label></th>
            <th><vue-numeric class="form-control" type="text" name="cus_salary" placeholder="고객연봉" v-model="cus_salary" currency="￦" separator="," style="width:55%"></vue-numeric></th>
          </tr>  
          <tr>
            <th><label class="customerlabel" for="ex1" data-toggle="tooltip" data-placement="top" title="주거래 은행을 선택하여 주세요">거래은행</label></th>
            <th>  
              <select class="form-control" name="bank_id" onchange="selectedBox(this)" v-model="bank_id" id="selectbox" style="width:55%">
                <option value="1">하나은행</option>
                <option value="2">신한은행</option>
                <option value="3">우리은행</option>
                <option value="4">국민은행</option>
                <option value="5">농협</option>
                <option value="6">기업은행</option>
              </select>
            </th>
          </tr>
          <tr>    
            <th><label class="customerlabel" for="ex1" data-toggle="tooltip" data-placement="top" title="입주하실 주택의 보증금을 입력하세요 ex) 80000000">임차보증금</label></th>
            <th><vue-numeric class="form-control" type="text" name="leasing_mortgage" placeholder="임차보증금" v-model="leasing_mortgage" currency="￦" separator="," style="width:55%"></vue-numeric></th>
          </tr> 
          <tr>
            <th><label style ="margin-left:60px" class="customerlabel" for="repayment" data-toggle="tooltip" data-placement="top" title="만기에 한번에 금액을 상환할지 부분적으로 상환할지 선택해 주세요">상환방법</label>  
                <button class="btn btn-primary" style="border:0px;" data-toggle="tooltip" data-placement="right" data-html="true" title="※ 대출 상환 방법 <br>
                              원리금균등상환 - 가장 일반적인 방법으로, 원금과 이자를 합한 상환금액이 매달 동일합니다.<br>                
                              만기일시상환 - 대출기간동안 매달 이자만 상환하고, 대출 만기일에 원금을 일시상환 합니다.<br>
                              부분만기&원리금상환 - 일부 금액은 만기일시상환하고 나머지 금액은 원리금상환합니다.<br><br>            
                              ※ 원금균등상환은 매월 상환금액이 달라지기 때문에 월세적정가격을 계산하지 못합니다.<br>그래서 상환방식에 원금균등상환방식은 고려하지 못했습니다.<br><br>
                              ※ 오차 가능성 안내<br>
                              본 대출금 상환 계산기는 월 단위로 계산 한 것이므로, <br>실제 대출 시작 일자에 일할 계산에 따른 약간의 차이는 있을 수 있습니다.">
            <i class="fa fa-question fa-2x"></i></button>
            </th>
            <th> <select class="form-control" name="repayment" onchange="selectedBox(this)" v-model="repayment" id="selectbox" style="width:55%">
                <option value="0">만기일시상환</option>
                <option value="1">부분만기&원리금상환</option>
                </select>
            </th>
          </tr>
          <tr> 
            <th>
              <label class="customerlabel" for="ex1" data-toggle="tooltip" data-placement="top" title="총 얼마를 대출 받을지 입력해 주세요 ex) 40000000">대출금액</label>
            </th>
            <th v-if="check=='0'">
              <vue-numeric class="form-control" type="text"  name="cus_loan" placeholder="대출금액" v-model="cus_loan" currency="￦" separator="," style="width:55%"></vue-numeric>
            </th>
            <th v-else-if="check=='1'">
              <vue-numeric class="form-control" type="text"  name="cus_loan" placeholder="대출금액" v-model="cus_loan" currency="￦" separator="," style="border: 1px solid #ff0000; width:55%"></vue-numeric>
              <h5 style ="color:red"><br>임차보증금에 비해 대출금액이 너무 큽니다.<br>최대한도는{{limit_money|currency}}입니다.</h5>
            </th>
            <th v-else-if="check=='2'">
              <vue-numeric class="form-control" type="text"  name="cus_loan" placeholder="대출금액" v-model="cus_loan" currency="￦" separator="," style="border: 1px solid #ff0000; width:55%"></vue-numeric>
              <h5 style ="color:red"><br><br>연봉에 비해 대출금액이 너무 큽니다.<br>최대한도는{{limit_money|currency}}입니다.</h5>
            </th>
            <th v-else-if="check=='3'">
              <vue-numeric class="form-control" type="text"  name="cus_loan" placeholder="대출금액" v-model="cus_loan" currency="￦" separator="," style="border: 1px solid #ff0000; width:55%"></vue-numeric>
              <h5 style ="color:red"><br>대출한도에 비해 대출금액이 너무 큽니다.<br>최대한도는{{limit_money|currency}}입니다.</h5>
            </th>
          </tr>
          <tr>
            <th>
              <label class="customerlabel" for="ex1" data-toggle="tooltip" data-placement="top" title="대출 기간을 (개월)단위로 선택하여 주세요">대출기간</label>
            </th>
            <th>
              <vue-numeric class="form-control" type="text" name="month_loan_period" placeholder="대출기간" currency="개월" currency-symbol-position="suffix" v-model="month_loan_period" style="width:55%"></vue-numeric>
              <h5 v-if="check2=='1'" style ="color:red"><br>대출기간은 12개월 이상 36개월 이내로 해주시기 바랍니다.</h5>
            </th>
          </tr>
          <tr v-if="repayment==='1'">
            <th>
              <label class="customerlabel" for="ex1" data-toggle="tooltip" data-placement="top" title="부분상환일시 총 얼마의 금액을 상환할 시 써주세요">원리금 상환금액</label>
            </th>
            <th>
              <vue-numeric class="form-control" type="text" name="repayment_money" placeholder="원리금 상환금액" v-model="repayment_money" currency="￦" separator="," v-bind:max="cus_loan" style="width:55%"></vue-numeric>
            </th>
          </tr>
        </table><br>
        
        <a v-if="check=='0' && check2=='0'" class="btn btn-xl" @click="testing" id="btn_loanpage" href="#recommend">확인</a> 
        <button v-else class="btn btn-xl" @click="testing" id="btn_loanpage" disabled='disabled' style="border-color:gray">확인</button> 
        <button class="btn btn-xl" type="reset" id="btn_loanpage" @click="reset" value="Reset">취소</button>
      </div>
    <div style="visibility:hidden;">
      {{limit_money}}
      {{check}}
      {{check2}}
    </div>
  </div> 
</div><br><br><!--container div--> 


<div class="container page-section">
  <div id ="recommend" style="height:24px"></div>
  <div v-if ="recom === 0"><br><br>
  </div>
  <div v-else-if ="recom === 1"><br><br>
    <h2 style="font-size: 40px"> 추천 상품 </h2>
    <hr class="colored">
    <div>
    <img v-bind:src="loan_img[current_array]" max-height="00px" max-width="600px">
    </div>
    <div>
      <table class="type09 col-md-12">
        <thead>
          <tr>
            <th scope="cols" style="visibility:hidden;">타이틀</th>
            <th scope="cols" style="visibility:hidden;">{{loan_good_name[current_array]}}</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">상품명</th>
            <td>{{loan_good_name[current_array]}}</td>
          </tr>
          <tr>
            <th scope="row">평균금리</th>
            <td>{{avg_int_rat[current_array]}}</td>
          </tr>
          <tr>
            <th scope="row">대출한도</th>
            <td>{{money_credit_line[current_array] | currency}}</td>
          </tr>
          <tr>
            <th scope="row">상환방식</th>
            <td>{{loan_repayment[current_array]===0?'만기일시상환':'부분만기 & 원리금상환'}}</td>
          </tr>
          <tr>
            <th scope="row">상세정보</th>
            <td><a v-bind:href="loan_url[current_array]" target="_blank" class="btn-primary" style="color:dodgerblue;
                  text-decoration: underline;
                  background-color:white;
                  border-color: white;
                  font-size: 15px;" >상세</a>
            </td>
          </tr>
        </tbody><br><br>
      </table>
    </div>
    <div>
      <button class="btn btn-default" @click="changeproduct" id="btn_loanpage">다음 상품</button>
      <a href="#go_calculate" class="btn btn-primary" @click="selectproduct" id="btn_loanpage">계산 하기</a>

    </div>
  </div>
  <div v-else><br><br>
    <h1> 추천된 상품이 없습니다.</h1>
    <h3> 대출금액이나 대출기한을 한번만 더 확인해주시기 바랍니다.</h3>
  </div><br><br><br><br><br><br>
       <div id ="go_calculate" style="height : 0px"></div>
<!-- 추천 div 끝 -->
</div>
<div v-if="isdetail===true">
    <computes />
</div>
<div v-else></div>
</section>
</template>

<script src="https://unpkg.com/vue-autoscroll"></script>
<script>
import Vue from 'vue'
import VueNumeric from 'vue-numeric'
import Computes from './Computes'
import axios from 'axios'
import {bus} from '../bus.js'

$(function () {
  $('[data-toggle="tooltip"]').tooltip()
});

export default {
  data () {
    return {
      cus_age: '0',
      cus_sex: '0',
      repayment: '0',
      repayment_money: '0',
      cus_salary: '0',
      cus_loan: '0',
      leasing_mortgage: '0',
      month_loan_period: '12',
      bank_id: '0',
      results: {},
      loan_img: {},
      current_array:0,
      recom:0,
      loan_good_num:{},
      loan_good_name:{},
      cus_num:{},
      check:'0',
      check2:'0',
      avg_int_rat:{},
      money_credit_line:{},
      loan_repayment:{},
      loan_url: {},
      isComputed:false,
      isdetail : false
    }
  },
  methods : {
    testing: async function(response, results) {
      axios({
        method : 'post',
        url : 'http://localhost:3000/process/testpost',
        data : {
          cus_age : this.cus_age,
          cus_sex : this.cus_sex,
          repayment : this.repayment,
          repayment_money : this.repayment_money,
          cus_salary : this.cus_salary,
          cus_loan : this.cus_loan,
          leasing_mortgage : this.leasing_mortgage,
          month_loan_period : this.month_loan_period,
          bank_id : this.bank_id,
        }
      }).then((response) => {
        this.bank_id = response.data.bank_id;
        console.log("확인1")
        console.log(response.data) 
        this.results = response.data
        console.log("확인2")
        console.log('데이터 값 결과 :' +response.data.length);
        if(response.data.length <= 0){
          this.recom = 2;
        }else{
        this.cus_num[0] = response.data[0].cus_num
          for(var i=0; i<response.data.length;i++){
            console.log("for statment" + i);
            console.log(response.data[i].loan_img);
            this.loan_img[i] = "./img/loanproduct/"+response.data[i].loan_img;
            console.log(this.loan_img[i]);
            this.loan_good_num[i] = response.data[i].loan_good_num;
            this.loan_good_name[i] = response.data[i].loan_good_name;
            this.avg_int_rat[i] = response.data[i].avg_int_rat;
            this.money_credit_line[i] = response.data[i].money_credit_line;
            this.loan_repayment[i] = response.data[i].loan_repayment;
            this.loan_url[i] = response.data[i].loan_url;

            this.recom = 1;
            console.log(this.loan_good_num[i]);
            }
          }
        console.log(this.results)
        this.current_array = 0;
        console.log(this.loan_img[0]),
        console.log(this.loan_img[1]),
        console.log(this.loan_img[2])
        }).catch(function (error) {
        console.log(error);
        });
      },
      
    changeproduct: function(){
      console.log("changeproduct 실행됨");
      console.log(this.results);
      console.log(this.results.length);
      console.log(this.current_array);
      this.current_array += 1;
        if(this.results.length <= (this.current_array)){
          alert('마지막 상품입니다.');
          this.current_array = 0;
        }else{
        console.log(this.current_array);
        }
      },

      selectproduct: function(){
      this.isdetail = true
      console.log("selectproduct 실행됨")
      console.log(this.loan_good_num[this.current_array])
      console.log(this.loan_good_name[this.current_array])  
        axios({
        method : 'post',
        url : 'http://localhost:3000/process/registerpost',
        data: {
          loan_good_num: this.loan_good_num[this.current_array],
          loan_good_name: this.loan_good_name[this.current_array],
          cus_num : this.cus_num[0]
        }})
        .then((response) => {
          console.log('select product 실행');
          console.log(this.loan_good_num[this.current_array]);
          console.log('send 실행');
          bus.$emit('send', this.cus_num);   
          console.log('데이터 받아오기 성공');
          console.log('select product 실행 종료');
          this.isComputed = true;
          console.log('reset inform  실행');
          bus.$emit('resetInform');
        })
        console.log(this.loan_good_num)
        console.log(this.loan_good_name)
      },
      
      reset: function(){
        this.cus_age= '0',
        this.cus_sex= '0',
        this.repayment= '0',
        this.repayment_money= '0',
        this.cus_salary= '0',
        this.cus_loan= '0',
        this.leasing_mortgage= '0',
        this.month_loan_period= '0',
        this.bank_id= '0',
        this.isComputed = false
      }
    },
    components: {
      VueNumeric,
      Computes
    },
    computed:{
      limit_money:function(){
      var limit1=this.leasing_mortgage*0.8;
      var limit2=this.cus_salary*3.5;
      var limit3=500000000;
      var limit4 = this.cus_loan;
        if(limit4 > limit1){
          this.check = 1;
        }else if(limit4 > limit2){
          this.check = 2;
        }else if(limit4 > limit3){
          this.check =3;
        }else{
          this.check =0;
        }

        if(this.month_loan_period <=36 && this.month_loan_period >=12 ){
        this.check2 = 0;
        }else{
        this.check2 = 1;
        }
      return Math.min(limit1,limit2,limit3);  
      }
    }
}
</script>

<style>
.tooltip-inner {
  max-width: 250px;
  width: 250px; 
} 

.form-control{
  width: 50%;
  display: inline;
  font-size: 1.5rem;
}

#selectbox{
  height: 3.1rem;
}
.customerlabel{
  width: 40%;
  font-size: 20px;
  text-align: center;
  color: black;
}
#btn_loanpage{
  background-color: white;
  color: black;
  border-radius: 1;
  border-color:black;
 
}
#loanbuttons{
      text-align: center;
}

table.type04 {
  border-collapse: separate;
  border-spacing: 1px;
  text-align: center;
  line-height: 1.5;
  border-top: 1px solid #ccc;
  margin : 2px 10px;
  float : center
}
table.type04 th {
    width: 400px;
    padding: 10px;
    font-weight: bold;
    vertical-align: top;
    border-bottom: 1px solid #ccc;
    text-align: center;
}
table.type04 td {
    width: 350px;
    padding: 10px;
    vertical-align: top;
    border-bottom: 1px solid #ccc;
    text-align: center;
}
    </style>

    <style>
table.type09 {
    border-collapse: collapse;
    text-align: center;
    line-height: 1.5;
    float : center

}
table.type09 thead th {
    padding: 10px;
    font-weight: bold;
    vertical-align: top;
    color: #369;
    border-bottom: 3px solid #036;
}
table.type09 tbody th {
    width: 150px;
    padding: 10px;
    font-weight: bold;
    vertical-align: top;
    border-bottom: 1px solid #ccc;
    background: #f3f6f7;
     text-align: center;
}
table.type09 td {
    width: 350px;
    padding: 10px;
    vertical-align: top;
    border-bottom: 1px solid #ccc;
     text-align: center;
}
</style>