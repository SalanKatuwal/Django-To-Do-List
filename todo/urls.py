from django.urls import path,include
from . import views
urlpatterns =[
    path('',views.login),
    path('register',views.register),
    path('verifyregister',views.verifyregister),
    path('verifylogin',views.verifylogin),
    path('home',views.home),
    path('addtask',views.addtask),
    path('logout',views.logout),
    path('complete_task/<int:task_id>/',views.complete_task,name="complete_task"),
    path('delete_task/<int:task_id>/',views.delete_task,name = "delete_task"),
]