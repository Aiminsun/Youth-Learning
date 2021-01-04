import requests
import re
import time
from lxml import html
import os
from qing import sqlinfo
from qing.models import *

etree = html.etree

url = 'http://news.cyol.com/node_67071.htm'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0'}



def url_html():
    try:
        # 先获取最新的一期
        # url = 'http://news.cyol.com/node_67071.htm'
        requ = requests.get(url, headers=headers)
        requ.encoding = "utf-8"
        html = etree.HTML(requ.text)

        data_url = html.xpath(
            '/html/body/div[@class="mianbody"]/dl[@class="listMM"]/dd[@class="picB"]/ul[@class="movie-list"]/li[1]/a/@href'
        )[0]  # 最新页面url 获取

        # 进入最新一期 获取标题 用于生成页面 标题
        requ_bt = requests.get(data_url, headers=headers)
        requ_bt.encoding = "utf-8"
        html_bt = etree.HTML(requ_bt.text)

        data_bt = html_bt.xpath('/html/head/title/text()')[0]  # 标题获取

        data_img = data_url.replace('index.html', 'images/end.jpg')  # 拼写图片

        answer = requests.get(data_url, headers=headers)  # 获取响应状态

        # print(answer.status_code)
        if answer.status_code == 200:  # 判断图片是否可以访问
            # data_url_bt 截图  data_img 标题  data_url 用于判断
            save(data_bt, data_img, data_url)
            return data_url

        else:
            user = Mistakes(mistakes='错误！请求截图响应不成功！ ')  # 保存错误，写日志
            user.save()

    except Exception as e:

        user = Mistakes(mistakes='%s' % e)  # 保存错误，写日志
        user.save()


def save(data_bt, data_img, data_url):
    # print(data_bt,data_img)
    imgsavepath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    # print(imgsavepath)
    img_save = requests.get(data_img, headers=headers)

    img_name = '\static\image\src\%s.jpg' % int(time.time())

    savepath = imgsavepath + img_name

    with open(savepath, "wb")as f:
        f.write(img_save.content)
        print('保存成功')

    # save(img_name, data_bt, data_url)
    sqlinfo.save_data(img_name, data_bt, data_url)
    # # with open('images/end.jpg','wb') as f:
    # #     img = requests.get(img_url)
    # #     f.write(img.content)
    # #     f.close()


def detection():
    dats_url = Data.objects.get(id=1).data_url

    requ = requests.get(url, headers=headers)
    requ.encoding = "utf-8"
    html = etree.HTML(requ.text)
    data_url = html.xpath(
        '/html/body/div[@class="mianbody"]/dl[@class="listMM"]/dd[@class="picB"]/ul[@class="movie-list"]/li[1]/a/@href'
    )[0]  # 最新页面url 获取

    if dats_url == data_url:

        return "It's the latest edition"

    else:
        url_html()
        return "updating......"







# if __name__ == '__main__':
#      # print(os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+'\static\image\src')
#      # url_html()
