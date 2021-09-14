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
    name_in_url = 'instructions'
    players_per_group = None
    num_rounds = 1
    # payment to inattentive subjects (usually =participation fee)
    pay_inattention = 3

    # How long the popup stays
    pop_up_duration = 5


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

