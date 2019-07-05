from django.contrib import admin

# Register your models here.

from .models import Question, Choice

# admin.site.register(Choice)
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
