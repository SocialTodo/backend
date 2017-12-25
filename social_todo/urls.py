from django.conf.urls import url
import social_todo.views

urlpatterns = [
    url('login', social_todo.views.log_in_user)
]