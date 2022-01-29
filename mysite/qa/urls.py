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
    LikeQuestionView,
    DislikeQuestionView,
    LikeAnswerView,
    DislikeAnswerView
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
    path("question/<int:pk>/answer",
         AnswerCreateView.as_view(), name="question-answer"),
    path('question/<int:pk>/like/', LikeQuestionView, name='like-question'),
    path('question/<int:pk>/dislike/', DislikeQuestionView, name='dislike-question'),
    path('question/<int:pk>/answer/<int:a_pk>/like/', LikeAnswerView, name='like-answer'),
    path('question/<int:pk>/answer/<int:a_pk>/dislike/', DislikeAnswerView, name='dislike-answer'),
]
