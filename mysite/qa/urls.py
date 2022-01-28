from django.urls import path
from . import views
from .views import (
    QuestionListView,
    QuestionDetailView,
    QuestionCreateView,
    QuestionUpdateView,
    QuestionDeleteView,
    UserQuestionListView,
    AnswerCreateView,
    LikeView,
    DislikeView,
)

app_name = "qa"
urlpatterns = [
    path("", QuestionListView.as_view(), name="home"),
    path("user/<str:username>", UserQuestionListView.as_view(), name="user-question"),
    path("question/<int:pk>/", QuestionDetailView.as_view(), name="question-detail"),
    path("question/new/", QuestionCreateView.as_view(), name="question-create"),
    path("question/<int:pk>/update",
         QuestionUpdateView.as_view(), name="question-update"),
    path("question/<int:pk>/delete",
         QuestionDeleteView.as_view(), name="question-delete"),
    path("question/<int:pk>/answer", AnswerCreateView.as_view(), name="question-answer"),
    path('like/<int:pk>/', LikeView, name='like-question'),
    path('dislike/<int:pk>/', DislikeView, name='dislike-question'),
]
