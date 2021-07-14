from otree.api import *

doc = """
Back button for multiple instructions pages
"""

class Constants(BaseConstants):
    name_in_url = 'back_button'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Instructions(Page):
    pass


class Task(Page):
    pass


page_sequence = [Instructions, Task]
