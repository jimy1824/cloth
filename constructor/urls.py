from django.conf.urls import url
from django.urls import path, include
from constructor import views
urlpatterns = [
    path('', views.Home.as_view(), name='home'),

]