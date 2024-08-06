from django import forms
from . models import Series

class SeriesForm(forms.ModelForm):
    class Meta:
        models=Series
        fields=['name','desc','year','img']