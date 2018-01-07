from django.conf.urls import url
from todo_lists import views

urlpatterns = [
    url('*', views),
]