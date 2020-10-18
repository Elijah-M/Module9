from PythonModulesAssignment import my_definitions as my_def

# Used for the print_dict function
a_dictionary = {1: "Gold",
                2: "Silver",
                3: "Bronze",
                4: "Participation Award"}

# Used for the print_set function
a_set = ("First", "Second", "Third", "Fourth")

if __name__ == '__main__':
    my_def.greeting()
    my_def.author("Elijah Morishita")
    my_def.print_dict(a_dictionary)
    my_def.print_set(a_set)
