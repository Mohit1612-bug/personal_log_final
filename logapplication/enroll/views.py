from django.shortcuts import render,HttpResponseRedirect
from .forms import UserSignUp,UserLogInForm,UserPasswordChange,TaskEdit,AddTask
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Task
from django.contrib.auth.models import User
from django.views import View
from reportlab.pdfgen import canvas
from django.http import HttpResponse
# Create your views here.
def some_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="projectmetadata.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(
    80, 800,
    "Project Name:- Persoanl Log"
    )
    p.drawString(
    80, 750,
    "Project Author:- Mohit Chaudhari"
    )
    p.drawString(
    80, 700,
    "Reg No:- 2018bit015"
    )
    p.drawString(
    80, 650,
    "Roll No:- A15"
    )
    p.drawString(
    80, 600,
    "Project Description:- In Personal Log Users Can Create There Personal tasks with deadline "
    )
    p.drawString(
    80, 550,
    "Project Contents:- Django,Pandas,Django REST API, And Many more.."
    )



    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response

class HomeView(View):
    def get(self,request):
        return render(request=request,template_name="enroll/home.html")
# def home(request):
#     return render(request=request,template_name="enroll/home.html")

class AboutView(View):
    def get(self,request):
        return render(request=request,template_name="enroll/about.html")

# def about(request):
#     return render(request=request,template_name="enroll/about.html")
class DataTableView(View):
    def get(self,request):
        users=User.objects.all();
        tasks=Task.objects.all();
        return render(request=request,template_name="enroll/datatable.html",context={'users':users,'tasks':tasks})


# def data_table(request):
#     users=User.objects.all();
#     tasks=Task.objects.all();
#     return render(request=request,template_name="enroll/datatable.html",context={'users':users,'tasks':tasks})
class SignUpView(View):
    def get(self,request):
        fm=UserSignUp()
        return render(request=request,template_name='enroll/signup.html',context={"form":fm})
    def post(self,request):
        fm=UserSignUp(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Account Has Been Created Succesfully")
            return HttpResponseRedirect('/login/')

# def signup(request):
#     if request.method=="POST":
#         fm=UserSignUp(request.POST)
#         if fm.is_valid():
#             fm.save()
#             messages.success(request,"Account Has Been Created Succesfully")
#             return HttpResponseRedirect('/login/')
#     else:
#         fm=UserSignUp()
#     return render(request=request,template_name='enroll/signup.html',context={"form":fm})


class ProfileView(View):
    def get(self,request):
        sm=AddTask();
        id=request.user.id;
        # extrainfo=Information.objects.filter(user__id=id)
        currentusertask=Task.objects.filter(user__id=id)
        return render(request,'enroll/profile.html',{'currentusertask':currentusertask,'name':request.user,'form':sm,})
    def post(self,request):
        sm=AddTask(request.POST)
        if sm.is_valid():
            sm.save();
            return HttpResponseRedirect('/profile/')


# def profile(request):
#     if request.user.is_authenticated:
#         if request.method=="POST":
#             sm=AddTask(request.POST)
#             if sm.is_valid():
#                 sm.save();
#                 return HttpResponseRedirect('/profile/')
#         else:
#             sm=AddTask();
#
#         id=request.user.id;
#         extrainfo=Information.objects.filter(user__id=id)
#         currentusertask=Task.objects.filter(user__id=id)
#         return render(request,'enroll/profile.html',{'currentusertask':currentusertask,'name':request.user,'form':sm,'info':extrainfo})
#     else:
#         return HttpResponseRedirect('/login/')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=UserLogInForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,"Logged Succesfully")
                    return HttpResponseRedirect('/profile/')
        else:
            fm=UserLogInForm()
        return render(request=request,template_name="enroll/login.html",context={'form':fm})
    else:
        return HttpResponseRedirect('/profile/')

class UserLogOutView(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect("/login/")

# def user_logout(request):
#     logout(request)
#     return HttpResponseRedirect("/login/")

def changepass(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=UserPasswordChange(request.user,request.POST)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect("/profile/")
        else:
            fm=UserPasswordChange(user=request.user)
        return render(request,'enroll/changepass.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

class DeleteTask(View):
    def get(self,request):
        pi=Task.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/profile/')

# def delete_task(request,id):
#     if request.user.is_authenticated:
#         pi=Task.objects.get(pk=id)
#         pi.delete()
#         return HttpResponseRedirect('/profile/')
#     else:
#         return HttpResponseRedirect('/login/')

def update_task(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=Task.objects.get(pk=id)
            fm=TaskEdit(request.POST,instance=pi)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect('/profile/')
        else:
            pi=Task.objects.get(pk=id)
            fm=TaskEdit(instance=pi)
        return render(request=request,template_name="enroll/updatetask.html",context={'form':fm})
    else:
        return HttpResponseRedirect('/login/')
