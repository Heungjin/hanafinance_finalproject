var listProduct = function(req, res) {
    console.log('process/listProduct호줄됨');
    var database = req.app.get('database');
    if (database) {
        database.query('select * from loan_goods,banks where loan_goods.loan_bank_id=banks.bank_id order by bank_id, avg_int_rat', function(err, data) {
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

module.exports.listProduct = listProduct;