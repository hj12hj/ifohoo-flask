# 自定义异常处理类
import json


class IfmsHttpException(Exception):
    def __init__(self, msg, code):
        super().__init__(self)
        self.msg = msg
        self.code = code

    def __str__(self) -> str:
        errorMsg = {
            "code": self.code,
            "msg": self.msg
        }
        return json.dumps(errorMsg)
