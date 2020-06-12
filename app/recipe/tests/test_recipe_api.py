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
        self.assertEqual(res.status_code,status.HTTP_201_CREATED)
        self.assertTrue(exists)

    def test_retrieve_recipses_with_name_filter(self):
        """Test retrieving recipies with filter in URL"""
        sample_recipe(name="Pizza")
        sample_recipe("Paella")
        
        pizza = Recipe.objects.filter(name = "Pizza").get()
        serializer = RecipeSerializer(pizza)
        res = self.client.get(RECIPE_URL+"?name=Pi") # TODO, not nice
        
        self.assertEqual(res.status_code,status.HTTP_200_OK)
        self.assertEqual(len(res.data),1)
        self.assertIn(serializer.data,res.data)
  
    def test_retrieve_by_id(self):
        """Test retrieving recipe by ID"""
        sample_recipe()
        
        recipe = Recipe.objects.all()[0]
        serializer = RecipeSerializer(recipe)
        url = reverse("recipe:recipe-detail",args=[recipe.id])
        res = self.client.get(url)
        
        self.assertEqual(res.status_code,status.HTTP_200_OK)
        self.assertEqual(serializer.data,res.data)

        
    def test_deleter(self):
        """Test delete recipe"""
        sample_recipe()
        
        recipe = Recipe.objects.all()[0]
        serializer = RecipeSerializer(recipe)
        url = reverse("recipe:recipe-detail",args=[recipe.id])
        res = self.client.delete(url)
        
        self.assertEqual(res.status_code,status.HTTP_204_NO_CONTENT)
        res = self.client.delete(url)
        self.assertEqual(res.status_code,status.HTTP_404_NOT_FOUND)

        
