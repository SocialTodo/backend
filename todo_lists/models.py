from django.db import models
from django.conf import settings

# Create your models here.

class TodoList(models.Model):
  #Defines the title to a todolist to be a maximum of 50 chars
  list_title = models.CharField(max_length=50)
  list_owner = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    related_name = 'lists',
    on_delete = models.CASCADE)
  creation_time = models.DateTimeField()
  update_time = models.DateTimeField()
  permitted_viewers = models.ManyToManyField(settings.AUTH_USER_MODEL)


  class Meta:
    ordering = ('list_owner','update_time')

  def __str__(self):
    return self.list_title

class TodoItem(models.Model):
  #Defines a todo item to be a maximum of 50 chars
  item_title = models.CharField(max_length=50)
  todo_list = models.ForeignKey(
    TodoList,
    related_name='list_items',
    on_delete=models.CASCADE)
  creation_time = models.DateTimeField()
  update_time = models.DateTimeField()

  class Meta(object):
    ordering = ('todo_list', 'update_time')

  def __str__(self):
    return self.item_title