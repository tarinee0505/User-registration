from django import forms
from app.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username','password']
        widgets = {'password':forms.PasswordInput}
        help_texts = {'username':''}


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['username']