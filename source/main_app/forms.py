from django import forms
from django.forms import widgets   

class GuestCardForm(forms.Form):
    name = forms.CharField(label='Имя автора', max_length=100, required=True)
    mail = forms.EmailField(label='Эл. почта', max_length=200, required=True)
    description = forms.CharField(label='Детали записи', max_length=1500, required=True, widget=widgets.Textarea)