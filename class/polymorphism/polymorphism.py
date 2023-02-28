"""
Polymorphism occurs when we want to allow the child class to have a method
 with the same name and a similar implementation as the parent
 class and we wish for that method you override the parent class method.
"""

import random


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


Lucilene = Person("Lucilene", "Martins", 85, status=True)
Daniel = Person("Daniel", "Barros", 87, status=True)


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

    def introduce(self):
        print("You are my mortal enemy!!!")


""" polymorphism = overriding a mthod introduce from Person class"""

Alex = Enemy('rock', 'Alex', 'Wayne', 75, status=False)

Alex.hurt(Lucilene)
Alex.insult(Lucilene)
Alex.steal(Lucilene)
Alex.introduce()
