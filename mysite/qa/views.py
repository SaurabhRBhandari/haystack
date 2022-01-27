from django.shortcuts import render
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
        context['answers'] = Answer.objects.filter(question=q).order_by('-timestamp')
        return context


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['question', 'description']

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
