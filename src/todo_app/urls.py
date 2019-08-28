"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeTask_view, name='task_home'),
    path('task/new/', views.TaskCreate_view.as_view(), name='task_create'),
    path('task/<int:pk>/update/', views.TaskUpdate_view.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', views.TaskDelete_view.as_view(), name='task_delete'),
    path('TodaysTask/', views.TodayTask_view, name='task_today'),
    path('WeeksTask/', views.WeekTask_view, name='task_week'),
    path('MonthsTask/', views.MonthTask_view, name='task_month'),
    path('SpareTimeTask/', views.SpareTimeTask_view, name='task_SpareTime'),
    path('task/<int:task_id>/CrossoffTask', views.CrossoffTask_view, name='task_crossoff'),
    path('task/<int:task_id>/UncrossTask/', views.UncrossTask_view, name='task_uncross'),
]



