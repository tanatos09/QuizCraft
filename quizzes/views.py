from django.shortcuts import render, redirect, get_object_or_404

from quizzes.forms import QuizForm, QuestionForm, AnswerForm
from quizzes.models import Quiz, Question


def home(request):  # domovska stranka
    return render(request, "home.html")


def create_quiz(request):  # vytvari kvizy
    if request.method == "POST":
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quiz_list')
    else:
        form = QuizForm()
    return render(request, 'quizzes/create_quiz.html')


def quiz_list(request):  # generuje seznam kvizu
    quizzes = Quiz.objects.all()
    return render(request, 'quizzes/quiz_list.html', {'quizzes': quizzes})


def quiz_detail(request, quiz_id):  # zobrazuje detail kvizu
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    return render(request, 'quizzes/quiz_detail.html', {'quiz': quiz, 'questions': questions})


def add_question(request, quiz_id):  # pridava otazky ke kvizu
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.quiz = quiz
            question.save()
            return redirect('quiz_detail', quiz_id=quiz.id)
    else:
        form = QuestionForm(initial={'quiz_id': quiz.id})
    return render(request, 'quizzes/add_question.html', {'form': form, 'quiz': quiz})

def add_answer(request, question_id): #pridani odpovedi k otazce
    question = get_object_or_404(Question, id=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect('quiz_detail', quiz_id=question.id)
    else:
        form = AnswerForm(initial={'question': question})
    return render(request, 'quezzes/add_answer', {'form': form, 'question': question})


