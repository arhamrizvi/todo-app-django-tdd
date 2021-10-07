from django.test import SimpleTestCase
from ..forms import TodoForm

class TestForms(SimpleTestCase):

    def test_todo_form_valid_data(self):
        form = TodoForm(data={
            'title':'Cook Food'
        })

        self.assertTrue(form.is_valid())

    def test_todo_form_no_data(self):
        form = TodoForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),1)