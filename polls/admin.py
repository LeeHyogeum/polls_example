from django.contrib import admin
from polls.models import Question, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [('Question Statement', {'fields' : ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'],'classes': ['collapse']})]

    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['questicon_text']

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)

# Register your models here.
