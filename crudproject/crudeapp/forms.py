from django import forms
from .models import user

class AddForm(forms.ModelForm):
    class Meta:
        model = user

        fields = ('firstname','lastname','username','password','email','age','phonenumber')

        widgets ={

            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'phonenumber':forms.TextInput(attrs={'class':'form-control'}),
            
        }