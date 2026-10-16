from django.db import models
from django import forms
# Create your models here.


class ImageSubmit(forms.Form):
   image_file = forms.ImageField(required=True, label="Use camera:",
      widget=forms.ClearableFileInput(attrs={
         'capture': 'environment',
         'accept': 'image/*',
      })
   )
class FileSubmit(forms.Form):
   image_file = forms.ImageField(required=True, label="Choose file:",
       widget=forms.ClearableFileInput(attrs={
          'accept': 'image/*',
      })
   )



class NumberInput(forms.Form):
   plastic_number = forms.CharField(required=True, label="",
      widget=forms.NumberInput(attrs={
         'placeholder': 'Plastic ID Number',
      })
      )


