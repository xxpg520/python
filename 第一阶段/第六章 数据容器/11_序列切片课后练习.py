"""
演示序列的切片的课后练习
"万过薪月,员序程马黑来,nohtyP学"
请使用学过的任何方式，得到“黑马程序员“
"""
my_str = "万过薪月,员序程马黑来,nohtyP学"

# 演示3中方法
# 倒序字符串，切片取出
result1 = my_str[::-1][9:14]
print(f"方式一，结果：{result1}")

# 切片取出，然后倒序
result2 = my_str[5:10][::-1]
print(f"方式一，结果：{result2}")

# split分隔"," replace替换"来"为空，倒序字符串
result3 = my_str.split(",")[1].replace("来", "")[::-1]
# split分隔后，得到一个列表：['万过薪月', '员序程马黑来', 'nohtyP学']
# 通过下表索引取出：员序程马黑来
# 通过.replace("来", "")去掉来结果： 员序程马黑
# 通过切片[::-1]得到 黑马程序员
print(f"方式一，结果：{result3}")
