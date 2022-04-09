from django.urls import re_path,path
from . import views


urlpatterns = [
    path('', views.index),
    path('item/<int:id>/',views.itemDetail),
    re_path(r'register/$',views.register),
    re_path(r'verify/$',views.verification),
    re_path(r'qrcreate/$',views.qrcreate),
    re_path(r'blog/$',views.blog),
    re_path(r'about/$',views.about),
    re_path(r'signin/$',views.signin),
    re_path(r'signup/$',views.signup),
    re_path(r'logout/$',views.signout)
]