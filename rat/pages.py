from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import time


class Intro(Page):
    pass

class FinalPage(Page):
    def vars_for_template(self):
        me = self.player
        return dict(
            my_payoff=me.payoff,
            my_payoff_real_money=me.payoff.to_real_world_currency(self.session),
            part_fee=self.session.config['participation_fee']
        )


class RatPage(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10']

    def get_timeout_seconds(self):
        return 180


page_sequence = [Intro, RatPage, FinalPage]
