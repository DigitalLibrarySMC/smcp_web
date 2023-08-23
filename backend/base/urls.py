from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
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
    path('searchperson/',views.searchperson,name='searchperson'),
    path('aboutchurch/',views.aboutchurch, name='aboutchurch'),
    path('aboutchurch/history',views.history, name='history'),
    path('aboutchurch/parishpriests',views.parishpriests, name='parishpriests'),
    path('aboutchurch/parishcouncil',views.council, name='parishcouncil'),
    path('aboutchurch/numbers',views.numbers, name='numbers'),
    path('results/',views.resultpage, name="resultpage"),
    path('scoreboard/',views.scoreboard, name="scoreboard"),
    path('notices/',views.notices, name="notices"),
    path('signup/',views.signup, name='signup'),
    path('sentemail/',views.sentemail, name='sentemail'),
    path('quizes/',include('quizes.urls')),
    path('reset_password/',views.CustomPasswordResetView.as_view(template_name='base/registration/password_reset.html'),name='password_reset'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='base/registration/password_reset_sent.html'),name='password_reset_done'), 
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='base/registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='base/registration/password_reset_done.html'),name='password_reset_complete'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)