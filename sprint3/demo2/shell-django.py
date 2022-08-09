# GERAR HISTORY iPYTHON E JOGAR PRA UM ARQUIVO
# history -o -f shell-django.py


# User Serializer
from users.serializers import UserSerializer

user_data = {
    "first_name": "Maraaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "email": "marceratops",
    "favorite_season": "algum",
}
serializer = UserSerializer(data=user_data)
serializer
serializer.is_valid()
serializer.errors
from users.serializers import UserSerializer

user_data = {
    "first_name": "Maraaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "email": "marceratops",
    "favorite_season": "algum",
}
serializer = UserSerializer(data=user_data)
serializer.is_valid()
serializer.errors
from users.serializers import UserSerializer, UserSerializer0

user_data = {
    "first_name": "Maraaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "email": "marceratops",
    "favorite_season": "algum",
}
serializer = UserSerializer(data=user_data)
serializer.is_valid()
serializer.errors

user_data = {
    "first_name": "Mar",
    "last_name": "Celo",
    "email": "marceratops@mail.com",
    "favorite_season": "Inverno",
}
serializer = UserSerializer(data=user_data)
serializer.is_valid()
serializer.errors
serializer.validated_data
serializer.validated_data["first_name"]
dict(serializer.validated_data)
serializer.data
from users.models import User

User.objects.create(**serializer.validated_data)
marcelo = User.objects.get(id=1)
marcelo
serializer = UserSerializer(marcelo)
serializer.data

user_data = {
    "first_name": "Mar",
    "last_name": "Celo",
    "email": "marceratops@mail.com",
    "favorite_season": "Inverno",
}
from users.serializers import UserSerializer

serializer = UserSerializer(data=user_data)
serializer.is_valid()
serializer.errors
from users.serializers import UserSerializer

user_data = {
    "first_name": "Mar",
    "last_name": "Celo",
    "email": "marceratops@mail.com",
    "favorite_season": "Inverno",
}
serializer = UserSerializer(data=user_data)
serializer.is_valid()
serializer.validated_data
marcelo = User.objects.get(id=1)
from users.models import User

marcelo = User.objects.get(id=1)
serializer = UserSerializer(marcelo)
serializer.data

# Recipe Serializer
from recipes.serializers import RecipeSerializer

recipe_data = {"name": "X-Python"}
serializer = RecipeSerializer(data=recipe_data)
serializer.is_valid()
serializer.validated_data
from recipes.models import Recipe

recipe = Recipe.objects.create(**serializer.validated_data)
recipe
from users.models import User

marcelo = User.objects.get(id=1)
marcelo.recipes
marcelo.recipes.all()
