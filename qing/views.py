from django.shortcuts import render
from qing.sqlinfo import *
from qing.requ import *
from django.http import JsonResponse

# Create your views here.


# 首页路由
def index(request):

    # a = alter_data()

    #
    # print(a)
    # print(data_bt,data_img)
    return render(request, 'index.html')


#  截图展示页面路由
def data(request):

    return render(request, 'data.html')


def voluntarily(request):
    txt = detection()
    return JsonResponse({
        'data': txt

    })


