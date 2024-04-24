"""
本函数用来将first name 和 last name 组合，并对首字母进行大写合成完整姓名
"""
def function_name(first_name , last_name):
    first = first_name.title()
    last = last_name.title()
    name = f'{first}{last}'
    return print(name)