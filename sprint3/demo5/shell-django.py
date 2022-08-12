from recipes.models import Recipe
from users.models import User
user_1 = User.objects.get(id=1)
user_1
recipe_data_1 = {"name": "Coxinha JS"}
recipe_1 = Recipe.objects.create(**recipe_data_1)
recipe
recipe_1
recipe_1.user
recipe_1.user = user_1
recipe_1.save()
user_2 = User.objects.get(id=2)
user_2
recipe_data_2 = {"name": "X-Python Calabreza"}
recipe_2 = Recipe.objects.create(**recipe_data_2, user=user_2)
recipe_2
recipe_2.user
user_3 = User.objects.get(id=3)
recipe_data_3 = {"name": "HTML ao molho branco", 'user': user_3}
recipe_data_3
recipe_3 = Recipe.objects.create(**recipe_data_3)
recipe_3.user

