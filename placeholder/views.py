from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
#from placeholder.models import EmailForm
from django.forms.util import ErrorList
from django.contrib import messages

def index(request):
#	if request.method == 'POST':
#		form = EmailForm(request.POST)
#		if form.is_valid():
#			new_form = form.save()
#			messages.success(request, "Got it! We'll keep you posted.")
#			return redirect('/#signup', new_form)
#		else:
#			return render_to_response('placeholder.html', {'form': form},
#								context_instance=RequestContext(request))
#	else:
#		form = EmailForm()
#		return render_to_response('placeholder.html', {'form': form},
#								context_instance=RequestContext(request))

