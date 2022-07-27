def func_args(*args) -> None:
    total = 0

    print(type(args))
    print(args)

    for number in args:
        total += number

    print(total)


def func_args_2(*args) -> None:
    args[0] = 'algo'
    my_lst = list(args)
    my_lst[0] = 'algo'

    return tuple(my_lst)


def func_kwargs(**kwargs):
    print(type(kwargs))
    print(kwargs)
