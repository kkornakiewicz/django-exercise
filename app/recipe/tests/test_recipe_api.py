from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Recipe

from recipe.serializers import RecipeSerializer

import pdb

RECIPE_URL = reverse('recipe:recipe-list')


def sample_recipe(name="Name",description = "Desc"):
    """Generate and save sample recipe with default data"""
    recipe = Recipe.objects.create(name=name,description=description)
    return recipe


class RecipeAPITest(TestCase):
    """Test recipe API"""

    def setUp(self):
        self.client = APIClient()
    

    def test_retrieve_recipes(self):
        """Test listing of all recipes"""
        sample_recipe()
        sample_recipe()

        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes,many=True)

        res = self.client.get(RECIPE_URL)
        self.assertEqual(res.status_code,status.HTTP_200_OK)
        self.assertEqual(len(res.data),2)
        self.assertEqual(serializer.data,res.data)

    def test_create_recipe(self):
        """Test put method for RecipeAPI"""
        
        payload = {"name" : "My recipe", 
                "description" : "This is test description",
                "ingredients" : [{"name" : "pizza"}] }
        
        res = self.client.post(RECIPE_URL,payload,format='json')
    
        exists = Recipe.objects.filter(
                name = payload['name'],
                description = payload['description'])
       
        self.assertTrue(exists)

        
