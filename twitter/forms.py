from  django import forms
from twitter.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Profile

