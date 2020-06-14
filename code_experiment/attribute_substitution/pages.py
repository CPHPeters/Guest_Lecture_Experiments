from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Page1(Page):
    form_model = 'player'
    form_fields = ['question_1']

class Page2(Page):
    form_model = 'player'
    form_fields = ['question_2']

page_sequence = [Page1, Page2]
