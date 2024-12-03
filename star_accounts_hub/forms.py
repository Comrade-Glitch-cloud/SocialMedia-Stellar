from django import forms
from django.contrib.auth.forms import UserCreationForm
from star_accounts_hub.models import CadetProfile
from django.contrib.auth.models import User

class CadetSignUpForm(UserCreationForm):
    valid_email = forms.EmailField()
    cadet_first_name = forms.CharField()
    cadet_last_name = forms.CharField()
    stellarname = forms.CharField()

    class Meta:
        model = User
        fields = ['stellarname', 'cadet_first_name', 'cadet_last_name', 'valid_email', 'password1', 'password2']


class CadetUpdateForm(forms.ModelForm):
    valid_email = forms.EmailField()
    cadet_first_name = forms.CharField()
    cadet_last_name = forms.CharField()
    stellarname = forms.CharField()
    cadet_picture = forms.ImageField(required=False)

    class Meta:
        model = CadetProfile
        fields = ['stellarname', 'valid_email', 'cadet_first_name', 'cadet_last_name', 'cadet_picture']
