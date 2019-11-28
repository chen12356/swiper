'''
Django中forms表单的使用
'''
from django import forms
from user.models import User
from user.models import Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nickname','gender','birthday','location']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    #由于在字段中存在距离的大小比较、与年龄的比较，单纯的验证表单不能满足需求
    #定义方法--> 进行清洗,函数命名规范：clean_字段名
    #清洗流程：is_valid() --> clean() --> clean_max_distance() -->super().clean()
    def clean_max_distance(self):
        """检查并且清晰max_distance字段"""
        cleaned_data = super().clean()
        #注意继承弗父类的clean(),跳过自身的clean(),否则会导致递归调用
        if cleaned_data['max_distance'] >= cleaned_data['min_distance']:
            return cleaned_data['max_distance']
        else:
            return forms.ValidationError('max_distance 不能小于 min_distance')
    def clean_max_dating_age(self):
        """检查并且清晰max_dating_age字段"""
        cleaned_data = super().clean()
        #注意继承弗父类的clean(),跳过自身的clean(),否则会导致递归调用
        if cleaned_data['max_dating_age'] >= cleaned_data['min_dating_age']:
            return cleaned_data['max_dating_age']
        else:
            return forms.ValidationError('max_dating_age 不能小于 min_dating_age')