from django import forms
from .models import Quizz


class QuizzForm(forms.ModelForm):
    class Meta:
        model = Quizz
        fields = 'questions'
