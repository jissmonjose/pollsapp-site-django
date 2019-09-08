from django.db import models


# Create your models here.
class Questions(models.Model):
    # Each model has a number of class variables, each of which
    # represents a database field in the model.
    # here CharField and DateTimeField r thr type of that field.
    # each model will have an id created automatically.
    # and it is auto incremented.
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # Choice model has a foreign key which is related to primary key of
    # Question model.
    # this tell that each choice is related to a question.
    # on_delete = models.CASCADE means, if a question is deleted
    # then its choice also deleted.
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# here v specified the models to be created, next to create this . Edit the mysite/settings.py file and add that
# dotted path to the INSTALLED_APPS models for our app, first need to include our app in
# the project, To include the app in our project, we need to add a reference to its configuration class in the
# INSTALLED_APPS setting. The PollsConfig class is in the pollsapp/apps.py file, so its dotted path is
# 'pollsapp.apps.PollsConfig. . Edit the mysite/settings.py file and add that dotted path to the INSTALLED_APPS.
