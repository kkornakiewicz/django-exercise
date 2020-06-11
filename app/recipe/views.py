from rest_framework import viewsets,mixins

from core.models import Recipe
from recipe.serializers import RecipeSerializer

class RecipeViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin):
    """Shows list of recipes"""
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer 
