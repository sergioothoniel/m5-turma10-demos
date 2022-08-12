from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status
from users.models import User

from .models import Recipe
from .serializers import RecipeSerializer


class RecipeView(APIView):
    def get(self, request: Request, user_id: int) -> Response:
        recipes = Recipe.objects.filter(user_id=user_id)

        serializer = RecipeSerializer(recipes, many=True)

        return Response(serializer.data)

    def post(self, request: Request, user_id: int) -> Response:
        # 1
        user = get_object_or_404(User, id=user_id)

        # user = get_object_or_404(User, **{"id": user_id})

        # search_dict = {"id": user_id}
        # user = get_object_or_404(User, **search_dict)

        serializer = RecipeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(user=user)

        return Response(serializer.data, status.HTTP_201_CREATED)


class RecipeDetailView(APIView):
    def patch(self, request: Request, user_id: int, recipe_id: int):
        # select agrupando User Recipe onde user_id = user_id and id = recipe_id
        # search_dict = {"id": recipe_id, "user_id": user_id}
        # recipe = get_object_or_404(Recipe, **search_dict)

        recipe = get_object_or_404(Recipe, id=recipe_id, user_id=user_id)

        serializer = RecipeSerializer(recipe, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
