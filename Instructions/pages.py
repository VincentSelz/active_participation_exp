from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Instruction(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4']

    def error_message(self, value):
        return self.player.set_error_message(value)


class Popup(Page):
    def vars_for_template(self):
        return dict(
            pay_inattent=Constants.pay_inattention,
            popup_duration=Constants.pop_up_duration
        )

page_sequence = [
    Instruction,
    Popup
]
