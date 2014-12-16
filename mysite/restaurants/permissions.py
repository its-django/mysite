#!/usr/bin/env python
# encoding: utf-8


def user_can_comment(user):
    """check if user has permission to comment

    :user: user to be check
    :returns: boolean

    """
    return user.is_authenticated and user.has_perm('restaurants.can_comment')
