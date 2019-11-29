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

    #抛弃了外键的使用，那么如何来两个模型有关联，上下 两个模型，存在一对一的关系。
    #利用 对象.属性.  ---> 则使用 property装饰器来实现，将方法当做属性来使用，这样方法也有自己的属性
    # 这就 和存在外建的写法有点一样了。
    @property
    def profile(self):
        if not hasattr(self,'_profile'):
            #利用hasattr来判断存不存在，如果有，那么就不查询数据库，否则赋值给变量self._profile
            # 有效的减少数据库的访问
            self._profile, _ = Profile.objects.get_or_create(id=self.id)  # 条件为：模型profile的id=当前user中的id，同一用户
        return self._profile

    def to_dict(self):
        return {
            'phonenum':self.phonenum,
            'nickname':self.nickname,
            'gender':self.gender,
            'birthday':str(self.birthday),  # 注意时间需要强转 str
            'location':self.location,
            'avatar':self.avatar,
        }

class Profile(models.Model):
    """个人资料--> 则位 user表中的一些扩充资料"""
    dating_gender = models.CharField(max_length=6,choices=User.SEX,default='male',verbose_name='匹配的性别')
    dating_location = models.CharField(max_length=15,choices=User.LOCATION,default='上海',verbose_name='目标的城市')
    min_distance = models.IntegerField(default=1, verbose_name='最小查找范围')
    max_distance = models.IntegerField(default=10, verbose_name='最大查找范围')
    min_dating_age = models.IntegerField(default=18, verbose_name='最小交友年龄')
    max_dating_age = models.IntegerField(default=50, verbose_name='最大交友年龄')
    vibration = models.BooleanField(default=True, verbose_name='是否开启震动')
    only_matche = models.BooleanField(default=True, verbose_name='不让未匹配的人看我的相册')
    auto_play = models.BooleanField(default=True, verbose_name='自动播放视频')
    class Meta:
        db_table = 'profile'
    def to_dict(self):
        return {
            'id': self.id,
            'dating_gender': self.dating_gender,
            'dating_location': self.dating_location,
            'min_distance': self.min_distance,
            'max_distance': self.max_distance,
            'min_dating_age': self.min_dating_age,
            'max_dating_age': self.max_dating_age,
            'vibration': self.vibration,
            'only_matche': self.only_matche,
            'auto_play': self.auto_play,
        }
