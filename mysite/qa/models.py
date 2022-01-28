from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    description = models.TextField(null=True, blank=True)
    views = models.IntegerField(default=0)
    answers = models.IntegerField(default=0)
    answered = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name='likes', default=None, blank=True)

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse("qa:question-detail", kwargs={"pk": self.pk})

    def total_likes(self):
        return self.likes.count()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.TextField()
    votes = models.IntegerField(default=0)
    accepted = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return f' {self.question} : {self.answer} '

    def get_absolute_url(self):
        return reverse("qa:question-detail", kwargs={"pk": self.question.pk})
