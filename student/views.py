from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from student.models import Resume
from partners.models import Offers
from .forms import LoginForm
from django.contrib.auth.models import User

# Create your views here

def auth(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/auth_student/profile')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'student/auth.html', {'form': form})


@login_required
def profile(request):
    print(request.user.is_authenticated)
    print(request.user.username)

    print(request.POST.get("information"))
    print(request.POST.get("about"))
    print(request.POST.get("iam"))

    stud = User.objects.get(username=request.user.username)
    data = Resume.objects.all()

    if not Resume.objects.filter(student_id=stud.id).exists():
        if request.method == 'POST':
            Resume.objects.create(student_id=stud, information=request.POST.get("information"), about=request.POST.get("about"), iam=request.POST.get("iam"),
                                  resume_send=False)
            data = Resume.objects.get(student_id=stud.id)
        else:
            data = None
    else:
        if request.method == 'POST':
            new_data = Resume.objects.get(student_id=stud.id)
            new_data.information = information=request.POST.get("information")
            new_data.about = information=request.POST.get("about")
            new_data.iam = information=request.POST.get("iam")
            new_data.save()
        data = Resume.objects.get(student_id=stud.id)


    offers_info = None
    offers_list = None
    if Offers.objects.filter(student=stud.id).exists():
         offers_info = Offers.objects.filter(student=stud.id)
         offers_list = [item for item in offers_info]

    if request.GET.get("accept_offer") == "True" and Offers.objects.filter(student=stud.id).exists():
        buf_company = request.GET.get("company_name")
        print(f"fdsf {buf_company}")
        offers_info = Offers.objects.get(student=stud.id, company=buf_company)
        offers_info.offer_send = True
        offers_info.save()
        offers_info = Offers.objects.filter(student=stud.id)
        offers_list = [item for item in offers_info]

        new_data = Resume.objects.get(student_id=stud.id)
        new_data.resume_accept = True
        new_data.save()

        data = Resume.objects.get(student_id=stud.id)

    elif request.GET.get("accept_offer") == "False" and Offers.objects.filter(student=stud.id).exists():
        buf_company = request.GET.get("company_name")
        print(f"fdsf {buf_company}")
        offers_info = Offers.objects.get(student=stud.id, company=buf_company)
        offers_info.offer_send = False
        offers_info.save()
        offers_info = Offers.objects.filter(student=stud.id)
        offers_list = [item for item in offers_info]

        new_data = Resume.objects.get(student_id=stud.id)
        new_data.resume_accept = False
        new_data.save()

        data = Resume.objects.get(student_id=stud.id)

    return render(request, 'student/profile.html', {'data':data, 'offers_info':offers_list})
