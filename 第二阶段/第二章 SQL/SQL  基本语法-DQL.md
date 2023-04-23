# SQL 基本语法
## 数据查询：DQL (Data Query Language)
**基本语法**
```commandline
select 字段列表|* from 表
```
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
**基本语法**
```
select 字段|聚合函数 from 表 [where 条件] group by 列;
```
例子：按照性别gender分组，统计男、女年龄平均值<br>
![img_15.png](img_15.png)
```commandline
select gender, avg(age) from student group by gender;
```
输出结果为：<br>
![img_16.png](img_16.png)<br>
也可以展示多个分组聚合
```commandline
select gender,sum(age),max(age),min(age),count(*), avg(age) from student group by gender;
```
输出结果：<br>
![img_17.png](img_17.png)<br>
## 排序
**基本语法**
```commandline
select 列|聚合函数|* from 表
where……
group by……
order by……[asc | desc]
```
例子 - 按照age从大到小排序 <br>
```commandline
select * from student where age > 20 order by age desc; 
```
![img_19.png](img_19.png)<br>
## 结果分页限制
**基本语法**
```commandline
select 列|聚合函数|* from 表
where……
group by……
order by……[asc | desc]
limit n[, m]
```
**例子**<br>
![img_23.png](img_23.png)<br>
限制输出5条数据
```commandline
select * from student limit 5;
```
![img_21.png](img_21.png)<br>
```commandline
select * from student limit 10,5; # 从11开始取5条输出
```
![img_22.png](img_22.png)<br>