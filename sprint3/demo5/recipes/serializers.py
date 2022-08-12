from ingredients.models import Ingredient
from ingredients.serializers import IngredientSerializer
from rest_framework import serializers

from .models import Recipe

# from users.serializers import UserSerializer


class RecipeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(allow_null=True, allow_blank=True, default=None)
    instructions = serializers.CharField(
        allow_null=True, allow_blank=True, default=None
    )
    user_id = serializers.IntegerField(read_only=True)

    ingredients = IngredientSerializer(many=True)

    def create(self, validated_data):
        # import ipdb

        # ipdb.set_trace()
        ingredients_list = validated_data.pop("ingredients")

        recipe = Recipe.objects.create(**validated_data)

        for ingredient_dict in ingredients_list:
            # ingredient_obj = Ingredient.objects.create(**ingredient_dict)
            # ingredient_obj = Ingredient.objects.get_or_create(**ingredient_dict)[0]
            # ingredient_obj, created = Ingredient.objects.get_or_create(
            #     **ingredient_dict
            # )
            ingredient_obj, _ = Ingredient.objects.get_or_create(**ingredient_dict)
            recipe.ingredients.add(ingredient_obj)

        return recipe

    def update(self, recipe: Recipe, validated_data: dict):
        ingredients_list = validated_data.pop("ingredients", None)

        if ingredients_list:
            ingredients_obj_list = []
            for ingredient_dict in ingredients_list:
                ingredient_obj, was_created = Ingredient.objects.get_or_create(
                    **ingredient_dict
                )
                ingredients_obj_list.append(ingredient_obj)
                recipe.ingredients.add(ingredient_obj)
            # recipe.ingredients.set(ingredients_obj_list)

        for key, value in validated_data.items():
            setattr(recipe, key, value)

        recipe.save()

        return recipe

