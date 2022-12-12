import datetime
from functools import wraps
from flask import jsonify


# 处理返回值
def handle_time_format(func):
    @wraps(func)
    def handle_result_wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return resolve_list(res)

    return handle_result_wrapper


def resolve_list(datas: list) -> list:
    if isinstance(datas, list):
        for data in datas:
            keys = list(data.keys())
            for key in keys:
                if type(data[key]) == datetime.datetime:
                    data[key] = data[key].strftime('%Y-%m-%d %H:%M:%S')
                if type(data[key]) == datetime.date:
                    data[key] = data[key].strftime('%Y-%m-%d')
        return datas
    elif isinstance(datas, dict):
        keys = list(datas.keys())
        for key in keys:
            if type(datas[key]) == datetime.datetime:
                datas[key] = datas[key].strftime('%Y-%m-%d %H:%M:%S')
            if type(datas[key]) == datetime.date:
                datas[key] = datas[key].strftime('%Y-%m-%d')
        return datas

    elif isinstance(datas,tuple):
        pass
