from django.utils.timezone import now
import factory
from polls.models import Poll, Choice


class PollFactory(factory.Factory):
    FACTORY_FOR = Poll

    question = factory.Sequence(lambda n: 'Question {0}'.format(n))
    pub_date = now()


class ChoiceFactory(factory.Factory):
    FACTORY_FOR = Choice

    poll = factory.SubFactory(PollFactory)
    choice_text = factory.Sequence(lambda n: 'Choice {0}'.format(n))



