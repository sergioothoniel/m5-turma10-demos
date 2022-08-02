import json


class JSONParser:
    @staticmethod
    def retrieve(filepath: str) -> list[dict]:
        print("retrieve JSONParser")
        with open(filepath, "r") as file:
            return json.load(file)

    @staticmethod
    def save(filepath: str, payload: list[dict]) -> None:
        print("save JSONParser")
        with open(filepath, "w") as file:
            json.dump(payload, file, indent=2, ensure_ascii=False)
