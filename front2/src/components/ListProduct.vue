<template>
<!-- 전체 리스트 -->
<section id="listproduct2">
  <div class ="container">
  <br><br><br><br><br><br><br>
  <div class="text-center wow fadeIn">
      <h2>전체 리스트 보기</h2>
      <hr class="colored">
</div>
    <div id="sel"></div>
    <div style="margin-left:180px"></div>
    <v-client-table :data="lists" :columns="columns" :options="options">
      <a slot="loan_url" slot-scope="props" target="_blank" :href="props.row.loan_url" style="color:dodgerblue;text-decoration: underline;background-color:transparent;border-color: white;font-size: 15px;" >상세</a>
    </v-client-table>
  </div>
  <br><br><br><br><br><br><br>
</section>
</template>

<script>
import axios from 'axios'
export default{
  data(){
    return{ 
      lists : [],
      columns: [ 'bank_name', 'loan_good_name','avg_int_rat','money_credit_line','loan_repayment','loan_url'],
      rows:[],
      options: {
        filterByColumn: false,
        perPage:6,
        perPageValues: [6, 12, 18],
        texts: {
          filter: "검색:",
          filterBy: 'Filtrar por {column}',
          count:' '
        },
        pagination: { chunk:10,dropdown:false},
        filterable:['bank_name', 'loan_good_name'],
        headings: {
          bank_name:'  은행　　 ↕',
          loan_good_name:'상품명　　　　 ↕',
          avg_int_rat:'평균금리　　 ↕',
          money_credit_line:'최대대출한도　　 ↕',
          loan_repayment:'상환방식',
          loan_url:'상세정보'
        },
      }
    }
  },
  mounted:function(){
    var list = this.lists;
    axios({
      method:'get',
      url:'http://localhost:3000/api/process/listProduct'    
    }).then(function(response){
        console.log('list product');
        console.log('전체 리스트 '+response.data.length);
        for(var i =0; i < response.data.length; i++){
          list.push({
          'bank_name' : response.data[i].bank_name,
          'loan_good_name' : response.data[i].loan_good_name,
          'avg_int_rat' : response.data[i]. avg_int_rat + '%',
          'money_credit_line' : response.data[i].money_credit_line + '원',
          'loan_repayment' : (response.data[i].loan_repayment===0?'만기일시상환':'부분만기 & 원리금상환'),
          'loan_url' : response.data[i].loan_url
          })
        }
      console.log('list product통신결과 : ' + list);
    })
  },
}
</script>

<style>
body {
  background: #fff;
}

#sel {
  margin-left: 10px;
}

#VueTables__limit_GW5qi{
  font-size: 15px
}



.VueTables__sortable:hover{
    background-color: darkgray;
    cursor:pointer;
}

.VuePagination{
  text-align: center;
}

.VueTables__date-filter {
  border: 1px solid #ccc;
  padding: 6px;
  border-radius: 4px;
  cursor: pointer;
}


th,
td {
  text-align: center;
}

th:nth-child(n + 2),
td:nth-child(n + 2) {
  text-align: center;
}
 
thead tr:nth-child(2) th {
  font-weight: normal;
  width:10px;
}

.VueTables__filter-placeholder {
  color: #aaa;
}

.VueTables__list-filter {
  height: 10px;
} 
</style>