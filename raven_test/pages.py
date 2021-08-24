from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class IntroRaven(Page):

    def before_next_page(self):
        import time
        # user has 4 minutes to complete the test
        self.participant.vars['expiry'] = time.time() + 4*60

class Raven1(Page):
    form_model = 'player'
    form_fields = ['raven_1']

    timer_text = 'Verbleibende Zeit:'
    def get_timeout_seconds(self):
        import time
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.get_timeout_seconds() > 3

class Raven2(Page):
    form_model = 'player'
    form_fields = ['raven_2']

    timer_text = 'Verbleibende Zeit:'
    def get_timeout_seconds(self):
        import time
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.get_timeout_seconds() > 3



class Raven3(Page):
    form_model = 'player'
    form_fields = ['raven_3']

    timer_text = 'Verbleibende Zeit:'
    def get_timeout_seconds(self):
        import time
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.get_timeout_seconds() > 3



class Raven4(Page):
    form_model = 'player'
    form_fields = ['raven_4']

    timer_text = 'Verbleibende Zeit:'
    def get_timeout_seconds(self):
        import time
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.get_timeout_seconds() > 3



class Raven5(Page):
    form_model = 'player'
    form_fields = ['raven_5']

    timer_text = 'Verbleibende Zeit:'
    def get_timeout_seconds(self):
        import time
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.get_timeout_seconds() > 3



class Raven6(Page):
    form_model = 'player'
    form_fields = ['raven_6']

    timer_text = 'Verbleibende Zeit:'
    def get_timeout_seconds(self):
        import time
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.get_timeout_seconds() > 3



class Raven7(Page):
    form_model = 'player'
    form_fields = ['raven_7']

    timer_text = 'Verbleibende Zeit:'
    def get_timeout_seconds(self):
        import time
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.get_timeout_seconds() > 3



class Raven8(Page):
    form_model = 'player'
    form_fields = ['raven_8']

    timer_text = 'Verbleibende Zeit:'
    def get_timeout_seconds(self):
        import time
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.get_timeout_seconds() > 3




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
