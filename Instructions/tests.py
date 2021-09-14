from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

from otree.api import SubmissionMustFail


class PlayerBot(Bot):

    def play_round(self):
        # Players 17 and 18 start; 18 drops out in s1, 20 in s2
        if not self.player.id_in_group in [18]:
            # STARTPAGE
            if self.player.id_in_group == 1:
                # Fail bc emails not the same
                yield SubmissionMustFail(
                    pages.StartPage, {
                        'email': '{}@bot.de'.format(
                            self.player.id_in_group
                        ),
                        'email_validate': '{}@bod.de'.format(
                            self.player.id_in_group
                        ),
                        'window_height': '1000px',
                        'window_width': '800px',
                        'user_agent': 'test',
                        'is_iPad_iOS13': False,
                        'consent1': 1
                    },
                    error_fields=['__all__']
                )
                # Fail bc no consent given
                # CANNOT BE CHECKED - consent condition is
                # validated via javascript!
                # yield SubmissionMustFail(
                #     pages.StartPage, {
                #         'email': '{}@bot.de'.format(
                #             self.player.id_in_group
                #         ),
                #         'email_validate': '{}@bot.de'.format(
                #             self.player.id_in_group
                #         ),
                #         'window_height': '1000px',
                #         'window_width': '800px',
                #         'user_agent': 'test',
                #         'is_iPad_iOS13': False,
                #         'consent1': 0
                #     }
                # )
                # Submit mobi
                yield pages.StartPage, {
                    'email': '{}@bot.de'.format(
                        self.player.id_in_group
                    ),
                    'email_validate': '{}@bot.de'.format(
                        self.player.id_in_group
                    ),
                    'window_height': '1000px',
                    'window_width': '800px',
                    'user_agent': 'Mobile',
                    'is_iPad_iOS13': False,
                    'consent1': 1
                }
            elif self.player.id_in_group == 2:
                # Submit multitouch
                yield pages.StartPage, {
                    'email': '{}@bot.de'.format(
                        self.player.id_in_group
                    ),
                    'email_validate': '{}@bot.de'.format(
                        self.player.id_in_group
                    ),
                    'window_height': '1000px',
                    'window_width': '800px',
                    'user_agent': 'test',
                    'is_iPad_iOS13': True,
                    'consent1': 1
                }
            else:
                yield pages.StartPage, {
                    'email': '{}@bot.de'.format(
                        self.player.id_in_group
                    ),
                    'email_validate': '{}@bot.de'.format(
                        self.player.id_in_group
                    ),
                    'window_height': '1000px',
                    'window_width': '800px',
                    'user_agent': 'test',
                    'is_iPad_iOS13': False,
                    'consent1': 1
                }
            # SCREENOUT
            # if self.player.id_in_group == 1:
            #     # Fail bc still mobile device
            #     # CANNOT BE TESTED - browser is validated
            #     # via javascript
            #     yield SubmissionMustFail(
            #         pages.ScreenOut, {
            #             'window_height2': '1000px',
            #             'window_width2': '800px',
            #             'user_agent2': 'Mobi',
            #             'is_iPad_iOS13_2': False,
            #         },
            #         error_fields=['__all__']
            #     )
            #     yield SubmissionMustFail(
            #         # Fail bc still multitouch touchpad
            #         # CANNOT BE TESTED - browser is validated
            #         # via javascript
            #         pages.ScreenOut, {
            #             'window_height2': '1000px',
            #             'window_width2': '800px',
            #             'user_agent2': 'test',
            #             'is_iPad_iOS13_2': True,
            #         }
            #     )
            if self.player.id_in_group in [1, 2]:
                yield pages.ScreenOut, {
                    'window_height2': '1000px',
                    'window_width2': '800px',
                    'user_agent2': 'test',
                    'is_iPad_iOS13_2': False,
                }
        else:
            yield pages.StartPage, {
                'email': '{}@bot.de'.format(
                    self.player.id_in_group
                ),
                'email_validate': '{}@bot.de'.format(
                    self.player.id_in_group
                ),
                'window_height': '1000px',
                'window_width': '800px',
                'user_agent': 'test',
                'is_iPad_iOS13': False,
                'consent1': 1
            }
