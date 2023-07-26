from django import forms  
from adminportal.models import leaveRequests

class leaveForm(forms.Form):
    class meta:
        model =leaveRequests
        fields=['leaveid','startDate','EndDate']



class Login(forms.Form):
  
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)