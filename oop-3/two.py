class insuffientbalerror(Exception):
    def __init__(self,msg):
        self.msg=msg
raise insuffientbalerror("low balance")