from django.urls import path
from . import views
from .views import PostListView, PostCreateView

# http://127.0.0.1:8000 = index.html
# http://127.0.0.1:8000/index = index.html
# http://127.0.0.1:8000/questions = questions.html
# http://127.0.0.1:8000/questions/3 = question-details.html

urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index),
    path("questions", PostListView.as_view(), name="questions"),
    path("category/<slug:slug>", views.questions_by_category, name="questions_by_category"),
    path("questions/<slug:slug>", views.question_details, name="question_details"),
    path("questions_import", PostCreateView.as_view(), name="question_form"),
    path('export-questions', views.export_questions_to_xlsx, name='export_questions'),
    path("completetest", views.completetest, name="completetest"),
    path("search-questions", views.QuestionSearchView.as_view(), name="search_questions"),
    path('contact/', views.contact, name='contact'),
]
