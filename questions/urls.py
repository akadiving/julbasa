from django.urls import path
from .views import QuestionList, RetrieveQuestion

app_name = "Questions"

urlpatterns = [
    path('', QuestionList.as_view(), name="question-list"),
    path('<str:pk>/', RetrieveQuestion.as_view(), name="question-id")
]
