from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
    def __init__(self, *args, **kwargs):
        super(RegisterForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({'class':'form1','placeholder':'Username'})
        self.fields['email'].widget.attrs.update({'class':'form1','placeholder':'Email'})
        self.fields['password1'].widget.attrs.update({'class':'form1','placeholder':'Password1'})
        self.fields['password2'].widget.attrs.update({'class':'form1','placeholder':'confirm password'})

            