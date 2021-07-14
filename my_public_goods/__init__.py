from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'my_public_goods'
    players_per_group = 3
    num_rounds = 1
    endowment = cu(1000)
    multiplier = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()


class Player(BasePlayer):
    # 提供額はプレイヤーごとに記録したいからPlayerクラスで定義
    contribution = models.CurrencyField(
        min = 0,
        max = Constants.endowment,
        label = "How much will you contribute?"
    )

# 利得を計算する関数
def set_payoffs(group: Group):
    players = group.get_players()
    contributions = [p.contribution for p in players]
    group.total_contribution = sum(contributions)
    group.individual_share = (
        group.total_contribution * Constants.multiplier / Constants.players_per_group
    )
    for p in players:
        p.payoff = Constants.endowment - p.contribution + group.individual_share

# PAGES
class MyPage(Page):
    pass

# フォームはPageで定義
class Contribute(Page):
    form_model = "player"
    form_fields = ["contribution"]

# 全員揃ったら、関数set_payoffsを実行
class ResultsWaitPage(WaitPage):
    body_text = "Custom body text"
    after_all_players_arrive = "set_payoffs"


class Results(Page):
    pass


page_sequence = [Contribute, ResultsWaitPage, Results]
