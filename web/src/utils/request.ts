import axios from 'axios';

const request = axios.create({
    baseURL: 'http://127.0.0.1',
    timeout: 5 * 60 * 1000,
    headers: {'Content-type': 'application/json'}
});

request.interceptors.request.use((config) => {
    return config;
});

// 添加响应拦截器
request.interceptors.response.use(
    function (response) {
        const {code, data} = response.data;
        // 后台响应0是正常
        if (code === 0) {
            return data;
        } else {
            return Promise.reject('出错了');
        }
    },
    function (error) {
        return Promise.reject(error);
    }
);
export default request;
