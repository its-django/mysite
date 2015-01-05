#!/usr/bin/env python
# encoding: utf-8


from django.test import TestCase
from django.contrib.auth.models import User
from django.test import client


class IndexWebpageTestCase(TestCase):

    """Simple Webpage visiting test"""

    def setUp(self):
        """setUp function
        :returns: TODO

        """
        self.c = client.Client()

    def test_index_visiting(self):
        """simple index  visiting
        :returns: TODO

        """
        resp = self.c.get('/index/')
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, '<h2>歡迎來到餐廳王</h2>')
        self.assertTemplateUsed(resp, 'index.html')


class LoginTestCase(TestCase):

    """Login test case"""

    def setUp(self):
        """create user
        :returns: TODO

        """
        User.objects.create_user('user', email='user@example.com', password='abcde')
        self.c = client.Client()

    def test_login_and_logout(self):
        """test login method using django auth

        """

        resp = self.c.get('/restaurants_list/')
        self.assertRedirects(resp, '/accounts/login/?next=/restaurants_list/')

        self.c.login(username='user', password='abcde')

        resp = self.c.get('/restaurants_list/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'restaurants_list.html')

        self.c.logout()
        resp = self.c.get('/restaurants_list/')
        self.assertRedirects(resp, '/accounts/login/?next=/restaurants_list/')

    def test_login_and_logout_by_http_protocol(self):
        """test login method using django auth

        """

        resp = self.c.get('/restaurants_list/')
        self.assertRedirects(resp, '/accounts/login/?next=/restaurants_list/')

        resp = self.c.post(
            '/accounts/login/', {'username': 'user', 'password': 'abcde'}, follow=True)
        self.assertEqual(resp.redirect_chain, [('http://testserver/index/', 302)])

        resp = self.c.get('/restaurants_list/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'restaurants_list.html')

        self.c.get('/accounts/logout/')
        resp = self.c.get('/restaurants_list/')
        self.assertRedirects(resp, '/accounts/login/?next=/restaurants_list/')
