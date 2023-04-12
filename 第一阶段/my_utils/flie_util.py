def print_file_info(file_name):
    """
    功能：接收传入文件的路径, 打印文件的全部内容, 如文件不存在则捕获异常, 输出提示信息,通过finally关闭文件对象
    :param file_name: 文件路径
    :return: None
    """
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
        print(f.read())
    except:
        print("打开文件出错了")
    finally:
        if f:
            f.close()

def append_to_file(file_name, data):
    """
    功能：接收文件路径以及传入数据,将数据追加写入到文件中
    :param file_name: 接收文件路径
    :param data: 将要追加的数据
    :return: None
    """
    f = open(file_name, "a",encoding="UTF-8")
    f.write(data)
    f.close()
    return None

if __name__ == "__main__":
    # print_file_info("d:/bi1ll.txt")
    append_to_file("d:/bill.txt", "我叫最比较喜欢吃饭\n")