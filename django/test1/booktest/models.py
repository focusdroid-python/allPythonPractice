from django.db import models

# Create your models here.


# 图书类
class BookInfo(models.Model):
    '''图书模型类'''
    # django里面自动添加id
    # CharField 说明是一个字符串， max_length指定字符串的最大长度
    btitle = models.CharField(max_length=20)

    # 出版日期，DateField说明是一个日期类型
    bpub_date = models.DateField()

    def __str__(self):
        # 返回书名
        return self.btitle


# 英雄人物类
# 英雄名  hname
# 性别  hgender
# 年龄  hage
# 备注  hcomment
# 关系属性 book建立图书类和英雄人物类之间的一对多关系
class HeroInfo(models.Model):
    '''英雄人物模型类'''
    hname = models.CharField(max_length=20)
    # x性别 BookInfo说明是bool类型, default 指定默认值，False代表男
    hgender = models.BooleanField(default=False)

    # 备注
    hcomment = models.CharField(max_length=128)

    # 关系属性 hbook 建立图书类和英雄人物之间的一对多关系
    hbook = models.ForeignKey('BookInfo')

    def __str__(self):
        return self.hname