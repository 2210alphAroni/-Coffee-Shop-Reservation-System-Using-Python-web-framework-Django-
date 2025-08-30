from django import forms
from contact.models import Form  

class ContactForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['name', 'email', 'subject', 'message']  