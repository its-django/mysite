# encoding: utf-8

from django import template
from django.http import HttpResponse


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
    with open('templates/math.html', 'r') as reader:
        t = template.Template(reader.read())
    c = template.Context({'s': s, 'd': d, 'p': p, 'q': q})
    return HttpResponse(t.render(c))
