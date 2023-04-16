"""
和文件相关的类定义
"""
from data_define import Record
# 先定义一个抽象类用来做顶层设计，确定有哪些功能需要实现
class FileReader:

    def read_data(self) -> list[Record]:
        """读取文件的数据，督导的每一条数据都转换程Record对象，将它们都封装到list内返回即可"""
        pass

class TextFileReader(FileReader):
    def __init__(self, path):
        self.path = path            # 定义成员变量记录文件路径
    # 复写（实现抽象方法）父类的方法
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")
        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()
            data_list = line.split(",")
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)
        f.close()
        return record_list
class JsonFileReader(FileReader):


if __name__ == '__main__':
    text_file_reader = TextFileReader("D:/2011年1月销售数据.txt")
    text_file_reader.read_data()