from django import forms
from .models import *
class TalabaForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=50)
    nums_of_books = forms.IntegerField(min_value=0, max_value=9)
    course = forms.IntegerField(min_value=1, max_value=7)
    senior = forms.BooleanField(required=False)

class kitobForm(forms.ModelForm):
    class Meta:
        model = kitob
        fields = '__all__'
class adminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = '__all__'

class muallifForm(forms.ModelForm):
    class Meta:
        model = Muallif
        fields = '__all__'
class recordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'
