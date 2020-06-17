from rest_framework import serializers

from core.models import Recipe, Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    """IngredientSerializer"""

    class Meta:
        model = Ingredient
        fields = ('name',)

class RecipeSerializer(serializers.ModelSerializer):
    """Recipe serializer"""  
    
    ingredients = IngredientSerializer(many=True)

    def create(self,validated_data):
        ingredients = validated_data.pop('ingredients')
        
        recipe = Recipe.objects.create(**validated_data)
        
        for ingredient in ingredients:
            Ingredient.objects.create(**ingredient,recipe=recipe)
        return recipe

    def update(self,instance,validated_data):
        ingredients = validated_data.pop('ingredients')    
        
        super(RecipeSerializer,self).update(instance,validated_data)
        
        Ingredient.objects.filter(recipe=instance).delete()
        for ingredient in ingredients:
            Ingredient.objects.create(**ingredient,recipe=instance)
        return instance


    class Meta:
        model = Recipe
        fields = ('id','name','description','ingredients',)
        read_only_fields = ('id',)

