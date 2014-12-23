#!/usr/bin/env python
# encoding: utf-8


from django.test import TestCase
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
