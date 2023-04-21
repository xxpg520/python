# SQL 基本语法
## 数据查询：DQL (Data Query Language)
**例子——查询整个表中数据:**
```commandline
select * from student;
```
![img_11.png](img_11.png)<br>
**查询 指定列**
```commandline
select id, name from student;
```
![img_12.png](img_12.png)<br>
**查询 列age 大于 20的数据**
```commandline
select * from student where age > 20;
```
![img_13.png](img_13.png)<br>
**查询 列gender 等于 男的数据**
```commandline
select * from student where gender = '男';
```
![img_14.png](img_14.png)<br>
## 分组聚合
**语法**
```
select 字段|聚合函数 from 表 [where 条件] group by 列;
```
例子：按照性别gender，统计男、女年龄平均值<br>
![img_15.png](img_15.png)
```commandline
select gender, avg(age) from student group by gender;
```
输出结果为：<br>
![img_16.png](img_16.png)<br>
也可以展示多个聚合
```commandline
select gender,sum(age),max(age),min(age),count(*), avg(age) from student group by gender;
```
输出结果：<br>
![img_17.png](img_17.png)<br>