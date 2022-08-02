class ExampleClass:
    def example_inst_method(self):
        print("example_inst_method ExampleClass")

    @classmethod
    def example_cls_method(cls):
        print("example_cls_method ExampleClass")

    @staticmethod
    def example_stc_method():
        print("example_stc_method ExampleClass")


class CSVParser(ExampleClass):
    @staticmethod
    def retrieve(filepath: str) -> list[dict]:
        print("retrieve CSVParser")

        return []

    @staticmethod
    def save(filepath: str, payload: list[dict]) -> None:
        print("save CSVParser")

    @staticmethod
    def specific_method():
        print("specific method CSVParser")
