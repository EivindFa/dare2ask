from django import forms
from django.contrib.auth.models import User

from dare2ask.models import Lecture
from dare2ask.models import UserProfile

class LectureForm(forms.ModelForm):
    title = forms.CharField(max_length=Lecture.max_length,
                help_text="Please enter the lecture room title.",)
    #print('1')
    #print(title)
    join_ID = forms.IntegerField(widget=forms.HiddenInput(), initial=-1, required=False)
    #print('2')
    #print(join_ID)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    #print('3')
    #print(slug)
    #print('FLAG 3 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    # An inline metaclass to provide addiional info on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Lecture
        fields = ('title', 'join_ID', )

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('picture', )
