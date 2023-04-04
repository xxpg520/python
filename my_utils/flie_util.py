"""
文件相关的工具包
函数: print_file_info(file_name), 接收传入文件的路径, 打印文件的全部内容, 如文件不存在则捕获异常, 输出提示信息,通过finally关闭文件对象
"""
def print_file_imfo(file_name):
    """
    功能：将给定的文件内容输出到控制台
    :param file_name: 即将被读取的文件路径
    :return: None
    """
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
        content = f.read()
        print("文件的全部内容如下：")
        print(content)
    except Exception as e:
        print(f"程序出现异常了，原因是:{e}")
    finally:
        if f:   # 如果变量是None，表示False，如果有任何内容，就是True
            f.close()


"""
函数: append_to_file(file_name, data), 接收文件路径以及传入数据,将数据追加写入到文件中
"""
def append_to_file(file_name, data):
    """
    功能：将指定的数据追加到指定的文件中
    :param file_name: 接收文件的路径
    :param data: 接收传入的数据
    :return: None
    """
    f = open(file_name, "a", encoding="UTF-8")
    f.write(data)
    f.write("\n")
    f.close()


if __name__ == "__main__":
    append_to_file("d:/test_append.txt", "····不懂")