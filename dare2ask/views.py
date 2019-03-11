from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from dare2ask.models import Lecture
from dare2ask.forms import LectureForm
from dare2ask.forms import UserForm, UserProfileForm

from datetime import datetime

#welcome/home
#about
#register – writes to database
#login
#join/create lecture
#in lecture – writes to database
#my profile
#edit my profile – writes to database
#logged out


def index(request):
	request.session.set_test_cookie()

	visitor_cookie_handler(request)

	context_dict = {}

	# Obtain our response object early so we can add cookie info
	response = render(request, 'dare2ask/index.html', context=context_dict)

	# Return response back to the user, updating any cookies that needed change
	return response

def about(request):
#	if request.session.test_cookie_worked():
#		print("TEST COOKIE WORKED!")
#		request.session.delete_test_cookie()

	context_dict = {}

	visitor_cookie_handler(request)

	return render(request, 'dare2ask/about.html', context=context_dict)

@login_required
def lecture(request):
    form = LectureForm()
    context_dict = {}

    # A HTTP Post?
    if request.method == 'POST':
        form = LectureForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            lec = form.save(commit=True)
            # Now that the lecture is saved
            # We could give a confirmation message
            # Bit since he most recent category added is on the index page
            # Then we can direct the user back to the index page.
            print(form.cleaned_data)
            return redirect('/dare2ask/lecture/' +
                (form.cleaned_data)['title'] )

        else:
            # The supplised form contained errors,
            # Print errors to terminal.
            print(form.errors)

    # Check that lectures exist
    try:
        lecture_list = Lecture.objects.order_by('-title')
        context_dict['lectures'] = lecture_list
    except Lecture.DoesNotExist:
        context_dict['lectures'] = None

    context_dict['form'] = form

    # Will handle the bad form, new form, or no form supplied cases
    # Will render the form with error messages
    return render(request, 'dare2ask/lecture.html', context_dict)

def in_lecture(request, lecture_name_slug):

    context_dict = {}

    try:
        # Look for category name slug with given name.
        # If not found, raise DoesNotExist exception.
        # So the .get() method returns one model instance or
        # raises an exception.
        lecture = Lecture.objects.get(slug = lecture_name_slug)

        # Retrieve all of the associated questions.
        # filter() will return a list of page objects or empty list
        #pages = Page.objects.filter(category = category)

        # Adds our results list to the template context under name pages.
        #context_dict['pages'] = pages

        # We also add the category object from the DB to the context
        # dictionary. We'll use this in the template to verify that
        # the category exists.
        context_dict['lecture'] = lecture

    except Lecture.DoesNotExist:
        # We get here if we didn't find the specified category
        # Template will display "no category" message
        context_dict['lecture'] = None
        #context_dict['pages'] = None

    return render(request, 'dare2ask/in_lecture.html', context=context_dict)

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
