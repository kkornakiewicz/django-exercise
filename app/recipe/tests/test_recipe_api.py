from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Recipe

from recipe.serializers import RecipeSerializer

RECIPE_URL = reverse('recipe:recipe-list')

class RecipeAPITes(TestCase):
    """Test recipe API"""

    def setUp(self):
        self.client = APIClient()
        
    def test_retrieve_recipes(self):
        """Test listing of all recipes"""
        Recipe.objects.create(name="A recipe",description="Sample description")
        Recipe.objects.create(name="A recipe 2",description="Sample description")
        
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes,many=True)

        res = self.client.get(RECIPE_URL)
        self.assertEqual(res.status_code,status.HTTP_200_OK)
        self.assertEqual(len(res.data),2)
        self.assertEqual(serializer.data,res.data)
