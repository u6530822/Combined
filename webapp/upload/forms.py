from django import forms
from .models import *

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text','extra','insert')


class ResultsPage(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text','title')

class BloodSampleForm(forms.ModelForm):
    Reference = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control form-control-user",}))
    LabNo = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control form-control-user",}))
    Date_Time = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control form-control-user", }))
    Potassium = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control form-control-user", }))
    Sodium = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control form-control-user", }))
    Chloride = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control form-control-user", }))
    MCH = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control form-control-user", }))
    class Meta:
        model = BloodSamples
        fields = ('Reference','LabNo','Date_Time','Potassium','Sodium','Chloride','MCH')


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control form-control-user",}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control form-control-user",}))
    class Meta:
        model = Login

        fields = ('username','password')








