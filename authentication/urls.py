from django.urls import path
from .import views


urlpatterns=[
    path('',views.index,name='index'),
    path('Home',views.home,name='home'),
    path('Signin',views.Signin,name='Signin'),
    path('Signup',views.Signup,name='Signup'),
    path('Signout',views.Signout,name='Signout'),
    path('Documentation',views.Documentation,name='Documentation'),
    path('Service',views.Services,name='Services'),
    path('contact',views.contact,name='contact'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('Account',views.Account,name='Account'),
    path('Dashboard',views.Dashboard,name='Dashboard'),
]