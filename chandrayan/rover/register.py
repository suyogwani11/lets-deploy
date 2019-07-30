from django import forms
from django.contrib.auth.models import User
from .userdetails import accdata
from .userdetails import UserProfileInfo


class resume(forms.ModelForm):
    # name = forms.CharField()
    # email = forms.EmailField()
    class Meta():
        model = accdata
        fields = "__all__"


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
