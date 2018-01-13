from django.conf.urls import url
from facebook_users import views

urlpatterns = [
    url('facebook_auth', views.authenticate_facebook_token),
    #url('test', social_todo.views.i_am_a_teapot_test)
]
