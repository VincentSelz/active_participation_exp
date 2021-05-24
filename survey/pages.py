from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'educ', 'work', 'income']


class Personality(Page):
    form_model = 'player'
    form_fields = ['pers1', 'pers2', 'pers3', 'pers4', 'pers5', 'pers6', 'pers7', 'pers8', 'pers9', 'pers10',
                   'pers11', 'pers12', 'pers13', 'pers14', 'pers15', 'pers_rely']

class Preferences1(Page):
    form_model = 'player'
    form_fields = ['risk', 'patience', 'punish_you', 'punish_other', 'alturism']

class Preferences2(Page):
    form_model = 'player'
    form_fields = ['pos_res', 'neg_res', 'trust', 'math', 'control']


page_sequence = [Demographics, Personality, Preferences1, Preferences2]
