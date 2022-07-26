def sum_two_numbers(num_1, num_2):
    print(num_1 + num_2)


# Type Hint
# def module_greetings(msg: str, module: int = 5):
#     my_var = f"{msg} M{module}"
#     print(my_var)

def module_greetings(msg: str, module=5):
    my_var = f"{msg.capitalize()} M{module}"
    print(my_var)
