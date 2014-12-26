#!/usr/bin/env python
# encoding: utf-8

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.utils import timezone
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView

from restaurants.models import Restaurant, Comment
from restaurants.forms import CommentForm
from restaurants.permissions import user_can_comment


class MenuView(DetailView):

    """show restaurant menu"""

    model = Restaurant
    template_name = 'menu.html'
    context_object_name = 'restaurant'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        """ return decorated dispatch

        :request: request
        :returns: return origin dispatch
        """
        return super(MenuView, self).dispatch(request, *args, **kwargs)


class RestaurantsView(ListView):

    """return restaurant list"""

    model = Restaurant
    template_name = 'restaurants_list.html'
    context_object_name = 'restaurants'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        """ return decorated dispatch

        :request: request
        :returns: return origin dispatch
        """
        return super(RestaurantsView, self).dispatch(request, *args, **kwargs)


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
    return render(request, 'comments.html', locals())
