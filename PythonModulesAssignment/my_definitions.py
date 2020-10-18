"""
Author: Elijah Morishita
elmorishita@dmacc.edu
10/18/2020
This program is used to test creating and using a module (.py file) that can
be used in another file via import
"""


def greeting():
    """
    This function prints a friendly greeting
    :return:
    """
    print('\n',
          '=' * 45,
          "\n Welcome to this Module-Creation-Test-Program!!!",
          '\n',
          '=' * 45)


def author(name):
    """
    This function prints the author's name, which is received through the parameter
    :param name:
    :return:
    """
    print("Author:", name)


def print_dict(dictionary):
    """
    This program prints a dictionary, which is received through the parameter
    :param dictionary:
    :return:
    """
    for x,y in dictionary.items():
        print(x, y)


def print_set(the_set):
    """
    This function prints a set, which is received through the parameter
    :param the_set:
    :return:
    """
    for x in the_set:
        print(x)
