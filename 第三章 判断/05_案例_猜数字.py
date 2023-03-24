"""
案例需求：
        定义一个数字（1~10，随机产生），通过3次判断来猜出数字

案例要求：
        1、数字随机产生，范围1~10
        2、有3次机会猜测数字，通过三层嵌套判断实现
        3、每次猜不中，会提示大了或小了
"""
import random
num = random.randint(1, 10)
print(num)
guess_num = int(input("猜猜我想的数字："))
if guess_num == num:
    print("你真厉害，第一次就猜中了")
else:
    print("猜错了")
    if guess_num > num:
        print("你猜的数字大了")
    else:
        print("你猜的数字小了")
    guess_num = int(input("猜猜我想的数字："))
    if guess_num == num:
        print("恭喜你，猜中了")
    else:
        print("猜错了")
        if guess_num > num:
            print("你猜的数字大了")
        else:
            print("你猜的数字小了")
        guess_num = int(input("猜猜我想的数字："))
        if guess_num == num:
            print("恭喜你，总算猜中")
        else:
            print("猜错了，没有机会了")
