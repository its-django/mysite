#!/usr/bin/env python
# encoding: utf-8

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import timezone

from restaurants.models import Restaurant, Comment


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


def comment(request, restaurant_id):
    """list comment or add new comment

    :request: client request
    :restaurant_id: restaurant id
    :returns: comment webpage if id is provided else return to restaurant list

    """
    if restaurant_id:
        r = Restaurant.objects.get(id=restaurant_id)
    else:
        return HttpResponseRedirect("/restaurants_list/")
    errors = []
    if request.POST:
        visitor = request.POST['visitor']
        content = request.POST['content']
        email = request.POST['email']
        date_time = timezone.localtime(timezone.now())
        if any(not request.POST[k] for k in request.POST):
            errors.append('* 有空白欄位，請不要留空')
        if '@' not in email:
            errors.append('* email格式不正確，請重新輸入')
        if not errors:
            Comment.objects.create(
                visitor=visitor, email=email,
                content=content,
                date_time=date_time,
                restaurant=r
            )
    return render_to_response('comments.html', RequestContext(request, locals()))
