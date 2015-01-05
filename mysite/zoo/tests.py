#!/usr/bin/env python
# encoding: utf-8


from django.test import TestCase

from zoo import models


class AnimalTestCase(TestCase):

    """Test animals' sound """

    def test_dog_says(self):
        """test dog says woof or not

        """
        dog = models.Dog(name='Snoopy')
        self.assertEqual(dog.says(), 'woof')

    def test_cat_says(self):
        """test cat says meow of not

        """
        cat = models.Cat(name='Garfield')
        self.assertEqual(cat.says(), 'meow')
