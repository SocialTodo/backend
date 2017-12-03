from django.conf.urls import url
import social_todo.views

urlpatterns = [
    url(r'^.*', social_todo.views.i_am_a_teapot_test)
]