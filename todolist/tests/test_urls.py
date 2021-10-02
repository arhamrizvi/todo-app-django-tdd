from django.test import SimpleTestCase
from django.urls import reverse, resolve
from todolist.views import index,updateTask

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        #assert 1 == 2
        url = reverse('list')
        print(resolve(url))
        self.assertEquals(resolve(url).func,index)

    def test_update_url_is_resolved(self):
        #assert 1 == 2
        url = reverse('update_task',args=['some-slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func,updateTask)
