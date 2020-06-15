<h1 align="center">Running Online Experiments</h1>

<p>
Want to learn how to build a state-of-the-art experiment and run it in an online participant pool? This repository will get you started. This repository mainly functions as a companion to guest lectures about programming experiments. However, the repository can also be used on a standalone basis. Recent slides and example code are provided in this repository.
</p>

<p align = "center">
  <span style='font-size: 15pt'><strong>Author:</strong> Christian Peters (<a href="https://www.tilburguniversity.edu/staff/c-p-h-peters">Profile</a>, <a href="http://www.christianpeters.site">Website</a>)</span>
</p>

<p align = "center">
   <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
</p>  

## Table of Contents

* [Introduction](#introduction)
* [Installation](#installation)
* [The Building Blocks of oTree](#otree)
    * [Templates](#templates)
    * [Models.py](#models)
    * [Pages.py](#pages)
    * [Settings.py](#settings)
* [Your First Experiment](#first_experiment)
* [Connecting oTree to Heroku](#heroku)
    * [oTree Hub](#otreehub)
    * [GitHub](#github)
    * [Command Prompt](#commandprompt)
* [Publishing your Experiment on Amazon Mechanical Turk](#mturk)
* [Questions?](#questions)
* [Disclaimer](#disclaimer)
* [License](#license)

<h2 id="introduction">Introduction</h2>

Welcome to this repository on how to run online experiments. The goal of this repository is help to get you from your initial research design to a programmed experiment that can be distributed to any participant pool. This will be divided into three steps. First, I will focus on how you can program an experiment using oTree software. oTree is opensource, platform-independent and online, allowing you to run experiments anywhere at any time. oTree is developed by Daniel Chen, Martin Schonger, and Chris Wickens (2016) and you can use it for free under a Creative Commons license. Although I will explain the building blocks of oTree programming, learning-by-doing is necessary. I would definitely recommend to have a look at <a href="https://otree.readthedocs.io/en/latest/" target="_blank">otree.readthedocs.io</a>, which is a large repository containing a lot of information about oTree. To learn oTree, no prior programming experience is necessary, although prior knowledge of Python, HTML, CSS, and Javascript can be helpful. Second, I show how to deploy your experiment to an online server to make it available through a webpage that participants can visit. Third, I show how to make your experiment available to an online participant pool (Amazon's Mechanical Turk).

Before getting started, I would like to mention one caveat. oTree allows for many features up-and-above other software such as chat functions, interactions, timeouts, etc. However, if you are designing a study that does not need such a design, usage of point-and-click software such as Qualtrics may be more efficient.

<h2 id="installation">Installation</h2>

<h3 id="setup">Getting Your Setup Ready</h3>
oTree is based on Django. Django is a rich framework that makes it easier to program web applications using the Python programming language. To use Django, you need to install Python. In case you have not installed Python before, you can download and install Python <a href="https://www.python.org/downloads/" target="_blank">here</a>.

Second, you may want to install a code editor that makes programming easier. A code editor highlights syntax, checks for errors, and helps debugging. An example of a code editor is <a href="https://www.jetbrains.com/pycharm/download/" target="_blank">PyCharm</a>. If you are a student or educator, you can download the professional version for free.

<h3 id="otree_installation">Installing oTree</h3>
Once Python and PyCharm are installed, you can start by opening your Command Prompt (or Terminal in case you use iOS). To install oTree, enter:

```bash
pip3 install -U otree
```

Once oTree is installed, you can create your first oTree project. By using the "cd" command (change directory) you can specify the path where you want to install the oTree project folder. For instance, when I would type:

```bash
cd "C:\Users\Christian\Desktop"
```

I would install it on my desktop. Specify the folder where you would like your oTree project to be located and hit:

```bash
otree startproject project_name
```

where you can input the name of your project for 'project_name'. Next, oTree will ask whether you want to install sample games. oTree includes a large library of sample games that you can use, these can also be examined and tested <a href="http://otree-demo.herokuapp.com/demo/" target="_blank">here</a>. If you want them to be included in your project folder hit "y" and if not hit "n". Next move into change the directory of the command prompt to inside your project folder by typing:

```bash
cd project_name
```

where you insert your project name for <i>project_name</i>, now the command prompt should indicate that you are in the project folder. In your case, you probably do not want to use one of the standard games provided by oTree but to create your own experiment. If so, you need to create an app. An app is a subset of an oTree project folder. An experiment (your project) can contain multiple apps. For instance, you may want your participants to first conduct a Public Goods Game and afterwards a Dictator Game. If so, you can create two separate apps in the same project. To create an app type:

```bash
otree startapp app_name
```

Now you can go to your project folder and inspect it. If all went correctly, you will be able to see your app in your project folder.

<h2 id="otree">The Building Blocks of oTree</h2>

Once you have installed oTree and created an app you are ready to build your own experiment. Before starting, it might be good to look at a 'finished product', an experiment that is actually used for research. <a href="https://taxexperiment.herokuapp.com" target="_blank">Click here</a> to see an experiment used in a recent study by Bart Dierynck, Martin Jacob, Maximilian Müller, Victor van Pelt, and myself. Examples of other experiments and example projects can be found at <a href="https://demo.otree.org" target="_blank">demo.otree.org</a>.

If you examine an experiment, you will see that from a programming-perspective an experiment consists of some things:

<ul>
  <li>Each page has a certain lay-out and text</li>
  <li>There are multiple pages in a certain order</li>
  <li>Variables are elicited from participants</li>
  <li>There are some rules of the experiment (e.g., monetary payoffs)</li>
</ul>

These can be seen as the four building blocks of oTree. Before we start programming an example experiment, I will first explain each of the building blocks. Please be aware that these building blocks only help you to get you started, for more information I recommend <a href="https://otree.readthedocs.io" target="_blank">otree.readthedocs.io</a>. You can edit each file by opening Pycharm. Click on `Open` and search for the directory of your oTree project (If you cannot find the oTree project folder see * [Installation](#installation)). Once you click on the project folder and `Ok` your project will open. You can for instance, click on one of the templates and the code of that template will show up in the main frame such as shown in the screenshot below.

![PyCharm](/images/pycharm.PNG)
<p align="center"><i>A screenshot of PyCharm with the default code for a Template</i></p>

<h3 id="templates">Templates</h3>

The first building block are the templates: every page in an experiment is a template with a certain lay-out and text. Templates are `.html` files in which you can use `HTML`, `CSS`, `Javascript`, and `Django`. You can use any HTML, CSS, and Javascript to build your experiment and change content and lay-out. Django is especially useful here as it allows you to call variables. For instance, if you want to show a choice that the participant made earlier you can call this variable using brackets:

``` html
In Round 1, you chose {{ player.choice_r1 }}.
```

In this case the text between brackets is the variable that is called. This variable called `choice_r1` is defined at the player level and hence we use `player.choice_r1`. When you are for example dealing with a group variable - such as the total amount contributed to a public good - or with a subsession variable - such as the round of the subsession - you use `group.` and `subsession.` before the variable, respectively.

Next to that, you can use `if`, `while`, and `for` statements to condition. For instance, if you use a textual manipulation in your experiment, you want to show one text to one condition, whereas you want to show another text to the other condition. For this we use brackets and percentage signs. For instance:
  
``` html
{% if player.treatment == 0 %}
  <p>The company made a profit last year.</p>
{% elif player.treatment == 1 %}
  <p>The company made a loss last year.</p>
{% endif %}
```

Here, if a participant is in treatment "0", she will see that the company made a profit last year. However, if the participant is in treatment "1", she will see that the company made a loss last year. Here `elif` stands for 'else if'. If you only have two treatments you could also use `{% else %}` instead of `{% elif player.treatment == 1 %}`, since else applies to every participant for which the `if`-statement is not satisfied. Do not forget the `{% endif %}` to indicate where your conditioning ends.

If you want to elicit variables from participants on a particular page you can use `{% formfields %}` if you want to elicit all variables allocated to this page in `pages.py` (this will be covered later), or `{% formfield player.choice_r1 %}` to elicit a particular variable.

<h3 id="models">Models.py</h3>

In `Models.py` you define the variables that will be stored in your data-output. For instance, if you want to ask the age of a participant you create a variable:

```python
age = models.IntegerField(label="What is your age?")
```
Here, a model is a database table and a field is one column within that table. In this case, an IntegerField is used, indicating that only integer numbers are valid. The `label` determines the text that is shown to participants next to the variable. There are six stringfields that you can use:

* `IntegerField` for integer numbers
* `FloatField` for numbers that may include decimals
* `StringField` for strings of text
* `LongStringField` for long strings of text
* `BooleanField` for True/False values
* `CurrencyField` for currency amounts

If you want to ask a multiple-choice question, you can also use an `IntegerField` with a predefined set of choices. For instance:

```python
    Financial_Literacy = models.IntegerField(
        label = "Suppose you had $100 in a savings account and the interest rate was 2% per year. After 5 years, how much do you think you would have in the account if you left the money to grow?",
        choices = [
            [1, 'More than $102'],
            [2, 'Exactly $102'],
            [3,'Less than $102'],
            [4,"I don't know"]
        ],
    )
```

As explained before, you can define variables at a `Subsession`, `Group` and `Player` level by including the variable under the appropriate class in `Models.py`. However, there is a fourth class called `Constants`. In `Constants` you can put variables that do not vary from player to player such as the number of rounds in the experiment.

If you want to allocate participants to a certain treatment. You need to use a function that can be called by `def` (define). 

```python
class Subsession(BaseSubsession):

    def creating_session(self):
        import itertools
        number = itertools.cycle([0, 1])
        for player in self.get_players():
            player.treatment = next(number)
```

In this code, whenever a subsession is created the following function is executed (`def creating_session(self):`). Here, `(self)` refers to the subsession that is created. We create a variable `number` that cycles between 0 and 1. `itertools.cycle` is a tool that can be used to make sure you have balanced treatments. Next, we start a `for-loop` in which for every player, the player is assigned to a variable `treatment`, which either takes the value `0` or `1`. To do so, you create an empty variable on the player level where the number can be stored:

```python
treatment = models.IntegerField()
```

<h3 id="pages">Pages.py</h3>

In `Pages.py` you define every page that is shown to participants and specify which variables are allocated to that page. For instance:

```python
class Instructions(Page):
    form_model = 'player'
    form_fields = ['Comprehension1', 'Comprehension2']
```

Here, Instructions is the name of the page, and `form_model` refers to the level at which the variables should be stored. `form_fields` includes a list of variables that can be elicited on the page. In this case, we include two comprehension checks that are further defined in `Models.py`. Next to defining and specifying variables for every page, `Pages.py` is also used to determine the page sequence.

```python
page_sequence = [Instructions, Main_Page, Results]
```

Moreover, there are a battery of functions that can be used to specify conditions for each page. For example, the `is_displayed()` function determines conditions to which participants the page is displayed. As functions are currently out of the scope of this tutorial, more information can be found <a href="https://otree.readthedocs.io/en/latest/pages.html" target="_blank">here</a>.

<h3 id="settings">Settings.py</h3>

The last building block of oTree is `Settings.py`. Here you define some overarching settings of your oTree project, such as the language used, the currency used, your admin username and password, how experimental currency translates to real-world currency, and the apps that are available. For the latter, if you have an app called `attribute_substitution`. You can make it available in your oTree server by typing:

```python
SESSION_CONFIGS = [
    dict(
       name='attribute_substitution',
       display_name="Attribute Substitution Game",
       num_demo_participants=3,
       app_sequence=['attribute_substitution']
    ),
]
```

Here, the name and display name are whatever you prefer (for name you cannot use spaces). The number of demo participants is the number of slots available to play a demo version of the experiment. The most important thing here is the `app_sequence`. In the `app_sequence` you define the sequence of apps that is displayed to participants. Suppose that you want to combine the `attribute_substitution` app with a public goods game or a survey, you can add `, public_goods` or `survey`, respectively.

<h2 id="first_experiment">Your First Experiment</h2>

Now you are familiar with the building blocks of oTree, you are ready to build your first experiment. As an illustration, I will use an experiment that is very easy to program: an experiment to test attribute substitution. Attribute substitution is a powerful psychological concept that occurs when an individual has to make a judgment (of a target attribute) that is computationally complex, and instead substitutes a more easily calculated heuristic attribute. The study by Strack, Martin, & Schwarz (1988) provides an excellent example of attribute substitution. In this study college students answered a survey that included these two questions: “How happy are you with your life in general?” and “How many dates did you have last month?”. The correlation between the two questions was negligible when they occurred in the order shown, but it rose to 0.66 when the dating question was asked first. This indicates that the students who had to make a difficult judgment about their happiness, substituted the target attribute (how happy they are) with an easier heuristic attribute (the number of dates they had last month).

We will replicate this study based on the building blocks. Instead of asking how many dates a person had, we will ask how many friends a person has on social media. Following the building blocks, our experiment needs to have:

* At least two pages (one for each question)
* Three variables (answer to the first question, answer to the second question, the participant's treatment)

To start, we define each variable in `Models.py` on the player-level:

```python
	treatment = models.IntegerField()
  question_1 = models.IntegerField(label="", blank=False)
  question_2 = models.IntegerField(label="", blank=False)
```

We leave the label empty such that we can vary the question between conditions in `Templates`. `blank=False` indicates that a participant cannot leave the field blank and an error will pop up if it is left blank. Next, we need a `function` to assign participants to a treatment. Here, we can use the same code as we used to assign participants to treatments in the [Models.py](#models) section. Next, we can make the templates: `Page1.html` and `Page2.html`. We want to vary the order of the questions, so on the first page we ask one treatment the happiness question and the other the social media question, whereas on the second page we reverse the order:

```python
{% if player.treatment == 0 %}
	<p>How many friends do you approximately have on social media?</p>
{% else %}
	<p>Please indicate on a scale from 1 to 10 how happy you are with your life in 	general.</p>
{% endif %}

{% formfields %}
```

Next, we have to specify the pages, the variables on each page, and the sequence of pages on `Pages.py`. As we use two pages with on every page one question at the player-level we can input the following:

```python
class Page1(Page):
    form_model = 'player'
    form_fields = ['question_1']

class Page2(Page):
    form_model = 'player'
    form_fields = ['question_2']

page_sequence = [Page1, Page2]
```

Finally, we need to specify the right settings in `Settings.py`. You can find example settings of `SESSION_CONFIGS` in the [Settings.py](#settings) section. After you have specified the right settings you are ready to test your experiment and deploy it to a server.

<h2 id="heroku">Connecting oTree to Heroku</h2>

In order to make the oTree instance accessible globally, a server is needed. We use <a href="http://herokuapp.com" target="_blank">Heroku</a>. Heroku is a cloud hosting server that provides a platform for apps, including app management and instant scaling (i.e., you pay for what you use). You can deploy an experiment to Heroku for free. However, if you run an experiment with a substantial number of participants, you must upgrade to a paid server. As you can immediately scale the server capacity it is not expensive to use. For instance, if you run your experiment in the timeframe of three days, you only pay 3/30th of the monthly fees as you scale it up before you use it and scale it down after you use it. After you have created an account on Heroku, download and install the <a href="https://devcenter.heroku.com/articles/heroku-cli" target="_blank">Heroku Command Line Interface</a>. After installing the Heroku Command Line Interface, there are three ways to deploy experiments to Heroku: oTree Hub, GitHub, and using your command prompt or terminal (for Mac users). oTree Hub is the easiest way and requires least coding. However, convenience comes at a cost as you can have limited free project space and everything you deploy using oTree Hub becomes publicly available immediately, unless you pay. GitHub also does not require programming and you can even auto-deploy your experiment everytime you commit changes to GitHub. If you are not daunted by some programming you can use the command line to deploy your experiment to Heroku. Next, I will discuss how to deploy by each method separately.

<h3 id="otreehub">oTree Hub</h3>

First, you can use <a href="https://www.otreehub.com/" target="_blank">oTree Hub</a>. Once you have registered at oTree Hub and connected oTree Hub with Heroku you can click on "Heroku Server Deployment". At the server deployment you can upload your project. If you set a project up for the first time you need to set up database management. To do so, go to your Heroku account and click on "Configure Add-ons". Subsequently, enable Heroku Postgres and Heroku Redis, as you don't want to spend money just yet start with the free package (hobby-dev). Now you are ready to go back to oTree Hub, where you can upload an .otreezip file. To create an oTree Zip file go to the path where your oTree project is located and use the command prompt:

```bash
cd "[oTree project path]"
otree zip
```

After running this code in the command prompt, an .otreezip file is created in your oTree project environment (where also your Settings.py file is located). You can upload this .otreezip file to oTree Hub, and oTree Hub will automatically deploy it to the Heroku server. Once you have done so, you can click on "Reset DB". Make sure to save copies of your data because resetting the database will remove all existing data. Your experiment will not be available online at: https://[yourappnamehere].herokuapp.com.

![oTree Hub Connect](/images/otreehub_connect.PNG)
<p align="center"><i>A screenshot of oTree Hub</i></p>

<h3 id="github">GitHub</h3>

Second, you can use <a href="https://github.com" target="_blank">GitHub</a>. If you are browsing this repository, this implies you are already on GitHub. If you have a GitHub account, you can integrate this with Heroku. In Heroku, create an app and click on "Deploy". Here, you can authorize Heroku to access your GitHub repositories. After authorizing Heroku, you can search for your GitHub repository and connect it to Heroku. You can either manually deploy your GitHub repository to Heroku or automatically deploy all pushes you make to GitHub. If you add new variables in your experiment, you should reset the database in Heroku by using the following code in the Command Prompt.

```bash
heroku login
heroku run "otree reset db" --APP your_appname
```
Alternatively, you can go to your app in Heroku, click on Heroku Postgres, Settings, and Reset Database.

![GitHub Connect](/images/github_connect.PNG)
<p align="center"><i>A screenshot of the GitHub integration in Heroku.</i></p>

<h3 id="commandprompt">Command Prompt</h3>

The third option is to deploy your experiment to Heroku by using your command prompt (or Terminal for iOS users). In this case, you do not need any third-party software except Heroku. To use the command prompt you need to follow the following steps:

Locate the project root folder (particular oTree instance).

```bash
cd '/Users/Name/Folder/'
```

If you have created a Heroku account, use the following command. If you do not have a Heroku account yet, you can create one <a href="https://signup.heroku.com/login" target="_blank">here</a>.

```bash
heroku login
```

<p style="text-align:justify;">If the above command does not work, you probably have not installed Heroku CLI properly. 

<p style="text-align:justify;">Then, you can create a new Heroku-app, if you don't have one yet.</p>

```bash
heroku create your_appname
```

Since you are already in the project root folder you can create the .git here.</p>

```bash
git init
heroku git:remote -a your_appname
```

You can push your code locally to Heroku. If you already have an app you can use '<span style="color:blue;>--your_appname</span>' to specifically refer to your app.

```bash
git add .
git commit -am "the message you want to commit"
```

Finally push the local repository to the Heroku server.

```bash
git push heroku master
```

If already used, reset the oTree database.

```bash
heroku run "otree resetdb" --APP your_appname
```

In order to view the Heroku app, enter the following command or enter the URL in your browser.

```
heroku open
```

##

If you add new variables in the models.py, you should reset the database in Heroku.

```bash
heroku login
heroku run "otree reset db" --APP your_appname
```

Or do it manually in the Heroku app, simlarly to the way described earlier. A related blog post on how to deploy your experiment to a server can be found on <a href="https://www.accountingexperiments.com/post/server-deployment/" target="_blank">Accounting Experiments</a>.

<h2 id="mturk">Publishing Your Experiment on Amazon Mechanical Turk</h2>

Now you have deployed your experiment to the Heroku server you are ready to run the experiment. Go to http://[your_app_name].herokuapp.com and click on "Sessions" in the header. If you want to run the experiment with students, you can create the session and share the session-wide link through e-mail or other channels. In case you want to run your experiment on Amazon's Mechanical Turk, this is easy as oTree is integrated with Amazon's Mechanical Turk. First, access your app in Heroku and click on 'Settings'. Next, go to Config Vars and fill in your `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` (both available through your Amazon AWS account security credentials), `DATABASE_URL`, `REDIS_URL` (both available through Heroku Add-ons), `OTREE_ADMIN_PASSWORD`, `OTREE_AUTH_LEVEL` (`STUDY` or `DEMO`), and `OTREE_PRODUCTION` (`1` or `0`, if `1` debug information is not displayed). 

Finally, you need to specify settings for your MTurk HIT in `Settings.py`. An example code can be found below:

```python
mturk_hit_settings = {
    'keywords': ['study', 'academic'],
    'title': 'Answer Two Questions',
    'description': 'This study is anonymous, please answer two questions about your daily life.',
    'frame_height': 500,
    #'preview_template': 'global/MTurkPreview.html',
    'template': 'global/mturk_template.html',
    'minutes_allotted_per_assignment': 45,
    'expiration_hours': 7*24, # 7 days
    #'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    'qualification_requirements': [
        # No-retakers
        {
            'QualificationTypeId': "30LLG2NWCXJ09FSUO3LGVGEKYUS095",
            'Comparator': "DoesNotExist",
        },
        # Only US
        {
            'QualificationTypeId': "00000000000000000071",
            'Comparator': "EqualTo",
            'LocaleValues': [{'Country': "US"}]
        },
        # At least x HITs approved
        {
            'QualificationTypeId': "00000000000000000040",
            'Comparator': "GreaterThanOrEqualTo",
            'IntegerValues': [500]
        },
        # At least x% of HITs approved
        {
            'QualificationTypeId': "000000000000000000L0",
            'Comparator': "GreaterThanOrEqualTo",
            'IntegerValues': [98]
        },
        ]
}
```

The keywords, title, description, and frame height define how the HIT is displayed to participants in Amazon's Mechanical Turk. The minutes allotted are the maximum amount of minutes that a participant can spend on the HIT. Make sure to make this long enough. Exploration hours deal with how long the experiment will be posted on MTurk. Qualification requirements are important as they describe which MTurkers can participate. A few examples are provided.

Once you have done so, you can go back to http://[your_app_name].herokuapp.com, click on "Sessions", click on the arrow next to "Create Session" and select "For MTurk". Subsequently, you can select the number of participants you want to recruit and publish your hit. Make sure to have enough money in your Amazon's Mechanical Turk account. A huge advantage of oTree is that payments (including bonuses) can be paid automatically through the oTree environment.

Also in `Settings.py` add to `SESSION_CONFIG_DEFAULTS` the following to indicate to oTree where the MTurk HIT Settings are located:

```python
'mturk_hit_settings': mturk_hit_settings,
```

![MTurk Connect](/images/mturk_connect.png)
<p align="center"><i>A screenshot of the MTurk integration in oTree.</i></p>

##

<h2 id="questions">Questions?</h2>

If you have questions or experience problems please use the `issues` tab of this repository. Also, <a href="http://victorvanpelt.com" target="_blank">Victor van Pelt</a> and I have created <a href="https://www.accountingexperiments.com" target="_blank">Accounting Experiments</a>. <a href="https://www.accountingexperiments.com" target="_blank">Accounting Experiments</a> is an online resource and community for sharing information about designing, programming, and analyzing data of accounting experiments.

<h2 id="disclaimer">Disclaimer</h2>

<p style="text-align:justify;">In this repository, I highlight my own preferred setup to run online experiments. There are many other ways to run online experiments that each have advantages and disadvantages. oTree is opensource under the MIT license with the added requirement of a citation of <a href="https://doi.org/10.1016/j.jbef.2015.12.001" target="_blank">Chen, Schonger, and Wickens (2016)</a>. I have no financial or any stake in the software I recommend. Information may be obsolete or inaccurate as software is continuously updating.</p>

<h2 id="license">License</h2>

[MIT](LICENSE) - Christian Peters - 2020

<p align = "center">
    <a href="https://www.buymeacoffee.com/lLgZJab19" target="_blank"><img src="https://bmc-cdn.nyc3.digitaloceanspaces.com/BMC-button-images/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>
</p>  
