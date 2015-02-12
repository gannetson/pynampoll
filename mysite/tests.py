from django.test import LiveServerTestCase
from selenium import webdriver
from django.conf import settings


class SeleniumTestCase(LiveServerTestCase):

    def setUp(self):
        if settings.SELENIUM_DRIVER == 'Firefox':
            self.browser = webdriver.Firefox()
        elif settings.SELENIUM_DRIVER == 'Chrome':
            self.browser = webdriver.Chrome()
        else:
            raise Exception("Please specify SELENIUM_DRIVER='Chrome' (or Firefox) in your local.py.")
        super(SeleniumTestCase, self).setUp()

    def tearDown(self):
        self.browser.quit()

    def visit_page(self, path):
        url = '%s%s' % (self.live_server_url,  path)
        return self.browser.get(url)


