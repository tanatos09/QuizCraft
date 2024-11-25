"""
URL configuration for QuizCraft project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from quizzes.views import quiz_list, create_quiz, quiz_detail, add_question, add_answer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', quiz_list, name='quiz_list'),
    path('quiz/create', create_quiz, name='create_quiz'),
    path('quiz/<int:quiz_id>/', quiz_detail, name='quiz_detail'),
    path('quiz/<int:quiz_id>/add', add_question, name='add_question'),
    path('questions/<int:quiz_id>/add_answer', add_answer, name='add_answer'),
]
