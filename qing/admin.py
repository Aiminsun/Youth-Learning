from django.contrib import admin
from qing import models


class Data_list(admin.ModelAdmin):

    data_list = ['data_img', 'data_str']


admin.site.register(models.Data, Data_list)

admin.site.register(models.Defore_data)

admin.site.register(models.Mistakes)


