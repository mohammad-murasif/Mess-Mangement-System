from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):

    return render(request,'UserPortal/home.html' )


def Emplogin(request):

    return render(request,'UserPortal/emplogin.html' )




def profile(request):





    return render(request,'userportal/profile.html')