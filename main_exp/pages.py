from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Task(Page):
    form_model = 'player'
    form_fields = [
        'draw_1','draw_2','draw_3','draw_4','draw_5','draw_6',
        'draw_7','draw_8','draw_9','draw_10','draw_11','draw_12',
        'draw_13','draw_14','draw_15','draw_16','draw_17','draw_18',
        'draw_19','draw_20','current_max_is','num_draws'
    ]
    def js_vars(self):
        if self.player.id_in_group == 1:
            lower_bound=Constants.high_ability[0]
            upper_bound=Constants.high_ability[1]
        elif self.player.id_in_group == 2:
            lower_bound=Constants.low_ability[0]
            upper_bound=Constants.low_ability[1]
        return dict(
            min=lower_bound,
            max=upper_bound,
        )

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [
    Task,
    ResultsWaitPage,
    Results]
