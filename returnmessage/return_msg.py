class ReturnMessage:
    def __init__(self, code=200, message="OK", data=None, maps=None):
        self.code = 200
        self.message = message
        self.returnData = data
        self.maps = {}
