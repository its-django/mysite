#!/usr/bin/env python
# encoding: utf-8

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from restaurants.models import Restaurant


def menu(request):
    """retrun a menu response

    :request: client request
    :returns: http response

    """
    if 'id' in request.GET and request.GET['id'] != '':
        restaurant = Restaurant.objects.get(id=request.GET['id'])
        return render_to_response('menu.html', locals())
    else:
        return HttpResponseRedirect("/restaurants_list/")


def list_restaurants(request):
    """retrun restaurant list

    :request: client request
    :returns: restaurant list webpage

    """
    restaurants = Restaurant.objects.all()
    return render_to_response('restaurants_list.html', locals())
