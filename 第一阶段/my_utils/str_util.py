
def str_reverse(s):
    """
    接收变量，将字符串反转返回
    :param s: 即将接收字符串的变量
    :return:  将字符串顺序反转后返回
    """
    return s[::-1]

def substr(s, x, y):
    """
    功能：按照下标x和y，对字符串进行切片
    :param s: 即将收到的字符串
    :param x: 起始切片下标
    :param y: 切片结束下标
    :return: 返回切盼后结果
    """
    return s[x:y:1]


if __name__ == "__main__":
    print(str_reverse("黑马程序员"))
    print(substr("今天天气好好哦", 2, 5))
