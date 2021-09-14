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
    task_timeout = 60*10
    cost = 1
    # payment to inattentive subjects (usually =participation fee)
    pay_inattention = 3

    high_ability = [35,100]
    low_ability =  [0,65]
    high_threshold = 90
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



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):

    # Comprehension Questions
    q1 = models.IntegerField(label="Die Auszahlung für Spieler 1 beträgt:")
    q2 = models.IntegerField(label="Die Auszahlung für Spieler 2 beträgt:")
    q3 = models.IntegerField(label="Die Auszahlung für Spieler 1 beträgt:")
    q4 = models.IntegerField(label="Die Auszahlung für Spieler 2 beträgt:")

    def set_error_message(self,value):
        correct_answers = {
                                "q1" : 81,
                                "q2" : 76,
                                "q3" : 88,
                                "q4" : 83,
                                 }

        list_answers = list(value.items())[0:] 
        list_correct_answers = list(correct_answers.items())

        if list_answers != list_correct_answers:

          Text = 'Sie haben nicht alle Fragen richtig beantwortet. Bitte lesen Sie die Instruktionen noch einmal und korrigieren Sie Ihre Antworten.'

          return Text

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


