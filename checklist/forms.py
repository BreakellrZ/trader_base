from django import forms
from django.forms import ModelForm

from .models import Checkbox



class ListForm(forms.ModelForm):

    class Meta:
        model = Checkbox
        fields = ('title','complete',)