# encoding: utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response


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


def menu(request):
    """retrun a menu response

    :request: client request
    :returns: http response

    """
    food = {'name': '番茄炒蛋', 'price': 60, 'comment': '好吃', 'is_spicy': False}
    return render_to_response('menu.html', locals())
