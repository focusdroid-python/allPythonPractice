from django.db import models

# Create your models here.
# 一类
class BookInfo(models.Model):
    '''图书模型类'''
    btitle = models.CharField(max_length=20)
    # 出版日期
    bpub_date = models.DateField()
    # 阅读量
    bread = models.IntegerField(default=0)
    # 评论量
    bcomment = models.IntegerField(default=0)
    # 删除标记
    isDelete = models.BooleanField(default=False)


# 多类
class HeroInfo(models.Model):
    '''英雄人物模型类'''
    # 英雄名
    hname = models.CharField(max_length=20)
    # 性别
    hgender = models.BooleanField(default=False)
    # 备注
    hcomment = models.CharField(max_length=200, null=True, blank=False)
    # 关系属性
    hbook = models.ForeignKey('BookInfo')
    # 删除标记
    isDelete = models.BooleanField(default=False)
'''
# 新闻类型类
class NewsType(models.Model):
    type_name = models.CharField(max_length=20)
    # 关系属性 代表类型下面的信息
    type_new = models.ManyToManyField('NewsInfo')

# 新闻类
class NewsInfo(models.Model):
    # 新闻标题
    title = models.CharField(max_length=128)
    # 发布时间
    pub_date = models.DateTimeField(auto_now_add=True)
    # 信息内容
    content = models.TextField()
    # 关系属性 代表信息所属的类型
    # news_type = models.ManyToManyField('NewType')
'''






















