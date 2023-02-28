""" Creating a class """


import random


class Person:

    """ initialize attributes to be used in/available for all \
       class methods in this class, and for class Objects created \
       by this class."""

    def __init__(self, firstname, lastname, health, status):
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        "all people  introduce themselves"
        print("Hi, I'm {} {}.".format(self.firstname, self.lastname))

    def emote(self):
        emotion = random.randrange(1, 3)

        if emotion == 1:
            print("{} is happy today".format(self.firstname))
        if emotion == 2:
            print("{} is sad right now".format(self.firstname))

    def status_change(self):
        if self.health == 100:
            print("{} is totally healthy!".format(self.firstname))

        elif self.health >= 70:
            print("{} is a little tired today".format(self.firstname))

        elif self.health >= 50:
            print("{} feels unwell.".format(self.firstname))

        elif self.health >= 40:
            print("{} goes to the doctor".format(self.firstname))

        else:
            print("{} is unconscious".format(self.firstname))


Lucilene = Person("Lucilene", "Martins", 55, status=True)


Lucilene.introduce()
Lucilene.emote()
Lucilene.status_change()
