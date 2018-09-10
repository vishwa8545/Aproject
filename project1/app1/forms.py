from django import forms
from .models import Blog


class  BasicForm(forms.ModelForm):


    class Meta:
        model = Blog
        fields = {'user','name',
        'age',
        'degree'}
