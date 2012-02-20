from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class GetOrNoneManager(models.Manager):
    """Adds get_or_none method to objects
    """
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None

class Definition(models.Model):
	dexercise = models.CharField('Exercise', max_length=200) # name of the exercise
	bweight = models.FloatField('% Body Weight') # percentage of bodyweight used
	blength = models.FloatField('% Body Length') # percentage of body height used
	wlength = models.FloatField('% Body, Weight Travels', null=True) # percentage of body height the weight used in the exercise travels

	def __unicode__(self):
		return self.dexercise

class Profile(models.Model):
	puser = models.OneToOneField(User) # ties back to user account from registration module
	pheight = models.FloatField('Height', null=True) # height of the user in meters
	pweight = models.FloatField('Weight', null=True) # weight of the user in kilograms
	objects = GetOrNoneManager()

	def __unicode__(self):
		return "%d %d" % (self.pheight, self.pweight) 

class ProfileForm(ModelForm):
	puser = forms.ModelChoiceField(User.objects.all(),
            widget=forms.HiddenInput())

	class Meta:
		model = Profile

class Session(models.Model):
	suser = models.ForeignKey(User)
	sdate = models.DateTimeField('Workout Date')
	slength = models.IntegerField('Workout Length') # time in seconds for the workout session
	objects = GetOrNoneManager()

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
	objects = GetOrNoneManager()

	def __unicode__(self):
		return "%d %d" % (self.eweight, self.edistance)
		
class ExerciseForm(ModelForm):
	esession = forms.ModelChoiceField(Session.objects.all(), widget=forms.HiddenInput())
	exercise = forms.ModelChoiceField(queryset=Definition.objects.all())

	class Meta:
		model = Exercise
