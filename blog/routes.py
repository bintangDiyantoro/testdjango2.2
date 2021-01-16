from django.urls import path
from .controllers import *


app_name = 'blog'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('detail/<str:slug>', Detail.as_view(), name='detail'),
    path('create', Create.as_view(), name='create'),
    path('edit/<str:slug>', Update.as_view(), name='edit'),
    path('delete/<str:slug>', Delete.as_view(), name='delete')
]
