from django.shortcuts import render
from .register import resume, UserForm, UserProfileInfoForm

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def roverfun(request):
    return render(request, "rover/rovermain.html")

# Create your views here.
def success(request):
    return render(request, "rover/successpage.html")

def rovboost(request):
    instance = resume()

    if request.method == 'POST':
        instance = resume(request.POST)

        if instance.is_valid():
            instance.save(commit=True)
            return success(request)
        else:
            print('Error form invalid')

    return render(request, "rover/booster.html", {'inject':instance})

def rovflap(request):
    return render(request, "rover/flaps.html")

def index(request):
    return render(request, "rover/index.html")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid()  and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, "rover/registration.html",
                            {'user_form':user_form,
                            'profile_form':profile_form,
                            'registered':registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account Not Active")

        else:
            print("Someone tried to login and failed!")
            print("Username:{} and password {}".format(username, password))
            return HttpResponse("invalid login details supplied!")

    else:
        return render(request,'rover/login.html',{})

# def images(request):
#     return render(request, 'i')
