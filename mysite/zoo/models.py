from django.db import models


class Animal(models.Model):

    """ Base model of other animals"""

    name = models.CharField(max_length=256)

    def says(self):
        """implemented by different animal.

        """
        raise NotImplementedError("I don't know what to say")

    class Meta:
        abstract = True


class Dog(Animal):

    def says(self):
        """return sound of dog
        :returns: "woof"

        """
        return 'woof'


class Cat(Animal):

    def says(self):
        """return sound of cat
        :returns: "meow"

        """
        return 'meow'
