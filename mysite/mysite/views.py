# encoding: utf-8

from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext


def here(request):
    """first view func

    :request: client request
    :returns: django http response

    """
    return HttpResponse('媽，我在這!')


def math(request, a, b):
    a = int(a)
    b = int(b)
    s = a + b
    d = a - b
    p = a * b
    q = a / b
    return render_to_response('math.html', {'s': s, 'd': d, 'p': p, 'q': q})


def welcome(request):
    """simple welcome page to demo query string

    :request: user request
    :returns: http response with username or origin welcome page

    """
    if 'user_name' in request.GET and request.GET['user_name'] != '':
        return HttpResponse('Welcome!~'+request.GET['user_name'])
    else:
        return render_to_response('welcome.html', locals())


def login(request):
    """user login webpage

    :request: client request
    :returns: index page if success, login page if fail

    """
    if request.user.is_authenticated():
        return HttpResponseRedirect('/index/')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/index/')
    else:
        return render_to_response('login.html', RequestContext(request, locals()))


def index(request):
    """index page

    :request: client request
    :returns: index webpage

    """
    return render(request, 'index.html', locals())


def logout(request):
    """logout view

    :request: client request
    :returns: index webpage

    """
    auth.logout(request)
    return HttpResponseRedirect('/index/')


def register(request):
    """new user register page

    :request: client request
    :returns: redirect to login page if success else register page

    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/accounts/login/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', locals())
