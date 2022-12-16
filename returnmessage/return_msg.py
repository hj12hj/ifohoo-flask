class ReturnMessage:
    def __init__(self, code=200, message="OK", data=None, maps=None):
        self.errorCode = "0"
        self.message = message
        self.returnData = data
        self.paramInfo = {}
        self.success = True
