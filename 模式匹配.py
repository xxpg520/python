"""
模式匹配
"""
# 当我们用if ... elif ... elif ... else ...判断时，会写很长一串代码，可读性较差。
score = "B"
if score == 'A':
    print('score is A.')
elif score == 'B':
    print('score is B.')
elif score == 'C':
    print('score is C.')
else:
    print('invalid score.')


# 使用match语句时，我们依次用case xxx匹配，并且可以在最后（且仅能在最后）
# 加一个case _表示“任意值”，代码较if ... elif ... else ...更易读。

match score:
    case 'A':
        print('score is A.')
    case 'B':
        print("score is B.")
    case 'C':
        print("score is C.")
    case _:  # _表示匹配道其他任何情况
        print('score is ???.')

"""
复杂匹配
"""
age = 15
match age:
    case x if x < 10:  # 表示当age<10时成立匹配，且赋值给变量x
        print(f'<10 years old:{x}')
    case 10:  # 仅匹配单个值
        print('10 years old.')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:  # 匹配多个值
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case _:
        print('not sure')

"""
匹配列表
"""
args = ['gcc', 'hello.c', 'world.c']
# args = ['clean']
# args = ['gcc']

match args:
    # 如果仅出现gcc,报错：
    case ['gcc']:
        print('gcc:missing source file(s).')

    # 出现gcc，且至少指定了一个文件：
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))

    # 仅出现clean:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command')
