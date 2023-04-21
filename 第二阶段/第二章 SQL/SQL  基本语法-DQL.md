# SQL 基本语法
## 数据查询：DQL (Data Query Language)
**例子——查询整个表中数据:**
```commandline
select * from student;
```
![img_11.png](img_11.png)

**查询 指定列**
```commandline
select id, name from student;
```
![img_12.png](img_12.png)

**查询 列age 大于 20的数据**
```commandline
select * from student where age > 20;
```
![img_13.png](img_13.png)

**查询 列gender 等于 男的数据**
```commandline
select * from student where gender = '男';
```
![img_14.png](img_14.png)