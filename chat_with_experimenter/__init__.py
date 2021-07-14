from otree.api import *


doc = """
Chat with experimenter, using Papercups
"""


class Constants(BaseConstants):
    name_in_url = 'chat_with_experimenter'
    players_per_group = None
    num_rounds = 1
    papercups_template = __name__ + '/papercups_kk.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class MyPage(Page):
    pass


page_sequence = [MyPage]
