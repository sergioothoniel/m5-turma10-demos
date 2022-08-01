# from utils.json_parser import read_json, write_json
from utils.json_parser import JSONParser


# pascal case PersonCard
class Person2:
    # # print("olá")
    # # Atributos de classe
    # life_expectancy = 90
    # wishlist = ["Faca Ginzu 2000"]

    # # Método de instancia
    # # Equivalente ao constructor
    # # __new__
    # # Dunder method
    # def __init__(self, name: str, cpf: str):
    #     self.name = name
    #     self.cpf = cpf
    #     self.instruments = ["Violao"]

    # # sobrescrevendo o __repr__
    # # def __repr__(self) -> str:
    # #     return f"{self.name} - {self.cpf}"

    # def __len__(self) -> int:
    #     return len(self.instruments)

    # def save(self) -> None:
    #     # self é o objeto referenciado da classe
    #     # print(self)
    #     # print(self.name)
    #     # print(type(self))

    #     persons = read_json("database.json")

    #     persons.append(self.__dict__)

    #     write_json("database.json", persons)

    # @staticmethod
    # def retrieve() -> list[dict]:
    #     return read_json("database.json")
    ...


class Person(JSONParser):
    life_expectancy = 90
    wishlist = ["Faca Ginzu 2000"]
    database = "database.json"

    def __init__(self, name: str, cpf: str):
        self.name = name
        self.cpf = cpf
        self.instruments = ["Violao"]

    def __len__(self) -> int:
        return len(self.instruments)

    def save(self) -> None:
        print("save Person")
        persons = super().retrieve(self.database)
        persons.append(self.__dict__)

        super().save(self.database, persons)

    @classmethod
    def retrieve(cls) -> list[dict]:
        print("retrieve Person")
        # Consigo alterar atributos de classe
        # cls.life_expectancy = 100
        return super().retrieve(cls.database)
