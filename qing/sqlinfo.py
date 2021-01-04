# !Unix/Linux/Mac
# -*- coding: utf-8 -*-
# name：孙爱民（Ai-min sun）
# 数据库操作文件，在这里写相关的数据库增删改查

from qing.models import *


def alter_data(request):
    """
    读取青年大学习数据
    :return:
    """
    img = Data.objects.get(id=1).data_img,
    data_str = Data.objects.get(id=1).data_str

    return {
        'open_img': img[0],
        'open_str': data_str

    }


def save_data(dat_img, dat_str, dat_url):
    """
        更新最新一期数据

    """
    print(dat_img, dat_str, dat_url)
    save_img = Data.objects.get(id=1)
    save_img.data_img = dat_img
    save_img.data_str = dat_str
    save_img.data_url = dat_url
    save_img.save()
    print('更新完成')
