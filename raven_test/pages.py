from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class IntroRaven(Page):
    pass

class Raven1(Page):
    form_model = 'player'
    form_fields = ['raven_1']


class Raven2(Page):
    form_model = 'player'
    form_fields = ['raven_2']


class Raven3(Page):
    form_model = 'player'
    form_fields = ['raven_3']


class Raven4(Page):
    form_model = 'player'
    form_fields = ['raven_4']


class Raven5(Page):
    form_model = 'player'
    form_fields = ['raven_5']


class Raven6(Page):
    form_model = 'player'
    form_fields = ['raven_6']


class Raven7(Page):
    form_model = 'player'
    form_fields = ['raven_7']


class Raven8(Page):
    form_model = 'player'
    form_fields = ['raven_8']



page_sequence = [
    IntroRaven,
    Raven1,
    Raven2,
    Raven3,
    Raven4,
    Raven5,
    Raven6,
    Raven7,
    Raven8,
]
