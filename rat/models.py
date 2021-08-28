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


author = 'Cavit Görkem Destan'

doc = """
Remote Associates Test in German
"""


class Constants(BaseConstants):
    name_in_url = 'rat'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    q1 = models.CharField(label='Teller - Kaiser - Gemüse') #suppe
    q2 = models.CharField(label='Fisch - Mine - Barren') #gold
    q3 = models.CharField(label='Anzug - Kapsel - Welt') #raum
    q4 = models.CharField(label='Wein - Körper - Tür') #glas
    q5 = models.CharField(label='Werk - Alarm - Leiter') #feuer
    q6 = models.CharField(label='Karte - Tuch - Tennis') #tisch
    q7 = models.CharField(label='Bau - Plan - Kosten') #stelle
    q8 = models.CharField(label='Wurm - Regal - Sendung') #buch
    q9 = models.CharField(label='Koffer - Kuh - Hose') #leder
    q10 = models.CharField(label='Schaukel - Bein - Kissen') #stuhl
