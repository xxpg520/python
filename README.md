# python

#### 介绍
用来学习
# 字符串操作
***
### 下标索引操作
```commandline
my_str = "itheima and itcast" # 定义字符串
# 通过下表索引 取值
value = my_str[2]
value2 = my_str[-16]
print(f"从字符串{my_str}取下标为2的元素，值是：{value},取下标为-16的元素，值是{value2}")
```
输出结果:
```从字符串itheima and itcast取下标为2的元素，值是：h,取下标为-16的元素，值是h```
***
### `index()` 查找 方法
```
my_str = "itheima and itcast" # 定义字符串
value = my_str.index("and") # 查找and起始下标
print(f"在字符串{my_str}中查找and，其起始下标是：{value}")
```
输出结果:

`在字符串itheima and itcast中查找and，其起始下标是：8`
***
### `replace(原, 现)` 替换 方法
```
my_str = "itheima and itcast" # 定义字符串
new_my_str = my_str.replace("it", "程序") # 将字符串it换成程序
print(f"将字符串{my_str},进行replace替换后得到：{new_my_str}")
```
输出结果:

`将字符串itheima and itcast,进行replace替换后得到：程序heima and 程序cast`
***
### `split()` 分割方法
```
my_str = "hello python itheima itcast"
my_str_list = my_str.split(" ")  # 以" "为分割
print(f"将字符串{my_str}进行split切分后得到：{my_str_list},类型是：{type(my_str_list)}")
```
输出结果:

`将字符串hello python itheima itcast进行split切分后得到：['hello', 'python', 'itheima', 'itcast'],类型是：<class 'list'>`
***
### `strip()` 方法
#### 第一种 `strip(无参数)`
```commandline
my_str = "  itheima and itcast  "
new_my_str = my_str.strip()  # 不传入参数，去除首尾空格
print(f"字符串{my_str}被strip后，结果是：{new_my_str}")
```
输出结果:

`字符串  itheima and itcast  被strip后，结果是：itheima and itcast`

#### 第二种 `strip(参数)`
```commandline
my_str = "12itheima and itcast21"
new_my_str = my_str.strip("12") #指定删除带有1、2的元素
print(f"字符串{my_str}被strip('12')后，结果是：{new_my_str}")
```
输出结果:
`字符串12itheima and itcast21被strip('12')后，结果是：itheima and itcast`
***
### 统计字符串中某字符串的出现次数，`count()`
```commandline
my_str = "itheima and itcast"
count = my_str.count("it") # 统计it出现的次数
print(f"字符串{my_str}中it出现的次数是：{count}")
```
输出结果:

`字符串itheima and itcast中it出现的次数是：2`
***
### 统计字符串的长度，`len()`
```commandline
num = len(my_str)
print(f"字符串{my_str}的长度是：{num}")
```
输出结果:

`字符串itheima and itcast的长度是：18`