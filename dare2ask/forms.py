from django import forms
from django.contrib.auth.models import User
from dare2ask.models import Lecture, Question
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

class QuestionForm(forms.ModelForm):
    text = forms.CharField(max_length=Question.max_length, help_text="Please enter your question.")
    #lecture = Lecture.objects.filter(title="abc")

    class Meta:
        model = Question
        fields = ('text', )


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    staff = forms.BooleanField(widget=forms.CheckboxInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'staff')

class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=False)

    class Meta:
	    model = UserProfile
	    exclude = ('user', )
