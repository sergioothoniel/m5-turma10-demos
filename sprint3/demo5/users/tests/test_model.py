from addresses.models import Address
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.test import TestCase
from users.models import User

# unittest
# pytest


class UserTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        # print("=" * 100)
        # print("setUpTestData executado")
        # print("=" * 100)
        cls.favorite_season_default = "Não especificado"

        cls.user_1_data = {
            "first_name": "ale",
            "last_name": "xandre",
            "email": "alenossauro@mail.com",
            "favorite_season": "Verão",
        }

        cls.user_2_data = {
            "first_name": "ale",
            "last_name": "xandre",
            "email": "alenossauro@mail.com",
        }

        cls.user_3_data = {
            "first_name": "mar",
            "last_name": "celo",
            "email": "marceratops@mail.com",
            "favorite_season": "Escolha Invalida",
        }

        cls.user_1 = User.objects.create(**cls.user_1_data)


        cls.user_2 = User.objects.create(**cls.user_2_data)
        cls.user_3 = User(**cls.user_3_data)

        address_data_1 = {"street": "Rua de Wano", "number": 1055}
        address_data_2 = {"street": "Rua da Lua", "number": 122}

        cls.address_1 = Address(**address_data_1)
        cls.address_2 = Address(**address_data_2)

    def test_one_to_one_relationship_with_address(self):
        print("executando test_one_to_one_relationship_with_address")
        self.address_1.user = self.user_1
        self.address_1.save()

        self.address_2.user = self.user_1
        # self.address_2.save()

        self.assertRaises(IntegrityError, self.address_2.save)

    def test_if_relationship_with_address_is_made(self):
        print("executando test_if_relationship_with_address_is_made")
        self.address_1.user = self.user_1
        self.address_1.save()
        msg = "Verifique o relacionamento 1:1 de user com address"

        # self.assertIs(self.user_1.address, self.address_1, msg)
        self.assertIs(self.user_1.address, self.address_2, msg)

    def test_user_fields(self):
        print("executando test_user_fields")

        # self.assertEqual(self.user_1.first_name, "a")
        self.assertEqual(self.user_1.first_name, self.user_1_data["first_name"])
        self.assertEqual(self.user_1.last_name, self.user_1_data["last_name"])
        self.assertEqual(self.user_1.email, self.user_1_data["email"])
        self.assertEqual(
            self.user_1.favorite_season, self.user_1_data["favorite_season"]
        )

    def test_first_name_max_length(self):
        print("test_first_name_max_length")
        expected_max_length = 10
        result_max_length = self.user_1._meta.get_field("first_name").max_length
        msg = "Vefique o max_length de `first_name`"

        self.assertEqual(result_max_length, expected_max_length, msg)

    def test_favorite_season_default_choice(self):
        print("test_favorite_season_default_choice")
        result_favorite_default = self.user_2.favorite_season
        msg = f"Verifique se o valor padrão para favorite_season é {self.favorite_season_default}"

        self.assertEqual(result_favorite_default, self.favorite_season_default, msg)

    def test_favorite_season_wrong_choice(self):
        print("test_favorite_season_wrong_choice")

        # with self.assertRaises(ValidationError):
        #     self.user_3.full_clean()

        self.assertRaises(ValidationError, self.user_3.full_clean)

    def test_get_full_name(self):
        print("test_get_full_name")
        first_name = self.user_1_data["first_name"].capitalize()
        last_name = self.user_1_data["last_name"].capitalize()
        expected_full_name = f"{first_name} {last_name}"

        result = self.user_1.get_full_name()

        self.assertEqual(result, expected_full_name)

    # def setUp(self) -> None:
    #     print()
    #     print("=" * 100)
    #     print("setUp executado")

    # def tearDown(self) -> None:
    #     print("tearDown executado")
    #     print("=" * 100)

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print()
    #     print("=" * 100)
    #     print("tearDownClass executado")
    #     print("=" * 100)

    # def test_method_1(self):
    #     print("executando method_1")
    #     print(self.user_1)
    #     # self.assertEqual(1, 2, "Verifique se 1 é igual a 1")

    # def test_method_2(self):
    #     print("executando method_2")
    #     print(self.user_1)

    # def test_method_3(self):
    #     print("executando method_3")
    #     print(self.user_1)
