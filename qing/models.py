from django.db import models

# Create your models here.


class Data(models.Model):  # 存储最新一期的 大学习标题及完成图片的路径
    id = models.IntegerField(primary_key=True)
    data_img = models.CharField(max_length=255, blank=True, null=True, verbose_name='图片路径')  # 图片路径
    data_str = models.CharField(max_length=255, blank=True, null=True, verbose_name='图片标题')  # 图片标题
    data_url = models.CharField(max_length=255, blank=True, null=True, verbose_name='原文链接')  # 原文链接 用于判断

    class Meta:
        managed = True
        db_table = 'Data'


class Defore_data(models.Model):  # 存储全部的青年大学习 封面 标题 及完成的图片路径
    id = models.IntegerField(primary_key=True)
    defore_time = models.CharField(max_length=255, blank=True, null=True, verbose_name='标题')  # 标题
    defore_fmimg = models.CharField (max_length=255, blank=True, null=True, verbose_name='封面')  # 封面
    defore_img = models.CharField(max_length=255, blank=True, null=True, verbose_name='完成的图片路径')  # 完成的图片路径
    defore_str = models.CharField(max_length=255, blank=True, null=True, verbose_name='标题')  # 标题

    class Meta:
        managed = True
        db_table = 'Defore_data'


class Mistakes(models.Model):  # 存储错误日志
    mistakes = models.CharField(max_length=255, blank=True, null=True, verbose_name='错误日志')

    class Meta:
        managed = True
        db_table = 'Mistakes'

