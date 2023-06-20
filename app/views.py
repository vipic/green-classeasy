from flask import render_template, request

from app.response import make_success_response, make_err_response
from run import app
from app.data import Data
from app.tool import pick
from app.download import download_task
import requests

res = Data()


@app.route('/')
def index():
    return render_template('app.html')


@app.route('/query', methods=["post"])
def query():
    """
    查询接口，返回原始数据
    :return:
    """
    params = request.get_json()
    url = "http://m.classeasy.cn/make/wx/notes"
    if "cookie" not in params:
        return make_err_response("未登录")
    if "timestamp" in params:
        url = f'http://m.classeasy.cn/make/wx/notes?v={params["timestamp"]}'

    cookies = {"GWSESSION": params['cookie']}
    print(url)
    try:
        response = requests.get(url, cookies=cookies)
        if not response.status_code == 200:
            return make_err_response(response.text, code=response.status_code)
        else:
            data = response.json()
            res.data = data
            return make_success_response(data)
    finally:
        pass


@app.route('/download', methods=["post"])
def download():
    params = request.get_json()
    if "id" not in params:
        return make_err_response("请选择日期")
    dd = pick(params['id'], res.data)
    result = download_task(dd)
    return make_success_response(result)


@app.route('/download_all', methods=["post"])
def download_all():
    for item in res.data:
        dd = pick(item['id'], res.data)
        result = download_task(dd)
    return make_success_response('done')
