from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.template import context
from .models import *
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


class QuestionListView(ListView):
    model = Question
    template_name = 'qa/home.html'
    context_object_name = 'questions'
    ordering = ['-timestamp']
    paginate_by = 5


class UserQuestionListView(ListView):
    model = Question
    template_name = 'qa/user_question.html'
    context_object_name = 'questions'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Question.objects.filter(user=user).order_by('-timestamp')


class QuestionDetailView(DetailView):
    model = Question

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        q = get_object_or_404(Question, pk=self.kwargs.get('pk'))
        context['answers'] = Answer.objects.filter(
            question=q).order_by('-timestamp')
        total_likes = q.total_likes()
        liked = False
        if q.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['total_likes'] = total_likes
        context['liked'] = liked
        total_dislikes = q.total_dislikes()
        disliked = False
        if q.dislikes.filter(id=self.request.user.id).exists():
            disliked = True
        context['total_dislikes'] = total_dislikes
        context['disliked'] = disliked
        return context


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['question', 'description' ,'question_image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Question
    fields = ['question', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.user:
            return True
        return False


class QuestionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Question
    success_url = "/"

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.user:
            return True
        return False


class AnswerCreateView(LoginRequiredMixin, CreateView):
    model = Answer
    fields = ['answer']
    template_name = 'qa/answer_question.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.question = get_object_or_404(
            Question, pk=self.kwargs.get('pk'))
        return super().form_valid(form)


@login_required
def LikeView(request, pk):
    q = get_object_or_404(Question, pk=pk)
    liked = False
    if q.likes.filter(id=request.user.id).exists():
        q.likes.remove(request.user)
        liked = False
    else:
        q.likes.add(request.user)
        q.dislikes.remove(request.user)
        liked = True
    return redirect(reverse('qa:question-detail', kwargs={'pk': pk}))


@login_required
def DislikeView(request, pk):
    q = get_object_or_404(Question, pk=pk)
    disliked = False
    if q.dislikes.filter(id=request.user.id).exists():
        q.dislikes.remove(request.user)
        disliked = False
    else:
        q.dislikes.add(request.user)
        q.likes.remove(request.user)
        disliked = True
    return redirect(reverse('qa:question-detail', kwargs={'pk': pk}))
