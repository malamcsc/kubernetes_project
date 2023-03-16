import json

class Response(object):
    
    def __init__(self, data = None, StatusCode = None, ErrorMessage = None):
        self.data = data
        self.StatusCode = StatusCode
        self.ErrorMessage = "" if ErrorMessage is None else ErrorMessage

        
    def serialize(self):
        return json.dumps({
            "data": self.data,
            "StatusCode": self.StatusCode.value,
            "ErrorMessage": self.ErrorMessage 
        })