from application.models import *
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
	if(request.user.id):
		user = User.objects.get(pk=request.user.id)
	else:
		user = None
	
	profile = Profile.objects.get_or_none(puser=request.user.id)
		
	return render_to_response('index.html', {'user': user, 'profile': profile, },
					context_instance=RequestContext(request))

def profile(request):
	# if they aren't logged in, 404
	user = get_object_or_404(User, pk=request.user.id)
	profile = Profile.objects.get_or_none(puser=request.user.id)
		
	if request.method == 'POST':
		form = ProfileForm(request.POST, instance=profile)
		if form.is_valid():
			form.save()
			return redirect("/")
		else:
			return render_to_response('profile.html', {'form': form, },
								context_instance=RequestContext(request))
	else:
		puser = User.objects.get(pk=request.user.id)
		form = ProfileForm(instance=profile, initial = {'puser': puser})
		return render_to_response('profile.html', {'form': form, },
								context_instance=RequestContext(request))
	
def session(request, session_id=None):
	# if they aren't logged in, 404
	user = get_object_or_404(User, pk=request.user.id)

	latest_session_list = Session.objects.filter(suser=user.id).order_by('sdate')[:10]
	session = Session.objects.get_or_none(pk=session_id, suser=user.id)
	
	if(session_id):
		exercise_list = Exercise.objects.filter(esession=session_id)
	else:
		exercise_list = None

	if request.method == 'POST':
		form = SessionForm(request.POST, instance=session)
		if form.is_valid():
			new_session = form.save()
			return redirect('/session/' + str(new_session.id))
		else:
			return render_to_response('session.html', {'form': form, 
								'latest_session_list': latest_session_list,
								'exercise_list': exercise_list,
								'session_id': session_id},
								context_instance=RequestContext(request))
	else:
		suser = User.objects.get(pk=request.user.id)
		form = SessionForm(instance=session, initial={'suser': suser})
		return render_to_response('session.html', {'form': form, 
								'latest_session_list': latest_session_list,
								'exercise_list': exercise_list,
								'session_id': session_id}, 
								context_instance=RequestContext(request))
	
def exercise(request, session_id, exercise_id=None):
	# see if they have access to this session
	user = get_object_or_404(User, pk=request.user.id)
	session = get_object_or_404(Session, pk=session_id, suser=user.id)

	exercise_list = Definition.objects.all().order_by('dexercise')
	latest_exercise_list = Exercise.objects.filter(esession=session_id)

	if request.method == 'POST':
		form = ExerciseForm(request.POST)
		new_exercise = form.save()
		if form.is_valid():
			form = ExerciseForm()
			return render_to_response('exercise.html', {'form': form, 
								'latest_exercise_list': latest_exercise_list,
								'exercise_list': exercise_list},
								context_instance=RequestContext(request))
		else:
			return render_to_response('exercise.html', {'form': form, 
								'latest_exercise_list': latest_exercise_list,
								'exercise_list': exercise_list},
								context_instance=RequestContext(request))
	else:
		form = ExerciseForm(initial={'esession': session_id})
		return render_to_response('exercise.html', {'form': form, 
								'latest_exercise_list': latest_exercise_list,
								'exercise_list': exercise_list}, 
								context_instance=RequestContext(request))
