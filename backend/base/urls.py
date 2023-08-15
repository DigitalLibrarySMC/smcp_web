from django.urls import path, include
from . import views
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
    path('aboutchurch/parishpriests',views.parishpriests, name='parishpriests'),
    path('aboutchurch/parishcouncil',views.council, name='parishcouncil'),
    path('aboutchurch/numbers',views.numbers, name='numbers'),
    path('results/',views.resultpage, name="resultpage"),
    path('scoreboard/',views.scoreboard, name="scoreboard"),
    path('signup/',views.signup, name='signup'),
    path('quizes/',include('quizes.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)