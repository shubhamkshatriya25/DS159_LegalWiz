from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *
from .models import NodalOfficer, Invoice, Advocate
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

#home page
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'aboutUs.html')


def signIn(request):

    if request.user.is_authenticated:
        return redirect('/admin')
    elif request.session.get('officer', False):
        return render(request,'Nodal_Officer/Dashboard.html')
    elif request.session.get('admin', False):
        return render(request,'Dashboard.html')
    else: 
        officer = NodalOfficer.objects.all()
        admin = Admin.objects.all()
        args = {
            'officer': officer,
            'admin': admin,
        }
        return render(request,'sign-in.html',args)

def submit(request):
    userID = request.POST['UserID']
    password = request.POST['pwd']
    dept = request.POST['dept']
    dic = {}
    officer = NodalOfficer.objects.get(userID=userID)
    if officer.password == password and officer.department == dept:
        request.session['officer'] = userID
        return render(request,'Nodal_Officer/Dashboard.html')
    else:
        dic['failure'] = True
        return render(request,'sign-in.html',dic)
   

def adminlogin(request):
    userID = request.POST['UserID']
    password = request.POST['pwd']
    dept = request.POST['dept']
    dic = {}
    admin = Admin.objects.get(userID=userID)
    if admin.password == password and admin.department == dept:
        request.session['admin'] = userID
        return render(request,'Dashboard.html')
    else:
        dic['failure'] = True
        return render(request,'sign-in.html',dic)
    # userID = request.POST['UserID']
    # password = request.POST['pwd']
    # dic = {}
    # user = auth.authenticate(username=userID,password=password)
    # if user is not None:
    #     login(request,user)
    #     return redirect('/admin')
    # else:
    #     dic['failure'] = True
    #     return render(request,'sign-in.html',dic)

def secretarylogin(request):
    userID = request.POST['UserID']
    password = request.POST['pwd']
    dic = {}
    user = auth.authenticate(username=userID,password=password)
    if user is not None:
        login(request,user)
        return redirect('/admin')
    else:
        dic['failure'] = True
        return render(request,'sign-in.html',dic)


def logout_view(request):
    logout(request)
 
def forgetpassword(request):
    return render(request,'reset-password.html')

def verifyaccount(request):
    username = request.POST['Username']
    email = request.POST['Email']
    dic = {}
    if User.objects.filter(username = username, email = email).exists():
        user =  User.objects.filter(username = username)
        return render(request,'change-password.html',{'account': user})
    else:
        dic['failure'] = True
        return render(request,'reset-password.html',dic)


def resetpassword(request):
    pass1 = request.POST['Password']
    pass2 = request.POST['ConfirmPassword']
    username = request.POST['Username']
    if pass1 == pass2:
        user = User.objects.get(username=username)
        user.set_password(pass1)
        user.save()
        subject = 'LegalWiz account password reset'
        message = 'Hello User, Your password has been reset.If this was you, then you can safely ignore this email. If this was not you, your account has been compromised. Please reset your password.Thanks, The LegalWiz team.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]
        send_mail(subject, message, email_from, recipient_list)
        return redirect('/sign-in')
    else:
        dic = {
            'failure': True,
            'account': User.objects.filter(username = username),
        }
        return render(request,'change-password.html',dic)


def advocates(request):
    if request.session.get('officer', False):
        advocates = Advocate.objects.all()
        length = len(advocates)
        return render(request,'Nodal_Officer/Advocate.html',{'advocates':advocates, 'length':length})
    else:
        return redirect('/')

def Dashboard(request):
    if request.session.get('officer', False):
        return render(request,'Nodal_Officer/Dashboard.html')

def addAdvocate(request):
    if request.session.get('officer', False):
        return render(request,'Nodal_Officer/addAdvocate.html')

def logout(request):
    if request.session.get('officer', False):
        del request.session['officer']
        return redirect('/')
    if request.session.get('admin', False):
        del request.session['admin']
        return redirect('/')

def hearing(request):
    if request.session.get('officer', False):
        if request.POST.get('filter', False):
            ctitle = request.POST.get('casetitle', False)
            caseno = request.POST.get('caseno', False)
            clast = request.POST.get('lastdate', False)
            if ctitle or caseno or clast:
                if ctitle and caseno and clast:
                    hear = Hearing.objects.filter(title=ctitle, case_no=caseno, lastHearing=clast)
                    fil = len(hear)
                elif ctitle and caseno:
                    hear = Hearing.objects.filter(title=ctitle, case_no=caseno)
                    fil = len(hear)
                elif ctitle and clast:
                    hear = Hearing.objects.filter(title=ctitle, lastHearing=clast)
                    fil = len(hear)
                elif caseno and clast:
                    hear = Hearing.objects.filter(case_no=caseno, lastHearing=clast)
                    fil = len(hear)              
                elif caseno:
                    hear = Hearing.objects.filter(case_no=caseno)
                    fil = len(hear)
                elif clast:
                    hear = Hearing.objects.filter(lastHearing=clast)
                    fil = len(hear)
                elif ctitle:
                    hear = Hearing.objects.filter(title=ctitle)
                    fil = len(hear)
        
            return render(request,'Nodal_Officer/Hearing.html',{'hear':hear, 'fil':fil})
            
        else :
            hear = Hearing.objects.all()
            length = len(hear)

            args = {'hear': hear,
                    'length': length }
    
            return render(request, 'Nodal_Officer/Hearing.html', args)
    else:
        return redirect('/')

def addHearing(request):
    if request.session.get('officer', False):
        if request.POST.get('clear', False) :
            return render(request, 'Nodal_Officer/addHearing.html')
   
    
        elif request.POST.get('submit', False) :
        
            a1 = request.POST.get('caseno', False)
            a2 = request.POST.get('casetitle', False)
            a3 = request.POST.get('casedpt', False)
            a4 = request.POST.get('lastdate', False)
            a5 = request.POST.get('conclusion', False)
            a6 = request.POST.get('nextdate', False)
              
        
    
            if a1 and a2 and a3 and a4 and a5 and a6:
                hear = Hearing()
                hear.case_no = a1
                hear.title = a2
                hear.department = a3
                hear.lastHearing = a4
                hear.conclusion = a5
                hear.nextHearing =a6
            
          
                hear.save()
                
                # return render(request, 'Nodal_Officer/Hearing.html')
                hear = Hearing.objects.all()
                length = len(hear)

                args = {'hear': hear,
                    'length': length }
    
                return render(request, 'Nodal_Officer/Hearing.html', args)

            else:
                dic = {}
                dic['failure'] = True
                return render(request, 'Nodal_Officer/addHearing.html', context = dic)

        else:
            return render(request, 'Nodal_Officer/addHearing.html')

def createAdvocate(request):
    if request.session.get('officer', False):
        name = request.POST['LawyerName']
        email = request.POST['LawyerEmail']
        contact = request.POST['LawyerContact']
        workarea = request.POST['LawyerWorkarea']
        aor = request.POST['LawyerAOR']

        advocate = Advocate()
        advocate.name=name
        advocate.email=email
        advocate.contact=contact
        advocate.workarea=workarea
        advocate.aor=aor
        advocate.save()
        return redirect('/Dashboard/advocates')
    else:
       return redirect('/') 

def advocatefilter(request):
    name = request.POST['Filter-name']
    email = request.POST['Filter-email']
    contact = request.POST['Filter-contact']
    if name or email or contact:
        if name and email and contact:
            advocates = Advocate.objects.filter(name=name,email=email,contact=contact)
            fil = len(advocates)
        elif name and email:
            advocates = Advocate.objects.filter(name=name,email=email)
            fil = len(advocates)
        elif name and contact:
            advocates = Advocate.objects.filter(name=name,contact=contact)
            fil = len(advocates)
        elif contact and email:
            advocates = Advocate.objects.filter(contact=contact,email=email)  
            fil = len(advocates)  
        elif email:
            advocates = Advocate.objects.filter(email=email)
            fil = len(advocates)
        elif contact:
            advocates = Advocate.objects.filter(contact=contact)
            fil = len(advocates)
        elif name:
            advocates = Advocate.objects.filter(name=name)
            fil = len(advocates)
        
        return render(request,'Nodal_Officer/Advocate.html',{'advocates':advocates, 'fil':fil})
    else:
        advocates = Advocate.objects.all()
        length = len(advocates)
        return render(request,'Nodal_Officer/Advocate.html',{'advocates':advocates, 'length': length})
    
def invoice(request):  
    
    #for filter invoice
    if request.session.get('officer', False):
        if request.POST.get('filter', False):
            advocate = request.POST.get('fil_ad', False)
            caseno = request.POST.get('fil_case', False)
            lcno = request.POST.get('fil_lc', False)
            if advocate or caseno or lcno:
                if advocate and caseno and lcno:
                    invoice = Invoice.objects.filter(ad_na=advocate, caseno=caseno, lcno=lcno)
                    fil = len(invoice)
                elif advocate and caseno:
                    invoice = Invoice.objects.filter(ad_na=advocate, caseno=caseno)
                    fil = len(invoice)
                elif advocate and lcno:
                    invoice = Invoice.objects.filter(ad_na=advocate, lcno=lcno)
                    fil = len(invoice)
                elif caseno and lcno:
                    invoice = Invoice.objects.filter(caseno=caseno, lcno=lcno)
                    fil = len(invoice)              
                elif caseno:
                    invoice = Invoice.objects.filter(caseno=caseno)
                    fil = len(invoice)
                elif lcno:
                    invoice = Invoice.objects.filter(lcno=lcno)
                    fil = len(invoice)
                elif advocate:
                    invoice = Invoice.objects.filter(ad_na=advocate)
                    fil = len(invoice)
        
                return render(request,'Nodal_Officer/Invoice.html',{'invoice':invoice, 'fil':fil})
        
     #view more button
        elif request.POST.get('view', False) :
        
            val = request.POST.get('view', False)
            #print(val)
            invoice = Invoice.objects.all()
        
            args = { 'invoice': invoice,
                'val': val}
        
            return render(request, 'viewmore.html', args)
    
        else:
            invoice = Invoice.objects.all()
            length = len(invoice)
  
            args = {'invoice': invoice,
                    'length': length }
    
            return render(request, 'Nodal_Officer/Invoice.html', args)
    


def addinvoice(request):
    
    if request.session.get('officer', False):
        if request.POST.get('clear', False) :
            return render(request, 'Nodal_Officer/invoiceForm.html')
   
    
        elif request.POST.get('submit', False) :
        
            a1 = request.POST.get('in_date', False)
            a2 = request.POST.get('in_sub', False)
            a3 = request.POST.get('dept', False)
            a4 = request.POST.get('caseno', False)
            a5 = request.POST.get('lcno', False)
            a6 = request.POST.get('ad_na', False)
            a7 = request.POST.get('casetitle', False)
            a8 = request.POST.get('casetype', False)
            a9 = request.POST.get('in_particulars', False)
            a10 = request.POST.get('in_total', False)
            a11= request.POST.get('in_due', False)        
        
    
            if a1 and a2 and a3 and a4 and a5 and a6 and a7 and a8 and a9 and a10 and a11:
                voice = Invoice()
                voice.in_date = a1
                voice.in_sub = a2
                voice.dept = a3
                voice.caseno = a4
                voice.lcno = a5
                voice.ad_na = a6
                voice.casetitle = a7
                voice.casetype = a8
                voice.in_particulars = a9
                voice.in_total = a10
                voice.in_due = a11
          
                voice.save()
                # invoice = Invoice.objects.all()
        
                # args = { 'invoice': invoice}
                # return render(request, 'Nodal_Officer/Invoice.html',args)
                return redirect('/Dashboard/invoice')

            else:
                dic = {}
                dic['failure'] = True
                return render(request, 'Nodal_Officer/invoiceForm.html', context = dic)

        else:
            return render(request, 'Nodal_Officer/invoiceForm.html')

def cases(request):
    if request.POST.get('filter',False):
        caseno = request.POST.get('filter-caseno',False)
        lcno = request.POST.get('filter-lcno',False)
        nh = request.POST.get('filter-nh',False)
        if caseno or lcno or nh:
            if caseno and lcno and nh:
                case = AddCases.objects.filter(case_number=caseno,lc_number=lcno,next_hearing_date=nh)
                fc = len(case)
            elif caseno and lcno:
                case = AddCases.objects.filter(case_number=caseno,lc_number=lcno)
                fc = len(case)
            elif caseno and nh:
                case = AddCases.objects.filter(case_number=caseno,next_hearing_date=nh)
                fc = len(case)
            elif nh and lcno:
                case = AddCases.objects.filter(next_hearing_date=nh,lc_number=lcno)   
                fc = len(case) 
            elif lcno:
                case = AddCases.objects.filter(lc_number=lcno)
                fc = len(case)
                print(fc)
            elif nh:
                case = AddCases.objects.filter(next_hearing_date=nh)
                fc = len(case)
            elif caseno:
                case = AddCases.objects.filter(case_number=caseno)
                fc = len(case)
               
            return render(request,'Nodal_Officer/Cases.html',{'case':case,'fc':fc})

    elif request.POST.get('we', False) :
        val = request.POST.get('we', False)
       
        print(val)
        viewmore = AddCases.objects.all()
        args = { 'viewmore': viewmore,
                'val': val}
        return render(request, 'viewmorecase.html', args)
    else:
        case=AddCases.objects.all()
        length=len(case)
        args={"case":case,"length":length}
        return render(request,'Nodal_Officer/Cases.html',args)
        

# def viewmore(request):
#     if request.session.get('officer',False):
#         return render(request,'viewmore.html')

   

def addcase(request):
    if request.session.get('officer',False):
        if request.POST.get('cancel',False):
            return render(request,'Nodal_Officer/Cases.html')
        elif request.POST.get('save',False):
            typeofcourt= request.POST.get('typeofcourt',False)
            typeofcase= request.POST.get('typeofcase',False)
            casenumber= request.POST.get('casenumber',False)
            caseregistrationdate= request.POST.get('caseregistrationdate',False)
            courtname= request.POST.get('courtname',False)
            subjectmatter= request.POST.get('subjectmatter',False)
            lcnumber= request.POST.get('lcnumber',False)
            section= request.POST.get('section',False)
            pcnumber= request.POST.get('pcnumber',False)
            casereceivingdate= request.POST.get('casereceivingdate',False)
            appearancedateofrespondent= request.POST.get('appearancedateofrespondent',False)
            pwcduedate= request.POST.get('pwcduedate',False)
            duedateoffilling= request.POST.get('duedateoffilling',False)
            title= request.POST.get('title',False)
            prayer= request.POST.get('prayer',False)
            filedbycorporation= request.POST.get('filedbycorporation',False)
            stampno= request.POST.get('stampno',False)
            firstappearanceofpeti= request.POST.get('firstappearanceofpeti',False)
            petitionercounselname= request.POST.get('petitionercounselname',False)
            representedcoordinator= request.POST.get('representedcoordinator',False)
            nexthearingdate=request.POST.get('nexthearingdate',False)
            app_isemployee= request.POST.get('app_isemployee',False)
            app_Name= request.POST.get('app_Name',False)
            app_Address= request.POST.get('app_Address',False)
            app_Contact= request.POST.get('app_Contact',False)
            app_dept= request.POST.get('app_dept',False)
            res_isemployee= request.POST.get('res_isemployee',False)
            res_Name= request.POST.get('res_Name',False)
            res_Address= request.POST.get('res_Address',False)
            res_Contact= request.POST.get('res_Contact',False)
            res_dept= request.POST.get('res_dept',False)
            ass_isprimarydept= request.POST.get('ass_isprimarydept',False)
            ass_dept= request.POST.get('ass_Department',False)
            ass_Assignedto= request.POST.get('ass_Assignedto',False)
            ass_Assignedon= request.POST.get('ass_Assignedon',False)
            ass_Datereceiptpwc= request.POST.get('ass_Datereceiptpwc',False)
            remark= request.POST.get('remark',False)
            standingcounsel= request.POST.get('standingcounsel',False)
            counselassignedon= request.POST.get('counselassignedon',False)
            vakalatnamafilingdate= request.POST.get('vakalatnamafilingdate',False)
            dateoffiling= request.POST.get('dateoffiling',False)
            isseniorcounselrequired= request.POST.get('isseniorcounselrequired',False)
            upload=request.FILES.get('file',False)

            if casenumber and lcnumber:
                add=AddCases()
                add.type_of_court=typeofcourt
                add.type_of_case=typeofcase
                add.case_number=casenumber
                add.case_registration_date=caseregistrationdate
                add.court_name=courtname
                add.subject_matter=subjectmatter
                add.lc_number=lcnumber
                add.section=section
                add.previous_casenumber=pcnumber
                add.case_receiving_date=casereceivingdate
                add.appearance_date_respondent=appearancedateofrespondent
                add.pwc_duedate=pwcduedate
                add.duedate_filing=duedateoffilling
                add.title=title
                add.prayer=prayer
                add.filedby_corporation=filedbycorporation
                add.stamp_no=stampno
                add.first_apperance_petitioner=firstappearanceofpeti
                add.petitioner_counsel_name=petitionercounselname
                add.represented_by_coordinator=representedcoordinator
                add.next_hearing_date=nexthearingdate
                add.app_isemployee=app_isemployee
                add.app_name=app_Name
                add.app_address=app_Address
                add.app_contact=app_Contact
                add.app_dept=app_dept
                add.res_isemployee=res_isemployee
                add.res_name=res_Name
                add.res_address=res_Address
                add.res_contact=res_Contact
                add.res_dept=res_dept
                add.ass_isprimarydept=ass_isprimarydept
                add.ass_dept=ass_dept
                add.ass_assignedon=ass_Assignedon
                add.ass_assignedto=ass_Assignedto
                add.ass_date_receipt_pwc=ass_Datereceiptpwc
                add.remark=remark
                add.standing_counsel=standingcounsel
                add.standingcounsel_assignedon=counselassignedon
                add.vakalatnama_filingdate=vakalatnamafilingdate
                add.date_of_filing_writtenstatement=dateoffiling
                add.standing_counsel_required=isseniorcounselrequired
                add.document=upload
                add.save()
                return render(request,'Nodal_Officer/Dashboard.html')
            else:
                dic={}
                dic['failure'] = True
                return render(request,'Nodal_Officer/addcase.html',context=dic)
        else:
            return render(request,'Nodal_Officer/addcase.html')


