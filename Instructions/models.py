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
    q1 = models.IntegerField(label="Die Auszahlung für das 1. Gruppenmitglied beträgt:")
    q2 = models.IntegerField(label="Die Auszahlung für das 2. Gruppenmitglied beträgt:")
    q3 = models.IntegerField(label="Die Auszahlung für das 1. Gruppenmitglied beträgt:")
    q4 = models.IntegerField(label="Die Auszahlung für das 2. Gruppenmitglied beträgt:")
    show_tab=models.IntegerField(initial=1)



    def set_error_message(self,value):
        correct_ans1 = {
                                "q1" : 81,
                                "q2" : 76,
                                 }

        correct_ans2 = {
                                "q3" : 88,
                                "q4" : 83,
                                 }

        list_answers1 = list(value.items())[0:2] 
        list_correct_answers1 = list(correct_ans1.items())
        list_answers2 = list(value.items())[2:4] 
        list_correct_answers2 = list(correct_ans2.items())

        if list_answers1 != list_correct_answers1 and list_answers2 == list_correct_answers2:

          Text1 = 'Sie haben nicht alle Fragen des Szenarios 1 richtig beantwortet. Bitte lesen Sie die Instruktionen noch einmal und korrigieren Sie Ihre Antworten.'

          self.show_tab = 8
          return Text1

        elif list_answers1 == list_correct_answers1 and list_answers2 != list_correct_answers2:

          Text2 = 'Sie haben nicht alle Fragen des Szenarios 2 richtig beantwortet. Bitte lesen Sie die Instruktionen noch einmal und korrigieren Sie Ihre Antworten.'

          self.show_tab = 9
          return Text2

        elif list_answers1 != list_correct_answers1 and list_answers2 != list_correct_answers2:

          Text12 = 'Sie haben nicht alle Fragen der Szenarien 1 und 2 richtig beantwortet. Bitte lesen Sie die Instruktionen noch einmal und korrigieren Sie Ihre Antworten.'

          self.show_tab = 8
          return Text12


