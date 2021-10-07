from django.test import TestCase
from ..models import *

class TestModels(TestCase):
    def setUp(self):
        self.task1 = Todo.objects.create(
            title = 'Task 1'
        )

    def test_list_is_assigned_id(self):
        self.assertEquals(self.task1.id,1)