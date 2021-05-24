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


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    age = models.IntegerField(label='Wie alt sind Sie?', min=13, max=125)

    gender = models.StringField(
        choices=[['female', 'Weiblich'], ['male', 'Männlich'], ['other', 'Divers']],
        label='Was ist Ihr Geschlecht?',
        widget=widgets.RadioSelect,
    )

    educ = models.StringField(
        choices=[['HS', 'Highschool'], ['BA', 'BA'], ['MA', 'Master'], ['more', 'More']],
        label='Was ist der höchste Abschluss, den Sie abgeschlossen haben?',
        widget=widgets.RadioSelect,
    )

    work = models.StringField(
        choices=[['student', 'Studierende'], ['worker', 'Arbeitnehmer'], ['retired', 'Pensioniert'], ['other', 'Andere']],
        label='Wie ist Ihr aktueller Status?',
        widget=widgets.RadioSelect,
    )

    income = models.IntegerField(label='Wie viel Geld haben Sie monatlich zur Verfügung? (in Euro)', min=0, max=99999)

    pers1 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label='gründlich arbeitet',
        widget=widgets.RadioSelectHorizontal
    )

    pers2 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label='kommunikativ, gesprächig ist',
        widget=widgets.RadioSelectHorizontal
    )

    pers3 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label='manchmal etwas grob zu anderen ist',
        widget=widgets.RadioSelectHorizontal
    )

    pers4 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label='originell ist, neue Ideen einbringt',
        widget=widgets.RadioSelectHorizontal
    )

    pers5 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label='sich oft Sorgen macht',
        widget=widgets.RadioSelectHorizontal
    )

    pers6 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label='verzeihen kann',
        widget=widgets.RadioSelectHorizontal
    )

    pers7 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label='eher faul ist',
        widget=widgets.RadioSelectHorizontal
    )

    pers8 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label='aus sich herausgehen kann, gesellig ist',
        widget=widgets.RadioSelectHorizontal
    )

    pers9 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label='künstlerische, ästhestische Erfahrungen schätzt',
        widget=widgets.RadioSelectHorizontal
    )

    pers10 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label='leicht nervös wird',
        widget=widgets.RadioSelectHorizontal
    )

    pers11 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label='Aufgaben wirksam und effizient erledigt',
        widget=widgets.RadioSelectHorizontal
    )

    pers12 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label='zurückhaltend ist',
        widget=widgets.RadioSelectHorizontal
    )

    pers13 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label='rücksichtsvoll und freundlich mit anderen umgeht',
        widget=widgets.RadioSelectHorizontal
    )

    pers14 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label='eine lebhafte Phantasie, Vorstellungen hat',
        widget=widgets.RadioSelectHorizontal
    )

    pers15 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label='entspannt ist, mit Stress gut umgehen kann',
        widget=widgets.RadioSelectHorizontal
    )

    pers_rely = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label='Meine Antworten sind zuverlässig',
        widget=widgets.RadioSelectHorizontal
    )

    risk = models.IntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        label='Wie sehr sind Sie bereit oder nicht bereit, Risiken einzugehen.',
        widget=widgets.RadioSelectHorizontal
    )

    patience = models.IntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        label='Wie sehr wären Sie bereit auf etwas, das für Sie heute Nutzen bringt, zu verzichten, um dadurch in Zukunft mehr zu profitieren?',
        widget=widgets.RadioSelectHorizontal
    )

    punish_you = models.IntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        label='Wie sehr wären Sie bereit, jemanden zu bestrafen, der <b> Sie </b> unfair behandelt, selbst wenn dies für Sie negative Konsequenzen haben würde?',
        widget=widgets.RadioSelectHorizontal
    )

    punish_other = models.IntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        label='Wie sehr wären Sie bereit, jemanden zu bestrafen, der <b> andere </b> unfair behandelt, selbst wenn dies für Sie Kosten verursachen würde?',
        widget=widgets.RadioSelectHorizontal
    )

    alturism = models.IntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        label='Wie sehr wären Sie bereit, für einen guten Zweck zu geben, ohne etwas als Gegenleistung zu erwarten.',
        widget=widgets.RadioSelectHorizontal
    )

    pos_res = models.IntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        label='Wenn mir jemanden einen Gefallen tut, bin ich bereit ihn zu erwidern.',
        widget=widgets.RadioSelectHorizontal
    )

    neg_res = models.IntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        label='Wenn ich sehr ungerecht behandelt werde, räche ich mich bei der ersten Gelegenheit, selbst wenn Kosten entstehen, um das zu tun.',
        widget=widgets.RadioSelectHorizontal
    )

    trust = models.IntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        label='Ich vermute, dass Leute nur die besten Absichten haben.',
        widget=widgets.RadioSelectHorizontal
    )

    math = models.IntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        label='Ich bin gut in Mathematik.',
        widget=widgets.RadioSelectHorizontal
    )

    control = models.IntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        label='Ich neige dazu, Aufgaben zu verschieben, auch wenn ich weiß, dass es besser wäre sie gleich zu tun.',
        widget=widgets.RadioSelectHorizontal
    )


