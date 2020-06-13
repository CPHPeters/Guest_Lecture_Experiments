from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'attribute_substitution'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        import itertools
        number = itertools.cycle([0,1])
        for player in self.get_players():
            player.treatment = next(number)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.IntegerField()
    question_1 = models.IntegerField(label="", blank=False)
    question_2 = models.IntegerField(label="", blank=False)
