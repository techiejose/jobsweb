import datetime

import extras as extras
from Tools.demo.spreadsheet import translate
from django import forms
from django.forms import DateInput, SelectDateWidget


from .models import Account, Job, Category

choice = Category.objects.all().values_list('name', 'name')
choicelist=[]
for item in choice:
    choicelist.append(item)

class SaveAccount(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('first_name', 'last_name','proffesion', 'email')

        widgets = {
            'first_name': forms.TimeInput(attrs= {'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'proffesion': forms.TimeInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),

        }

        def clean_password2(self):
            password = self.cleaned_data.get('password')
            password_confirmation = self.cleaned_data.get('password_confirmation')

            if password != password_confirmation:
                raise forms.ValidationError("Your passwords do not match")
            return password


class SaveJobs(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('company', 'position', 'category', 'description', 'type', 'process', 'salary', 'deadline')

        widgets = {
            'company': forms.TextInput(attrs= {'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choicelist, attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'process': forms.Textarea(attrs={'class': 'form-control'}),
            'salary': forms.TextInput(attrs={'class': 'form-control'}),
            'deadline': SelectDateWidget(),

        }

class SaveJob1(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('company', 'position', 'category', 'description', 'type', 'process', 'salary', 'deadline')

        widgets = {
            'company': forms.TextInput(attrs= {'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choicelist, attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'process': forms.Textarea(attrs={'class': 'form-control'}),
            'salary': forms.TextInput(attrs={'class': 'form-control'}),
            'deadline': SelectDateWidget(),

        }