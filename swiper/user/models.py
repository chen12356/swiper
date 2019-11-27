from django.db import models

# Create your models here.

class User(models.Model):
    #设置类似枚举
    SEX = (
        ('male','男性'),
        ('female','女性')
    )
    LOCATION = (
        ('上海','上海'),
        ('北京','北京'),
        ('福州','福州'),
        ('广州','广州'),
        ('宁德','宁德'),
        ('深圳','深圳'),
        ('厦门','厦门'),
        ('武汉','武汉'),
    )
    phonenum = models.CharField(max_length=15,unique=True,verbose_name='手机号')
    nickname = models.CharField(max_length=20,default='匿名用户',verbose_name='昵称')
    gender = models.CharField(max_length=6,choices=SEX,default='male',verbose_name='性别')
    birthday = models.DateField(default='1990-01-01',verbose_name='生日')
    # choices --> 设置该属性：则该字段的值，只能在其中进行选取。
    location = models.CharField(max_length=15,choices=LOCATION,default='上海',verbose_name='现处城市')
    avatar = models.CharField(max_length=256,verbose_name='头像')
    class Meta:
        db_table = 'user'