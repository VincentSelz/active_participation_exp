from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random as random

def get_timeout_seconds(self):
    participant = self.participant
    import time
    return participant.vars['expiry'] - time.time()

class DemoIntro(Page):
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

class TrueStart(Page):
    def before_next_page(self):
        participant = self.participant
        import time
        participant.vars['expiry'] = time.time() + Constants.task_timeout

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'

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

class Type(Page):
    pass

class Total_Results(Page):
    def vars_for_template(self):
        me = self.player
        opponent = me.get_others_in_group()[0]
        return dict(
            my_performance=me.current_max_is,
            my_costs=me.total_costs,
            my_task_earning=me.task_earning,
            my_bonus_earning=me.bonus_earning,
            my_payoff=me.payoff,
            my_payoff_real_money=me.payoff.to_real_world_currency(self.session),
            other_performance=opponent.current_max_is,
            total_performance=max(me.current_max_is,opponent.current_max_is),
            pay_inattent=Constants.pay_inattention
        )

class Animation(Page):
    timeout_seconds = 10
    def is_displayed(self):
        return get_timeout_seconds(self) > 3

class Popup(Page):
    timeout_seconds = 5
    def before_next_page(self):
        if self.timeout_happened == False:
            me = self.player
            me.attention_check = 1


class Task0(Page):
    get_timeout_seconds = get_timeout_seconds
    def is_displayed(self):
        return get_timeout_seconds(self) > 3

    def vars_for_template(self):
        me = self.player
        if me.type == 'r1':
            me.lowerbound=Constants.high_ability[0]
            me.upperbound=Constants.high_ability[1]
        elif self.player.type == 'r2':
            me.lowerbound=Constants.low_ability[0]
            me.upperbound=Constants.low_ability[1]
        return dict(
            lower=me.lowerbound,
            upper=me.upperbound,
            my_max=0,
            my_num_draws=0,
        )

    def before_next_page(self):
        if self.timeout_happened == False:
            me = self.player
            me.draw_1 = random.randint(me.lowerbound,me.upperbound)
            self.participant.vars['draws']=[0,me.draw_1,]
            me.num_draws = 1
            me.current_max_is = max(self.participant.vars['draws'])

class Task1(Page):
    get_timeout_seconds = get_timeout_seconds
    def is_displayed(self):
        return get_timeout_seconds(self) > 3

    def vars_for_template(self):
        me = self.player
        return dict(
            lower=me.lowerbound,
            upper=me.upperbound,
            my_max=me.current_max_is,
            my_num_draws=me.num_draws,
            my_last=self.participant.vars['draws'][-1],
        )
        
    def before_next_page(self):
        if self.timeout_happened == False:
            me = self.player
            me.draw_2 = random.randint(me.lowerbound,me.upperbound)
            self.participant.vars['draws'].append(me.draw_2)
            me.num_draws = me.num_draws + 1
            me.current_max_is = max(self.participant.vars['draws'])

class Task2(Page):
    get_timeout_seconds = get_timeout_seconds
    def is_displayed(self):
        return get_timeout_seconds(self) > 3

    def vars_for_template(self):
        me = self.player
        return dict(
            lower=me.lowerbound,
            upper=me.upperbound,
            my_max=me.current_max_is,
            my_num_draws=me.num_draws,
            my_last=self.participant.vars['draws'][-1],
        )
        
    def before_next_page(self):
        if self.timeout_happened == False:
            me = self.player
            me.draw_3 = random.randint(me.lowerbound,me.upperbound)
            self.participant.vars['draws'].append(me.draw_3)
            me.num_draws = me.num_draws + 1
            me.current_max_is = max(self.participant.vars['draws'])

class Task3(Page):
    get_timeout_seconds = get_timeout_seconds
    def is_displayed(self):
        return get_timeout_seconds(self) > 3

    def vars_for_template(self):
        me = self.player
        return dict(
            lower=me.lowerbound,
            upper=me.upperbound,
            my_max=me.current_max_is,
            my_num_draws=me.num_draws,
            my_last=self.participant.vars['draws'][-1],
        )
        
    def before_next_page(self):
        if self.timeout_happened == False:
            me = self.player
            me.draw_4 = random.randint(me.lowerbound,me.upperbound)
            self.participant.vars['draws'].append(me.draw_4)
            me.num_draws = me.num_draws + 1
            me.current_max_is = max(self.participant.vars['draws'])


class Task4(Page):
    get_timeout_seconds = get_timeout_seconds
    def is_displayed(self):
        return get_timeout_seconds(self) > 3

    def vars_for_template(self):
        me = self.player
        return dict(
            lower=me.lowerbound,
            upper=me.upperbound,
            my_max=me.current_max_is,
            my_num_draws=me.num_draws,
            my_last=self.participant.vars['draws'][-1],
        )
        
    def before_next_page(self):
        if self.timeout_happened == False:
            me = self.player
            me.draw_5 = random.randint(me.lowerbound,me.upperbound)
            self.participant.vars['draws'].append(me.draw_5)
            me.num_draws = me.num_draws + 1
            me.current_max_is = max(self.participant.vars['draws'])

class Task5(Page):
    get_timeout_seconds = get_timeout_seconds
    def is_displayed(self):
        return get_timeout_seconds(self) > 3

    def vars_for_template(self):
        me = self.player
        return dict(
            lower=me.lowerbound,
            upper=me.upperbound,
            my_max=me.current_max_is,
            my_num_draws=me.num_draws,
            my_last=self.participant.vars['draws'][-1],
        )
        
    def before_next_page(self):
        if self.timeout_happened == False:
            me = self.player
            me.draw_6 = random.randint(me.lowerbound,me.upperbound)
            self.participant.vars['draws'].append(me.draw_6)
            me.num_draws = me.num_draws + 1
            me.current_max_is = max(self.participant.vars['draws'])

class Task6(Page):
    get_timeout_seconds = get_timeout_seconds
    def is_displayed(self):
        return get_timeout_seconds(self) > 3

    def vars_for_template(self):
        me = self.player
        return dict(
            lower=me.lowerbound,
            upper=me.upperbound,
            my_max=me.current_max_is,
            my_num_draws=me.num_draws,
            my_last=self.participant.vars['draws'][-1],
        )
        
    def before_next_page(self):
        if self.timeout_happened == False:
            me = self.player
            me.draw_7 = random.randint(me.lowerbound,me.upperbound)
            self.participant.vars['draws'].append(me.draw_7)
            me.num_draws = me.num_draws + 1
            me.current_max_is = max(self.participant.vars['draws'])

class Task7(Page):
    get_timeout_seconds = get_timeout_seconds
    def is_displayed(self):
        return get_timeout_seconds(self) > 3

    def vars_for_template(self):
        me = self.player
        return dict(
            lower=me.lowerbound,
            upper=me.upperbound,
            my_max=me.current_max_is,
            my_num_draws=me.num_draws,
            my_last=self.participant.vars['draws'][-1],
        )
        
    def before_next_page(self):
        if self.timeout_happened == False:
            me = self.player
            me.draw_8 = random.randint(me.lowerbound,me.upperbound)
            self.participant.vars['draws'].append(me.draw_8)
            me.num_draws = me.num_draws + 1
            me.current_max_is = max(self.participant.vars['draws'])

class Task8(Page):
    get_timeout_seconds = get_timeout_seconds
    def is_displayed(self):
        return get_timeout_seconds(self) > 3

    def vars_for_template(self):
        me = self.player
        return dict(
            lower=me.lowerbound,
            upper=me.upperbound,
            my_max=me.current_max_is,
            my_num_draws=me.num_draws,
            my_last=self.participant.vars['draws'][-1],
        )
        
    def before_next_page(self):
        if self.timeout_happened == False:
            me = self.player
            me.draw_9 = random.randint(me.lowerbound,me.upperbound)
            self.participant.vars['draws'].append(me.draw_9)
            me.num_draws = me.num_draws + 1
            me.current_max_is = max(self.participant.vars['draws'])

class Task9(Page):
    get_timeout_seconds = get_timeout_seconds
    def is_displayed(self):
        return get_timeout_seconds(self) > 3

    def vars_for_template(self):
        me = self.player
        return dict(
            lower=me.lowerbound,
            upper=me.upperbound,
            my_max=me.current_max_is,
            my_num_draws=me.num_draws,
            my_last=self.participant.vars['draws'][-1],
        )
        
    def before_next_page(self):
        if self.timeout_happened == False:
            me = self.player
            me.draw_10 = random.randint(me.lowerbound,me.upperbound)
            self.participant.vars['draws'].append(me.draw_10)
            me.num_draws = me.num_draws + 1
            me.current_max_is = max(self.participant.vars['draws'])

class Task10(Page):
    get_timeout_seconds = get_timeout_seconds
    def is_displayed(self):
        return get_timeout_seconds(self) > 3

    def vars_for_template(self):
        me = self.player
        return dict(
            lower=me.lowerbound,
            upper=me.upperbound,
            my_max=me.current_max_is,
            my_num_draws=me.num_draws,
            my_last=self.participant.vars['draws'][-1],
        )
        
    def before_next_page(self):
        if self.timeout_happened == False:
            me = self.player
            me.draw_11 = random.randint(me.lowerbound,me.upperbound)
            self.participant.vars['draws'].append(me.draw_11)
            me.num_draws = me.num_draws + 1
            me.current_max_is = max(self.participant.vars['draws'])


class Task11(Page):
    get_timeout_seconds = get_timeout_seconds
    def is_displayed(self):
        return get_timeout_seconds(self) > 3

    def vars_for_template(self):
        me = self.player
        return dict(
            lower=me.lowerbound,
            upper=me.upperbound,
            my_max=me.current_max_is,
            my_num_draws=me.num_draws,
            my_last=self.participant.vars['draws'][-1],
        )
        
    def before_next_page(self):
        if self.timeout_happened == False:
            me = self.player
            me.draw_12 = random.randint(me.lowerbound,me.upperbound)
            self.participant.vars['draws'].append(me.draw_12)
            me.num_draws = me.num_draws + 1
            me.current_max_is = max(self.participant.vars['draws'])

class Task12(Page):
    get_timeout_seconds = get_timeout_seconds
    def is_displayed(self):
        return get_timeout_seconds(self) > 3

    def vars_for_template(self):
        me = self.player
        return dict(
            lower=me.lowerbound,
            upper=me.upperbound,
            my_max=me.current_max_is,
            my_num_draws=me.num_draws,
            my_last=self.participant.vars['draws'][-1],
        )
        
    def before_next_page(self):
        if self.timeout_happened == False:
            me = self.player
            me.draw_13 = random.randint(me.lowerbound,me.upperbound)
            self.participant.vars['draws'].append(me.draw_13)
            me.num_draws = me.num_draws + 1
            me.current_max_is = max(self.participant.vars['draws'])

class Task13(Page):
    get_timeout_seconds = get_timeout_seconds
    def is_displayed(self):
        return get_timeout_seconds(self) > 3

    def vars_for_template(self):
        me = self.player
        return dict(
            lower=me.lowerbound,
            upper=me.upperbound,
            my_max=me.current_max_is,
            my_num_draws=me.num_draws,
            my_last=self.participant.vars['draws'][-1],
        )
        
    def before_next_page(self):
        if self.timeout_happened == False:
            me = self.player
            me.draw_14 = random.randint(me.lowerbound,me.upperbound)
            self.participant.vars['draws'].append(me.draw_14)
            me.num_draws = me.num_draws + 1
            me.current_max_is = max(self.participant.vars['draws'])

class Task14(Page):
    get_timeout_seconds = get_timeout_seconds
    def is_displayed(self):
        return get_timeout_seconds(self) > 3

    def vars_for_template(self):
        me = self.player
        return dict(
            lower=me.lowerbound,
            upper=me.upperbound,
            my_max=me.current_max_is,
            my_num_draws=me.num_draws,
            my_last=self.participant.vars['draws'][-1],
        )
        
    def before_next_page(self):
        if self.timeout_happened == False:
            me = self.player
            me.draw_15 = random.randint(me.lowerbound,me.upperbound)
            self.participant.vars['draws'].append(me.draw_15)
            me.num_draws = me.num_draws + 1
            me.current_max_is = max(self.participant.vars['draws'])

class Task15(Page):
    get_timeout_seconds = get_timeout_seconds
    def is_displayed(self):
        return get_timeout_seconds(self) > 3

    def vars_for_template(self):
        me = self.player
        return dict(
            lower=me.lowerbound,
            upper=me.upperbound,
            my_max=me.current_max_is,
            my_num_draws=me.num_draws,
            my_last=self.participant.vars['draws'][-1],
        )
        
    def before_next_page(self):
        if self.timeout_happened == False:
            me = self.player
            me.draw_16 = random.randint(me.lowerbound,me.upperbound)
            self.participant.vars['draws'].append(me.draw_16)
            me.num_draws = me.num_draws + 1
            me.current_max_is = max(self.participant.vars['draws'])

class Task16(Page):
    get_timeout_seconds = get_timeout_seconds
    def is_displayed(self):
        return get_timeout_seconds(self) > 3

    def vars_for_template(self):
        me = self.player
        return dict(
            lower=me.lowerbound,
            upper=me.upperbound,
            my_max=me.current_max_is,
            my_num_draws=me.num_draws,
            my_last=self.participant.vars['draws'][-1],
        )
        
    def before_next_page(self):
        if self.timeout_happened == False:
            me = self.player
            me.draw_17 = random.randint(me.lowerbound,me.upperbound)
            self.participant.vars['draws'].append(me.draw_17)
            me.num_draws = me.num_draws + 1
            me.current_max_is = max(self.participant.vars['draws'])

class Task17(Page):
    get_timeout_seconds = get_timeout_seconds
    def is_displayed(self):
        return get_timeout_seconds(self) > 3

    def vars_for_template(self):
        me = self.player
        return dict(
            lower=me.lowerbound,
            upper=me.upperbound,
            my_max=me.current_max_is,
            my_num_draws=me.num_draws,
            my_last=self.participant.vars['draws'][-1],
        )
        
    def before_next_page(self):
        if self.timeout_happened == False:
            me = self.player
            me.draw_18 = random.randint(me.lowerbound,me.upperbound)
            self.participant.vars['draws'].append(me.draw_18)
            me.num_draws = me.num_draws + 1
            me.current_max_is = max(self.participant.vars['draws'])

class Task18(Page):
    get_timeout_seconds = get_timeout_seconds
    def is_displayed(self):
        return get_timeout_seconds(self) > 3

    def vars_for_template(self):
        me = self.player
        return dict(
            lower=me.lowerbound,
            upper=me.upperbound,
            my_max=me.current_max_is,
            my_num_draws=me.num_draws,
            my_last=self.participant.vars['draws'][-1],
        )
        
    def before_next_page(self):
        if self.timeout_happened == False:
            me = self.player
            me.draw_19 = random.randint(me.lowerbound,me.upperbound)
            self.participant.vars['draws'].append(me.draw_19)
            me.num_draws = me.num_draws + 1
            me.current_max_is = max(self.participant.vars['draws'])

class Task19(Page):
    get_timeout_seconds = get_timeout_seconds
    def is_displayed(self):
        return get_timeout_seconds(self) > 3

    def vars_for_template(self):
        me = self.player
        return dict(
            lower=me.lowerbound,
            upper=me.upperbound,
            my_max=me.current_max_is,
            my_num_draws=me.num_draws,
            my_last=self.participant.vars['draws'][-1],
        )
        
    def before_next_page(self):
        if self.timeout_happened == False:
            me = self.player
            me.draw_20 = random.randint(me.lowerbound,me.upperbound)
            self.participant.vars['draws'].append(me.draw_20)
            me.num_draws = me.num_draws + 1
            me.current_max_is = max(self.participant.vars['draws'])

class Task20(Page):
    get_timeout_seconds = get_timeout_seconds
    def is_displayed(self):
        return get_timeout_seconds(self) > 3

    def vars_for_template(self):
        me = self.player
        return dict(
            lower=me.lowerbound,
            upper=me.upperbound,
            my_max=me.current_max_is,
            my_num_draws=me.num_draws,
            my_last=self.participant.vars['draws'][-1],
        )
        


page_sequence = [
#    Instruction,
#    Type,
#    DemoIntro,
#    Demo,
    TrueStart,
    Task0,
    Animation,
    Task1,
    Animation,
    Task2,
    Animation,
    Task3,
    Animation,
    Task4,
    Animation,
    Task5,
    Animation,
    Task6,
    Animation,
    Task7,
    Animation,
    Task8,
    Animation,
    Task9,
    Animation,
    Task10,
    Animation,
    Task11,
    Animation,
    Task12,
    Animation,
    Task13,
    Animation,
    Task14,
    Animation,
    Task15,
    Animation,
    Task16,
    Animation,
    Task17,
    Animation,
    Task18,
    Animation,
    Task19,
    Animation,
    Task20,
    Popup,
    Individual_Results,
    Hypothetical1,
    Hypothetical2,
    Hypothetical3,
    Hypothetical4,
    Hypothetical5,
    Hypothetical6,
    Bonus,
    ResultsWaitPage,
    Total_Results,
]
