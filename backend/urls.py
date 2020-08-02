from django.urls import path
from . import views

urlpatterns = [
    # static page urls
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('submit',views.submit,name="submit"),
    path('sign-in',views.signIn,name="signIn"),
]
 
