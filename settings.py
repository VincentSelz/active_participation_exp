from os import environ


SESSION_CONFIGS = [
    dict(
        name='social_treatment',
        display_name='Social Treatment',
        num_demo_participants=2,
        app_sequence=['StartPage','Iban','Instructions','main_exp','survey', 'bigfive','raven_test','rat'],
    ),
    dict(
        name='noisy_treatment',
        display_name='Noisy Tretment',
        num_demo_participants=2,
        app_sequence=['StartPage','Iban','main_exp_noisy','survey', 'bigfive','raven_test','rat'],
    ),
    dict(
        name='computer_treatment',
        display_name='Computer Treatment',
        num_demo_participants=2,
        app_sequence=['StartPage','Iban','Instructions_comp','main_exp_computer','survey', 'bigfive','raven_test','rat'],
    ),
    dict(
        name='main_exp',
        display_name='Main Task',
        num_demo_participants=2,
        app_sequence=['main_exp'],
    ),
    dict(
        name='main_exp_noisy',
        display_name='Main Task - Noisy',
        num_demo_participants=2,
        app_sequence=['main_exp_noisy'],
    ),
    dict(
        name='main_exp_computer',
        display_name='Main Task - Computer',
        num_demo_participants=2,
        app_sequence=['main_exp_computer'],
    ),
    dict(
        name='survey',
        display_name='Survey',
        num_demo_participants=2,
        app_sequence=['survey'],
    ),
    dict(
        name='Instructions',
        display_name='Instructions (social)',
        num_demo_participants=2,
        app_sequence=['Instructions'],
    ),
    dict(
        name='Instructions_comp',
        display_name='Instructions (computer)',
        num_demo_participants=2,
        app_sequence=['Instructions_comp'],
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
        name='rat',
        display_name='Remote Associates Test',
        num_demo_participants=2,
        app_sequence=['rat'],
    ),
    dict(
        name='raven',
        display_name='Raven IQ Test',
        num_demo_participants=2,
        app_sequence=['raven_test'],
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.15, participation_fee=3.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'de'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(
        name='experiments',
        display_name='ExperimentS',
    ),
    dict(
        name='experimentn',
        display_name='ExperimentN',
    ),
    dict(
        name='experimentc',
        display_name='ExperimentC',
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
