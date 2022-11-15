from django import  forms
from django.forms import ModelForm

from .models import *


# Member structure format 
class MemberForm(forms.ModelForm):
    
    # Return all fields in model
    class Meta: 
        model = Member
        fields = '__all__'