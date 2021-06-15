from . import pages
from ._builtin import Bot
from otree.api import Submission
import random


class PlayerBot(Bot):

    def play_round(self):
        if not self.participant.vars['failed_comprehension']:
            yield (pages.Sociodemographics, {'gender': random.randint(1, 2), 'age': random.randint(16, 90), 'education': random.randint(1, 8), 'income': random.randint(1, 10)})
            yield (pages.AttentionCheck1, {'attention_check': random.randint(1, 5)})
            yield (pages.IntroRaven)
            yield (pages.Raven1, {'raven_1': random.randint(1, 8)})
            yield (pages.Raven2, {'raven_2': random.randint(1, 8)})
            yield (pages.Raven3, {'raven_3': random.randint(1, 8)})
            yield (pages.Raven4, {'raven_4': random.randint(1, 8)})
            yield (pages.Raven5, {'raven_5': random.randint(1, 8)})
            yield (pages.Raven6, {'raven_6': random.randint(1, 8)})
            yield (pages.Raven7, {'raven_7': random.randint(1, 8)})
            yield (pages.Raven8, {'raven_8': random.randint(1, 8)})
            yield (pages.GenderQn, {'gender_performance_pref': random.randint(1, 2)})
        yield (pages.FinishedTasks)
        yield (pages.PayoffandGoodbye)
