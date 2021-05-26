# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

# additional models import / requires "localflavor" to be installed
from localflavor.generic.models import IBANField, BICField


author = 'Felix Albrecht ,Thomas Graeber, Thorben Woelk'

doc = """
Standardized End Page
"""


class Constants(BaseConstants):
    name_in_url = 'YIA4vPp0'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    iban = IBANField(verbose_name="IBAN")

    bic = BICField(verbose_name="BIC")

    whichbank = models.StringField(verbose_name="Name der Bank:", max_length=50)

    bankname = models.StringField(verbose_name="Nachname:", max_length=50)

    bankvname = models.StringField(verbose_name="Vorname:", max_length=50)

    street = models.StringField(verbose_name="Straße / Hausnr.:", max_length=50)

    city = models.StringField(verbose_name="Stadt:", max_length=50)

    zipcode = models.IntegerField(verbose_name="PLZ:")

    user_agent = models.StringField(blank=True)
    window_height = models.StringField(blank=True)
    window_width = models.StringField(blank=True)

    ibanmsgseen = models.PositiveIntegerField(default=0)

    consent2 = models.IntegerField()
    consent3 = models.IntegerField()
