"""
Author: Elijah Morishita
elmorishita@dmacc.edu
10/19/2020
This program is used to test creating and using a package with
multiple modules (.py files) that can be used in another file via import
"""
from definitions import dictionary_ops, greeting, set_ops

# This dictionary is used for the print_dict function from the dictionary_ops module
another_dict = {"Once": 1,
                "Twice": 2,
                "Thrice": 3}

# This set is used for the print_set function from the set_ops module
another_set = ("Ichi", "Ni", "San")

if __name__ == '__main__':
    greeting.greeting()
    greeting.author("Elijah Morishita")
    dictionary_ops.print_dict(another_dict)
    set_ops.print_set(another_set)
