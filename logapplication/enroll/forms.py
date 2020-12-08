from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django import forms
from .models import Task
class UserSignUp(UserCreationForm):
    password1 = forms.CharField(
        label=("Password"),
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'})
    )
    password2 = forms.CharField(
        label=("Password (Again)"),
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'})
    )
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={
            'email':'Email',
        }
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }
class UserLogInForm(AuthenticationForm):
    username = forms.CharField(
        label=("Username"),
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    password = forms.CharField(
        label=("Password"),
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'})
    )
    class Meta:
        model=User

class UserPasswordChange(PasswordChangeForm):
    old_password=forms.CharField(
        label=("Old Password"),
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    new_password1=forms.CharField(
        label=("New password"),
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'})
    )
    new_password2=forms.CharField(
        label=("Confirm password"),
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'})
    )
    class Meta:
        model=User

class AddTask(forms.ModelForm):
    due_date=forms.DateTimeField(
        label=("Due Date"),
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    class Meta:
        model=Task
        fields=['user','task_name','task_status','task_description','due_date',]
        widgets={
            'task_name':forms.TextInput(attrs={'class':'form-control'}),
            'task_description':forms.TextInput(attrs={'class':'form-control'}),
            'task_status':forms.TextInput(attrs={'class':'form-control'}),
            # 'due_date':forms.DateTimeInput(attrs={'class':'form-control'}),
        }
class TaskEdit(forms.ModelForm):
    class Meta:
        model=Task
        fields=['task_name','task_status','task_description','due_date']
        widgets={
            'task_name':forms.TextInput(attrs={'class':'form-control'}),
            'task_description':forms.TextInput(attrs={'class':'form-control'}),
            'task_status':forms.TextInput(attrs={'class':'form-control'}),
            'due_date':forms.DateTimeInput(attrs={'class':'form-control'}),
        }
