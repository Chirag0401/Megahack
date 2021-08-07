from django.urls import path
from .views import index, team, register, val
urlpatterns = [
    path('',index,name="index"),
    path('register/',register,name="register"),
     path('team/',team,name="team"),
     path('validate/',val,name="validate")
]
