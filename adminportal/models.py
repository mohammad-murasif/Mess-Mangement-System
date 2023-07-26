from django.db import models
from django.core.validators import RegexValidator
from ckeditor.fields import RichTextField
from PIL import Image
from django.contrib.auth.models import  User





class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Student Name",max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="Enter phone number without +91")
    phone_num = models.CharField(validators=[phone_regex], max_length=112, blank=False, unique=True) # Validators should be a list
    email= models.EmailField(verbose_name="Email",max_length=255,blank=False,unique=True,null=False)
    hostel= models.CharField(verbose_name="Hostel Name",max_length=100)
    room_no=models.IntegerField(verbose_name="Room No.")
    profilepic= models.ImageField(default='assets/profilepics/default.jpg',upload_to='assets/profilepics',verbose_name='profile')
    def save(self, *args,**kwargs):
        super().save(*args,**kwargs)

        img=Image.open(self.profilepic.path)

        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.profilepic.path)    

    def __str__ (self):

        return " %s" %(self.name )



class MessFee(models.Model):
    trans_id=models.AutoField(primary_key=True ,verbose_name="Transaction ID")
    std_id=models.ForeignKey(Student,verbose_name="Student ID",on_delete=models.PROTECT)
    reciept_id=models.IntegerField(verbose_name="Reciept ID",unique=True,null=False,blank=False)
    paid_amount=models.IntegerField(verbose_name="Amount Paid",blank=False,default=0)
    bal_amount=models.IntegerField(verbose_name="Balance",default=0)
    Pay_date = models.DateTimeField(verbose_name="Payment",auto_now=True)
    fee_month=models.CharField(blank=False, null=False, max_length=255)
    end_date=models.CharField(blank=False, null=False , max_length=255)
    def __str__ (self):

        return "Reciept ID: %s , Student ID.: %s" %(self.pk,self.std_id )


class MessMenu(models.Model):
    monday=models.TextField()
    tuesday=RichTextField()
    wednesday=RichTextField()
    thursday=RichTextField()
    friday=RichTextField()
    saturday=RichTextField()
    sunday=RichTextField()



    def __str__ (self):

        return "ID: %s " %(self.pk)

class Updates(models.Model):
    id=models.AutoField(primary_key=True ,verbose_name="ID")
    heading=models.TextField(blank=False)
    text=models.TextField(blank=False)


    def __str__(self):
        return "ID: %s Heading:%s"%(self.id,self.heading)

class Person(models.Model):
    name = models.CharField(max_length=100)
    marks = models.CharField(max_length=100)


class Company(models.Model):
    Company_name=models.CharField(blank=False,verbose_name="Company Name",max_length=255)
    Address=models.CharField(blank=False,verbose_name="Address",max_length=255)
    Owner_name=models.CharField(blank=False,verbose_name="owner Name",max_length=255)
    Owner_Phonenum=models.CharField(blank=False,verbose_name="Phone Num",max_length=15)
    telephone=models.CharField(verbose_name="Telephone",max_length=20,blank=True)
    Company_email= models.EmailField(verbose_name="Email",max_length=255 ,blank=True)
    website= models.CharField(verbose_name="Website",max_length=255 ,blank=True)
    image= models.ImageField(default='assets/logo.jpg',upload_to='assets',verbose_name='logo')
    signature= models.ImageField(default='assets/signatureDef.png',upload_to='assets', verbose_name='Signature')
    def save(self, *args,**kwargs):
        super().save(*args,**kwargs)

        img=Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


    def __str__(self):
        return "Owner: %s"%(self.Owner_name)



