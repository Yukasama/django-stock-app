from django import forms

class Login():
    email = forms.CharField(max_length=500)