from django.contrib import admin

# Register your models here.

from .models import Question, Choice

admin.site.register(Choice)


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)
