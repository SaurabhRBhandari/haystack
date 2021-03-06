from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    description = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name='likes', default=None, blank=True)
    dislikes = models.ManyToManyField(
        User, related_name='dislikes', default=None, blank=True)
    question_image = models.ImageField(
        null=True, blank=True, upload_to='question_pics')

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse("qa:question-detail", kwargs={"pk": self.pk})

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    answer_likes = models.ManyToManyField(
        User, related_name='answer_likes', default=None, blank=True)
    answer_dislikes = models.ManyToManyField(
        User, related_name='answer_dislikes', default=None, blank=True)
    def __str__(self):
        return f' {self.question} : {self.answer} '

    def get_absolute_url(self):
        return reverse("qa:question-detail", kwargs={"pk": self.question.pk})
    
    def total_likes(self):
            return self.answer_likes.count()

    def total_dislikes(self):
        return self.answer_dislikes.count()
