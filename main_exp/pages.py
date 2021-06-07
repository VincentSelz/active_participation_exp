from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    pass

class Type(Page):
    pass

class Demo(Page):
    def js_vars(self):
        if self.player.type == 'r1':
            random_draw=Constants.high_example
            lower_bound=Constants.high_ability[0]
            upper_bound=Constants.high_ability[1]
        elif self.player.type == 'r2':
            random_draw=Constants.low_example
            lower_bound=Constants.low_ability[0]
            upper_bound=Constants.low_ability[1]
        return dict(
            random_draw=random_draw,
            animation_time=Constants.animation_time,
            min=lower_bound,
            max=upper_bound,
        )

class Task(Page):
    timeout_seconds = Constants.task_timeout
    form_model = 'player'
    form_fields = [
        'draw_1','draw_2','draw_3','draw_4','draw_5','draw_6',
        'draw_7','draw_8','draw_9','draw_10','draw_11','draw_12',
        'draw_13','draw_14','draw_15','draw_16','draw_17','draw_18',
        'draw_19','draw_20','current_max_is','num_draws','attention_check',
        'prompt_counter','Task_warnings'
    ]
    def js_vars(self):
        pop_up_start=Constants.pop_up_time
        pop_up_end=(Constants.pop_up_time-Constants.pop_up_duration)
        if self.player.type == 'r1':
            lower_bound=Constants.high_ability[0]
            upper_bound=Constants.high_ability[1]
        elif self.player.type == 'r2':
            lower_bound=Constants.low_ability[0]
            upper_bound=Constants.low_ability[1]
        return dict(
            min=lower_bound,
            max=upper_bound,
            pop_up_start=pop_up_start,
            pop_up_end=pop_up_end,
            animation_time=Constants.animation_time
        )

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'

class Individual_Results(Page):
    def vars_for_template(self):
        me = self.player
        return dict(
            my_performance=me.current_max_is,
            my_costs=me.total_costs
        )

class Total_Results(Page):
    def vars_for_template(self):
        me = self.player
        opponent = me.get_others_in_group()[0]
        return dict(
            my_performance=me.current_max_is,
            my_costs=me.total_costs,
            my_payoff=me.payoff,
            other_performance=opponent.current_max_is,
            total_performance=max(me.current_max_is,opponent.current_max_is)
        )


page_sequence = [
    Demo,
    Task,
    ResultsWaitPage,
    Individual_Results,
    Total_Results]
