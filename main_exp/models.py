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
    task_timeout = 600
    cost = 1
    high_ability = [20,40]
    low_ability =  [10,20]
    #total timeout
    timeout = 20
    # modal onset time before timeout So, 10 means 10 seconds before the timeout.
    pop_up_time = 10
    # How long it stays
    pop_up_duration = 5


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()


class Group(BaseGroup):
    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        total_performance = max(p1.current_max_is,p2.current_max_is)
        for sub in [p1,p2]:
            if sub.attention_check == 1:
                sub.total_costs = (Constants.cost * sub.num_draws)
                sub.payoff = c(total_performance - sub.total_costs)
            else:
                #sub.total_costs = 0
                sub.payoff = c(0)

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
    attention_check = models.IntegerField()
    current_max_is = models.IntegerField()
    num_draws = models.IntegerField()
    total_costs = models.IntegerField()

    # Prompt Counter
    prompt_counter = models.IntegerField()
    Task_warnings = models.FloatField()
