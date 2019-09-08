from django.urls import path
from . import views

app_name = 'pollsapp'

# create a route and calls the view function.
# and give a name for that route.
urlpatterns = [
    path('', views.index, name='index')
]
