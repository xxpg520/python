"""
猜数字案例
要求：
    设置一个范围1-100的随机整数变量，通过while循环，配合yinput语句，判断输入的数字是否等于随机数
    无限次机会，直到猜中为止
    每一次猜不中，会提示大了或笑了
    猜完数字后，提示猜了几次
提示：
随机数可以使用：
import random
num = random.randint(1,100)
"""
import random
num = random.randint(1,100)
guess = int(input("请输入我心里想的数字："))
gasses = 1
while guess != num:
    gasses += 1
    if guess > num:
        print("猜的大了，再来")
    else:
        print("猜的小了，再来")
    guess = int(input("请输入我心里想的数字："))
print(f"恭喜你，猜对了,共猜了{gasses}次")


