# 将数字类型转换成字符串
num_str = str(11)
print((type(num_str)), num_str)

float_str = str(11.345)
print(type(float_str), float_str)
# 将字符串转换成数字
num = int("11")
print(type(num), num)

num2 = float("11.345")
print(type(num2), num2)

# 整数转换浮点数
float_num = float(11)
print(type(float_num),float_num)

# 浮点数转整数
int_num = int(11.345)
print(type(int_num),int_num)
# 只会转换小数点左边的整数，丢失小数点右边的内容