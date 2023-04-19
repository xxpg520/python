# SQL 访问和处理数据库的标准的计算机语言
## SQL语言的分类(基于功能划分为4类)

* 数据定义：DDL (Data definition Language)
  * 库的创建删除、表的创建删除等
* 数据操纵：DML (Data Manipulation language)
  * 新增数据、删除数据、修改数据等
* 数据口精致：DCL (Data control Language)
  * 新增用户、删除用户、密码修改、权限管理等
* 数据查询：DQL (Data Query Language)
  * 基于需求查询和计算数据
## SQL 语法特征
1. 大小写不敏感
2. 可以多行写入,但要以`;`来结束
3. 支持注释:
   * 单行注释: `-- 注释内容`
   * 单行注释: `# 注释内容`
   * 多行注释: `/* 注释内容 */`
## SQL 基本语法
### DDL——库管理
**显示数据库** `show databases;`<br>
**使用数据库** `use 数据库名称`<br>
**创建数据库** `create database 数据库名称 [charst UTF8];`<br>
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


