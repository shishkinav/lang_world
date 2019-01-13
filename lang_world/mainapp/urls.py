from django.urls import re_path
import mainapp.views as mainapp


app_name = 'mainapp'

urlpatterns = [
    re_path(r'^$', mainapp.index, name='index'),

]