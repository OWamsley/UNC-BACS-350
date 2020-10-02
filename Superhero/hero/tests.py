from django.test import TestCase

from .models import Superhero
from .hero import list_heroes

class CrudTests(TestCase):
    
    def test_num_heroes(self):
        num_heroes = len(list_heroes())
        self.assertEqual(num_heroes, 0)
        
