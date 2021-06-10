from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from radiogrid import RadioGridField

author = 'Philipp Chapkovski, chapkovski@gmail.com'

doc = """
Big Five 15-item inventory

Rammstedt, B., & John, O. P. (2007). Measuring personality in one minute or less: A 10-item short version of the 
Big Five Inventory in English and German. Journal of research in Personality, 41(1), 203-212.

https://www.westmont.edu/_academics/departments/psychology/documents/rammstedt_and_john.pdf
"""


class Constants(BaseConstants):
    name_in_url = 'bigfive'
    players_per_group = None
    num_rounds = 1
    bigfive = dict(extraversion=[5, 1, 8],
                   agreeableness=[2, 6, 12],
                   conscientiousness=[7, 0, 11],
                   neuroticism=[14, 4, 10],
                   openness=[3, 9, 13],
                   reliability=[15, 15, 15])
    bigfive_categories = bigfive.keys()


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


ROWS = (
    (1, " gründlich arbeitet"),
    (2, " kommunikativ, gesprächig ist"),
    (3, " manchmal etwas grob zu anderen ist"),
    (4, " originell ist, neue Ideen einbringt"),
    (5, " sich oft Sorgen macht"),
    (6, " verzeihen kann"),
    (7, " eher faul ist"),
    (8, ' aus sich herausgehen kann, gesellig ist'),
    (9, ' künstlerische, ästhestische Erfahrungen schätzt'),
    (10, ' leicht nervös wird'),
    (11, ' Aufgaben wirksam und effizient erledigt'),
    (12, ' zurückhaltend ist'),
    (13, ' rücksichtsvoll und freundlich mit anderen umgeht'),
    (14, ' eine lebhafte Phantasie, Vorstellungen hat'),
    (15, ' entspannt ist, mit Stress gut umgehen kann'),
    (16, ' Meine Antworten sind zuverlässig'),
)

VALUES = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
    (6, "6"),
    (7, "7"),
)



class Player(BasePlayer):
    bigfive = RadioGridField(rows=ROWS, values=VALUES, require_all_fields=True,
                             verbose_name='Ich bin jemand, der ...', )

    extraversion = models.FloatField()
    agreeableness = models.FloatField()
    conscientiousness = models.FloatField()
    neuroticism = models.FloatField()
    openness = models.FloatField()
    reliability = models.FloatField()

    def conversion(self, method):
        i, j, k = Constants.bigfive[method]
        if i == 3:
            return (int(self.bigfive[i]) + int(self.bigfive[j]) + int(self.bigfive[k]))/3
        elif i == 15:
            return int(self.bigfive[i])
        else:
            return (8 - int(self.bigfive[i]) + int(self.bigfive[j]) + int(self.bigfive[k]))/3
