from django.contrib import admin

# Register your models here.
from quizz.models import Quizz, Question, Answer


admin.site.register(Quizz)

admin.site.register(Answer)


class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


admin.site.register(Question, QuestionAdmin)
