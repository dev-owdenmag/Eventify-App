from django import forms
from .models import Participants

class ParticipantForm(forms.ModelForm):
    class Meta:
        model Participant
        fields = ['first_name', 'last_name', 'phone', 'email', 'occupation', 'company']
        widgets ={
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
        }