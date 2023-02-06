#here you can edit the admin forms on the /admin page. 
#You can create, style and combine object forms  here.

from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display= ('pub_date', 'question_text', 'published_recently')
    list_filter=['pub_date']
    search_fields=['question_text']
    fieldset = [
        (None, {'fields':'pub_date'}), 
        ("Date information",{'fields':'question_text'})
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
