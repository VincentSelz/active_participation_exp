from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
	Currency as c, currency_range
)
import decimal
import random
#from django.core.mail import send_mail
# from otree import widgets

from django.db import models as django_models



author = ''

doc = """
	Start Page for Online Experiments
"""


class Constants(BaseConstants):
	name_in_url = 'IajrWRoi'
	players_per_group = None
	num_rounds = 1


class Subsession(BaseSubsession):
	pass


class Group(BaseGroup):
	pass


class Player(BasePlayer):
	
	# Stores the subject's email address, used to identify the subject 
	# across the two sessions.
	email = django_models.EmailField(verbose_name='')
	# Auxiliary field to allow for server side email validation.
	email_validate = django_models.EmailField(verbose_name='')

	# Save user's browser data on StartPage Page, 
	# before mobiles are screened out. 
	user_agent = models.StringField()
	window_height = models.StringField()
	window_width = models.StringField()
	is_iPad_iOS13 = models.BooleanField()

	# Save user's browser data on StartPage Page, 
	# after mobiles have been screened out. 
	user_agent2 = models.StringField()
	window_height2 = models.StringField()
	window_width2 = models.StringField()
	is_iPad_iOS13_2 = models.BooleanField()

