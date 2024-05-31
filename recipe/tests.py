from django.test import TestCase
from django.urls import reverse
from .models import Recipe, Category
import datetime

class RecipeViewTests(TestCase):

    def setUp(self):
        category = Category.objects.create(name='Desserts')
        Recipe.objects.create(title='Test Recipe 1', description='Description 1', instructions='Instructions 1', ingredients='Ingredients 1', created_at=datetime.datetime(2023, 5, 17), category=category)
        Recipe.objects.create(title='Test Recipe 2', description='Description 2', instructions='Instructions 2', ingredients='Ingredients 2', created_at=datetime.datetime(2023, 6, 18), category=category)

    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Recipe 1')
        self.assertContains(response, 'Test Recipe 2')