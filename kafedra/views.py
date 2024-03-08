from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from partners.models import Offers
from .forms import LoginForm

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
                    return redirect('/auth_kafedra/profile_kafedra')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'kafedra/auth.html', {'form': form})


@login_required
def profile(request):
    print(request.user.is_authenticated)
    print(request.user.username)

    data = Offers.objects.all()

    return render(request, 'kafedra/profile.html', {"data":data})
