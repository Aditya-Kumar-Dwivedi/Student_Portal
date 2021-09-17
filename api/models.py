from django.db import models


# Create your models here.

class Student(models.Model):
    username=models.TextField(max_length=50, default="",null=False,unique=True)
    password=models.TextField(max_length=40,null=False,unique=False)
    Name=models.CharField(max_length=50,default="",null=False,unique=False)
    photo=models.ImageField(upload_to="api/images",default="")
    DateOfBirth=models.DateField(null=True)
    Contact=models.IntegerField(default=0,null=False)
    AlternateContact=models.IntegerField(default=0)
    Branch=models.TextField(default='')
    Programme=models.TextField(default='')
    Category=models.TextField(default='')
    SubCategory=models.TextField(default='')
    IdentificationMark=models.TextField(default='')
    FeeWaiver=models.TextField(default='')
    EntranceExam=models.TextField(default='')
    YearOfEntranceExam=models.IntegerField(default=0)
    ApplicationNo=models.IntegerField(default=0)
    AIRRank=models.IntegerField(default=0)
    CategoryRank=models.IntegerField(default=0)
    Gender=models.TextField(default='')
    RollNo=models.IntegerField(default=1)
    EnrollmentNumber=models.CharField(max_length=20,default='')
    AdmissionSource=models.CharField(max_length=15,default="JEE MAINS")
    Nationality=models.CharField(max_length=10,default="",null=False)
    Religion=models.CharField(max_length=10,default='')
    Hosteler=models.BooleanField(default='True')
    ModeOfTransport=models.CharField(max_length=10,default='')
    Email=models.EmailField(default='')
    OfficialEmail=models.EmailField(default='')
    BloodGroup=models.CharField(max_length=10,default='',null=True)
    Aadhaar=models.IntegerField(default=1,null=False)
    Fathername=models.CharField(max_length=50,default='',null=False)
    Mothername=models.CharField(max_length=50,default='',null=False)
    FatherContact=models.IntegerField(default=1)
    FatherMail=models.EmailField(default='')



    def __str__(self):
        return self.username

class StoredSessions(models.Model):
    key = models.CharField(unique=True,max_length=50,null=False,default="")
    username = models.TextField(max_length=50, default="",null=False)
