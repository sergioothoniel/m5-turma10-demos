from persons.person import Person
from persons.person_serializer import PersonSerializer


def multi_heritance():
    # Person.retrieve()
    p1 = Person("Chrystian", "5555")
    p1.save()

    p1.specific_method()


def multi_level_heritance():
    # Person.example_inst_method()
    Person.example_cls_method()
    Person.example_stc_method()

    p1 = Person("Chrystian", "5555")
    p1.example_inst_method()


def validators():
    extra_key_data = {
        "name": "Chrystian",
        "cpf": "5555",
        "is_married": False,
        "age": 30,
        "instruments": ["Piano"],
        "extra_key_1": "extra_value",
        "extra_key_1": "extra_value2",
        "extra_key_2": "extra_value",
    }
    # x = 10
    # x = 20
    # print("original data:")
    # print(extra_key_data, end="\n\n")

    # Cleaner
    # serializer = PersonSerializer(**extra_key_data)

    # serializer.clean_data()
    # print("cleaned data:")
    # print(serializer.data)

    missing_required_key_data = {
        # "name": "Chrystian",
        # "cpf": "5555",
        "is_married": False,
        "age": 30,
        # "instruments": ["Piano"],
        "extra_key_1": "extra_value",
        "extra_key_1": "extra_value2",
        "extra_key_2": "extra_value",
    }

    # Required Keys
    # serializer = PersonSerializer(**missing_required_key_data)
    # serializer = PersonSerializer(**extra_key_data)

    # serializer.is_valid()
    # print("required keys errors:")
    # print(serializer.errors, end="\n\n")

    # print("required keys data:")
    # print(serializer.data)

    # if not serializer.is_valid():
    #     print("required keys errors:")
    #     print(serializer.errors, end="\n\n")
    # else:
    #     print("required keys data:")
    #     print(serializer.data)

    wrong_values_data = {
        # "name": 1,
        "cpf": 333,
        "is_married": "False",
        "age": 30,
        "instruments": {"Piano"},
        "extra_key_1": "extra_value",
    }

    serializer = PersonSerializer(**wrong_values_data)
    # serializer = PersonSerializer(**extra_key_data)

    if not serializer.is_valid():
        print("data type errors:")
        print(serializer.errors, end="\n\n")
    else:
        print("data type data:")
        print(serializer.data)

    # p1 = Person(**serializer.data)


def main():
    # multi_heritance()
    # multi_level_heritance()
    validators()


if __name__ == "__main__":
    main()
