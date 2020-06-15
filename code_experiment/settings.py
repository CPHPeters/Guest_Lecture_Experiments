from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

mturk_hit_settings = {
    'keywords': ['study', 'academic'],
    'title': 'Answer Two Questions',
    'description': 'This study is conducted anonymously. Answer two questions about your daily life.',
    'frame_height': 500,
    #'preview_template': 'global/MTurkPreview.html',
    'template': 'global/mturk_template.html',
    'minutes_allotted_per_assignment': 5,
    'expiration_hours': 7*24, # 7 days
    #'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    # 'qualification_requirements': [
    #     # No-retakers
    #     {
    #         'QualificationTypeId': "30LLG2NWCXJ09FSUO3LGVGEKYUS095",
    #         'Comparator': "DoesNotExist",
    #     },
    #     # Only US
    #     {
    #         'QualificationTypeId': "00000000000000000071",
    #         'Comparator': "EqualTo",
    #         'LocaleValues': [{'Country': "US"}]
    #     },
    #     # At least x HITs approved
    #     {
    #         'QualificationTypeId': "00000000000000000040",
    #         'Comparator': "GreaterThanOrEqualTo",
    #         'IntegerValues': [500]
    #     },
    #     # At least x% of HITs approved
    #     {
    #         'QualificationTypeId': "000000000000000000L0",
    #         'Comparator': "GreaterThanOrEqualTo",
    #         'IntegerValues': [98]
    #     },
    #     ]
}

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc="", 'mturk_hit_settings': mturk_hit_settings
)

SESSION_CONFIGS = [
    dict(
       name='attribute_subsitution',
       display_name="Attribute Substitution Game",
       num_demo_participants=3,
       app_sequence=['attribute_substitution']
    ),
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 't#6s^86)7x-5&_7ets-@m137vd5@*wv*7y9npk6&ze-^c^^7(!'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
