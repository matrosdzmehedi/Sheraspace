from .models import PersonCv
from django import forms



class MyCvForm(forms.ModelForm):
    class Meta(object):
        model = PersonCv
        fields = ['name','dob', 'phone', 'address', 'institute',
                  'ps_year', 'f_name', 'gender', 'email', 'district', 'subject']

        widgets = {
            
            'dob': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type':"date"

                }
            ),
    
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),  'phone': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ), 'address': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ), 'institute': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ), 'ps_year': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ), 'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            
            'f_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
             'subject': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
