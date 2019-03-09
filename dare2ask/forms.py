from django import forms
from django.contrib.auth.models import User
from dare2ask.models import Lecture
from dare2ask.models import UserProfile

class LectureForm(forms.ModelForm):
    title = forms.CharField(max_length=Lecture.max_length,
                help_text="Please enter the lecture room title.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline metaclass to provide addiional info on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Lecture
        fields = ('title',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    staff = forms.BooleanField(widget=forms.CheckboxInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'staff')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('picture', )
