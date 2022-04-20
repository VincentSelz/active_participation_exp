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
    name_in_url = 'main_exp_option'
    players_per_group = None
    num_rounds = 1
    #total timeout
    task_timeout = 60*1
    cost = 1
    # payment to inattentive subjects (usually =participation fee)
    pay_inattention = 3

    high_ability = [35,100]
    low_ability =  [0,65]
    high_threshold = 90
    computer_max_no_draw = 60
    # Examples
    high_example = 68
    low_example = 33
    #total timeout
    timeout = 4000
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
    bonus_points = 10
    # Outside Option
    outside_offer = 55



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):

    # Outside Option
    option_accepted = models.IntegerField(
        choices=[
            [1, 'Ja, ich akzeptiere.'],
            [0, 'Nein, ich möchte (selbst) mitmachen.'],
        ],
        widget=widgets.RadioSelect
    )
    # Type
    type = models.StringField(initial='r2')
    lowerbound=models.IntegerField()
    upperbound=models.IntegerField()
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
    draw_21 = models.IntegerField(blank=True)
    draw_22 = models.IntegerField(blank=True)
    draw_23 = models.IntegerField(blank=True)
    draw_24 = models.IntegerField(blank=True)
    draw_25 = models.IntegerField(blank=True)
    draw_26 = models.IntegerField(blank=True)
    draw_27 = models.IntegerField(blank=True)
    draw_28 = models.IntegerField(blank=True)
    draw_29 = models.IntegerField(blank=True)
    draw_30 = models.IntegerField(blank=True)
    draw_31 = models.IntegerField(blank=True)
    draw_32 = models.IntegerField(blank=True)
    draw_33 = models.IntegerField(blank=True)
    draw_34 = models.IntegerField(blank=True)
    draw_35 = models.IntegerField(blank=True)
    draw_36 = models.IntegerField(blank=True)
    draw_37 = models.IntegerField(blank=True)
    draw_38 = models.IntegerField(blank=True)
    draw_39 = models.IntegerField(blank=True)
    draw_40 = models.IntegerField(blank=True)
    draw_41 = models.IntegerField(blank=True)
    draw_42 = models.IntegerField(blank=True)
    draw_43 = models.IntegerField(blank=True)
    draw_44 = models.IntegerField(blank=True)
    draw_45 = models.IntegerField(blank=True)
    draw_46 = models.IntegerField(blank=True)
    draw_47 = models.IntegerField(blank=True)
    draw_48 = models.IntegerField(blank=True)
    draw_49 = models.IntegerField(blank=True)
    draw_50 = models.IntegerField(blank=True)
    draw_51 = models.IntegerField(blank=True)
    draw_52 = models.IntegerField(blank=True)
    draw_53 = models.IntegerField(blank=True)
    draw_54 = models.IntegerField(blank=True)
    draw_55 = models.IntegerField(blank=True)
    draw_56 = models.IntegerField(blank=True)
    draw_57 = models.IntegerField(blank=True)
    draw_58 = models.IntegerField(blank=True)
    draw_59 = models.IntegerField(blank=True)
    draw_60 = models.IntegerField(blank=True)

    attention_check = models.IntegerField(initial=0)
    current_max_is = models.IntegerField(initial=0)
    num_draws = models.IntegerField(initial=0)
    total_costs = models.IntegerField(initial=0)
    task_earning = models.IntegerField()
    bonus_earning = models.IntegerField()

    # Prompt Counter
    prompt_counter = models.IntegerField()
    Task_warnings = models.FloatField()

    # Attention check livepage
    def live_attention(self, data):
        if data==1:
            self.attention_check = 1

    # set computer performance
    computer_performance = models.IntegerField()
    total_performance = models.IntegerField()

    def set_payoffs(self):
        self.computer_performance = 0
        for x in range(1, Constants.computer_max_no_draw+1):
            if self.computer_performance>Constants.high_threshold: break
            self.computer_performance = random.randint(Constants.high_ability[0], Constants.high_ability[1])
        total_performance = max(self.current_max_is,self.computer_performance)
        if self.attention_check == 1 and self.option_accepted == 0:
            self.total_costs = (Constants.cost * self.num_draws)
            self.task_earning = total_performance - self.total_costs
            self.bonus_earning = Constants.bonus_points*(self.bonusq==0)
            self.payoff = c(total_performance - self.total_costs + Constants.bonus_points*(self.bonusq==0))
        else:
            #self.total_costs = 0
            self.bonus_earning = Constants.bonus_points*(self.bonusq==0)
            self.payoff = c(Constants.bonus_points*(self.bonusq==0))

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
    bonusq = models.IntegerField(label="Ihre Antwort:")


