-- ### 数据库命令

    --链接数据库
    mysql -uroot -pmysql

    --退出数据库
    exit/quit/ctrl + d

    --查看当前多少数据库
    show databases;

    --显示当前数据库时间
    select now();

    --显示当前版本
    select version()

    -- 创建数据库
    -- create database 数据库名字
    create database python04;
    -- 指定编码格式[非常重要]
    create database python04new charset=utf8

    -- 查看创建数据库的语句
    show create database python04;

    -- 删除数据库
    -- drop database 数据库名字
    drop database python04;

    -- 查看当前使用的数据库
    select database();

    --使用数据库
    -- use 数据库名字
    use pythyon04new;

-- 数据库中表操作

    -- 查看数据库中的所有表
    show tables;

    -- 创建表
    -- auto_increment
    -- not null
    -- primary key
    -- default
    -- create table 数据表名字（字段 类型 约束 ）
    create table xxxx(id int, name varchar(30));
    create table yyyy(id int not null primary key auto_increment, name varchar(30));

    -- 创建students表
    create table students(
        id int unsigned not null primary key,
        name varchar(30),
        age tinyint unsigned,
        height decimal(5,2),
        gender enum('男','女','中性','保密') default '保密',
        cls_id int unsigned
    )
    -- 创建一个班级classes表
    create table classes(id int unsigned not null auto_increment primary key)

    -- desc 查看表结构
    desc xxxx

    --修改表-添加字段
    -- alter table 表名字 add 列名 类型
    alter table students add birthday datetime;

    --修改表-修改字段：不重命名版
    -- alter table 表名字 modify 列名 类型及约束
    alter table student modify birthday date;

    -- 修改表-修改字段：重命名版
    -- alter table 表名字 change 原名 新名 类型及约束
    alter table students change birthday birth date default '1980-01-01'


    --修改表-删除字段
    --alter table 表名字 drop 列名
    alter table students drop high;

    --修改表-删除字段(标记删除)

    --删除表
    --drop table 表名字

---- 增删改查
    -- 全列插入
    -- insert into 表名字 values();
    insert into students values();

    +--------+-------------------------------------+------+-----+---------+-------+
    | Field  | Type                                | Null | Key | Default | Extra |
    +--------+-------------------------------------+------+-----+---------+-------+
    | id     | int(10) unsigned                    | NO   | PRI | NULL    |       |
    | name   | varchar(30)                         | YES  |     | NULL    |       |
    | age    | tinyint(3) unsigned                 | YES  |     | NULL    |       |
    | height | decimal(5,2)                        | YES  |     | NULL    |       |
    | gender | enum('男','女','中性','保密')       | YES  |     | 保密    |       |
    | cls_id | int(10) unsigned                    | YES  |     | NULL    |       |
    | birth  | date                                | YES  |     | NULL    |       |
    +--------+-------------------------------------+------+-----+---------+-------+

    --部分插入
    --insert into 表名(列1，...) values(值1,...)
    insert into students (name, gender) values('王旭','五大')


    --多行插入
    insert into students (name, gender) values('王旭','五大'),('王旭2','五大2')

----修改
    --update 表名 set 列1=值1,列2=值2, where id=1；
    update student set gender=2 where id=1

---删除数据
    ---delete from 表名字 where 条件;
    delete from students where id=1;

    ---逻辑删除
    alter table students add is_delete bit default 0;



----查询基本使用
    --查询所有列
    --select * from 表名字
    select * from students;
    select * from students where name='focusdroid';
    select * from students where id > 5;


    select name,gender from students;


    select name as 姓名,gender as 性别 from students;




























