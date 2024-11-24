from django.shortcuts import render, redirect, get_object_or_404

from quizzes.forms import QuizForm, QuestionForm
from quizzes.models import Quiz, Question


def home(request):
    return render(request, "home.html")

def create_quiz(request):
    if request.method == "POST":
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quiz_list')

    else: form = QuizForm()
    return render(request, 'quizzes/create_quiz.html')

def add_question(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.quiz = quiz
            question.save()
            return redirect('quiz_detail', quiz_id=quiz.id)
    else:
        form = QuestionForm(initial={'quiz_id': quiz.id})
    return render(request, 'quizzes/add_question.html', {'form': form})


