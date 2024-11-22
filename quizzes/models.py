from django.db.models import Model, CharField, TextField, DateTimeField, ForeignKey, CASCADE, BooleanField


class Quiz(Model):
    title = CharField(max_length=100)
    description = TextField()
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quiz: {self.title} - {self.description[:30]}"

    def __repr__(self):
        return f'Quiz(id={self.id}, title={self.title}, description={self.description[:20]}'

class Question(Model):
    quiz = ForeignKey(Quiz, on_delete=CASCADE, related_name='questions')
    text = TextField()

    def __str__(self):
        return f"Question: {self.quiz} - {self.text[:30]}"

    def __repr__(self):
        return f'Question: {self.quiz} - {self.text[:20]}'

class Answer(Model):
    question = ForeignKey(Question, on_delete=CASCADE, related_name='answers')
    text = TextField()
    is_correct = BooleanField(default=False)

    def __str__(self):
        return f"Answer: {self.question} - {self.text[:30]}"

    def __repr__(self):
        return f'Answer: {self.question} - {self.text[:20]} - {self.is_correct}'