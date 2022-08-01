from persons.person import Person
from utils.json_parser import JSONParser


def class_attrs():
    # let p1 new Person()

    # p1, p2 e p3 são instancias de Person (ou objetos da classe Person)
    p1 = Person()
    p2 = Person()
    p3 = Person()

    print(type(p1))
    print(type(p2))
    print(type(p3))

    print("-" * 100)

    print(p1)
    print(p2)
    print(p3)

    print("-" * 100)

    # Atributo de classe imutável (int)
    p1.life_expectancy = 1000
    print(p1.life_expectancy)
    print(p2.life_expectancy)
    print(p3.life_expectancy)

    print("-" * 100)

    # Atributo de classe mutável (list)
    p1.wishlist.append("Poltrona Gamer RGB")
    print(p1.wishlist)
    print(p2.wishlist)
    print(p3.wishlist)


def inst_attrs():
    p1 = Person("person1", "111")
    p2 = Person("person2", "222")
    p3 = Person("person3", "333")

    # Atributo de instancia imutável (str)
    p1.name = "name changed"
    print(p1.name)
    print(p2.name)
    print(p3.name)

    print("-" * 100)

    # Atributo de instancia mutável (list)
    p1.instruments.append("Cavaquinho")
    print(p1.instruments)
    print(p2.instruments)
    print(p3.instruments)


def dunder_methods():
    p1 = Person("person1", "111")
    p2 = Person("person2", "222")
    p3 = Person("person3", "333")

    # print(p1)
    # print(p2)
    # print(p3)

    # forma explicita
    # print(p1.__repr__())

    p1.instruments.append("Cavaquinho")
    # print(len(p1))

    print(p1.__dict__)
    print(type(p1.__dict__))
    print(p2.__dict__)
    print(p3.__dict__)


def inst_methods():
    p1 = Person("person1", "111")
    p2 = Person("person2", "222")
    p3 = Person("person3", "333")

    p1.save()
    # Person.save()
    # Person.save(p1)
    ...


def static_method():
    p1 = Person("person1", "111")

    result = Person.retrieve()
    print(result)

    result_2 = p1.retrieve()
    print(result_2)


def json_class():
    result = JSONParser.retrieve("database.json")
    print(result)

    result.append({"name": "Chrystian"})

    JSONParser.save("database.json", result)


def heritance():
    p1 = Person("Chrystian", "555")

    p1.save()
    result = Person.retrieve()
    print(result)


def main():
    # class_attrs()
    # inst_attrs()
    # dunder_methods()
    # inst_methods()
    # static_method()
    # json_class()
    heritance()


if __name__ == "__main__":
    main()
