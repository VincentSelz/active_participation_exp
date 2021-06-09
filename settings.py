from os import environ


SESSION_CONFIGS = [
    dict(
        name='main_exp',
        display_name='Main Experiment',
        num_demo_participants=2,
        app_sequence=['main_exp'],
    ),
    dict(
        name='survey',
        display_name='Survey',
        num_demo_participants=2,
        app_sequence=['survey'],
    ),
    dict(
        name='StartPage',
        display_name='Start Page',
        num_demo_participants=2,
        app_sequence=['StartPage'],
    ),
    dict(
        name='Iban',
        display_name='IBAN Module',
        num_demo_participants=2,
        app_sequence=['Iban'],
    ),
    dict(
        name='bigfive',
        display_name='Big Five',
        num_demo_participants=2,
        app_sequence=['bigfive'],
    ),
    dict(
        name='Allin1',
        display_name='All apps',
        num_demo_participants=2,
        app_sequence=['StartPage','main_exp','survey', 'bigfive','Iban'],
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'de'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(
        name='experiment',
        display_name='Experiment',
        participant_label_file='_rooms/real_exp.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'adminweb56'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '$t7t4i*%#f6%#)639kf*wkj_ig*l8o^6w&kpr%j$yv*li4arlm'

INSTALLED_APPS = ['otree', 'radiogrid']
