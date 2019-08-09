__author__ = 'wanderknight'
__time__ = '2019/8/9 20:31'

from django.conf.urls import url

from ..views.oj import ClassgroupAPI

urlpatterns = [
    url(r"^classgroup/?$", ClassgroupAPI.as_view(), name="classgroup_api"),
]
