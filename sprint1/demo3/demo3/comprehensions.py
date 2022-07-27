def list_c(max_range: int) -> list:
    # Caso base 1
    # numbers = []

    # for number in range(1, max_range):
    #     numbers.append(number)

    # return numbers

    # equivalente ao map
    # return [number for number in range(1, max_range)]
    # Copia de lista
    # return [number * 'a' for number in range(1, max_range)]

    # Caso base 2
    # numbers = []

    # for number in range(1, max_range):
    #     if number % 2 == 0:
    #         numbers.append(number)

    # return numbers
    # equivalente ao filter
    # return [number for number in range(1, max_range) if number % 2 == 0]

    # Caso base 3
    # numbers = []

    # for number in range(1, max_range):
    #     if number % 2 == 0:
    #         numbers.append('par')
    #     else:
    #         numbers.append('impar')

    # return numbers

    # equivalente ao filter
    my_list = [
        "par" if number % 2 == 0 else "impar"
        for number in range(1, max_range)
    ]
    return my_list


def zip_example(keys: list, values: list):
    my_zip = zip(keys, values)

    # print(my_zip)
    # print(type(my_zip))

    print(dict(my_zip))
    # print(list(zip('abcdefg', range(3), range(1, 4))))
