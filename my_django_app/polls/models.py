from django.db import models
from django.utils import timezone

class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

  @classmethod
  def create(self, question_text='', pub_date=timezone.now()):
    return self(question_text=question_text, pub_date=pub_date)

  def __str__(self):
    return f"{self.question_text} -> {self.pub_date}"

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
  def __str__(self):
    return f"{self.choice_text}"

class Layout(models.Model):
  template_name = models.CharField(max_length=200)

  def __str__(self):
    return self.template_name