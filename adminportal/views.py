from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from .models import Student, MessFee, Person , Company
from django.contrib import messages

from .forms import addstudentdetails, Login, PayementForm, MenuForm,EditStudent
from django.contrib.auth.decorators import login_required 
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime as dt
from django.db.models import Q

#PDF
import os
from messmanagementsys.settings import MEDIA_ROOT
from datetime import datetime
from django.conf import settings
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage
from weasyprint import HTML, CSS
from django.shortcuts import HttpResponse

def home(request):
    if request.user.is_staff:
        if request.method== 'POST':
            form  = addstudentdetails(request.POST)
            if form.is_valid():
                form.save()
                username=form.cleaned_data.get('username')
                messages.success(request,f'Account created for {username} , Now You are able to login!')
                return redirect('login')
        else:
            form = addstudentdetails()
        return render(request,'adminportal/home.html',{'form':form})
    else:
        messages.error(request, 'You are not authorized to access!')
        return redirect("login")



def AdminLogin(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'You are not a staff!')
                return redirect('login')
        else:
            messages.error(request, 'Enter valid username and password')
            return redirect('login')

    return render(
        request, 'adminportal/login.html')


@login_required
def dashboard(request):
    now=dt.now()
    thismonth =now.strftime('%Y-%m')
    if request.user.is_staff:
        current_user = request.user
        messages.success(request, f'Welcome {current_user}')
        count = len(Student.objects.all())
        bjrc_student = len(Student.objects.filter(hostel='BJRC'))
        apj = len(Student.objects.filter(hostel='APJ'))
        block_a = len(Student.objects.filter(hostel='BLOCK A'))
        block_b = len(Student.objects.filter(hostel='BLOCK B'))
        block_c = len(Student.objects.filter(hostel='BLOCK C'))
        nursing = len(Student.objects.filter(hostel='NURSING HOSTEL'))
        fatima_zehra = len(Student.objects.filter(hostel='FATIMA ZEHRA'))
        # ******* This Month payments
        total_payments=len(MessFee.objects.filter(fee_month=thismonth))
        BJRC_payments=len(MessFee.objects.filter(fee_month=thismonth).values() and MessFee.objects.filter(std_id_id__in=Student.objects.filter(hostel='BJRC')))
        APJ_payments=len(MessFee.objects.filter(fee_month=thismonth).values() and MessFee.objects.filter(std_id_id__in=Student.objects.filter(hostel='APJ')))
        BLOCKA_payments=len(MessFee.objects.filter(fee_month=thismonth).values() and MessFee.objects.filter(std_id_id__in=Student.objects.filter(hostel='BLOCK A')))
        BLOCKB_payments=len(MessFee.objects.filter(fee_month=thismonth).values() and MessFee.objects.filter(std_id_id__in=Student.objects.filter(hostel='BLOCK B')))
        BLOCKC_payments=len(MessFee.objects.filter(fee_month=thismonth).values() and MessFee.objects.filter(std_id_id__in=Student.objects.filter(hostel='BLOCK C')))
        NURSING_payments=len(MessFee.objects.filter(fee_month=thismonth).values() and MessFee.objects.filter(std_id_id__in=Student.objects.filter(hostel='NURSING HOSTEL')))
        fatimazehra_payments=len(MessFee.objects.filter(fee_month=thismonth).values() and MessFee.objects.filter(std_id_id__in=Student.objects.filter(hostel='FATIMA ZEHRA')))
        #   ******* DUES THIS MONTH*******
        dues_thismonth=len(MessFee.objects.filter(Q(fee_month=thismonth) and ~Q(bal_amount=0)).values())
        BJRCdues_thismonth=len(MessFee.objects.filter(~Q(bal_amount=0) and Q(fee_month=thismonth) and  Q(std_id_id__in=Student.objects.filter(hostel='BJRC'))).values())
        APJdues_thismonth=len(MessFee.objects.filter(Q(fee_month=thismonth) and Q(bal_amount__gt=0) and Q(std_id_id__in=Student.objects.filter(hostel='APJ'))).values())
        BLOCKAdues_thismonth=len(MessFee.objects.filter(Q(fee_month=thismonth) and Q(bal_amount__gt=0) and Q(std_id_id__in=Student.objects.filter(hostel='BLOCK A'))).values())
        BLOCKBdues_thismonth=len(MessFee.objects.filter(Q(fee_month=thismonth) and Q(bal_amount__gt=0) and Q(std_id_id__in=Student.objects.filter(hostel='BLOCK B'))).values())
        BLOCKCdues_thismonth=len(MessFee.objects.filter(Q(fee_month=thismonth) and Q(bal_amount__gt=0) and Q(std_id_id__in=Student.objects.filter(hostel='BLOCK C'))).values())
        Nursingdues_thismonth=len(MessFee.objects.filter(Q(fee_month=thismonth) and Q(bal_amount__gt=0) and Q(std_id_id__in=Student.objects.filter(hostel='NURSING HOSTEL'))).values())
        Fatimazehradues_thismonth=len(MessFee.objects.filter(Q(fee_month=thismonth) and Q(bal_amount__gt=0) and Q(std_id_id__in=Student.objects.filter(hostel='FATIMA ZEHRA'))).values())
        #    *******PREVIOUS DUES*********
        dues_othermonths=len(MessFee.objects.filter(Q(bal_amount__gt=0)).exclude(fee_month=thismonth))
        BJRCdues_othermonths=len(MessFee.objects.filter(Q(bal_amount__gt=0) and Q(std_id_id__in=Student.objects.filter(hostel='BJRC'))).exclude(fee_month=thismonth))
        APJdues_othermonths=len(MessFee.objects.filter(Q(bal_amount__gt=0) and Q(std_id_id__in=Student.objects.filter(hostel='APJ'))).exclude(fee_month=thismonth))
        BLOCKAdues_othermonths=len(MessFee.objects.filter(Q(bal_amount__gt=0) and Q(std_id_id__in=Student.objects.filter(hostel='BLOCK A'))).exclude(fee_month=thismonth))
        BLOCKBdues_othermonths=len(MessFee.objects.filter(Q(bal_amount__gt=0) and Q(std_id_id__in=Student.objects.filter(hostel='BLOCK B'))).exclude(fee_month=thismonth))
        BLOCKCdues_othermonths=len(MessFee.objects.filter(Q(bal_amount__gt=0) and Q(std_id_id__in=Student.objects.filter(hostel='BLOCK C'))).exclude(fee_month=thismonth))
        Nursingdues_othermonths=len(MessFee.objects.filter(Q(bal_amount__gt=0) and Q(std_id_id__in=Student.objects.filter(hostel='NURSING HOSTEL'))).exclude(fee_month=thismonth))
        Fatimazehradues_othermonths=len(MessFee.objects.filter(Q(bal_amount__gt=0) and Q(std_id_id__in=Student.objects.filter(hostel='FATIMA ZEHRA'))).exclude(fee_month=thismonth))


        context = {
            'count': count,
            'bjrc_student': bjrc_student,
            'current_user': current_user,
            'apj': apj,
            'block_a': block_a,
            'block_b': block_b,
            'block_c': block_c,
            'nursing': nursing,
            'fatima_zehra': fatima_zehra,
            'total_payments':total_payments,
            'BJRC_payments':BJRC_payments,
            'APJ_payments':APJ_payments,
            'BLOCKA_payments':BLOCKA_payments,
            'BLOCKB_payments':BLOCKB_payments,
            'BLOCKC_payments':BLOCKC_payments,
            'NURSING_payments':NURSING_payments,
            'fatimazehra_payments':fatimazehra_payments,
            'dues_thismonth':dues_thismonth,
            'BJRCdues_thismonth':BJRCdues_thismonth,
            'APJdues_thismonth':APJdues_thismonth,
            'BLOCKAdues_thismonth':BLOCKAdues_thismonth,
            'BLOCKBdues_thismonth':BLOCKBdues_thismonth,
            'BLOCKCdues_thismonth':BLOCKCdues_thismonth,
            'Nursingdues_thismonth':Nursingdues_thismonth,
            'Fatimazehradues_thismonth':Fatimazehradues_thismonth,
            'dues_othermonths':dues_othermonths,
            'BJRCdues_othermonths':BJRCdues_othermonths,
            'APJdues_othermonths':BJRCdues_othermonths,
            'BLOCKAdues_othermonths':BLOCKAdues_othermonths,
            'BLOCKBdues_othermonths':BLOCKBdues_othermonths,
            'BLOCKCdues_othermonths':BLOCKCdues_othermonths,
            'Nursingdues_othermonths':Nursingdues_othermonths,
            'Fatimazehradues_othermonths':Fatimazehradues_othermonths,


        }
        return render(request, 'adminportal/dashboard.html', context)
    else:
        messages.error(request, 'You are not authorized to access!')
        return redirect("login")



def addstudent(request):
    if request.user.is_staff:
        if request.POST:
            name = request.POST['name'].capitalize()
            email = request.POST['email']
            to_email=[email]
            phone_num = int(request.POST['phone_num'])
                                    #DEfault passs for accounts
            default_pass='@'+str(phone_num)
            hostel = request.POST['hostel']
            room_no = request.POST['room_no']
            form = addstudentdetails(request.POST)
            if form.is_valid():
                check_existing = Student.objects.filter(
                    phone_num=phone_num) or Student.objects.filter(email=email).exists() or User.objects.filter(username=str(phone_num)).exists()
                if check_existing:
                    messages.success(request, f'{email} or {phone_num} already registered!!')
                    return redirect('addstudent')
                else:
                    user = User.objects.create_user(username=str(phone_num),
                                    email=email,
                                    password=default_pass)
                    user.save()
                    user=User.objects.get(username=str(phone_num))
                    new_std = Student(user_id=user.pk,name=name, phone_num=phone_num,
                        email=email, hostel=hostel, room_no=room_no)
                    new_std.save()
                    subject = f"Registration in Mess BGSBU"
                    message = f"Hi {name}\nYou have been successfully registered!\nlogin details\n username: {email}\n Pass:{default_pass}"
                    mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, to_email)
                    mail.send()
                    messages.success(request, f'{name} Successfully added!')
                    return redirect('addstudent')
        else:
            form = addstudentdetails()
            recent_stds=Student.objects.order_by('-id')[:10]
        return render(request, 'adminportal/addstudent.html', {'form': form,'recent_stds':recent_stds})
    else:
        messages.error(request, 'You are not authorized to access!')
        return redirect("login")



@login_required
def view_students(request):
    if request.user.is_staff:
        if 'q' in request.GET:
            q = request.GET['q']
            page_obj = Student.objects.filter(
                name__icontains=q,) | Student.objects.filter(phone_num=q).values() | Student.objects.filter(hostel__icontains=q).values()
            page_num = request.GET.get('page', 1)
            paginator = Paginator(page_obj, 10)  # 6 employees per page

            return render(request, 'adminportal/viewstudent.html', {'page_obj': page_obj})
        else:
            students_list = Student.objects.all().order_by('-id')
            page_num = request.GET.get('page', 1)
            paginator = Paginator(students_list, 8)  # 6 employees per page

            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                # if page is not an integer, deliver the first pag
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)

            return render(request, 'adminportal/viewstudent.html', {'page_obj': page_obj})
    else:
        messages.error(request, 'You are not authorized to access!')
        return redirect("login")

@login_required
def ViewPayments(request):
    if request.user.is_staff:        
        if 'q' in request.GET:
            q = request.GET['q']
            page_obj = MessFee.objects.filter(Q(std_id_id__in=Student.objects.filter(name__icontains=q)) or Q(reciept_id=q))
            page_num = request.GET.get('page', 1)
            paginator = Paginator(page_obj, 10)  #10 payments per page
            return render(request, 'adminportal/viewpayments.html', {'page_obj': page_obj})
        else:
            payments_all = MessFee.objects.all().order_by('-trans_id')
            page_num = request.GET.get('page', 1)
            paginator = Paginator(payments_all, 10)  # 10 payemnts per page
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                # if page is not an integer, deliver the first pag
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)

            return render(request, 'adminportal/viewpayments.html', {'page_obj': page_obj})
    else:
        messages.error(request, 'You are not authorized to access!')
        return redirect("login")

@login_required
def edit(request, pk):
    if request.user.is_staff:
        edit_std=get_object_or_404(Student,pk=pk)
        user_std=get_object_or_404(User,id=edit_std.user_id)
        if request.method== 'GET':
            form=EditStudent(instance=edit_std)
            recent_stds=Student.objects.order_by('-id')[:10]
            return render(request, "adminportal/editstudent.html", {'recent_stds':recent_stds,'form':form})
        elif request.method== 'POST':
            try:
                form=EditStudent(request.POST or None,request.FILES or None ,instance=edit_std)
                if form.is_valid():
                    form.save()
                    user_std.username= str(request.POST['phone_num'])
                    user_std.email=request.POST['email']
                    user_std.save()
                    messages.success(request, f'Details updated for {edit_std.name} Successfully!')
                    return redirect('view-students')
                else:
                    check_existing = Student.objects.filter(phone_num=edit_std.phone_num) or Student.objects.filter(email=request.POST['id_phone_num']).exists() or  User.objects.filter(username=str(request.POST['id_phone_num'])).exists()
                    if check_existing:
                        messages.error(request,f'{edit_std.email} or {edit_std.phone_num} already registered!')
                        return redirect('editstudent',pk)

            except Exception as e:
                    messages.error(request,'Oops Something went wrong!')
                    return redirect('editstudent',pk)
                
    else:
        messages.error(request, 'You are not authorized to access!')
        return redirect("login")


@login_required
def PayView(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = PayementForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, f'Payment Successfull')
                return redirect('payfee')
        else:
            form = PayementForm()
            recent_pays=MessFee.objects.order_by('-trans_id')[:10]
            return render(request, 'adminportal/pay.html', {'form': form,'recent_pays':recent_pays})
    else:
        messages.error(request, 'You are not authorized to access!')
        return redirect("login")


@login_required
def PayDirect(request, pk):
    if request.user.is_staff:
        pay_std = get_object_or_404(Student, pk=pk)
        if request.method == 'GET':
            return render(request, 'adminportal/paydirect.html', {'pay_std': pay_std})
        else:
            form = PayementForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, f'Payment Successfull')
                return redirect('payfee')
    else:
        messages.error(request, 'You are not authorized to access!')
        return redirect("login")

@login_required
def menuview(request):
    if request.user.is_staff:
        if request.method == 'GET':
            form=MenuForm()
            return render(request, 'adminportal/messmenu.html', {'form':form})
        else:
            redirect('dashboard')
    else:
        messages.error(request, 'You are not authorized to access!')
        return redirect("login")





def invoice(request, std_id,trans_id):
    if request.user.is_staff:
        Current_std=Student.objects.get(id=std_id)
        Current_payement=MessFee.objects.get(trans_id=trans_id)
        company_details= Company.objects.get(id=1)
        Current_payement.fee_month=Current_payement.fee_month+'-01'
        fee_month = datetime.strptime(Current_payement.fee_month, '%Y-%m-%d').date()
        fee_month=fee_month.strftime('%B ,%Y')
        pay_date=Current_payement.Pay_date.strftime("%d-%b-%Y, %H:%M:%S %p")
        data={
                'std_name':Current_std.name,
                'std_id':Current_std.id,
                'std_email':Current_std.email,
                'std_hostel':Current_std.hostel,
                'std_profile':Current_std.profilepic,
                'payment_fee_month':fee_month,
                'payment_paid_amount':Current_payement.paid_amount,
                'payment_bal_amount':Current_payement.bal_amount,
                'payment_reciept_id':Current_payement.reciept_id,
                'c_Company_name':company_details.Company_name,
                'c_Owner_Phonenum':company_details.Owner_Phonenum,
                'c_email':company_details.Company_email,
                'c_Address':company_details.Address,
                'c_signature':company_details.signature,
                'c_image':company_details.image,
                'payment_pay_date':pay_date,
                
        }
        return render(request,'adminportal/invoice.html',data)
    else:
        messages.error(request, 'You are not authorized to access!')
        return redirect("login")
    # html_template = get_template('adminportal/invoice.html')
    # pdf_file = HTML(string=html_template).write_pdf()
    # response = HttpResponse(pdf_file, content_type='application/pdf')
    # response['Content-Disposition'] = 'filename="home_page.pdf"'
    # return response


# for generating pdf invoice



def pdf(request, std_id,trans_id,*args, **kwargs):
    if request.user.is_staff:
        try:
                Current_std=Student.objects.get(id=std_id)
                Current_payement=MessFee.objects.get(trans_id=trans_id)
                company_details= Company.objects.get(id=1)
                Current_payement.fee_month=Current_payement.fee_month+'-01'
                fee_month = datetime.strptime(Current_payement.fee_month, '%Y-%m-%d').date()
                fee_month=fee_month.strftime('%B ,%Y')
                pay_date=Current_payement.Pay_date.strftime("%m/%d/%Y, %H:%M:%S")

        except:
            return HttpResponse("505 Not Found")
        data={
                'std_name':Current_std.name,
                'std_id':Current_std.id,
                'std_email':Current_std.email,
                'std_hostel':Current_std.hostel,
                'std_profile':Current_std.profilepic,
                'payment_fee_month':fee_month,
                'payment_paid_amount':Current_payement.paid_amount,
                'payment_bal_amount':Current_payement.bal_amount,
                'payment_reciept_id':Current_payement.reciept_id,
                'c_Company_name':company_details.Company_name,
                'c_Owner_Phonenum':company_details.Owner_Phonenum,
                'c_email':company_details.Company_email,
                'c_Address':company_details.Address,
                'c_signature':company_details.signature,
                'c_image':company_details.image,
                'MEDIA_ROOT':MEDIA_ROOT,
                'payment_pay_date':pay_date,
                
            }
        template_path='adminportal/invoice3.html'
        pdf_html = render_to_string(template_path, data)
        pdf_file = HTML(string=pdf_html,base_url=request.build_absolute_uri()).write_pdf(presentational_hints=True)

        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'filename="mypdf.pdf"'
        email=[data['std_email']]

        subject = f"Invoice from {data['c_Company_name']}"
        message = f"Invoice for month {data['payment_fee_month']}"
        mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, email)
        mail.attach('mypdf.pdf', pdf_file, 'application/pdf')
    
        try:
            mail.send(fail_silently = False)
            return HttpResponse("Mail Sent")
        except:
            return HttpResponse("Mail Not Sent")

    else:
        messages.error(request, 'You are not authorized to access!')
        return redirect("login")
        # return response

