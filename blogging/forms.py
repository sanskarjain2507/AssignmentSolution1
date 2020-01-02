from django import forms

class blogForm(forms.Form):
    charData=forms.CharField()
    fileData=forms.FileField()