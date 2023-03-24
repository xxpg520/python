"""
练习案例：求1-100的和
需求：通过while循环，计算从1累加到100的和

"""
num = 0
sum = 1
while num <= 100:
    sum += num
    num += 1
print(sum)