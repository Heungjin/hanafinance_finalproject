var fs = require('fs');
var ejs = require('ejs');
var http = require('http');
var mysql = require('mysql');
var express = require('express');
var bodyParser = require('body-parser');

// DB 연결 
var conn = mysql.createConnection({
    host: 'hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com',
    port: '3306',
    database: 'hanaproject',
    user: 'admin',
    password: 'wjsgmdwls'
});
console.log("DB에 연결됨")
var app = express();

// 서버 생성 
http.createServer(app).listen(8000, function() {
    console.log('Server running at hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com:3306')
})

app.use(bodyParser.urlencoded({
    extended: true
}));

app.get('/age_statistic_prefer', function(request, response) {
    fs.readFile('age_statistic_prefer.html', 'utf8', function(error, data) {

        conn.query('select * from statistic_age', [], function(error, result) {
            response.writeHead(200, {
                'Content-Type': 'text/html'
            });
            response.end(ejs.render(data, {
                data: result
            }));
        });
    });
});

app.get('/age_statistic_repayment', function(request, response) {
    fs.readFile('age_statistic_repayment.html', 'utf8', function(error, data) {

        conn.query('select * from statistic_age', [], function(error, result) {
            response.writeHead(200, {
                'Content-Type': 'text/html'
            });
            response.end(ejs.render(data, {
                data: result
            }));
            console.log(result[0].m0_20);
        });
    });
});

app.get('/amount_statistic_repayment', function(request, response) {
    fs.readFile('amount_statistic_repayment.html', 'utf8', function(error, data) {

        conn.query('select * from statistic_loan_amount', [], function(error, result) {
            response.writeHead(200, {
                'Content-Type': 'text/html'
            });
            response.end(ejs.render(data, {
                data: result
            }));
        });
    });
});

app.get('/amount_statistic_prefer', function(request, response) {
    fs.readFile('amount_statistic_prefer.html', 'utf8', function(error, data) {

        conn.query('select * from statistic_loan_amount', [], function(error, result) {
            response.writeHead(200, {
                'Content-Type': 'text/html'
            });
            response.end(ejs.render(data, {
                data: result
            }));
        });
    });
});

app.get('/salary_statistic_prefer', function(request, response) {
    fs.readFile('salary_statistic_prefer.html', 'utf8', function(error, data) {

        conn.query('select * from statistic_salary', [], function(error, result) {
            response.writeHead(200, {
                'Content-Type': 'text/html'
            });
            response.end(ejs.render(data, {
                data: result
            }));
        });
    });
});

app.get('/list_statistic', function(request, response) {
    fs.readFile('list_statistic.html', 'utf8', function(error, data) {
        var temp = {};

        conn.query('select * from statistic_list', [], function(error, result) {
            conn.query('select * from loan_goods', [], function(error2, result2) {
                temp.data1 = result;
                temp.data2 = result2;
                response.writeHead(200, {
                    'Content-Type': 'text/html'
                });
                response.end(ejs.render(data, {
                    data: temp
                }));
            });
        });
    });
});