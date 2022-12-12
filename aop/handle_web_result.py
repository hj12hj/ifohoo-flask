from functools import wraps

from flask import jsonify

from returnmessage import ReturnMessage


# web处理返回值处理成json
def handle_web_result(func):
    @wraps(func)
    def handle_result_wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if isinstance(res, str):
            return res
        if isinstance(res, ReturnMessage):
            return jsonify(res.__dict__)
        return res

    return handle_result_wrapper
