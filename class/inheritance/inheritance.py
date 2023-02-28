import random

"""Inheritance is when we use the attributes and methods from the parent
 class and make those attributes and methods available to the child's class."""


class Person:

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

"""
 super().__init__(firstname, lastname, health, status) way to use inheritance in the classes
"""


class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status)
        self.weapon = weapon

    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10

        elif self.weapon == 'stick':
            other.health -= 5

        print(other.health)

    def insult(self, other):
        if self.health <= 80:
            print("{}, you are tired and weak".format(other.firstname))

    def steal(self, other):
        print("ha ha ha, {}, I have your stuff!".format(other.firstname))

        if other.status == True:
            other.status = False


Alex = Enemy('rock', 'Alex', 'Wayne', 75, status=False)

Alex.hurt(Lucilene)
Alex.insult(Lucilene)
Alex.steal(Lucilene)
