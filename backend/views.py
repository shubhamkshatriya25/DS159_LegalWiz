from django.shortcuts import render,redirect
# Create your views here.

#home page
def index(request):
    return render(request,'index.html')


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
