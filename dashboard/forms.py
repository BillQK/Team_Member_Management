from django import  forms
from django.forms import ModelForm

from .models import *

class MemberForm(forms.ModelForm):
    
    class Meta: 
        model = Member
        fields = '__all__'