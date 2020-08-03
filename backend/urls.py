from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    # static page urls
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('submit',views.submit,name="submit"),
    path('sign-in',views.signIn,name="signIn"),
    path('submit/forgetpassword',views.forgetpassword,name="forgetpassword"),
    path('submit/resetpassword',views.resetpassword,name="resetpassword"),
    path('submit/verifyaccount',views.verifyaccount,name="verifyaccount"),
    # path('adminlogin',views.adminlogin,name="adminlogin"),
    # path('secretarylogin',views.secretarylogin,name="secretarylogin"),
 
    # Dashboard URLs
    path('logout',views.logout,name="logout"),
    path('Dashboard',views.Dashboard,name="Dashboard"),
    
    path('Dashboard/advocates',views.advocates,name="advocates"), 
    path('Dashboard/advocates/addAdvocate',views.addAdvocate,name="addAdvocate"),
    path('createAdvocate',views.createAdvocate,name="createAdvocate"), 
    path('advocatefilter',views.advocatefilter,name="advocatefilter"),

    path('Dashboard/hearing/addHearing',views.addHearing,name="addHearing"),
    path('Dashboard/hearing',views.hearing,name="hearing"),

    path('Dashboard/invoice',views.invoice,name="invoice"),
    path('Dashboard/invoice/addinvoice',views.addinvoice,name="addinvoice"),

    path('Dashboard/cases',views.cases,name="cases"),
    path('Dashboard/Cases/addcase',views.addcase,name="addcase"),

    path('Dashboard/closecase',views.closecase,name="closecase"),
    path('Dashboard/runningcase',views.runningcase,name="runningcase"),
    path('id/',views.caseidform,name="id"),


    #Admin Dashboard URLs
    path('AdminDashboard',views.AdminDashboard,name="AdminDashboard"),

    path('AdminDashboard/Adminadvocates',views.Adminadvocates,name="Adminadvocates"), 
    path('Adminadvocatefilter',views.Adminadvocatefilter,name="Adminadvocatefilter"),

    path('AdminDashboard/Adminhearing',views.Adminhearing,name="Adminhearing"),

    path('AdminDashboard/Admininvoice',views.Admininvoice,name="Admininvoice"),

    path('AdminDashboard/Admincases',views.Admincases,name="Admincases"),
    path('AdminDashboard/AddNodalOfficer',views.AddNodalOfficer,name="AddNodalOfficer"),
    path('AdminDashboard/AddNodalOfficer/createNodalOfficer',views.createNodalOfficer,name="createNodalOfficer"),

     # Secretary URLs
    path('SecretaryDashboard',views.SecretaryDashboard,name="SecretaryDashboard"),
    path('SecretaryDashboard/Adminlist',views.Adminlist,name="Adminlist"),
    path('SecretaryDashboard/Adminlist/AddAdmin',views.AddAdmin,name="AddAdmin"),
    path('SecretaryDashboard/Adminlist/AddAdmin/createAdmin',views.createAdmin,name="createAdmin")
]
urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
 
