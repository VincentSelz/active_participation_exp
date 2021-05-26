from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class StartPage(Page):

    form_model = 'player'
    form_fields = [
        'email',
        'email_validate',
        'window_height',
        'window_width',
        'user_agent',
        'is_iPad_iOS13',
    ]

    def vars_for_template(self):
        return {
            # has to be added in settings.py in SESSION_CONFIG_DEFAULTS
            # 'super': self.session.config['super'],
            # 'supermail': self.session.config['supermail'],
        }

    def error_message(self, values):
        if values['email'] != values['email_validate']:
            return """Die eingegebenen E-Mail-Adressen stimmen nicht überein."""

    def before_next_page(self):
        # parti = self.request.build_absolute_uri(self.player.participant._start_url())
        # self.request.session["otree"] = parti
        # self.request.session.set_expiry(1209600) # timeout 2 weeks
        pass


class ScreenOut(Page):
    """ Page to screen out participants with mobile devices.
        Only displayed if participant is using a mobile; checks
        whether participant is using a mobile device on reloading;
        Shows a next button only if page is reloaded not using a
        mobile device.
    """

    form_model = 'player'
    form_fields = [
        'window_height2',
        'window_width2',
        'user_agent2',
        'is_iPad_iOS13_2'
    ]

    def is_displayed(self):
        if any(x in self.player.user_agent for x in [
            'iPhone',
            'iPad',
            'Android',
            'Mobi',
            'PlayBook',
            'BlackBerry',
            'Edge',
            'MSIE',
            'Trident'
        ]) or self.player.is_iPad_iOS13 is True:
            return True
        else:
            return False

class Intro(Page):
    def vars_for_template(self):
        conversion = self.session.config['real_world_currency_per_point']
        participation_fee = self.session.config['participation_fee']
        return dict(conversion=conversion,
                participation_fee=participation_fee)

page_sequence = [
    StartPage,
    ScreenOut,
    Intro
]
