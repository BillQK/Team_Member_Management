from django.urls import path 
from . import views 


# URLConf
urlpatterns = [
    path('', views.index, name="list"),
    path('add', views.add, name='add_member'),
    path('edit/<str:pk>', views.edit, name='edit_member'),
    path('delete/<str:pk>', views.delete, name='delete_member')
    
]
