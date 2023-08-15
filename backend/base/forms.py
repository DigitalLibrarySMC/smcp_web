from django.forms import ModelForm 
from .models import person, family, bcc_unit
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class familyform(ModelForm):
    class Meta:
      model = family
      fields = '__all__'


class personform(ModelForm):
    class Meta:
      model = person
      fields = '__all__'

class bcc_unitform(ModelForm):
    class Meta:
      model = bcc_unit
      fields = '__all__'

class SignUpForm(UserCreationForm):
    phone = forms.CharField(required=True, help_text='Required. Enter a valid phone number.')
    avatar = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'password1', 'password2')
