from django.urls import path
from . import views
from .views import (
    QuestionListView,
    QuestionDetailView,
    QuestionCreateView,
    QuestionUpdateView,
    QuestionDeleteView
)

app_name = "qa"
urlpatterns = [
    path("", QuestionListView.as_view(), name="home"),
    path("question/<int:pk>/", QuestionDetailView.as_view(), name="question-detail"),
    path("question/new/", QuestionCreateView.as_view(), name="question-create"),
    path("question/<int:pk>/update",
         QuestionUpdateView.as_view(), name="question-update"),
    path("question/<int:pk>/delete",
         QuestionDeleteView.as_view(), name="question-delete"),

]
