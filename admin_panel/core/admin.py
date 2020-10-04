from django.contrib import admin

from .models import *


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	list_display_links = list_display
	search_fields = ('name', 'text')


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	list_display_links = list_display
	search_fields = ('name', )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	list_display = ('id', 'text')
	list_display_links = list_display
	search_fields = ('text', )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'description')
	list_display_links = list_display
	search_fields = ('name', 'description')
