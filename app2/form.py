from django import forms
from app2.models import student

class studentform(forms.ModelForm):
    class Meta:
        model = student
        fields = ['name','email']