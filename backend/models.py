from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Admin(models.Model):
    userID      = models.CharField(max_length=30,primary_key=True)
    email       = models.CharField(max_length=30)
    name        = models.CharField(max_length=50)
    contact     = models.CharField(max_length=15)
    department  = models.CharField(max_length=30)
    password    = models.CharField(max_length=50)

    def __str__(self):
        return self.userID 


class NodalOfficer(models.Model):
    userID      = models.CharField(max_length=30,primary_key=True)
    email       = models.CharField(max_length=30)
    name        = models.CharField(max_length=50)
    contact     = models.CharField(max_length=15)
    department  = models.CharField(max_length=30)
    password    = models.CharField(max_length=50)

    def __str__(self):
        return self.userID 
    

class Invoice(models.Model):
    in_date = models.CharField(max_length=20)
    in_sub = models.CharField(max_length=50)
    dept = models.CharField(max_length=50)
    caseno = models.CharField(max_length=50)
    lcno = models.CharField(max_length=50)
    ad_na = models.CharField(max_length=50)
    casetitle = models.CharField(max_length=20)
    casetype = models.CharField(max_length=20)
    in_particulars = models.CharField(max_length=500)
    in_total = models.IntegerField()
    in_due = models.IntegerField()    

class Advocate(models.Model):
    email       = models.CharField(max_length=30)
    name        = models.CharField(max_length=50)
    contact     = models.CharField(max_length=15)
    workarea    = models.CharField(max_length=50)
    aor         = models.CharField(max_length=20) 

    def __str__(self):
        return self.name  

class Hearing(models.Model):
    case_no       = models.CharField(max_length=30)
    title        = models.CharField(max_length=50)
    lastHearing     = models.CharField(max_length=30)
    conclusion    = models.CharField(max_length=150)
    nextHearing         = models.CharField(max_length=30)
    department      = models.CharField(max_length=30)
    def __str__(self):
        return self.case_no



class AddCases(models.Model):
    type_of_court=models.CharField(max_length=50,choices=(
        ("Supreme Court","Supreme Court"),
        ("Junior Division Court","Junior Division Court"),
        ("Senior Division Court","Senior Division Court"),
        ("Consumer Court","Consumer Court"),
        ("Family Court","Family Court"),
        ("Sale Tax Tribunal","Sale Tax Tribunal"),
        ("Additional District Judge Court","Additional District Judge Court")
    ),default="Supreme Court")
       
    type_of_case=models.CharField(max_length=50,
    choices=(
        ("Criminal Case","Criminal Case"),
        ("Property Case","Property Case"),
        ("Divorse Case","Divorse Case"),
        ("Civil Case","Civil Case"),
    ))
    case_number=models.CharField(max_length=50,primary_key=True)
    case_registration_date=models.CharField(max_length=50)
    court_name=models.CharField(max_length=50,
    choices=(
        ("BMC High Court","BMC High Court"),
        ("Junior Court","Junior Court"),
        ("NyayMandir","NyayMandir"),
        ("Lal Court","Lal Court"),
    ))
    subject_matter=models.CharField(max_length=50,
    choices=(
        ("Cheque Bounce Matter","Cheque Bounce Matter"),
        ("Unauthorized Construction","Unauthorized Construction"),
        ("Property Tax Matter","Property Tax Matter"),
        ("Estabhlishment Matter","Estabhlishment Matter"),
        ("Advertisement Matter","Advertisement Matter"),
        ("A.F.A Act","A.F.A Act"),
        ("Against Disimisal 106 Appointment Matter","Against Disimisal 106 Appointment Matter"),
        ("Public Health Related Matter","Public Health Related Matter"),
    ))
    lc_number=models.CharField(max_length=50,unique=True)
    section=models.CharField(max_length=50,
    choices=(
        ("148","148"),
        ("152","152"),
        ("160","160"),
        ("180","180"),
    ))
    previous_casenumber=models.CharField(max_length=50)
    case_receiving_date=models.CharField(max_length=50)
    appearance_date_respondent=models.CharField(max_length=50)
    pwc_duedate=models.CharField(max_length=50)
    duedate_filing=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    prayer=models.CharField(max_length=50)
    filedby_corporation=models.CharField(max_length=3,default="No",
    choices=(
        ("Yes","Yes"),
        ("No","No")
    ))
    stamp_no=models.CharField(max_length=50)
    first_apperance_petitioner=models.CharField(max_length=50)
    petitioner_counsel_name=models.CharField(max_length=50)
    represented_by_coordinator=models.CharField(max_length=50)
    next_hearing_date=models.CharField(max_length=50,default="xx/xx/2020")
    app_isemployee=models.CharField(max_length=3,default="No",
    choices=(
        ("Yes","Yes"),
        ("No","No")
    ))
    app_name=models.CharField(max_length=100)
    app_address=models.CharField(max_length=200)
    app_contact=models.IntegerField()
    app_dept=models.CharField(max_length=50,
    choices=(
        ("Central Railway","Central Railway"),
        ("Ministry of Agriculture","Ministry of Agriculture"),
        ("Urban Development(UD)","Urban Development(UD)"),
        ("Forest Department","Forest Department"),
        ("Department of Home","Department of Home"),
        ("Ministry of Textile","Ministry of Textile"),

    ))
    res_isemployee=models.CharField(max_length=3,default="No",
    choices=(
        ("Yes","Yes"),
        ("No","No")
    ))
    res_name=models.CharField(max_length=100)
    res_address=models.CharField(max_length=200)
    res_contact=models.IntegerField()
    res_dept=models.CharField(max_length=50,
    choices=(
        ("Central Railway","Central Railway"),
        ("Ministry of Agriculture","Ministry of Agriculture"),
        ("Urban Development(UD)","Urban Development(UD)"),
        ("Forest Department","Forest Department"),
        ("Department of Home","Department of Home"),
        ("Ministry of Textile","Ministry of Textile"),
    ))
    ass_isprimarydept=models.CharField(max_length=3,default="No",
    choices=(
        ("Yes","Yes"),
        ("No","No")
    ))
    ass_dept=models.CharField(max_length=50)
    ass_assignedto=models.CharField(max_length=50)
    ass_assignedon=models.CharField(max_length=50)
    
    ass_date_receipt_pwc=models.CharField(max_length=50)
    remark=models.CharField(max_length=500)
    standing_counsel=models.CharField(max_length=50)
    standingcounsel_assignedon=models.CharField(max_length=50)
    vakalatnama_filingdate=models.CharField(max_length=50)
    date_of_filing_writtenstatement=models.CharField(max_length=50)
    standing_counsel_required=models.CharField(max_length=3,default="No",
    choices=(
        ("Yes","Yes"),
        ("No","No")
    ))
    document = models.FileField(null=True,blank=True)

    