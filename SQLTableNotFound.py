from captosexceptions import  CaptosExceptions
class SQLTableNotFoundException(CaptosExceptions):
    def __init__(self,error_id=1,type_error="Service error",message="SQL table not found",name_service=None,send_to_qeue=True):
        super
        self.id=error_id
        self.type_error=type_error
        self.message=message
