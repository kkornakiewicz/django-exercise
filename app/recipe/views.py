from rest_framework import viewsets,mixins

from core.models import Recipe, Ingredient
from recipe.serializers import RecipeSerializer, IngredientSerializer

class RecipeViewSet(viewsets.GenericViewSet,
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin):
    """Shows list of recipes"""
    # queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
   
    def get_queryset(self):
        queryset = Recipe.objects.all()
        start_name = self.request.query_params.get('name')
        
        if start_name is not None:
            queryset = Recipe.objects.filter(name__startswith=start_name)

        return queryset

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
