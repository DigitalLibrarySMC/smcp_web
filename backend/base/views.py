from django.shortcuts import render, redirect, get_object_or_404
from  .forms import familyform, personform, bcc_unitform
from .models import bcc_unit, family, person, parishpreist
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q



def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST' :
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not Exists")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')
             

    context = {'page': page}
    return render(request, 'base/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')


def home(request):
    return render(request, 'base/home.html')

def parishdirectory(request):
    units = bcc_unit.objects.all().order_by('unitnumber')
    context = {'units':units}
    return render(request,'base/parishdirectory.html', context)


@login_required(login_url='login')
def addbcc_unit(request):
    form  = bcc_unitform()
    if request.method == 'POST':
        form = bcc_unitform(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
    context = {'form': form}
    return render(request, 'base/form.html', context)


@login_required(login_url='login')
def addfamily(request):
    form  = familyform()
    if request.method == 'POST':
        form = familyform(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
    context = {'form': form}
    return render(request, 'base/form.html', context)


@login_required(login_url='login')
def addperson(request):
    form  = personform()
    if request.method == 'POST':
        form = personform(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
    context = {'form': form}
    return render(request, 'base/form.html', context)

def unitpage(request, pk):
    unit = get_object_or_404(bcc_unit, unitnumber=pk)
    familys = family.objects.filter(unitnumber=unit).order_by('familynumber')
    context = {'unit': unit, 'familys': familys}
    return render(request, 'base/unitpage.html', context)
        
def familypage(request, pk):
    fam=family.objects.get(familynumber=pk)
    context = {'fam':fam}
    return render(request, 'base/familypage.html', context )

def searchperson(request):
    cat = request.POST.get('cat')
    q= request.POST.get('q') if request.POST.get('q') != None else ''
    if cat == 'name':
        persons = person.objects.filter(name__icontains=q)
    elif cat == 'occupation':
        persons = person.objects.filter(occupation__icontains=q)
    elif cat == 'age':
        persons = person.objects.filter(age__icontains=q)
    elif cat == 'familynumber':
        persons = person.objects.filter(familynumber__familynumber__icontains=q)

    elif cat=='age less than':
        persons= person.objects.filter(age__lt=q)
    elif cat =='age greater than':
        persons= person.objects.filter(age__gt=q)
    
    else:
        persons =person.objects.filter(
            Q(name__icontains=q) |
            Q(occupation__icontains=q) |
            Q(age__icontains=q) 
        )
    context = {'persons':persons,'cat':cat}
    return render(request,'base/searchperson.html',context)
      

def aboutchurch(request):
    page='aboutchurch'
    with open('G:\\Documents\\GitHub\\smcp_web\\backend\\static\\text\\holyservice', 'r') as file:
        holyservice = file.readlines()

    context = {'holyservice': holyservice,'page':page}
    return render(request, 'base/aboutchurch.html', context)

def parishpriests(request):
    page = 'parishpriests'
    parishpriests = parishpreist.objects.all()
    context = {'parishpriests':parishpriests,'page':page}
    return render(request,'base/aboutchurch.html',context)