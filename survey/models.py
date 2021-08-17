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

    # number of levels
    n = 10

    # Levels of scale for self-assessment
    levels = [str(j) for j in range(n + 1)]

    # Choices
    choices = [[str(j), ''] for j in range(n + 1)]



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
        choices=[['HS', 'Abitur'], ['BA', 'Grundstudium'], ['MA', 'Master'], ['more', 'höher, nämlich']],
        label='Was ist der höchste Abschluss, den Sie abgeschlossen haben?',
        widget=widgets.RadioSelect,
    )

    work = models.StringField(
        choices=[['student', 'Studierende'], ['worker', 'Arbeitnehmer'], ['retired', 'Pensioniert'], ['other', 'Anderse']],
        label='Wie ist Ihr aktueller Status?',
        widget=widgets.RadioSelect,
    )

    income = models.IntegerField(label='Wie viel Geld haben Sie monatlich zur Verfügung? (in Euro)', min=0, max=99999)

    risk = models.StringField(
        choices=Constants.choices,
        label='Wie sehr sind Sie bereit oder nicht bereit, Risiken einzugehen?',
        widget=widgets.RadioSelect
    )

    patience = models.StringField(
        choices=Constants.choices,
        label='Wie sehr wären Sie bereit auf etwas, das für Sie heute Nutzen bringt, zu verzichten, um dadurch in Zukunft mehr zu profitieren?',
        widget=widgets.RadioSelect
    )

    punish_you = models.StringField(
        choices=Constants.choices,
        label='Wie sehr wären Sie bereit, jemanden zu bestrafen, der "Sie" unfair behandelt, selbst wenn dies für Sie negative Konsequenzen haben würde?',
        widget=widgets.RadioSelect
    )

    punish_other = models.StringField(
        choices=Constants.choices,
        label='Wie sehr wären Sie bereit, jemanden zu bestrafen, der "andere" unfair behandelt, selbst wenn dies für Sie Kosten verursachen würde?',
        widget=widgets.RadioSelect
    )

    alturism = models.StringField(
        choices=Constants.choices,
        label='Wie sehr wären Sie bereit, für einen guten Zweck zu geben, ohne etwas als Gegenleistung zu erwarten.',
        widget=widgets.RadioSelect
    )

    pos_res = models.StringField(
        choices=Constants.choices,
        label='Wenn mir jemanden einen Gefallen tut, bin ich bereit ihn zu erwidern.',
        widget=widgets.RadioSelect
    )

    neg_res = models.StringField(
        choices=Constants.choices,
        label='Wenn ich sehr ungerecht behandelt werde, räche ich mich bei der ersten Gelegenheit, selbst wenn Kosten entstehen, um das zu tun.',
        widget=widgets.RadioSelect
    )

    trust = models.StringField(
        choices=Constants.choices,
        label='Ich vermute, dass Leute nur die besten Absichten haben.',
        widget=widgets.RadioSelect
    )

    math = models.StringField(
        choices=Constants.choices,
        label='Ich bin gut in Mathematik.',
        widget=widgets.RadioSelect
    )

    control = models.StringField(
        choices=Constants.choices,
        label='Ich neige dazu, Aufgaben zu verschieben, auch wenn ich weiß, dass es besser wäre sie gleich zu tun.',
        widget=widgets.RadioSelect
    )


