# SQL 基本语法
## 数据操纵：DML (Data Manipulation language)
**插入数据——语法**
`insert into 表(列1,列2,列3……) values(值1,值2,值3)`
例:
```
insert into student(id) values(1),(2),(3);
```
---
![img.png](img.png)<br>

---
多列插入1:
`insert into student(id, name, age) values(4, '林俊节', 33),(5, '周杰轮', 31);`<br>
---
![img_1.png](img_1.png)

---
多列插入2:
`insert into student values(5, '张学油', 33),(6, '王力鸿', 31);`<br>
---
![img_2.png](img_2.png)

---