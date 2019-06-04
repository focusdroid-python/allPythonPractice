## mysql

### mysql数据类型,约束
    > 整数    int  bit
    > 小数    decimal
    > 字符串  varchar  char
    > 日期类型 date, time, datetime
    > 枚举类型 enum
    ```
        decimal表示浮点数，如decimal（5，2）共存5位数，小数占两位
        char 表示固定长度的字符串，如char（3）
        varchar 表示可变长度的字符串
        字符串text表示存储大文本，当字符超过4000时推荐使用
        
        TINYINT  1  -128 ～ 127         0 ～ 255
        SMALLINT 2   -32768 ～ 32767     1 ～ 65535
        MEDIUMINT 3  -8388608 ～ 8388607 0 ～ 16777215
        INT       4  -2147483648 ～ 2147483647 0 ～ 4294967295
        
        DATE  4   ‘2020-01-01’
        TIME  3    ‘12：59：59’
        DATETIME 8  ‘2020-12-12 12：59：59’
        YEAR  1   ‘2020’
        TIMESTAMP  4  ‘1970-01-01 00：00：01’ UTC ～ ‘2038-01-01 00：00：01’UTC
    ```
    > 
### mysql约束 
    >
   
      主键  primary key 物理上的存储顺序
      非空  not null  此子段不能为空
      唯一  unipue  此字段不允许重复
      默认  default  当不填写时为默认值
      外键  foreign key  对关系进行约束，当为关系字段填写时，会到关联表中查询此值是否存在，若不存在就抛出异常
    >
      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     