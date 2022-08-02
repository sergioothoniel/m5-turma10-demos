from utils.csv_parser import CSVParser
from utils.json_parser import JSONParser


# mro
class Person(JSONParser, CSVParser):
    database = "database.json"

    def __init__(
        self, name: str, cpf: str, is_married: bool, age: int, instruments: list
    ):
        self.name = name
        self.cpf = cpf
        self.is_married = is_married
        self.age = age
        self.instruments = instruments

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

        return super().retrieve(cls.database)
