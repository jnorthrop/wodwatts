from django.db import models
from django import forms

import datetime

#class Email(models.Model):
#	email = models.EmailField(max_length=300)
#	entry_date = models.DateTimeField()

#	def __unicode__(self):
#		return self.email

#class EmailForm(forms.ModelForm):
#	entry_date = forms.DateTimeField(widget=forms.HiddenInput(), initial=datetime.datetime.now().replace(microsecond=0))

#	class Meta:
#		model = Email

