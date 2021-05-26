# -*- coding: utf-8 -*-
from __future__ import division

import random

from otree.common import Currency as c, currency_range

from . import pages
from ._builtin import Bot
from .models import Constants

from otree.api import Submission


class PlayerBot(Bot):
    """Bot that plays one round"""

    def play_round(self):

        yield Submission(pages.Iban, {'iban': 'DE12500105170648489890', 'bic': 'AABSDE31', 'whichbank': 'Sparkasse Köln', 'bankname': 'Schmidt', 'bankvname': 'Heiko', 'street': 'Kölnstraße 1', 'city': 'Bonn', 'zipcode': 53129, 'user_agent': 'User-agent header sent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36', 'window_height': 642, 'window_width': 1404, 'ibanmsgseen': 1, 'consent2': 1, 'consent3': 1}, check_html=False)
        # yield (pages.BankAccount, {
        #     'iban': 'DE12345678901234567890',
        #     'bic': '10020000'
        # })

        # yield (pages.Verification, {
        #     'verification': True,
        # })

        # yield (pages.End)

