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
    path('adminlogin',views.adminlogin,name="adminlogin"),
    path('secretarylogin',views.secretarylogin,name="secretarylogin"),
 
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

    

    
]
urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
 
