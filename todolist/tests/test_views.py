from django.test import TestCase, Client
from django.urls import reverse
from ..models import Todo
import json

class TestViews(TestCase):

    def setUp(self):
        """
        This method runs before the execution of each test case.
        """
        self.client = Client() # This is a testing browser that enables us to make http requests within Django tests. it is to mimic client behaviour.
        self.list_url = reverse('list') # The reverse function is imported in order to return a url when the url’s name is passed in as an argument.
        self.test1 = Todo.objects.create(
            title='test1',
        )

    def test_list_GET(self):
        """
        Checks if the url is working and it gets the template
        """
        response = self.client.get(self.list_url) # test code

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'todolist/list.html')


    def test_list_POST_adds_new_item(self):
        """
        When you add an item
        """
        
        response = self.client.post(self.list_url,{
            'title':'test1'
        })

        self.assertEquals(response.status_code,302)
        self.assertEquals(self.test1.title,'test1')

    def test_list_POST_no_item(self):
        """
        when no data is added
        """
        
        response = self.client.post(self.list_url)

        self.assertEquals(response.status_code,302)
        self.assertAlmostEquals(self.test1.title.count('title'),0)

    def test_list_create(self):
        """
        Creatng an item
        """
        url = reverse('list')
        response = self.client.post(url,{
            'title':'test2'
        })

        project2 = Todo.objects.get(id=2)
        self.assertEquals(project2.title,'test2')
