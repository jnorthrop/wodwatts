from application.models import *
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
	latest_user_list = User.objects.all().order_by('id')[:10]

	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return redirect("/" + str(new_user.id))
		else:
			return render_to_response('index.html', {'user': form, 'latest_user_list': latest_user_list},
								context_instance=RequestContext(request))
	else:
		form = UserForm()
		return render_to_response('index.html', {'user': form, 'latest_user_list': latest_user_list},
								context_instance=RequestContext(request))
	
def session(request, user_id):
	latest_session_list = Session.objects.filter(suser=user_id).order_by('sdate')[:10]

	if request.method == 'POST':
		form = SessionForm(request.POST)
		if form.is_valid():
			new_session = form.save()
			return redirect('/' + str(user_id) + '/' + str(new_session.id))
		else:
			return render_to_response('session.html', {'session': form, 'latest_session_list': latest_session_list},
								context_instance=RequestContext(request))
	else:
		form = SessionForm(initial={'suser': user_id})
		return render_to_response('session.html', {'session': form, 'latest_session_list': latest_session_list},
								context_instance=RequestContext(request))
	
def exercise(request, user_id, session_id):
	latest_exercise_list = Exercise.objects.filter(esession=session_id)
	exercise_list = Definition.objects.all().order_by('dexercise')

	if request.method == 'POST':
		form = ExerciseForm(request.POST)
		new_exercise = form.save()
		if form.is_valid():
			form = ExerciseForm()
			return render_to_response('exercise.html', {'exercise': form, 'latest_exercise_list': latest_exercise_list, 'exercise_list': exercise_list},
								context_instance=RequestContext(request))
		else:
			return render_to_response('exercise.html', {'exercise': form, 'latest_exercise_list': latest_exercise_list, 'exercise_list': exercise_list},
								context_instance=RequestContext(request))
	else:
		form = ExerciseForm(initial={'esession': session_id})
		return render_to_response('exercise.html', {'exercise': form, 'latest_exercise_list': latest_exercise_list, 'exercise_list': exercise_list},
								context_instance=RequestContext(request))
