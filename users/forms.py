from django.contrib.auth.models import User
from django.forms import forms, ModelForm
from django import forms
from .models import Profile
from django.contrib.admin import widgets

class DateInput(forms.DateInput):
    input_type = 'date'



class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Еще раз', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
        #'date_of_birth','time_of_birth','city','gender','photo')

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'time_of_birth','city1','city2','gender','photo')
        widgets = {'date_of_birth': DateInput(),
                   'time_of_birth': widgets.AdminTimeWidget, }