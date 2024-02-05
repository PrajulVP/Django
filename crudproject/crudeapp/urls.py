from django.urls import path
from .import views

urlpatterns=[
    path('', views.values, name='user'),
    path('view/', views.view, name='view'),
    path('detailview/<str:pk>', views.detailview, name='detailview'),
    path('update/<str:pk>', views.update, name='update'),
    path('delte/<str:pk>', views.delete, name='delete'),
    path('login/', views.login, name='login'),
    path('userlog/',views.userlog, name='userlog'),
    path('welcome'  , views.welcome, name='welcome'),
    path('logout/', views.logoutuser, name="logout"),
    path('adminlog/', views.adminlog, name="adminlog"),
    path('alog/', views.alog, name="alog"),
]