from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


def vars_for_all_templates(self):
    return dict(
        levels=Constants.levels,
        choices=Constants.choices
    )


class BigFive(Page):
    form_model = 'player'
    form_fields = ['bigfive']

    def before_next_page(self):
        for i in Constants.bigfive_categories:
            setattr(self.player, i, getattr(self.player, 'conversion')(i))

class Rely(Page):
    form_model = 'player'
    form_fields = ['reliability']


page_sequence = [
    BigFive,
    Rely,
]
