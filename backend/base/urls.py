from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('addbcc_unit',views.addbcc_unit,name='addbcc_unit'),
    path('addfamily',views.addfamily,name='addfamily'),
    path('addperson',views.addperson,name='addperson'),
    path ('parishdirectory',views.parishdirectory,name='parishdirectory'),
    path ('unitpage/<str:pk>',views.unitpage,name='unitpage'),
    path ('familypage/<str:pk>',views.familypage,name='familypage'),
    path('login/',views.loginPage, name='login'),
    path('logout/',views.logoutUser, name='logout'),
    
]