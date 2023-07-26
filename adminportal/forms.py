from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from ckeditor.fields import RichTextFormField
from django.forms.forms import Form  
from .models import Student , Person,MessFee,MessMenu
from django.contrib.auth.forms import UserCreationForm
# class CustomUserCreationForm(UserCreationForm):  
#     username = forms.CharField(label='username', min_length=5, max_length=150)  
#     email = forms.EmailField(label='email')  
#     password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
#     password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)  
  
#     def username_clean(self):  
#         username = self.cleaned_data['username'].lower()  
#         new = User.objects.filter(username = username)  
#         if new.count():  
#             raise ValidationError("User Already Exist")  
#         return username  
  
#     def email_clean(self):  
#         email = self.cleaned_data['email'].lower()  
#         new = User.objects.filter(email=email)  
#         if new.count():  
#             raise ValidationError(" Email Already Exist")  
#         return email  
  
#     def clean_password2(self):  
#         password1 = self.cleaned_data['password1']  
#         password2 = self.cleaned_data['password2']  
  
#         if password1 and password2 and password1 != password2:  
#             raise ValidationError("Password don't match")  
#         return password2  
  
#     def save(self, commit = True):  
#         user = User.objects.create_user(  
#             self.cleaned_data['username'],  
#             self.cleaned_data['email'],  
#             self.cleaned_data['password1']  
#         )  
#         return user  
class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model = User
        fields=['username','email','password1','password2']


class addstudentdetails(forms.ModelForm):
    class Meta:
        model = Student
        fields=['name','phone_num','email','hostel','room_no','profilepic']
        # labels = {'name': "Name", "phone_num": "Mobile Number",'email':"Email","hostel":"Hostel","room_no":"room_no"}

class EditStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields=['name','phone_num','email','hostel','room_no','profilepic']
        # labels = {'name': "Name", "phone_num": "Mobile Number",'email':"Email","hostel":"Hostel","room_no":"room_no","profilepic":profilepic}


class PayementForm(forms.ModelForm):
    class Meta:
        model = MessFee
        fields='__all__'

class Login(forms.Form):
  
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)



class PersonForm(forms.Form):
    class meta:
        model = Person
        fields = '__all__'


class MenuForm(forms.Form):
    class meta:
        model = MessMenu
        fields = '__all__'
