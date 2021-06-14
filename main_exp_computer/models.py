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
    name_in_url = 'main_exp_computer'
    players_per_group = None
    num_rounds = 1
    #total timeout
    task_timeout = 40
    cost = 1

    high_ability = [35,100]
    low_ability =  [0,65]
    high_threshold = 90
    # Examples
    high_example = 68
    low_example = 33
    #total timeout
    timeout = 2000
    # modal onset time before timeout So, 10 means 10 seconds before the timeout.
    pop_up_time = 10
    # How long it stays
    pop_up_duration = 5
    # duration of the animation
    animation_time = 5


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # Type
    type = models.StringField(initial='r2')
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

    # set computer performance
    computer_performance = models.IntegerField(initial=random.randint(Constants.high_threshold, Constants.high_ability[1]))
    total_performance = models.IntegerField()

    def set_payoffs(self):
        total_performance = max(self.current_max_is,self.computer_performance)
        if self.attention_check == 1:
            self.total_costs = (Constants.cost * self.num_draws)
            self.payoff = c(total_performance - self.total_costs)
        else:
            #self.total_costs = 0
            self.payoff = c(0)

