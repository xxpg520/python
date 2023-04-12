"""
演示list列表的循环，使用while和for循环2种方式
"""

def list_while_func():
    """
    使用while循环遍历列表的演示函数
    :return:None
    """
    my_list = ["传智教育", "黑马程序员", "Python"]
    # 循环控制遍历通过下标索引来控制，默认0
    # 每一次循环将下表索引变量+1
    # 循环条件：下表索引变量 < 列表的元素量
    index = 0  # 初始值为0
    while index < len(my_list):
        # 通过index变量取出对应下表的元素
        element = my_list[index]
        print(f"列表的元素：{element}")

        # 至关重要 将循环变量（index)每一次循环都+1
        index += 1
list_while_func()

def list_for_func():
    """
    使用for循环遍历列表的演示函数
    :return:None
    """
    my_list = [1, 2, 3, 4, 5]
    for element in my_list:
        print(f"列表的元素有：{element}")

list_for_func()