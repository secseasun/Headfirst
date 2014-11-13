"""一个函数来规范文本，统一主程序进来的文本，规范为：继承list的类的集合
    最终数据类型为字典{名字：运动员类}
    主程序只需要调用函数，输出结果"""
import glob
import pickle

class Athlete(list):                            #运动员类，继承自list
    def __init__(self,name,brith,times=[]):
        list.__init__([])
        self.name=name
        self.brith=brith
        self.extend(times)
    def top3(self):
        return(sorted(set([sanitize(each_one) for each_one in self]))[0:3])


def sanitize(time_string):
    if ":" in time_string:
        splitter=":"
    elif "-" in time_string:
        splitter="-"
    else:
        return(time_string)
    return(time_string.split(splitter,1)[0]+"."+time_string.split(splitter,1)[1])


def get_sanitize_data(filepath):          #返还数据，名字，生日，list
    try:
        with open(filepath) as opened_file:
            data_read=opened_file.readline()
        data_split=data_read.strip().split(",")
        return(Athlete(data_split.pop(0),data_split.pop(0),data_split))   #最后为data_read
    except IOError as ioerr:
        print("file error: "+str(ioerr))
        return(None)


all_files=glob.glob("*.txt")    #获得所有文件

all_athlete_data={}

for each_file in all_files:    #从每个文件中获得名字：成绩的字典
    data=get_sanitize_data(each_file)
    all_athlete_data[data.name]=data
with open("all_athlete_data.pickle","wb") as data_to_write:
    pickle.dump(all_athlete_data,data_to_write)
with open("all_athlete_data.pickle","rb") as data_read:
    print(pickle.load(data_read))
