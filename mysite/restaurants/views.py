#!/usr/bin/env python
# encoding: utf-8

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import timezone
from django.contrib.auth.decorators import login_required, user_passes_test

from restaurants.models import Restaurant, Comment
from restaurants.forms import CommentForm
from restaurants.permissions import user_can_comment


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


@login_required
def list_restaurants(request):
    """retrun restaurant list

    :request: client request
    :returns: restaurant list webpage

    """
    restaurants = Restaurant.objects.all()
    request.session['restaurants'] = restaurants
    return render_to_response('restaurants_list.html', locals())


@user_passes_test(user_can_comment, login_url='/accounts/login/')
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
        f = CommentForm(request.POST)
        if f.is_valid():
            visitor = request.POST['visitor']
            content = request.POST['content']
            email = request.POST['email']
            date_time = timezone.localtime(timezone.now())
            Comment.objects.create(
                visitor=visitor, email=email,
                content=content,
                date_time=date_time,
                restaurant=r
            )
            f = CommentForm(initial={'content': '我沒意見'})
    else:
        f = CommentForm(initial={'content': '我沒意見'})
    return render_to_response('comments.html', RequestContext(request, locals()))
