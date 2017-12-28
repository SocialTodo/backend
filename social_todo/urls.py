from django.conf.urls import url
import social_todo.views

urlpatterns = [
    url('login', social_todo.views.log_in_user),
    url('test', social_todo.views.i_am_a_teapot_test)
]