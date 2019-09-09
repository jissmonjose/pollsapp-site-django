from django.urls import path

from . import views

app_name = 'pollsapp'

# create a route and calls the view function.
# and give a name for that route.

# here v capture an integer parameter 'question_id' from url so v use angle brackets,
# and this 'question_id' value is passed as an argument  to the parameter
# 'question_id' in views.detail function.

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>', views.detail, name='detail'),
]
