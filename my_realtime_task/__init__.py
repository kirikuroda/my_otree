from otree.api import *
import random
import numpy as np

doc = """
Your app description
"""

class Constants(BaseConstants):
    name_in_url = 'my_simple_survey'
    players_per_group = 3
    num_rounds = 4
    trial = [
        ["How many meters high is Mount Fuji?", 3776],
        ["How many kilometers is one full marathon?", 42.195],
        ["What year is it now?", 2021],
        ["How many countries and regions will participate in Tokyo 2020 Olympics?", 206]
    ]
    order = np.random.permutation([0, 1, 2, 3])


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    answer = models.FloatField(label = "Please enter your answer.")
    name = models.StringField(label = "Please enter your name (e.g., Kiri).")
    result = models.StringField()
    done = models.IntegerField()
    rank = models.IntegerField()

def set_name(player: Player):
    if (player.round_number == 1):
        player.participant.name = player.name

# PAGES
class MyName(Page):
    form_model = "player"
    form_fields = ["name"]
    @staticmethod
    def is_displayed(player):
         # Only Round 1
        return player.round_number == 1
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_name(player)

def initialize_done(group: Group):
    players = group.get_players()
    for player in players:
        player.done = 0
        player.rank = 0

class WaitPlayersPage(WaitPage):
    after_all_players_arrive = "initialize_done"

class Quiz(Page):
    form_model = "player"
    form_fields = ["answer"]
    # timeout_seconds = 10
    @staticmethod
    def vars_for_template(player):
        return dict(
            self_id = player.id_in_group,
            question = Constants.trial[Constants.order[player.round_number - 1]][0]
        )
    @staticmethod
    def live_method(player, data):
        player.done = 1
        id = player.id_in_group
        players = player.get_others_in_group()
        players_id = [player.id_in_group for player in players]
        response = dict(id_in_group = id, answer = data)
        message = {}
        for i in range(len(players_id)):
            message[players_id[i]] = response
            player.rank += players[i].done
        player.rank += 1
        return message

class CountdownPage(Page):
    timeout_seconds = 5

class ResultsWaitPage(WaitPage):
    pass

def correct_or_not(group: Group):
    players = group.get_players()
    for player in players:
        if player.answer == Constants.trial[Constants.order[player.round_number - 1]][1]:
            player.result = "Correct"
        else:
            player.result = "Wrong"

class PreFeedbackPage(WaitPage):
    after_all_players_arrive = "correct_or_not"

class Results(Page):
    @staticmethod
    def vars_for_template(player):
        return dict(
            self_id = player.id_in_group
        )

page_sequence = [MyName, WaitPlayersPage, CountdownPage, Quiz, PreFeedbackPage, Results]
