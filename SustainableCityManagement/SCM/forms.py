
from django import forms
from .models import UserDetails


class UserLoginForm(forms.ModelForm):
    userName = forms.CharField(widget = forms.TextInput(attrs={"placeholder":"Username", "class":"form-control"}))
    password = forms.CharField(widget = forms.TextInput(attrs={"placeholder":"Password", "class":"form-control"}))  

    class Meta:
        model = UserDetails
        fields = [
            'userName',
            'password'
            ]    

        
        