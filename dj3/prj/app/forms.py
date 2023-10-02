from django import forms

class MyForm(forms.Form):
    name = forms.CharField(max_length = 100)
    age = forms.IntegerField()
    email = forms.EmailField()