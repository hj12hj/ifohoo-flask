from functools import wraps
from flask import jsonify, request
from variables.local_page_helper import local_page_info


# 请求数据透传处理 透传到controller params  json_data headers
def handle_web_request(func):
    @wraps(func)
    def handle_request_wrapper(*args, **kwargs):
        try:
            params = request.args
        except Exception as e:
            params = None

        try:
            json_data = request.json
        except Exception as e:
            json_data = None

        try:
            headers = request.headers
        except Exception as e:
            headers = None

        res = func(params=params, json_data=json_data, headers=headers)
        return res

    return handle_request_wrapper
