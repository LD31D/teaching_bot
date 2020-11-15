from django.db import models


class Lesson(models.Model):
	name = models.CharField(max_length=256)
	text = models.TextField()
	test = models.ForeignKey('Test', on_delete=models.SET_NULL, blank=True, null=True)
	task = models.ForeignKey('Task', on_delete=models.SET_NULL, blank=True, null=True)

	def __str__(self):
		return self.name


class Task(models.Model):
	name = models.CharField(max_length=256)
	description = models.TextField()

	def __str__(self):
		return self.name


class Test(models.Model):
	name = models.CharField(max_length=256)
	questions = models.ManyToManyField('Question', blank=True, default=None)

	def __str__(self):
		return self.name


class Question(models.Model):
	ANSWERS = (
			('a', 'A'),
			('b', 'B'),
			('c', 'C')
		)
	text = models.TextField()
	answer = models.CharField(max_length=1, choices=ANSWERS, default='a')

	def __str__(self):
		return self.text
