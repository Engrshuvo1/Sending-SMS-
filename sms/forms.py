
from django import forms
from .models import *

class ThreadForms(forms.ModelForm):
   
    class Meta:    
        
        model = ThreadModel
        
        fields = '__all__'


class MessageForm(forms.ModelForm):
   
    class Meta:    
        
        model = MessageModel
        
        fields = '__all__'