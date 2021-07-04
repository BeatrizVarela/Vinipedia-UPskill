from django.urls import path

from quizz.views import quizz_view

app_name = 'quizz'

urlpatterns = [
    path('', quizz_view, name='quizz'),
]
