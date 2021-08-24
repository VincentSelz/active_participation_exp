from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range, safe_json
)

import math

import random

author = 'Zheng Li'

doc = """
Raven tests
"""


class Constants(BaseConstants):
    """Contains constants of the current experiment app."""
    name_in_url = 'raven_test'
    players_per_group = None
    num_rounds = 1

    SCALE = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'),
             (7, '7'), (8, '8')]

    #solutions = [5, 6, 5, 3, 2, 6, 6, 4]


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    """Contains group-level objects of the current experiment app."""
    pass


class Player(BasePlayer):
    """Contains player-level objects of the current experiment app."""

    expiry = models.FloatField()

    raven_1 = models.PositiveIntegerField(
        initial=None,
        choices=Constants.SCALE,
        verbose_name='',
        blank=False,
        widget=widgets.RadioSelectHorizontal()
    )
    raven_2 = models.PositiveIntegerField(
        initial=None,
        choices=Constants.SCALE,
        verbose_name='',
        blank=False,
        widget=widgets.RadioSelectHorizontal()
    )
    raven_3 = models.PositiveIntegerField(
        initial=None,
        choices=Constants.SCALE,
        verbose_name='',
        blank=False,
        widget=widgets.RadioSelectHorizontal()
    )
    raven_4 = models.PositiveIntegerField(
        initial=None,
        choices=Constants.SCALE,
        verbose_name='',
        blank=False,
        widget=widgets.RadioSelectHorizontal()
    )
    raven_5 = models.PositiveIntegerField(
        initial=None,
        choices=Constants.SCALE,
        verbose_name='',
        blank=False,
        widget=widgets.RadioSelectHorizontal()
    )
    raven_6 = models.PositiveIntegerField(
        initial=None,
        choices=Constants.SCALE,
        verbose_name='',
        blank=False,
        widget=widgets.RadioSelectHorizontal()
    )
    raven_7 = models.PositiveIntegerField(
        initial=None,
        choices=Constants.SCALE,
        verbose_name='',
        blank=False,
        widget=widgets.RadioSelectHorizontal()
    )
    raven_8 = models.PositiveIntegerField(
        initial=None,
        choices=Constants.SCALE,
        verbose_name='',
        blank=False,
        widget=widgets.RadioSelectHorizontal()
    )
