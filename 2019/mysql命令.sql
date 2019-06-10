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



---- 链接查询
    --内链接[取交集]
    -- inner join ...on
    --select ... from 表A inner join 表B；
    select * from students inner join classes on cls_id;

    --使用students中的cls_id 对用classes表中的
    select * from students inner join classes on students.cls_id=classes.id;

    --按照要求现实姓名班级
    select student.*, classes.name from stutents as s inner join classes as c on s.cls_id=c.id;

    --按照班级排序 order by
    select student.*, classes.name from stutents as s inner join classes as c on s.cls_id=c.id order by c.name;


    ---- left join  [谁写在left join左边就以谁为基准,没有就为null]
    select * from students as s left join classes as c on s.cls_id=c.id;

    -- 查询没有班级的学生
    select * from students as s left join classes as c on s.cls_id=c.id where c.id is null;

---子关联
    --把一张表当成两张表，做关联
    select * from china as c inner join china as city on c.id=city.p_id having c.name='陕西省';


    select * from china where p_id=(select id from china where name='陕西省'); -- 子查询


---子查询
    --select里边嵌套select
    select * from students where height=(select max(height) from students);



	insert into goods values(0, 'r510vc 15.6英寸笔记本', '笔记本', '华硕', 3399, default, default);
	insert into goods values(0, 'y400n 14.0英寸笔记本', '笔记本, '联想', 4999, default, default);
	insert into goods values(0, 'g15th 15.6英寸笔记本, '游戏本', '雷神', 3399, default, default);
	insert into goods values(0, 'x550cc 15.6英寸笔记本', '笔记本', '华硕', 2799, default, default);
	insert into goods values(0, 'x240 超极本', '超极本', '华硕', 4880, default, default);
	insert into goods values(0, 'u330p 13.3英寸超极本', '超级本', '联想', 4299, default, default);
	insert into goods values(0, 'svp13226scb 触控笔记本', '超级本', '索尼', 7999, default, default);
	insert into goods values(0, 'ipad mini 7.9英寸平板电脑', '平板电脑', '苹果', 1998, default, default);
	insert into goods values(0, 'ipad air 9.7英寸平板电脑', '平板电脑', '苹果', 3388, default, default);
	insert into goods values(0, 'ipad air 9.7英寸平板电脑', '平板电脑', '苹果', 3388, default, default);
    insert into goods values(0, '华为P30', '服务器', '华为', 3200, 1,0);


    --查询每种里边最贵的信息
    -- left join 以左边为基准找符合左边信息的
    select * from (select cate_name, max(price) as max_price from goods group by cate_name) as g_new left join goods as g on g_new.cate_name=g.cate_name and g_new.max_price = g.price;

    -- 查询每种里边最贵的信息[只查看名字，描述，价格]
    select g_new.cate_name, g.name, g.price from (select cate_name, max(price) as max_price from goods group by cate_name) as g_new left join goods as g on g_new.cate_name=g.cate_name and g_new.max_price = g.price order by g_new.cate_name;

----拆表
    --1.先建一张新表
    create table if not exists goods_cates(
        id int unsigned primary key auto_increment,
        name varchar(40) not null
    )
    --2.把查到的cate_name放在新表里边
--     select cate_name from goods group by cate_name;
    -- 只把名字写到新表 [不用values]
    insert into goods_cates (name) select cate_name from goods group by cate_name;
    --关联两个表中的值
    update goods as g inner join goods_cates as c g.cate_name=c.name set g.cate_name=c.id
    -- 修改goods表中的cate_name为cate_id
    alter table goods change cate_name cate_id int unsigned not null;

    --关联外键
    -- //如果1452，就是关联的外键超出范围了
    alter table goods add foreign key (cate_id) references goods_cates(id);

    --取消外键
    alter table goods drop foreign key CONSTRAINT--【来自show create database goods】


    ---创建视图
    --
        create view 视图名称 as select 语句

        -- 查看视图
        show tables;
        -- 使用视图
        select * from v_goods_info;
        --删除视图
        -- select view 视图名称
        --创建视图
        create view v_goods_info as select g.* from goods as g left join goods_cates as g_c on g.cate_id=g_c.id left join goods_brands as g_b on g.brand_id=g_b.id;

        --视图的作用
        --0.提高了重用性，就像一个函数
        --1.对数据库重构，不影响程序运行
        --2.提高安全性能，可以对不同用户
        --3.让数据更加清晰

    ---事务
        --所谓是事务，就是一个操作序列，这些操作要么执行，要么不执行，他是一个不可分割的单位
        --事物的四大特性（ACID）
        --0.原子性
        --1.一致性
        --2.隔离性
        --3.持久性

        ---开启事务
        -- 1. start transaction
        -- 2. select balance from checking where customer_id=10332255
        -- 3. update checking set balance = balance - 200.00 where customer_id=1023553;
        -- 4. update saving set balance = balance + 200.00 where customer_id=1023553;
        -- 5. commit

        ---使用事务
        --1. use jing_dong (使用数据库)
        --2. show create table goods
        --3. begin / start transaction (开启事务)
        --4. 将增删改处理完成之后， commit 提交
        -- rollback (回滚事务，回到未commit之前在缓存中的数据)

        ---索引
        --查看索引
        -- show index from 表名
        --建张表，写入十万条数据
        --开启时间检测
        set profiling=1;
        -- 查找第一万台第一万条数据
        select * from test_index where title='ha-99999';
        --查看执行时间
        show profiles;

        --为表title_index的title列建立索引
--         create index 索引名称 on 表名(字段名称(长度));
        -- 如果字段是字符串，需要制定长度，建议长度与定义字段长度一致
        -- 字段类型如果不是字符串，可以不填写长度部分
        create index titlt_index on test_index(title(10));

        --执行查询语句
        select * from test_index where title='ha-99999';

        show profiles;

        --删除索引
        drop index


----权限管理
    --查看那所有用户
    select host,user from user;
    select host,user,authorization from user;

    -- 创建用户和授权
    -- grant 权限列表 on 数据库 to '用户名'@'访问主机' identified by '密码';
     --1。使用root登陆, 再输入密码
     mysql -uroot -p
     --2。添加权限
     grant select on jing_dong.* to 'laowang'@'localhost' identified by '123456';
     grant all privileges on jing_dong.* to 'laowang'@'localhost' identified by '123456';
     --3。 查看添加的权限
     select host,user,authorization from user;

     ---修改权限
     grant 新权限 on 数据库 to 账户@主机 with grant option;
     --刷新权限
     flush privileges;

     --修改密码
     use mysql;
     update user set authentication_string=password('密码') where user='用户名';
     flush privileges;

     ---创建一个服务器上所有库所有表的权限，
     grant peplication slave on *.* to 'slavr'@'%' identified by 'slave';
     flush privileges;

     --如果在本地使用连不上，
     --打开 vi /etc/mysql/mysql.conf.d/mysql.cnf
     --注释  bind-address    - 127.0.0.1
     -- sudo service mysql restart


     --删除账户
    --drop user '用户名'@'%' --%代表root权限
     drop user '用户'@'主机'

     --mysql主从服务器
     --将主服务器同步数据到其他服务器上
     --1. 数据备份
     mysqldump -uroot -p 数据库名 > python.sql


    --------恢复数据库
    --1。 连接数据库,创建新的数据库
    --2. 退出连接，执行如下命令
    mysql -uroot -p 新数据库名 < python.sql



    --4.1 在主服务器上执行命令
    mysqldump -uroot -p --all-databases 00lock-all-tables > ~/master_db.sql
    --输入密码


    ---4.2在从服务器上，执行命令
    mysql -root -pmysql < master_db.sql

    --4.3配置主服务器
    sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf
    ---找到83行,,取消注释
    --server-id     =2
    -- log_bing     = /var/log/mysql/mysql-bin.log

    ---4.4重启服务器
    sudo service mysql restart

    ---注意：从服务器上的server-id要和主服务器不一样就行
    --从服务器 service=1

    --4.5登入主服务器中的mysql创建从服务器同步数据使用的账号
    --mysql -uroot -p

    GRANT PEPLICATION SLAVE ON *.* TO 'slave'@'%' identified by 'slave';
    flush privileges;

    --4.6在从服务器上
    change master to master_host='主服务器ip', master_user='slave', master_password='slave',
    master_log_file='mysql-bin.000006', master_log_pos=590;
    --上面的master_log_file=show master status中的File的值        master_log_pos,,也是show master status中的position

    --4。7 从服务器show slave status
    -- show slave status \G;
    --slave_IO_Runing YES
    --Slave_SQL_Runing YES
    --表示同步成功














