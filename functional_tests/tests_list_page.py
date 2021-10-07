from selenium import webdriver
from todolist.models import *
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time
class TestListPage(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_user_sees_list(self):
        task1 = Todo.objects.create(
            title='tests'
        )
        
        self.browser.get(self.live_server_url)
        time.sleep(20)
        # the user sees the project on the screen
        self.assertEquals(self.browser.find_element_by_tag_name('span').text,
        'tests'
        )

