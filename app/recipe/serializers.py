from rest_framework import serializers

from core.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    """Recipe serializer"""

    class Meta:
        model = Recipe
        fields = ('id','name','description',)
        read_only_fields = ('id',)
