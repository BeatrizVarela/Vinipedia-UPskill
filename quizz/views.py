
from django.shortcuts import render
from .models import Quizz
# Create your views here.


def quizz_view(request):
    quizz = Quizz.objects.get(name="Wine-Knowledge")
    return render(request, 'quizz/quizz.html', {'quizz': quizz})