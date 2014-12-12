#!/usr/bin/env python
# encoding: utf-8

from django.shortcuts import render_to_response

from restaurants.models import Restaurant


def menu(request):
    """retrun a menu response

    :request: client request
    :returns: http response

    """
    restaurants = Restaurant.objects.all()
    return render_to_response('menu.html', locals())
