var age_statistic = function(req, res) {
    console.log('process/age_statistic 호줄됨');
    var database = req.app.get('database');
    if (database) {
        database.query('select * from statistic_age', function(err, data1) {
            if (err) {
                console.error('err:%s', err);
                res.end();
                return;
            }
            if (data1) {
                console.dir(data1);
                console.log('상품정보 불러오는데 성공1111');

                database.query('select * from loan_goods', function(err2, data2) {
                    if (err2) {
                        console.error('err:%s', err2);
                        res.end();
                        return;
                    }
                    if (data2) {
                        console.dir(data2);
                        console.log('상품정보 불러오는데 성공2222');

                        var temp = {};
                        temp.data1 = data1;
                        temp.data2 = data2;

                        res.json(temp);

                    } else {
                        console.log('상품없음.');
                        res.json({ error: 'db에 저장된 상품이 없습니다.' });
                    }
                })



            } else {
                console.log('상품없음.');
                res.json({ error: 'db에 저장된 상품이 없습니다.' });
            }
        })
    } else {
        res.writeHead(200, {
            "Content-Type": 'text/html;charset=utf8'
        });
        res.write('<h1>데이터베이스 연결 실패</h1>');
        res.write('<div><p>DB에 연결하지 못했습니다.</p></div>');
        res.end();
    }
};

var amount_statistic = function(req, res) {
    console.log('process/amount_statistic 호줄됨');
    var database = req.app.get('database');
    if (database) {
        database.query('select * from statistic_loan_amount', function(err, data) {
            if (err) {
                console.error('err:%s', err);
                res.end();
                return;
            }
            if (data) {
                console.dir(data);
                console.log('상품정보 불러오는데 성공');
                res.json(data);

            } else {
                console.log('상품없음.');
                res.json({ error: 'db에 저장된 상품이 없습니다.' });
            }
        })
    } else {
        res.writeHead(200, {
            "Content-Type": 'text/html;charset=utf8'
        });
        res.write('<h1>데이터베이스 연결 실패</h1>');
        res.write('<div><p>DB에 연결하지 못했습니다.</p></div>');
        res.end();
    }
};

var list_statistic = function(req, res) {
    console.log('process/list_statistic 호줄됨');
    var database = req.app.get('database');
    if (database) {
        database.query('select * from statistic_list', function(err1, data1) {
            if (err1) {
                console.error('err:%s', err1);
                res.end();
                return;
            }
            if (data1) {
                console.dir(data1);
                console.log('상품정보 불러오는데 성공1');

                database.query('select * from loan_goods', function(err2, data2) {
                    if (err2) {
                        console.error('err:%s', err2);
                        res.end();
                        return;
                    }
                    if (data2) {
                        console.dir(data2);
                        console.log('상품정보 불러오는데 성공2');

                        var temp = {};
                        temp.data1 = data1;
                        temp.data2 = data2;

                        res.json(temp);

                    } else {
                        console.log('상품없음.');
                        res.json({ error: 'db에 저장된 상품이 없습니다.' });
                    }
                })
            } else {
                console.log('상품없음.');
                res.json({ error: 'db에 저장된 상품이 없습니다.' });
            }
        })
    } else {
        res.writeHead(200, {
            "Content-Type": 'text/html;charset=utf8'
        });
        res.write('<h1>데이터베이스 연결 실패</h1>');
        res.write('<div><p>DB에 연결하지 못했습니다.</p></div>');
        res.end();
    }
};

module.exports.age_statistic = age_statistic;
module.exports.amount_statistic = amount_statistic;
module.exports.list_statistic = list_statistic;



// var age_statistic_prefer = function(req, res) {
//     console.log('/process/age_statistic_prefer');
//     var database = req.app.get('database');
//     database.getConnection(function(err, conn) {
//         if (err) {
//             console.log('DB연결 중 오류발생');
//             if (conn) {
//                 conn.release();
//             }
//             callback(err, null);
//             return;
//         }
//         console.log('DB연결 Thread');
//         fs.readFile('age_statistic_prefer.html', 'utf8', function(error, data) {
//             var exec = conn.query('select * from statistic_age', [], function(error, result) {
//                 conn.release();
//                 console.log('실행 대상 SQL : ' + exec.sql);
//                 callback(null, result);
//                 res.end(ejs.render(data, {
//                     data: result
//                 }));
//             });
//         });

//     })
// };



// app.get('/age_statistic_repayment', function(request, response) {
//     fs.readFile('age_statistic_repayment.html', 'utf8', function(error, data) {

//         conn.query('select * from statistic_age', [], function(error, result) {
//             response.writeHead(200, {
//                 'Content-Type': 'text/html'
//             });
//             response.end(ejs.render(data, {
//                 data: result
//             }));
//             console.log(result[0].m0_20);
//         });
//     });
// });

// app.get('/amount_statistic_repayment', function(request, response) {
//     fs.readFile('amount_statistic_repayment.html', 'utf8', function(error, data) {

//         conn.query('select * from statistic_loan_amount', [], function(error, result) {
//             response.writeHead(200, {
//                 'Content-Type': 'text/html'
//             });
//             response.end(ejs.render(data, {
//                 data: result
//             }));
//         });
//     });
// });

// app.get('/amount_statistic_prefer', function(request, response) {
//     fs.readFile('amount_statistic_prefer.html', 'utf8', function(error, data) {

//         conn.query('select * from statistic_loan_amount', [], function(error, result) {
//             response.writeHead(200, {
//                 'Content-Type': 'text/html'
//             });
//             response.end(ejs.render(data, {
//                 data: result
//             }));
//         });
//     });
// });

// app.get('/salary_statistic_prefer', function(request, response) {
//     fs.readFile('salary_statistic_prefer.html', 'utf8', function(error, data) {

//         conn.query('select * from statistic_salary', [], function(error, result) {
//             response.writeHead(200, {
//                 'Content-Type': 'text/html'
//             });
//             response.end(ejs.render(data, {
//                 data: result
//             }));
//         });
//     });
// });

// app.get('/list_statistic', function(request, response) {
//     fs.readFile('list_statistic.html', 'utf8', function(error, data) {
//         var temp = {};

//         conn.query('select * from statistic_list', [], function(error, result) {
//             conn.query('select * from loan_goods', [], function(error2, result2) {
//                 temp.data1 = result;
//                 temp.data2 = result2;
//                 response.writeHead(200, {
//                     'Content-Type': 'text/html'
//                 });
//                 response.end(ejs.render(data, {
//                     data: temp
//                 }));
//             });
//         });
//     });
// });