from rest_framework import serializers

# from users.serializers import UserSerializer


class RecipeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(allow_null=True, allow_blank=True, default=None)
    instructions = serializers.CharField(
        allow_null=True, allow_blank=True, default=None
    )
    # user = UserSerializer()
