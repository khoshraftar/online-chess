from django import forms
class sign_up(forms.Form):
    name=forms.CharField()
    key=forms.CharField()
    email=forms.EmailField()

