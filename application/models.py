from django.db import models
from django.forms import ModelForm
from django import forms

class Definition(models.Model):
	dexercise = models.CharField('Exercise', max_length=200) # name of the exercise
	bweight = models.FloatField('% Body Weight') # percentage of bodyweight used
	blength = models.FloatField('% Body Length') # percentage of body height used
	wlength = models.FloatField('% Body, Weight Travels', null=True) # percentage of body height the weight used in the exercise travels

	def __unicode__(self):
		return self.dexercise

class User(models.Model):
	uuser = models.CharField('User name', max_length=100) # user name
	uheight = models.FloatField('Height', null=True) # height of the user in meters
	uweight = models.FloatField('Weight', null=True) # weight of the user in kilograms

	def __unicode__(self):
		return "%s %d %d" % (self.uuser, self.uheight, self.uweight) 

class UserForm(ModelForm):
	class Meta:
		model = User

class Session(models.Model):
	suser = models.ForeignKey(User)
	sdate = models.DateTimeField('Workout Date')
	slength = models.IntegerField('Workout Length') # time in seconds for the workout session

	def _unicode__(self):
		return "%s %d" % (self.sdate, self.slength)

class SessionForm(ModelForm):
	suser = forms.ModelChoiceField(User.objects.all(), widget=forms.HiddenInput())
	class Meta:
		model = Session

class Exercise(models.Model):
	esession = models.ForeignKey(Session)
	exercise = models.ForeignKey(Definition)
	eweight = models.FloatField('Work Weight', null=True) # weight lifted
	edistance = models.FloatField('Miles', null=True) # distance traveled during exercise

	def __unicode__(self):
		return "%d %d" % (self.eweight, self.edistance)
		
class ExerciseForm(ModelForm):
	esession = forms.ModelChoiceField(Session.objects.all(), widget=forms.HiddenInput())
	class Meta:
		model = Exercise
