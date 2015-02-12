from django.utils.timezone import now
import factory
from polls.models import Poll, Choice


class PollFactory(factory.Factory):
    FACTORY_FOR = Poll

    question = factory.Sequence(lambda n: 'Question {0}'.format(n))
    pub_date = now()

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        obj = model_class(*args, **kwargs)
        obj.save()
        return obj

class ChoiceFactory(factory.Factory):
    FACTORY_FOR = Choice

    poll = factory.SubFactory(PollFactory)
    choice_text = factory.Sequence(lambda n: 'Choice {0}'.format(n))

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        obj = model_class(*args, **kwargs)
        obj.save()
        return obj

