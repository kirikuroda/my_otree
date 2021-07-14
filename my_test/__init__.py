from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'my_test'
    players_per_group = 3 # 3人のゲーム
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    subtraction_answer = models.IntegerField()
    


# PAGES
class MyPage(Page):
    form_model = "player"
    form_fields = ["subtraction_answer"]
    @staticmethod
    def live_method(player, data):
        my_id = player.id_in_group
        response = dict(id_in_group = my_id, answer = data)
        return {0: response}


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, Results]
