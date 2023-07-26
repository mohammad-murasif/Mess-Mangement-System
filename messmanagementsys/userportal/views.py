from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .forms import  Login ,leaveForm
from django.contrib.auth.decorators import login_required 
from adminportal.models import Student ,MessFee, MessMenu,Company
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
import datetime as dt
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from adminportal.forms import MenuForm

from adminportal.forms import EditStudent


# Create your views here.
def home(request):
    companyDetails=Company.objects.last()
    if request.user.is_authenticated:
        Current_std= get_object_or_404(Student,user_id=request.user.id)

        return render(request,'UserPortal/home.html',{'companyDetails':companyDetails,'current_user':Current_std})  


    return render(request,'UserPortal/home.html', {'companyDetails':companyDetails} )


def userlogin(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('u-dashboard')
            else:
                messages.error(request, 'You are not a active user')
                return redirect('u-dashboard')
        else:
            messages.error(request, 'Enter valid username and password')
            return redirect('u-login')
    return render(request,'userportal/login.html' )




@login_required
def dashboard(request):
    
    Current_std= get_object_or_404(Student,user_id=request.user.id)
    messages.success(request,f"Welcome {Current_std.name}")
    feeMonths=MessFee.objects.filter(Q(std_id_id=Current_std.id))
    dueMonths=MessFee.objects.filter(Q(std_id_id=Current_std.id),~Q(bal_amount=0))


    return render(request,'userportal/dashboard.html',{'current_user':Current_std,'feeMonths':feeMonths,'dueMonths':dueMonths})



@login_required
def profile(request):
    if request.user.is_active:
        edit_std=get_object_or_404(Student,user_id=request.user.id)
        user_std=get_object_or_404(User,id=request.user.id)
        if request.method== 'GET':
            form=EditStudent(instance=edit_std)
            return render(request, "userportal/profile.html", {'form':form,'current_user':edit_std})
        elif request.method== 'POST':
            try:
                form=EditStudent(request.POST or None,request.FILES or None ,instance=edit_std)
                if form.is_valid():
                    form.save()
                    user_std.username= str(request.POST['phone_num'])
                    user_std.email=request.POST['email']
                    user_std.save()
                    messages.success(request, f'Details updated for {edit_std.name} Successfully!')
                    return redirect('u-profile')
                else:
                    check_existing = Student.objects.filter(phone_num=edit_std.phone_num) or Student.objects.filter(email=request.POST['id_phone_num']).exists() or  User.objects.filter(username=str(request.POST['id_phone_num'])).exists()
                    if check_existing:
                        messages.error(request,f'{edit_std.email} or {edit_std.phone_num} already registered!')
                        return redirect('u-profile')

            except Exception as e:
                    messages.error(request,'Oops Something went wrong!')
                    return redirect('u-profile')
                
    else:
        messages.error(request, 'You are not authorized to access!')
        return redirect("userlogin")

    return render(request,'userportal/profile.html')


def payments(request):
    if request.user.is_active:
        Current_std= get_object_or_404(Student,user_id=request.user.id)        
        if 'q' in request.GET:
            q = request.GET['q']
            page_obj = MessFee.objects.filter(Q(std_id_id__in=Student.objects.filter(name__icontains=q)) or Q(reciept_id=q))
            page_num = request.GET.get('page', 1)
            paginator = Paginator(page_obj, 10)  #10 payments per page
            return render(request, 'userportal/viewpayments.html', {'page_obj': page_obj,'current_user':Current_std})
        else:
            Current_std= get_object_or_404(Student,user_id=request.user.id)
            payments_all = MessFee.objects.filter(std_id_id=Current_std.id)
            page_num = request.GET.get('page', 1)
            paginator = Paginator(payments_all, 10)  # 10 payemnts per page
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                # if page is not an integer, deliver the first pag
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)

            return render(request, 'userportal/payments.html', {'page_obj': page_obj,'current_user':Current_std})
    else:
        messages.error(request, 'You are not authorized to access!')
        return redirect("u-login")


    return render(request,'userportal/payments.html')


def applyleave(request):
    if request.user.is_active:
        if request.method=='POST':
            pass
        form=leaveForm()
        print(form)
        return render(request,'userportal/applyleave.html')
    else:
        messages.error(request,'You must login first!')
        return redirect('u-login')

def feedback(request):



    return render(request,'userportal/feedback.html')

def messmenu(request):
    form=MessMenu.objects.last()
    Current_std= get_object_or_404(Student,user_id=request.user.id)   

    return render(request,'userportal/messmenu.html',{'form':form,'current_user':Current_std})

def applyfornoc(request):


    return render(request,'userportal/noc.html')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'userportal/passchange.html', {
        'form': form
    })