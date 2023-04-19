## SQL 基本语法
### DDL——库管理
**显示数据库** `show databases;`<br>
**使用数据库** `use 数据库名称`<br>
**创建数据库** `create database 数据库名称 [charset UTF8];`<br>
**删除数据库** `drop database 数据库名称;`<br>
**查看当前使用数据库**`select database();`
### DDL——表管理
**查看有那些表** `show tables;` 注意:需要先选择数据库<br> 

**创建表** 
```
create table 表名称(
    列名称 列类型,
    列名称 列类型,
    ……
);
```
**——列类型有：**

|     列类型     |        代表        |
|:-----------:|:----------------:|
|     int     |        整数        |
|    float    |       浮点数        |
| varchar(长度) | 文本，长度为数字，做最大长度限制 | |
|    date     |       日期类型       |
|  timestamp  |      时间戳类型       |
  
**删除表**  `drop tables 表名称;`<br>


