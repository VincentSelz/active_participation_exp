from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random as random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'main_exp'
    players_per_group = 2
    num_rounds = 1
    timeout = 600
    cost = 1
    high_ability = [20,40]
    low_ability =  [10,20]


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
        print(Constants.high_ability[0])
        #t1 = self.group.get_player_by_id(1)
        #t2 = self.group.get_player_by_id(2)


class Group(BaseGroup):
    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        total_performance = max(p1.current_max_is,p2.current_max_is)
        for sub in [p1,p2]:
            sub.total_costs = (Constants.cost * sub.num_draws)
            sub.payoff = c(total_performance - sub.total_costs)


class Player(BasePlayer):

    # Draws
    draw_1 = models.IntegerField(blank=True)
    draw_2 = models.IntegerField(blank=True)
    draw_3 = models.IntegerField(blank=True)
    draw_4 = models.IntegerField(blank=True)
    draw_5 = models.IntegerField(blank=True)
    draw_6 = models.IntegerField(blank=True)
    draw_7 = models.IntegerField(blank=True)
    draw_8 = models.IntegerField(blank=True)
    draw_9 = models.IntegerField(blank=True)
    draw_10 = models.IntegerField(blank=True)
    draw_11 = models.IntegerField(blank=True)
    draw_12 = models.IntegerField(blank=True)
    draw_13 = models.IntegerField(blank=True)
    draw_14 = models.IntegerField(blank=True)
    draw_15 = models.IntegerField(blank=True)
    draw_16 = models.IntegerField(blank=True)
    draw_17 = models.IntegerField(blank=True)
    draw_18 = models.IntegerField(blank=True)
    draw_19 = models.IntegerField(blank=True)
    draw_20 = models.IntegerField(blank=True)
    current_max_is = models.IntegerField()
    num_draws = models.IntegerField()
    total_costs = models.IntegerField()
