from django.db import models


# Create your models here.
class Quizz(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_questions(self):
        return self.questions.all()  # Related name in Question Model

    class Meta:
        ordering = ("name",)


class Question(models.Model):
    quizz = models.ForeignKey(Quizz, null=True, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

    def get_answers(self):
        return self.answers.all()

    class Meta:
        ordering = ("text",)


class Answer(models.Model):
    text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE, related_name='answers')
    option = models.BooleanField(default=False)

    def __str__(self):
        return self.text
