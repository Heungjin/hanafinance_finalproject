// 설정값을 가지고 있는 모듈
module.exports = {
    server_port: 3000 || process.env.PORT,
    route_info: [{
            file: './test',
            path: '/process/testpost',
            method: 'testpost',
            type: 'post'
        },
        {
            file: './test',
            path: '/process/testget',
            method: 'testget',
            type: 'get'
        },
        {
            file: './test',
            path: '/process/registerpost',
            method: 'registerpost',
            type: 'post'
        },
        {
            file: './test',
            path: '/api/process/getuser',
            method: 'getuser',
            type: 'get'
        },
        {
            file: './list',
            path: '/api/process/listProduct',
            method: 'listProduct',
            type: 'get'
        },
        {
            file: './stat',
            path: '/api/process/age_statistic',
            method: 'age_statistic',
            type: 'get'
        },
        {
            file: './stat',
            path: '/api/process/amount_statistic',
            method: 'amount_statistic',
            type: 'get'
        },
        {
            file: './stat',
            path: '/api/process/list_statistic',
            method: 'list_statistic',
            type: 'get'
        }

    ]
};