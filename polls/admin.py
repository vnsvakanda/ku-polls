"""This is the admin file for admin and creating the question and choice."""

from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    """This is class to define the number of line that must included."""

    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    """This is class for admin to managing the question."""

    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date', 'end_date'], 'classes': ['collapse']}),
    ]

    list_display = ('question_text', 'pub_date', 'end_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
