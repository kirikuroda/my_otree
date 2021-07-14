from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'random_question_order'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    aaa = models.BooleanField()
    bbb = models.BooleanField()
    ccc = models.StringField()
    ddd = models.IntegerField()


# PAGES
class MyPage(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        import random

        form_fields = ['aaa', 'bbb', 'ccc', 'ddd']
        random.shuffle(form_fields)
        return form_fields


page_sequence = [MyPage]
