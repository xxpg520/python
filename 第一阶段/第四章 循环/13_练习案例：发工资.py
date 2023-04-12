import random
money = 10000
for i in range(1, 21):
    num = random.randint(1, 10)
    if money < 1000:
        print("工资发完了，下个月领取吧")
        break
    elif num <= 5:
        print(f"员工{i}号，绩效分{i},低于5，不发工资，下一位，")
        continue
    else:
        money -= 1000
        print(f"员工{i}号,发放工资1000元，账户余额{money}")
