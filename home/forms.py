from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User



class edit_password_form(UserChangeForm):
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    

    class Meta:
        model = User
        fields = ('first_name','last_name','username')

