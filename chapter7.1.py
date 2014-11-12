"""一个函数来规范文本，统一主程序进来的文本，规范为：继承list的类的集合
    在读取过程中还需要规范list类中的文本，这又是另一个函数
    主程序只需要调用函数，输出结果"""

class Athete(list):
    def __init__(self,name,brith,times=[]):
        list.__init__=[]
        self.name=name
        self.brith=birth
    def top3():
        return("")

def sanitize(time_string):
    if ";" in time_string:
        splitter=";"
    elif "," in time_string:
        splitter=","
    else:
        return(time_string)
    return(time_string.split(splitter,1)[0]+"."
           +time_string.split(splitter,1)[1])
