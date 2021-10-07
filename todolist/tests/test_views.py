from django.test import TestCase, Client
from django.urls import reverse
from ..models import Todo
import json

class TestViews(TestCase):

    def setUp(self):
        """
        This method runs before the execution of each test case.
        """
        self.client = Client() # This is a testing browser that enables us to make http requests within Django tests.
        self.list_url = reverse('list') # The reverse function is imported in order to return a url when the url’s name is passed in as an argument.
        # Todo.objects.create(
        #     title='Just a test',
        # )

    def test_list_GET(self):
        """
        Checks if the url is working and it gets the template
        """
        response = self.client.get(self.list_url) # test code

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'todolist/list.html')


    # def test_list_POST_adds_new_item(self):
    #     """
    #     """
    #     Todo.objects.create(
    #         title='Just a test',
    #     )
    #     response = self.client.post(self.list_url,{
    #         'title':'Just a test'
    #     })

    #     self.assertEquals(response.status_code,302)
    #     self.assertAlmostEquals(Todo.first().title,'Just a test')

    # def test_list_POST_no_item(self):
    #     """
    #     """
    #     Todo.objects.create(
    #         title='Just a test',
    #     )
    #     response = self.client.post(self.list_url,{
    #         'title':'Just a test'
    #     })

    #     self.assertEquals(response.status_code,302)
    #     self.assertAlmostEquals(Todo.count(),0)

    # def test_list_create(self):
    #     url = reverse('list')
    #     response = self.client.post(url,{
    #         'title':'project2'
    #     })

    #     project2 = Todo.objects.get(id=11)
    #     self.assertEquals(project2.title,'project2')
