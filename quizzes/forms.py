
from django.forms import ModelForm
from .models import Quiz, Question, Answer

class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'
        labels = {
            'title' : 'Title',
            'description' : 'Description',
        }

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        labels = {
            'text' : 'Question text',
        }

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'
        labels = {
            'text' : 'Answer text',
            'is_correct' : 'Correct answer',
        }