from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.contrib.auth.models import User
from student.models import Resume
from .models import Offers

# Create your views here.
def auth(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/auth_partners/profile_part')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'partners/auth.html', {'form': form})

@login_required
def profile_part(request):
    print(request.user.is_authenticated)
    print(request.user.username)

    data = Resume.objects.all()

    if request.method == 'POST':
        print(request.user.username)
        print(request.POST.get('usernamestud'))

        company = User.objects.get(username=request.user.username)
        student = User.objects.get(username=request.POST.get('usernamestud'))

        if not Offers.objects.filter(company=company, student=student).exists():
            print("НАДО СОЗДАТЬ")
            Offers.objects.create(company=company, student=student, send=True)
            resume_data = Resume.objects.get(student_id=student)
            resume_data.resume_send = True
            resume_data.save()

    return render(request, 'partners/profile.html', {'data':data, "offers":Offers.objects.all()})
