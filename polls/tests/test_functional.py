from mysite.tests import SeleniumTestCase
from polls.factories import PollFactory, ChoiceFactory


class PollsSeleniumTestCase(SeleniumTestCase):

    def setUp(self):
        super(PollsSeleniumTestCase, self).setUp()
        self.poll = PollFactory.create_batch(10, choice__set=ChoiceFactory.create_batch(3))

    def test_polls(self):
        self.visit_page('/polls/')
        import ipdb;ipdb.set_trace()

