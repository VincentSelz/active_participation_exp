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
    #total timeout
    task_timeout = 60*10
    cost = 1
    # payment to inattentive subjects (usually =participation fee)
    pay_inattention = 3

    high_ability = [35,100]
    low_ability =  [0,65]
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
    animation_time = 10
    # for hypothetical questions
    high_ability_alt = [35,85]
    low_ability_alt = [0,85]
    cost_alt = 3


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
        for p in self.get_players():
            if self.round_number == 1:
                if p.id_in_group == 1:
                    p.participant.vars['type'] = 'r1'
                elif p.id_in_group == 2:
                    p.participant.vars['type'] = 'r2'
            p.type = p.participant.vars['type']



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

    # Type
    type = models.StringField()
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
    num_draws = models.IntegerField(initial=0)
    total_costs = models.IntegerField()

    # Prompt Counter
    prompt_counter = models.IntegerField()
    Task_warnings = models.FloatField()

    # Hypothetical questions
    strategy = models.LongStringField(label="Ihre Antwort:")
    altcost = models.LongStringField(label="Ihre Antwort:")
    altbound = models.LongStringField(label="Ihre Antwort:")
    belief = models.IntegerField(label="Ihre Antwort:")
    # dynamically adjust limits
    def belief_max(self):
        if self.type=='r1':
            return Constants.low_ability[1]
        elif self.type=='r2':
            return Constants.high_ability[1]
    def belief_min(self):
        if self.type=='r1':
            return Constants.low_ability[0]
        elif self.type=='r2':
            return Constants.high_ability[0]

    expectation = models.LongStringField(label="Ihre Antwort:")
    ideal = models.LongStringField(label="Ihre Antwort:")
