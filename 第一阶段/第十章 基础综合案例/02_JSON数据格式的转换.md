# 什么是json
* JSON是一种轻量级的数据交互格式，可以按照JSON指定的格式去阻止和封装数据
* JSON本质上是一个带有特定格式的字符串
## 主要功能：
json就是一种在各个编程语言中流通的数据格式，负责不同变成语言中的数据传递和交互，类似于：<br>
* 国际通用语言——英语<br>
* 中国56个民族不同地区的通用语言——普通话

## Python转换json
### 列子1 —— 将 列表 转换成 json
```
import json  # 导入模块
# 准备列表，列表内每一个元素都是字典，将其转换为JSON
data = [{"name": "张大山", "age": "11"}, {"name": "王大锤", "age": "13"}, {"name": "赵小虎", "age": "16"}]
json_str = json.dumps(data, ensure_ascii=False)  # 如果转换的内容有中文，需要ensure_ascii=False
print(type(json_str))
print(json_str)
```
输出结果：
```commandline
<class 'str'>
[{"name": "张大山", "age": "11"}, {"name": "王大锤", "age": "13"}, {"name": "赵小虎", "age": "16"}]
```
### 列子2 —— 将 字典 转换json
```commandline
import json  # 导入模块
# 准备字典，将字典转换为JSON
d ={"name": "周杰伦", "addr": "台北"}
json_str = json.dumps(d, ensure_ascii=False)
print(type(json_str))
print(json_str)
```
输出结果：
```commandline
<class 'str'>
{"name": "周杰伦", "addr": "台北"}
```
## json转换Python
### 列子1 —— 将json字符串 转换 列表
```commandline
# 将JSON字符串转换为Python数据类型[{k: v, k: v}, {k: v,k: v}]
s = '[{"name": "张大山", "age": "11"}, {"name": "王大锤", "age": "13"}, {"name": "赵小虎", "age": "16"}]'
l = json.loads(s)
print(type(l))
print(l)
```
输出结果：
```commandline
<class 'list'>
[{'name': '张大山', 'age': '11'}, {'name': '王大锤', 'age': '13'}, {'name': '赵小虎', 'age': '16'}]
```
### 列子1 —— 将json字符串 转换 字典
```commandline
# 将JSON字符串转换为Python数据类型{k: v, k: v}
s = '{"name": "周杰伦", "addr": "台北"}'
l = json.loads(s)
print(type(l))
print(l)
```
输出结果：
```commandline
<class 'dict'>
{'name': '周杰伦', 'addr': '台北'}
```