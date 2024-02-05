from django.db import models
from django.utils import timezone
from django.utils.version import datetime

"""
In python manage.py shell:
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from polls.models import Question, Choice

d = datetime.now(tz=ZoneInfo('Asia/Kolkata'))
q = Question(question_text="Question one", pub_date=d)
q.save()
q = Question(question_text="Question two", pub_date=d + timedelta(days=1))
q.save()
q.choice_set.create(choice_text='choice 1')
q.choice_set.create(choice_text='choice 2')
"""

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

