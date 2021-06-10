from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


def vars_for_all_templates(self):
    return dict(
        levels=Constants.levels,
        choices=Constants.choices
    )

class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'educ', 'work', 'income']

class Risk(Page):
    form_model = 'player'
    form_fields = ['risk']

class Preferences1(Page):
    form_model = 'player'
    form_fields = ['patience', 'punish_you', 'punish_other', 'alturism']

class Preferences2(Page):
    form_model = 'player'
    form_fields = ['pos_res', 'neg_res', 'trust', 'math', 'control']


page_sequence = [Demographics, Risk, Preferences1, Preferences2]
