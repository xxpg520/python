# 函数: str_reverse(s), 接受传入字符串, 将字符串反转返回
# 函数: sub_str(s, x, y), 按照下标x和y,对字符串进行切片

def str_reverse():
    str1 = str(input("请输入任意字符串:"))
    str2 = str1[::-1]
    return str2