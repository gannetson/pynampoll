from mysite.tests import SeleniumTestCase
from polls.factories import PollFactory, ChoiceFactory


class PollsSeleniumTestCase(SeleniumTestCase):

    def setUp(self):
        super(PollsSeleniumTestCase, self).setUp()
        self.polls = PollFactory.create_batch(10)
        for poll in self.polls:
            poll.save()
            ChoiceFactory.create_batch(3, poll=poll)


    def test_polls(self):
        self.visit_page('/polls/')
        questions  = self.browser.find_elements_by_css_selector("ul li a")

        self.assertEqual(questions[1].text, self.polls[1].question)
        questions[2].click()
        title = self.browser.find_element_by_tag_name("h1")
        self.assertEqual(title.text, self.polls[2].question)

        # Select second choice & click submit
        self.browser.find_elements_by_css_selector("label")[1].click()
        self.browser.find_element_by_css_selector("input[type=submit]").click()

        # Check the score
        exit_polls = self.browser.find_elements_by_css_selector("ul li")
        self.assertEqual(exit_polls[0].text, "Choice 6 -- 0 votes")
        self.assertEqual(exit_polls[1].text, "Choice 7 -- 1 vote")
        self.assertEqual(exit_polls[2].text, "Choice 8 -- 0 votes")


