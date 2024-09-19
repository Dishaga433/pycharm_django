from tkinter.font import names

from django.urls import path

from todo_app import views

urlpatterns = [
    path('dash',views.dash,name="dash"),
    path('index',views.index,name="index"),
    path('read',views.read,name="read")
]

