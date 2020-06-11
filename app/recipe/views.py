from rest_framework import viewsets,mixins

from core.models import Recipe, Ingredient
from recipe.serializers import RecipeSerializer, IngredientSerializer

class RecipeViewSet(viewsets.GenericViewSet,
        mixins.ListModelMixin,
        mixins.CreateModelMixin):
    """Shows list of recipes"""
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
