from otree.api import *




class Constants(BaseConstants):
    name_in_url = 'redirect_to_other_website'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    citizenship = models.StringField()



class MyPage(Page):
    form_model = 'player'
    form_fields = ['citizenship']


class Redirect(Page):
    @staticmethod
    def js_vars(player: Player):
        # google is just an example. you should change this to qualtrics or whatever survey provider
        # you are using.
        return dict(redirect_url='https://www.google.com/search?q=' + player.citizenship)


page_sequence = [MyPage, Redirect]
