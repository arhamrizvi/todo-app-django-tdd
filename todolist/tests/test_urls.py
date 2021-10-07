from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from ..views import index#,updateTask

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolves(self):
        """
        Testing urls
        """
        url = reverse('list')
        print(resolve(url))
        self.assertEquals(resolve(url).func,index)

    # def test_update_url_is_resolved(self):
    #     #assert 1 == 2
    #     url = reverse('update_task',args=['some-slug'])
    #     print(resolve(url))
    #     self.assertEquals(resolve(url).func,updateTask)
