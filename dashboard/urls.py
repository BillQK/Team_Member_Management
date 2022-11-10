from django.urls import path 
from . import views 


# URLConf
urlpatterns = [
    path('', views.index, name="list"),
    path('add', views.add),
    path('edit/<str:pk>', views.update, name='edit_member')
]
