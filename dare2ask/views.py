from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

from dare2ask.models import Lecture, UserProfile, Question
from dare2ask.forms import LectureForm, SearchForm, QuestionForm
from dare2ask.forms import UserForm, UserProfileForm
from dare2ask.decorators import is_staff

from datetime import datetime

def index(request):
	request.session.set_test_cookie()

	visitor_cookie_handler(request)

	context_dict = {}
	# Obtain our response object early so we can add cookie info
	response = render(request, 'dare2ask/index.html', context=context_dict)

	# Return response back to the user, updating any cookies that needed change
	return response

#@is_staff
def about(request):
#	if request.session.test_cookie_worked():
#		print("TEST COOKIE WORKED!")
#		request.session.delete_test_cookie()

	context_dict = {}

	visitor_cookie_handler(request)

	return render(request, 'dare2ask/about.html', context=context_dict)

@login_required
def lecture(request):
    formLec = LectureForm()
    context_dict = {}

    # A HTTP Post?
    if request.method == 'POST':
        if 'lecture' in request.POST:
        	formLec = LectureForm(request.POST)

	        # Have we been provided with a valid form?
	        if formLec.is_valid():
	            # Save the new category to the database.
	            lec = formLec.save(commit=True)
	            # Now that the lecture is saved
	            # We could give a confirmation message
	            # Bit since he most recent category added is on the index page
	            # Then we can direct the user back to the index page.
	            print(formLec.cleaned_data)
	            return redirect('/dare2ask/lecture/' +
	                (formLec.cleaned_data)['title'] )

	        else:
	            # The supplised form contained errors,
	            # Print errors to terminal.
	            print(formLec.errors)

    elif request.method == 'GET':
        formLec = SearchForm(request.GET)

        # Have we been provided with a valid form?
        if formLec.is_valid():
            print(formLec.cleaned_data)
            return redirect('/dare2ask/search/' +
				(formLec.cleaned_data)['name'])

        else:
	        # The supplised form contained errors,
	        # Print errors to terminal.
            print(formLec.errors)

    # Check that lectures exist
    try:
        lecture_list = Lecture.objects.order_by('-title')
        context_dict['lectures'] = lecture_list
    except Lecture.DoesNotExist:
        context_dict['lectures'] = None

    context_dict['form'] = formLec

    # Will handle the bad form, new form, or no form supplied cases
    # Will render the form with error messages
    return render(request, 'dare2ask/lecture.html', context_dict)

def search(request, search_slug):
	print(search_slug)
	for lec in Lecture.objects.order_by('title'):
		# if search_slug in
		print(lec)
	return HttpResponse("Hello")

def in_lecture(request, lecture_name_slug):
	form = QuestionForm()
	context_dict = {'form': form}
	try:
		# Look for lecture name slug with given name.
		# If not found, raise DoesNotExist exception.
		# So the .get() method returns one model instance or
		# raises an exception.
		lecture = Lecture.objects.get(slug = lecture_name_slug)

		# Retrieve all of the associated questions.
		# filter() will return a list of question objects or empty list
		questions = Question.objects.filter(lecture = lecture)

		# Adds our results list to the template context under name pages.
		context_dict['questions'] = questions

		# We also add the lecture object from the DB to the context
		# dictionary. We'll use this in the template to verify that
		# the lecture exists.
		context_dict['lecture'] = lecture
	except Lecture.DoesNotExist:
		# We get here if we didn't find the specified category
		# Template will display "no category" message
		context_dict['lecture'] = None

	if request.method == 'POST':
		print("REQUEST=",request.body,"\n",request.POST)
		if "Create Question" in request.POST.get('create_question', 'None'):
			form = QuestionForm(request.POST)
			if form.is_valid():
				q = form.save(commit=False)
				q.lecture = context_dict['lecture']
				q.save()
			else:
				print(form.errors)
				'''elif "upvote_question" in request.POST:
			# Get the current question
			print("UPVOTING")
			i = int(request.POST['upvote_question'])-1
			question = context_dict["questions"][0]
			question.upvotes += 1
			question.save()'''
		elif "answered_question" in request.POST:
			i = int(request.POST['answered_question'])-1
			question = context_dict["questions"][i]
			if question.answered == True:
				question.answered = False
			else:
				question.answered = True
			question.save()
		else:
			print("UNRECOGNIZED")

	return render(request, 'dare2ask/in_lecture.html', context=context_dict)

#@is_staff
def delete_conf(request, lecture_name_slug):
    context_dict = {}

    try:
        lecture = Lecture.objects.get(slug = lecture_name_slug)

        context_dict['lecture'] = lecture

    except Lecture.DoesNotExist:
        context_dict['lecture'] = None
        print('context_dict["lecture"]= None')
    return render(request, 'dare2ask/delete_conf.html', context_dict)

def delete(request, lecture_name_slug):
    lec = get_object_or_404(Lecture, slug = lecture_name_slug).delete()
    return HttpResponseRedirect('/dare2ask')

# A helper method
def get_server_side_cookie(request, cookie, default_val=None):
	val = request.session.get(cookie)
	if not val:
		val = default_val
	return val

def visitor_cookie_handler(request):
	visits = int(get_server_side_cookie(request, 'visits', '1'))

	last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
	last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

	# If it's been more than a day since the last visit:
	if (datetime.now() - last_visit_time).days > 0:
		visits = visits + 1
		# Update the last visit cookie
		request.session['last_visit'] = str(datetime.now())
	else:
		# Set the last visit cookie
		request.session['last_visit'] = last_visit_cookie

	# Update/set the visits cookie
	request.session['visits'] = visits

@login_required
def register_profile(request):
	form = UserProfileForm()
	if request.method == 'POST':
		form = UserProfileForm(request.POST, request.FILES)
		if form.is_valid():
			user_profile = form.save(commit=False)
			user_profile.user = request.user
			user_profile.save()
			# if form.lecturer:
			# 	userprofile.lecturer = True

			return redirect('index')
		else:
			print(form.errors)

	context_dict = {'form':form}

	return render(request, 'dare2ask/profile_registration.html', context_dict)

@login_required
def profile(request, username):
	try:
		user = User.objects.get(username=username)
	except User.DoesNotExist:
		return redirect('index')

	userprofile = UserProfile.objects.get_or_create(user=user)[0]
	form = UserProfileForm(
		{'picture': userprofile.picture, 'lecturer': userprofile.lecturer})

	if request.method == 'POST':
		form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
		if form.is_valid():
			form.save(commit=True)
			return redirect('dare2ask:profile', user.username)
		else:
			print(form.errors)

	return render(request, 'dare2ask/profile.html',
		{'userprofile': userprofile, 'selecteduser': user, 'form': form})


@login_required
def like_question(request):
	l_id = None; # l_id == like_id
	if request.method == 'GET':
		l_id = request.GET['like_id'];  # getting "like_id" from the button in ajax.js
		likes = 0;
		all_likes = ""
		if l_id:
			q = Question.objects.get(id=int(l_id));
			if q:
				likes = q.upvotes + 1;
				q.upvotes = likes;
				q.save();
				# Get parent lecture of question
				l = q.lecture
				# Get all questions with this parent lecture
				all_qs = Question.objects.filter(lecture=l)
				for n in all_qs:
					print(n.upvotes)
					all_likes += str(n.upvotes)
					all_likes += " "
	return HttpResponse(all_likes)
