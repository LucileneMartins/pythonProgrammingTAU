"""
 ARGUMENTS - Positional Arguments
"""


def addition2(a, b):
    print(a+b)


addition2(20, 50)


def user_info(name, age, city):
    """
    This function prints name , age and city from an argument provided by function.
    """
    print('{} is {} years old, from {}'.format(name, age, city))


user_info('Lucilene', 32, 'Rio de Janeiro')



# Keyword Arguments - keyword arguments, you don't need to follow the positional order of the argument.


def user_info1(name, age=50, city="sao paulo"):
    """
    This function prints name , age and city from an argument provided by function.
    """
    print('{} is {} years old, from {}'.format(name, age, city))


user_info1(name="Bahia")

# The *args allows a function to take any number of positional arguments. - 75000
#The **kwargs allows a function to take any number of keyword arguments. - hire_date = "September 2010"

# *args and **kwargs
def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}. Her email is {}.".format(fname, lname, company, email))

application("Jess", "Ingrass", "mail @ mail.com", "Teach Code", 75000, hire_date = "September 2010")


