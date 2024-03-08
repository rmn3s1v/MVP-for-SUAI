from django import forms
from .models import Resume

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class Info(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ["student_id", "information", "about", "iam"]
