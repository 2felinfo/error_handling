from dataclasses import  dataclass
@dataclass
class CaptosExceptions(Exception):
    error_id:int
    trace_back:str
    message:str
    name_service=str
    send_to_queue=bool

    def __int__(self,error_id,type_error="",message="",name_service=None,send_to_qeue=True):
        self.error_id=error_id
        self.type_error=type_error
        self.message=message
        self.name_service=name_service
        self.send_to_queue=send_to_qeue
        super().__init__(message)

    def convert_error_to_dict(self):
        result=dict()
        result['error_id']=self.error_id
        result['type_error']=self.type_error
        result['message']=self.message
        result['name_service']=self.name_service
        return  result

    def __str__(self):
        return "Exception with id ="+self.error_id+"traceback="+self.type_error+" message="+self.message

