from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Type(Page):
    pass

class DemoIntro(Page):
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

class TrueStart(Page):
    pass

class Task(Page):
    timeout_seconds = Constants.task_timeout
    form_model = 'player'
    live_method = 'live_attention'

    form_fields = [
        'draw_1','draw_2','draw_3','draw_4','draw_5','draw_6',
        'draw_7','draw_8','draw_9','draw_10','draw_11','draw_12',
        'draw_13','draw_14','draw_15','draw_16','draw_17','draw_18',
        'draw_19','draw_20','current_max_is','num_draws',
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
    pass

class Individual_Results(Page):
    def vars_for_template(self):
        me = self.player
        return dict(
            my_performance=me.current_max_is,
            my_costs=Constants.cost * me.num_draws,
            pay_inattent=Constants.pay_inattention
        )

class Hypothetical1(Page):
    form_model = 'player'
    form_fields = ['strategy']

class Hypothetical2(Page):
    form_model = 'player'
    form_fields = ['altcost']

    def vars_for_template(self):
        return dict(
            cost=Constants.cost,
            cost_alt=Constants.cost_alt
        )


class Hypothetical3(Page):
    form_model = 'player'
    form_fields = ['altbound']

    def vars_for_template(self):
        if self.player.type == 'r1':
            lower_bound=Constants.high_ability[0]
            upper_bound=Constants.high_ability[1]
            lower_alt=Constants.high_ability_alt[0]
            upper_alt=Constants.high_ability_alt[1]
        elif self.player.type == 'r2':
            lower_bound=Constants.low_ability[0]
            upper_bound=Constants.low_ability[1]
            lower_alt=Constants.low_ability_alt[0]
            upper_alt=Constants.low_ability_alt[1]
        return dict(
            min=lower_bound,
            max=upper_bound,
            min_alt=lower_alt,
            max_alt=upper_alt,
        )


class Hypothetical4(Page):
    form_model = 'player'
    form_fields = ['belief']

    def vars_for_template(self):
        if self.player.type == 'r1':
            lower_opp=Constants.low_ability[0]
            upper_opp=Constants.low_ability[1]
        elif self.player.type == 'r2':
            lower_opp=Constants.high_ability[0]
            upper_opp=Constants.high_ability[1]
        return dict(
            min_opp=lower_opp,
            max_opp=upper_opp,
        )

class Hypothetical5(Page):
    form_model = 'player'
    form_fields = ['expectation']

class Hypothetical6(Page):
    form_model = 'player'
    form_fields = ['ideal']

class Bonus(Page):
    form_model = 'player'
    form_fields = ['bonusq']

    # calculate payoffs here
    def before_next_page(self):
        self.player.set_payoffs()


class Total_Results(Page):
    def vars_for_template(self):
        me = self.player
        return dict(
            my_performance=me.current_max_is,
            my_costs=me.total_costs,
            my_task_earning=me.task_earning,
            my_bonus_earning=me.bonus_earning,
            my_payoff=me.payoff,
            my_payoff_real_money=me.payoff.to_real_world_currency(self.session),
            other_performance=me.computer_performance,
            total_performance=max(me.current_max_is,me.computer_performance),
            pay_inattent=Constants.pay_inattention
        )


page_sequence = [
#    Instruction,
    Type,
    DemoIntro,
    Demo,
    TrueStart,
    Task,
    Individual_Results,
    Hypothetical1,
    Hypothetical2,
    Hypothetical3,
    Hypothetical4,
    Hypothetical5,
    Hypothetical6,
    Bonus,
#    ResultsWaitPage,
    Total_Results,
]
