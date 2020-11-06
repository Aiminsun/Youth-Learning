# 无聊的工具系列——青年大学习截图获取

**无聊的工具系列——青年大学习截图获取**

![](https://qn.kmvtc.cn/static/picture/logo.png)




一款青年大学习截图实时获取器，使用Python Django开发，响应式的前端样式，自动触发通过爬虫获取最新青年大学习截图生成，居家旅行形式主义必备！


## 不仅仅是形式

*在？青年大学习截图发一下？
![Pandao editor.md](https://qn.kmvtc.cn/static/image/602636cd7cd98d10a65de361363fb80e79ec90d6.jpg)


为了预防这种情况，花了两天时间写了这个截图获取小项目，是的 一个无聊的工具。

采用Django 开发 喜欢的话点个star*

> 实现原理，发现通过url拼接可获得完成学习页面的图片，通过爬虫爬取最新一期学习获取相关图片，通过仿真页，来‘蒙混过关’，通过感谢[小狼Syaoran](https://blog.csdn.net/ztyssb666/article/details/108639473)的一篇博客，给了灵感来源，特别感谢！

### 项目在线体验地址

#### [青年大学习截图生成](https://qn.kmvtc.cn/ "青年大学习截图生成")


项目截图


![电脑页](https://data.kmvtc.cn/forum/202010/31/dawd.png)

![截图页](https://data.kmvtc.cn/forum/202010/31/qrqwd.png)

![手机页](https://data.kmvtc.cn/forum/202010/31/dwdwda.png)





------------


# 项目运行项目运行
```python
# 1. 下载解压文件，运行以下命令，安装项目需要的库
pip freeze>requirements.txt 

# 2.迁移数据，生成表，请依次运行以下命令

python manage.py makemigrations

python manage.py migrate

# 3. 创建超级管理员 ，用于后台

python manage.py createsuperuser

# 4.导入项目内预数据，必须先导入，不然报错
python manage.py data.json

# 5.运行项目
python manage.py runserver

```

### 帮助

如有问题请发送邮箱 ：1404711457@qq.com

![](https://qn.kmvtc.cn/static/picture/logo.png)


