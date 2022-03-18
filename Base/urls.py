from django.urls import re_path,path
from . import views


urlpatterns = [
    path('', views.index),
    path('item/<int:id>/',views.itemDetail),
    re_path(r'register/$',views.register),
    re_path(r'verify/$',views.verification)
]