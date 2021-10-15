from django.contrib import admin
from .models import Question, Answer

# Register your models here.

class AnswerStackedInline(admin.StackedInline):
    model = Answer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerStackedInline]
    list_display = ("author", "body", "difficulty",)