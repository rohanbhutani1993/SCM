
from django import forms
from .models import UserDetails


class UserLoginForm(forms.ModelForm):
    userName = forms.CharField(widget = forms.TextInput(attrs={"placeholder":"Username"}))
    password = forms.CharField(widget = forms.TextInput(attrs={"placeholder":"Password"}))  

    class Meta:
        model = UserDetails
        fields = [
            'userName',
            'password'
            ]    

        
        