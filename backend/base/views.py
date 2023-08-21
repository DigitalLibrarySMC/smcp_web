from django.shortcuts import render, redirect, get_object_or_404
from  .forms import familyform, personform, bcc_unitform,SignUpForm
from .models import bcc_unit, family, person, parishpreist, parishcouncil, phoneno,CustomUser
from results.models import Result
from quizes.models import Quiz
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q, Max
import phonenumbers

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)

            # Process the uploaded profile picture
            profile_picture = form.cleaned_data['avatar']
            if profile_picture:
                user.avatar = profile_picture
            user.phone_number = form.cleaned_data['phone_number']

            user.save()

            # Log the user in
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'base/form.html', {'form': form})

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = CustomUser.objects.get(username=username)
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Username OR password is incorrect')
        except CustomUser.DoesNotExist:
            messages.error(request, "User does not exist")

    context = {'page': page}
    return render(request, 'base/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def home(request):
    with open('static\\text\\notifications', 'r') as file:
        lines = file.readlines()
    return render(request, 'base/home.html',{'lines':lines})

def parishdirectory(request):
    units = bcc_unit.objects.all().order_by('unitnumber')
    with open('static\\text\\notifications', 'r') as file:
        lines = file.readlines()
    context = {'units':units,'lines':lines}
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

    elif cat=='age_less_than':
        persons= person.objects.filter(age__lt=q)
    elif cat =='age_greater_than':
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
    with open('static\\text\\holyservice', 'r') as file:
        holyservice = file.readlines()
    with open('static\\text\\notifications', 'r') as myfile:
        lines = myfile.readlines()

    context = {'holyservice': holyservice,'page':page,'lines':lines}
    return render(request, 'base/aboutchurch.html', context)

def parishpriests(request):
    page = 'subabout'
    column1 = 'priestname'
    column2 = 'duration'
    with open('static\\text\\notifications', 'r') as file:
        lines = file.readlines()
    churchdata = parishpreist.objects.all()
    context = {'churchdata':churchdata,'page':page,
               'column1':column1,'column2':column2,'lines':lines}
    return render(request,'base/aboutchurch.html',context)
def council(request):
    page = 'subabout'
    churchdata = parishcouncil.objects.all()
    column1 = 'name'
    column2 = 'desigination'
    column3 = 'phone'
    with open('static\\text\\notifications', 'r') as file:
        lines = file.readlines()
    context = {'churchdata': churchdata, 'page': page,
               'column1':column1,'column2':column2,'column3':column3,'lines':lines}
    return render(request, 'base/aboutchurch.html', context)


def numbers(request):
    page = 'subabout'
    column1 = 'name'
    column2 = 'phone'
    column3 = 'designation'
    churchdata = phoneno.objects.all()
    with open('static\\text\\notifications', 'r') as file:
        lines = file.readlines()
    context = {'churchdata':churchdata,'page':page,
               'column1':column1,'column2':column2,'column3':column3,'lines':lines}
    return render(request,'base/aboutchurch.html',context)

def resultpage(request):
    page = 'resultpage'
    column1 = 'User_Name'
    column2 = 'Quiz'
    column3 = 'Score(%)'
    column4 = 'Time_Taken(seconds)'
    users= CustomUser.objects.all()
    data = {}
    for user in users:
     results = Result.objects.filter(user=user)
     attemptedquiz = {}
     for result in results:
         if result.quiz.name in attemptedquiz.keys():
             scoreandtime = attemptedquiz[result.quiz.name]
             scoreandtime = scoreandtime.split()
             score = float(scoreandtime[0])
             print(score)
             if score < result.score:
                 attemptedquiz[result.quiz.name] = str(result.score)+" "+str(result.time)
         else:
             attemptedquiz[result.quiz.name]=str(result.score)+" "+str(result.time)
     data[user.username] = attemptedquiz
    with open('static\\text\\notifications', 'r') as file:
        lines = file.readlines()
    context = {'data':data,'page':page,'column1':column1,'column2':column2,'column3':column3,'column4':column4,'lines':lines}
    return render(request,'base/resultpage.html',context)

def scoreboard(request):
    page = 'scoreboard'
    column1 = 'User_Name'
    column2 = 'Score'
    users = CustomUser.objects.all()
    data = {}
    for user in users:
        score = 0
        results = Result.objects.filter(user=user)
        for result in results:
            score += result.score
        score = round(score,2)
        data[user.username] = score    
    scores =sorted(data.values(), reverse=True)
    descendingdata = {}
    for score in scores:
        for key,value in data.items():
            if value == score:
                descendingdata[key] = score
    with open('static\\text\\notifications', 'r') as file:
        lines = file.readlines()
    context = {'data':descendingdata,'page':page,'column1':column1,'column2':column2,'lines':lines}
    return render(request,'base/resultpage.html',context)

def notices(request):
        with open('static\\text\\notices\\latest', 'r') as file:
            notices = file.readlines()
        with open('static\\text\\notifications', 'r') as myfile:
            lines = myfile.readlines()
        return render(request, 'base/notices.html',{'notices':notices,'lines':lines})

def history(request):
        with open('static\\text\\history', 'r') as file:
            notices = file.readlines()
        with open('static\\text\\notifications', 'r') as myfile:
            lines = myfile.readlines()
        return render(request, 'base/notices.html',{'notices':notices,'lines':lines})