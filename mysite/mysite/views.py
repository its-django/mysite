# encoding: utf-8

from django.http import HttpResponse


def here(request):
    """first view func

    :request: client request
    :returns: django http response

    """
    return HttpResponse('媽，我在這!')
