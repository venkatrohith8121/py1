# user defiened error 
class tetserror(Exception):
    def __init__(self,msg):
        self.msg=msg
def testcase():
    if False:
        print("gm")
    else:
        try:
            raise print("test error")
        except:
            
testcase()