# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-11-27 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dating_gender', models.CharField(choices=[('male', '男性'), ('female', '女性')], default='male', max_length=6, verbose_name='匹配的性别')),
                ('dating_location', models.CharField(choices=[('上海', '上海'), ('北京', '北京'), ('福州', '福州'), ('广州', '广州'), ('宁德', '宁德'), ('深圳', '深圳'), ('厦门', '厦门'), ('武汉', '武汉')], default='上海', max_length=15, verbose_name='目标的城市')),
                ('min_distance', models.IntegerField(default=1, verbose_name='最小查找范围')),
                ('max_distance', models.IntegerField(default=10, verbose_name='最大查找范围')),
                ('min_dating_age', models.IntegerField(default=18, verbose_name='最小交友年龄')),
                ('max_dating_age', models.IntegerField(default=50, verbose_name='最大交友年龄')),
                ('vibration', models.BooleanField(default=True, verbose_name='是否开启震动')),
                ('only_matche', models.BooleanField(default=True, verbose_name='不让未匹配的人看我的相册')),
                ('auto_play', models.BooleanField(default=True, verbose_name='自动播放视频')),
            ],
            options={
                'db_table': 'profile',
            },
        ),
    ]
