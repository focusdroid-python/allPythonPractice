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



-- 查询
    -- 创建一个表
    create table students(
        id int unsigned primary key not null auto_increment,
        name varchar(20) default '',
        age tinyint unsigned default 0,
        height decimal(5,2),
        gender enum('男','女','保密') default '保密',
        cls_id int unsigned default 0,
        id_delete bit default 0
    );

    insert into students values
    (0, '王旭',18, 180.00,1, 1,0),
    (0, '彭于晏',30, 181.00,1, 1,0),
    (0, '小露露',23, 156.00,2, 1,0),
    (0, '刘德华',56, 180.00,2, 0,0),
    (0, '周杰伦',42, 180.00,2, 1,0),
    (0, '陈坤',39, 177.00,2, 0,0),
    (0, '刘亦菲',38, 155.00,1, 1,0),
    (0, '陈小云',31, 161.00,1, 1,0),
    (0, '奶茶',45, 166.00,1, 0,0),
    (0, '吴小小',18, 155.00,1, 0,0);

    --查询所有字段
    -- select * from 表名字

    -- 查询指定字段
    --select 列1，列2  from 表名

    -- 使用as给字段起别名
    --select 字段 as 名字 from 表名


    -- 消除重复行
    --distinct 字段
    select distinct gender from students;


--条件查询
    --比较运算符
    --select ... from 表名 where ...
    -- <   >   <=   >=   =  !=或者<>

    -- 逻辑运算符
    -- select * from studnet where age>30 and gender='女'
    -- and  or  not

-- 模糊查询
    --like %代表一个或多个[效率较低]     rlike正则
    select name from students where name='王';
    select name from students where name like '王%';

    -- 查询有2个字的名字
    select name from students where name like '__';

    -- 查询有3个字的名字
    select name from students where name like '___';

    -- 查询有2-3个字的名字
    select name from students where name like '__%';



    ----rlike
    select * from students where name rlike '^王.*';

    select * from students where name rlike '^王.*小$';

---- 范围查询
    -- in   not in     between ... and ...       not between ... and ...

    select * from students where age in (12,30,30);

    select * from students where age between 18 and 40;
    select * from students where age not between 18 and 40;

    -- is null      is not null

    select * from students where is_delete is null;

--- 排序
    ----order by asc[下面两种一样]
    select * from students where (age between 18 and 35) and gender=1 order by age;
    select * from students where (age between 18 and 35) and gender=1 order by age asc;

    ----desc
    select * from students where (age between 18 and 30) and gender=2 order by height desc;

    select * from students where (age between 18 and 30) and gender=2 order by height desc,age asc,id desc;


--- 聚合函数
    -- count
    select * from students where gender=1;
    select count(*) from students where gender=1;
    select count(*) as 男性总数 from students where gender=1;

    -- max

    --min

    --sum 总数

    --avg 平均数

    --round
    select round(sum(age)/count(*),8) from students;


    --- 这种情况必须配合分组，
    select name,round(sum(age)/count(*),8) from students;
--- 分组
    --group by

    --失败的，必须按照类别进行分组依据
    select * from students group by gender;

    -- 必须含有分组依据
    select gender, count(*) from students group by gender;
    select gender, avg(age) from students group by gender;

    --计算男性的人数
    -- where gender=1 group by 类别
    select gender, count(*) from students where gender=1 group by gender;

    -- 查看同种性别的别名
    -- group_concat(name, age, height)
    select gender, group_concat(name, age, height) from students where gender=1 group by gender;

    -- having
    -- 对分组进行条件判断，where对结果进行判断

    select gender, group_concat(name, gender, age) from students group by gender having avg(age) > 30;



    --查询每种性别中人数多于2的信息
    select gender, group_concat(name,'',gender) from students group by gender having count(*) > 2;


------limit 在最后边
    -- limit(第n页-1)*每个页个数, 每夜个数
    select * from students limit 0,5;   -- 1-5
    select * from students limit 1,5;   -- 2-6

    --
    select * from students where gender=2 order by height desc limit 0,2;























