// testing post
// var testpost = function(req, res) {
//     console.log('post test호출');
//     res.send({
//         message: `노드서버로부터 ~ ${req.body.text1},${req.body.text2},${req.body.text3},${req.body.text4},${req.body.text5},${req.body.text6} 전달받음`
//     })
// };




var registerpost = function(req, res) {
    console.log('/process/registerpost');

    var paramloan_good_name = req.body.loan_good_name || req.query.loan_good_name;
    var paramloan_good_num = req.body.loan_good_num || req.query.loan_good_num;
    var paramcus_num = req.body.cus_num || req.query.cus_num;

    console.log("post send data " + paramloan_good_num);

    var database = req.app.get('database');
    if (database) {
        registerproduct(database, paramloan_good_name, paramloan_good_num, paramcus_num, function(err, result) {
            if (err) {
                console.error('계산 테이블2 정보 추가 중 에러 발생' + err.stack);
            }

            if (result) {
                console.dir(result);
                console.log('계산 테이블2 정보 추가 추가 성공');
                res.json(result)

            } else {
                res.writeHead(200, {
                    "Content-Type": 'text/html;charset=utf8'
                });
                res.write('<h1>계산 테이블2 정보 추가 추가 실패</h1>');
                res.end();
            }

        });
    } else {
        res.writeHead(200, {
            "Content-Type": 'text/html;charset=utf8'
        });
        res.write('<h1>데이터베이스 연결 실패</h1>');
        res.write('<div><p>DB에 연결하지 못했습니다.</p></div>');
        res.end();
    }
}



var testpost = function(req, res) {
    console.log('/process/testpost호출됨.');
    var cus_age = req.body.cus_age || req.query.cus_age;
    var cus_sex = req.body.cus_sex || req.query.cus_sex;
    var repayment = req.body.repayment || req.query.repayment;
    var repayment_money = req.body.repayment_money || req.query.repayment_money;
    var cus_salary = req.body.cus_salary || req.query.cus_salary;
    var cus_loan = req.body.cus_loan || req.query.cus_loan;
    var leasing_mortgage = req.body.leasing_mortgage || req.query.leasing_mortgage;
    var month_loan_period = req.body.month_loan_period || req.query.month_loan_period;
    var bank_id = req.body.bank_id || req.query.bank_id;
    // var money_credit_line = req.body.money_credit_line || req.query.money_credit_line;
    // num1 = num1 * 1;
    // num2 = num2 * 1;
    // num3 = num3 * 1;
    console.log('parameter : %s, %s, %s, %s,%s,%s,%s,%s,%s', cus_age, cus_sex, repayment, repayment_money, cus_salary, cus_loan, leasing_mortgage, month_loan_period, bank_id);

    var database = req.app.get('database');
    if (database) {
        addUser(database, cus_age, cus_sex, repayment, repayment_money, cus_salary, cus_loan, leasing_mortgage, month_loan_period, bank_id, function(err, result) {
            // 데이터 삽입 중 에러 발생 시 처리
            if (err) {
                console.error('사용자 추가 중 에러 발생' + err.stack);
            } // 에러 처리

            // result가 있음 : 정상적으로 데이터가 들어감.
            if (result) {
                recommendLoan(database, cus_age, cus_sex, repayment, repayment_money, cus_salary, cus_loan, leasing_mortgage, month_loan_period, bank_id, function(err, rows) {

                    if (err) {
                        console.error('상품 추천 중 에러 발생' + err.stack);
                    }

                    if (rows) {
                        console.dir(rows);
                        console.log('상품 추천 성공');
                        res.json(rows);
                        //res.send(rows);
                    } else {

                        console.log('상품 추천 실패');
                        res.json({ error: '추천 상품이 없습니다. 다시 검색해주세요' });
                    }

                });
                console.dir(result);
                console.log('사용자 정보 추가 성공');


            } else {
                res.writeHead(200, {
                    "Content-Type": 'text/html;charset=utf8'
                });
                res.write('<h1>사용자 정보 추가 실패</h1>');
                res.end();
            }
        });



    } else {
        res.writeHead(200, {
            "Content-Type": 'text/html;charset=utf8'
        });
        res.write('<h1>데이터베이스 연결 실패</h1>');
        res.write('<div><p>DB에 연결하지 못했습니다.</p></div>');
        res.end();
    }

}



var recommendLoan = function(database, cus_age, cus_sex, repayment, repayment_money, cus_salary, cus_loan, leasing_mortgage, month_loan_period, bank_id, callback) {
    console.log('recommend 호출');
    database.getConnection(function(err, conn) {
        if (err) {
            console.log('DB 연결 중 오류 발생');
            if (conn) {
                conn.release();
            }
            callback(err, null);
            return;
        }
        console.log('데이터베이스 연결 Thread');

        var temp = cus_salary * 3.5;
        var ac_loan = cus_loan;
        console.log('repayment : ' + repayment);

        var data = ['loan_good_num', 'loan_good_name', 'loan_bank_id', 'avg_int_rat', 'money_credit_line', 'rate_credit_line', 'salary_credit_line', 'month_loan_period_line', 'loan_repayment', 'loan_url', 'loan_img', 'num_recommend', 'chatbot_img', 'chatbot_description', 'chat_recommend', 'cus_num'];
        // if (repayment == 0) {
        //     var exec = conn.query('select ?? from loan_goods as loan, customer_info as customer where loan.loan_bank_id = ? and ? <= loan.month_loan_period_line and (? <= loan.money_credit_line and ? <= (cast(loan.rate_credit_line as decimal(5,2)) * ?) and ? <= ?) and cus_num in (select Max(cus_num) from customer_info) order by loan.avg_int_rat', [data, bank_id, month_loan_period, ac_loan, ac_loan, leasing_mortgage, ac_loan, temp], function(err, result) {
        //         conn.release();
        //         console.log('실행 대상 SQL : ' + exec.sql);
        //         if (err) {
        //             console.log('sql 수행 중 에러 발생함');
        //             console.dir(err);

        //             callback(err, null);
        //             return;
        //         }
        //         callback(null, result);
        //     });
        // } else {
        //     var exec = conn.query('select ?? from loan_goods as loan, customer_info as customer where loan.loan_repayment = ? and loan.loan_bank_id = ? and  ? <= loan.month_loan_period_line and(? <= (cast(loan.rate_credit_line as decimal(5,2)) * ?) and ? <= (loan.rate_credit_line * ?) and ? <= ?) and cus_num in (select Max(cus_num) from customer_info) order by loan.avg_int_rat', [data, repayment, bank_id, month_loan_period, ac_loan, ac_loan, leasing_mortgage, ac_loan, temp], function(err, result) {
        //         conn.release();
        //         console.log('실행 대상 SQL : ' + exec.sql);
        //         if (err) {
        //             console.log('sql 수행 중 에러 발생함');
        //             console.dir(err);

        //             callback(err, null);
        //             return;
        //         }
        //         callback(null, result);
        //     });
        // }













        if (cus_loan <= (leasing_mortgage * 0.7)) {
            console.log('0.7추천됨');

            if (repayment == 0) {
                var exec = conn.query('select ?? from loan_goods as loan, customer_info as customer where loan.loan_bank_id = ? and ? <= loan.month_loan_period_line and (? <= loan.money_credit_line  and ? <= ?) and cus_num in (select Max(cus_num) from customer_info) order by loan.avg_int_rat', [data, bank_id, month_loan_period, ac_loan, ac_loan, temp], function(err, result) {
                    conn.release();
                    console.log('실행 대상 SQL : ' + exec.sql);
                    if (err) {
                        console.log('sql 수행 중 에러 발생함');
                        console.dir(err);

                        callback(err, null);
                        return;
                    }
                    callback(null, result);
                });
            } else {
                var exec = conn.query('select ?? from loan_goods as loan, customer_info as customer where loan.loan_repayment = ? and loan.loan_bank_id = ? and  ? <= loan.month_loan_period_line and(? <= loan.money_credit_line  and ? <= ?) and cus_num in (select Max(cus_num) from customer_info) order by loan.avg_int_rat', [data, repayment, bank_id, month_loan_period, ac_loan, ac_loan, temp], function(err, result) {
                    conn.release();
                    console.log('실행 대상 SQL : ' + exec.sql);
                    if (err) {
                        console.log('sql 수행 중 에러 발생함');
                        console.dir(err);

                        callback(err, null);
                        return;
                    }
                    callback(null, result);
                });
            }





        } else {
            console.log('여기서 추천받음');
            if (repayment == 0) {
                var exec = conn.query("select ?? from loan_goods as loan, customer_info as customer where cast(loan.rate_credit_line as decimal(5,1))=0.8 and loan.loan_bank_id = ? and ? <= loan.month_loan_period_line and (? <= loan.money_credit_line  and ? <= ?) and cus_num in (select Max(cus_num) from customer_info) order by loan.avg_int_rat", [data, bank_id, month_loan_period, ac_loan, ac_loan, temp], function(err, result) {
                    conn.release();
                    console.log('실행 대상 SQL : ' + exec.sql);
                    if (err) {
                        console.log('sql 수행 중 에러 발생함');
                        console.dir(err);

                        callback(err, null);
                        return;
                    }
                    callback(null, result);
                });
            } else {
                var exec = conn.query("select ?? from loan_goods as loan, customer_info as customer where cast(loan.rate_credit_line as decimal(5,1))=0.8  and loan.loan_repayment = ? and loan.loan_bank_id = ? and  ? <= loan.month_loan_period_line and(? <= loan.money_credit_line  and ? <= ?) and cus_num in (select Max(cus_num) from customer_info) order by loan.avg_int_rat", [data, repayment, bank_id, month_loan_period, ac_loan, ac_loan, temp], function(err, result) {
                    conn.release();
                    console.log('실행 대상 SQL : ' + exec.sql);
                    if (err) {
                        console.log('sql 수행 중 에러 발생함');
                        console.dir(err);

                        callback(err, null);
                        return;
                    }
                    callback(null, result);
                });
            }











        }







        conn.on('error', function(err) {
            console.log('데이터베이스 연결 시 에러 발생함.');
            console.dir(err);
            callback(err, null);

        });
    });
}


var searchUser = function(database, callback) {
    console.log('searchUser 호출');
    database.getConnection(function(err, conn) {
        if (err) {
            console.log('DB연결 중 오류 발생');
            if (conn) {
                conn.release();
            }
            callback(err, null);
            return;
        }
        console.log('데이터베이스 연결 Thread');

        var exec = conn.query('select Max(cus_num) from customer_info', function(err, result) {
            conn.release();
            console.log('실행 대상 SQL' + exec.sql);

            if (err) {
                console.log('SQL 수행 중 에러 발생함');
                console.dir(err);

                callback(err, null);
                return;
            }
            callback(null, result);
        });
    });
}



var registerproduct = function(database, loan_good_name, loan_good_num, cus_num, callback) {
    console.log('register product');
    database.getConnection(function(err, conn) {
        if (err) {
            console.log('DB 연결 중 오류 발생');
            if (conn) {
                conn.release();
            }
            callback(err, null);
            return;
        }
        console.log('데이터베이스 연결 Thread');


        console.log('register product call' + loan_good_num);
        console.log('######################' + cus_num);

        var data = {
            loan_good_name: loan_good_name,
            loan_good_num: loan_good_num,
            cus_num: cus_num
        }

        var exec = conn.query('insert into tb_calc2 set ?', data, function(err, result) {
            conn.release();
            console.log('실행 대상 SQL:' + exec.sql);

            if (err) {
                console.log('SQL 수행 중 에러 발생함');
                console.dir(err);

                callback(err, null);
                return;
            }
            callback(null, result);
        });
        conn.on('error', function(err) {
            console.log('데이터베이스 연결 시 에러 발생함');
            console.dir(err);

            callback(err, null);
        });
    });
}


var addUser = function(database, cus_age, cus_sex, repayment, repayment_money, cus_salary, cus_loan, leasing_mortgage, month_loan_period, bank_id, callback) {
    console.log('addUser호출됨');
    database.getConnection(function(err, conn) {
        if (err) {
            console.log('DB연결 중 오류발생');
            if (conn) {
                conn.release();
            }
            callback(err, null);
            return;
        }
        console.log('데이터베이스 연결 Thread');

        var data = {
            cus_age: cus_age,
            cus_sex: cus_sex,
            repayment: repayment,
            repayment_money: repayment_money,
            cus_salary: cus_salary,
            cus_loan: cus_loan,
            leasing_mortgage: leasing_mortgage,
            month_loan_period: month_loan_period,
            bank_id: bank_id
        }
        var exec = conn.query('insert into customer_info set ?', data, function(err, result) { // set : 모든 컬럼에 data를 삽입, ?는 데이터로 대응

            conn.release();
            console.log('실행 대상 SQL : ' + exec.sql);

            if (err) {
                console.log('SQL 수행 중 에러 발생함.');
                console.dir(err);
                callback(err, null);
                return;
            }
            // err가 없을 경우
            console.log(result);
            callback(null, result); // result는 router에 등록되어있는 callback함수로 전달
        });

        // conn이 잘 들어왔을 경우
        conn.on('error', function(err) {
            console.log('데이터베이스 연결 시 에러 발생함.');
            console.dir(err);

            callback(err, null);

        });

    });

}


var senduser = function(database, callback) {
    console.log('send user 호출');
    database.getConnection(function(err, conn) {
        if (err) {
            console.log('DB 연결 중 오류 발생');
            if (conn) {
                conn.release();
            }
            callback(err, null);
            return;
        }
        console.log('데이터베이스 연결 Thread');

        var exec = conn.query('select * from customer_info, loan_goods, tb_calc2, banks ' +
            'where customer_info.cus_num = tb_calc2.cus_num ' +
            'and loan_goods.loan_good_num = tb_calc2.loan_good_num ' +
            'and loan_goods.loan_bank_id = banks.bank_id ' +
            'and tb_calc2.cus_num in ((select Max(cus_num) from tb_calc2))',
            function(err, result) {
                conn.release();
                console.log('실행 대상 SQL' + exec.sql);
                if (err) {
                    console.log('SQL 수행 중 에러 발생함');
                    console.dir(err);

                    callback(err, null);
                    return;
                }
                callback(null, result);
            });
    });
}


var getuser = function(req, res) {
    console.log('getuser 호출');

    var database = req.app.get('database');

    if (database) {
        senduser(database, function(err, result) {
            if (err) {
                console.error('추천 정보 및 유저 정보 받기 에러 발생' + err.stack);
                res.end();
                return;
            }

            if (result) {
                console.dir(result);
                console.log('추천 정보 및 유저 정보 받기 성공');
                res.json(result);
            } else {
                res.writeHead(200, {
                    "Content-Type": 'text/html;charset=utf8'
                });
                res.write('<h1>추천 정보 및 유저 정보 받기 실패</h1>');
                res.end();
            }
        });
    } else {
        res.writeHead(200, {
            "Content-Type": 'text/html;charset=utf8'
        });
        res.write('<h1>데이터베이스 연결 실패</h1>');
        res.write('<div><p>DB에 연결하지 못했습니다.</p></div>');
        res.end();
    }
}



// testing 

var testget = function(req, res) {
    console.log('get test호출');
    res.send({
        message: `Hello! Have fun!`
    })
};


module.exports.testpost = testpost;
module.exports.testget = testget;
module.exports.registerpost = registerpost;
module.exports.getuser = getuser;