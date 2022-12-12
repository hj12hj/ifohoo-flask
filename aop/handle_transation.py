import datetime
from functools import wraps
from variables.local_connetion import local_connect
from flask import jsonify, request


# 事务注解
def transaction(func):
    @wraps(func)
    def transaction_wrapper(*args, **kwargs):
        conn = None
        try:
            conn = local_connect.conn
            if conn is None:
                raise RuntimeError("conn is None!")
            conn.begin()
            res = func(*args, **kwargs)
            conn.commit()
            return res
        except Exception as e:
            conn.rollback()
            raise Exception(str(e))

    return transaction_wrapper
