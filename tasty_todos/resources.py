from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tasty_todos.models import Todo


class TodoResource(ModelResource):
    class Meta:
        queryset = Todo.objects.all()
        resource_name = 'todo'
        authorization = Authorization() # no authorization is done
        always_return_data = True # make POST requests return the created object