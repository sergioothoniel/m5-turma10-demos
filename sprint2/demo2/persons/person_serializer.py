class DataValidationError(Exception):
    ...


class PersonSerializer:
    valid_inputs = {
        "name": str,
        "cpf": str,
        "is_married": bool,
        "age": int,
        "instruments": list,
    }

    def __init__(self, *args, **kwargs):
        self.data = kwargs
        self.errors = {}

    def is_valid(self) -> bool:
        print("original data:")
        print(self.data, end="\n\n")

        self.clean_data()

        try:
            self.validate_required_keys()
            self.validate_data_types()

            return True
        except DataValidationError:
            return False

    def clean_data(self):
        # data_keys = self.data.keys()
        data_keys = tuple(self.data.keys())

        # data_keys = list(self.data.keys())
        # data_keys = set(self.data.keys())
        # print(data_keys)

        for key in data_keys:
            if key not in self.valid_inputs.keys():
                # print(key)
                self.data.pop(key)

    def validate_required_keys(self):
        for valid_key in self.valid_inputs.keys():
            # Verificar se está faltando uma chave obrigatoria
            if valid_key not in self.data.keys():
                self.errors[valid_key] = "missing key"

        # if {} / {'name': 'missing key'}
        if self.errors:
            raise DataValidationError

    def validate_data_types(self):
        for valid_key, valid_type in self.valid_inputs.items():
            if type(self.data[valid_key]) is not valid_type:
                # self.errors[valid_key] = "wrong data type"
                # self.errors.update({valid_key: f"wrong data type {valid_type}"})
                # valid_type = str.__name__

                self.errors.update(
                    {valid_key: f"wrong data type {valid_type.__name__}"}
                )

        if self.errors:
            raise DataValidationError
