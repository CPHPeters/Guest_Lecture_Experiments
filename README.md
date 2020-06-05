<h1 align="center">Running Online Experiments</h1>

<p>
Want to learn how to build a state-of-the-art experiment and run it in an online participant pool? This repository will get you started.
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
* [Building your Experiment in oTree](#otree)
* [Connecting oTree to Heroku](#heroku)
    * [oTree Hub](#otreehub)
    * [GitHub](#github)
    * [Command Prompt](#commandprompt)
* [Publishing your Experiment on Amazon Mechanical Turk](#mturk)
* [Questions?](#questions)
* [Disclaimer](#disclaimer)
* [License](#license)

<h2 id="introduction">Introduction</h2>

<p style="text-align:justify;">Welcome to this repository on how to run online experiments. The goal of this repository is help to get you from your initial research design to a programmed experiment that can be distributed to any participant pool. This will be divided into three steps. First, I will focus on how you can program an experiment using oTree software. oTree is platform-independent and online, allowing you to run experiments anywhere at any time. Although I will explain the building blocks of oTree programming, learning-by-doing is necessary. I would definitely recommend to have a look at <a href="https://otree.readthedocs.io/en/latest/" target="_blank">otree.readthedocs.io</a>, which is a large repository containing a lot of information about oTree. To learn oTree, no prior programming experience is necessary, although prior knowledge of Python, HTML, CSS, and Javascript can be helpful. Second, I show how to deploy your experiment to an online server to make it available through a webpage that participants can visit. Third, I show how to make your experiment available to an online participant pool (Amazon's Mechanical Turk).</p>

<p style="text-align:justify;">Before getting started, I would like to mention one caveat. oTree allows for many features up-and-above other software such as chat functions, interactions, timeouts, etc. However, if you are designing a study that does not need such a design, usage of point-and-click software such as Qualtrics may be more efficient.</p>

<h2 id="installation">Installation</h2>

<h3 id="setup">Getting Your Setup Ready</h3>
<p style="text-align:justify;">oTree is based on Django. Django is a rich framework that makes it easier to program web applications using the Python programming language. To use Django, you need to install Python. In case you have not installed Python before, you can download and install Python <a href="https://www.python.org/downloads/" target="_blank">here</a>.</p>

<p style="text-align:justify;">Second, you may want to install a code editor that makes programming easier. A code editor highlights syntax, checks for errors, and helps debugging. An example of a code editor is <a href="https://www.jetbrains.com/pycharm/download/" target="_blank">PyCharm</a>. If you are a student or educator, you can download the professional version for free.</p>

<h3 id="otree_installation">Installing oTree</h3>
<p style="text-align:justify;">Once Python and PyCharm are installed, you can start by opening your Command Prompt (or Terminal in case you use iOS). To install oTree, enter:</p>

```bash
pip3 install -U otree
```

<p style="text-align:justify;">Once oTree is installed, you can create your first oTree project. By using the "cd" command (change directory) you can specify the path where you want to install the oTree project folder. For instance, when I would type:</p>

```bash
cd "C:\Users\Christian\Desktop"
```

<p style="text-align:justify;">I would install it on my desktop. Specify the folder where you would like your oTree project to be located and hit:</p>

```bash
otree startproject project_name
```

<p style="text-align:justify;">where you can input the name of your project for 'project_name'. Next, oTree will ask whether you want to install sample games. oTree includes a large library of sample games that you can use, these can also be examined and tested <a href="http://otree-demo.herokuapp.com/demo/" target="_blank">here</a>. If you want them to be included in your project folder hit "y" and if not hit "n". Next move into change the directory of the command prompt to inside your project folder by typing:</p>

```bash
cd project_name
```

<p style="text-align:justify;">where you insert your project name for <i>project_name</i>, now the command prompt should indicate that you are in the project folder. In your case, you probably do not want to use one of the standard games provided by oTree but to create your own experiment. If so, you need to create an app. An app is a subset of an oTree project folder. An experiment (your project) can contain multiple apps. For instance, you may want your participants to first conduct a Public Goods Game and afterwards a Dictator Game. If so, you can create two separate apps in the same project. To create an app type:</p>

```bash
otree startapp app_name
```

<p style="text-align:justify;">Now you can go to your project folder and inspect it. If all went correctly, you will be able to see your app in your project folder.</p>

<h2 id="otree">Building Your Experiment in oTree</h2>

<h2 id="heroku">Connecting oTree to Heroku</h2>

<p style="text-align:justify;">In order to make the oTree instance accessible globally, a server is needed. We use <a href="http://herokuapp.com" target="_blank">Heroku</a>. Heroku is a cloud hosting server that provides a platform for apps, including app management and instant scaling (i.e., you pay for what you use). You can deploy an experiment to Heroku for free. However, if you run an experiment with a substantial number of participants, you must upgrade to a paid server. As you can immediately scale the server capacity it is not expensive to use. For instance, if you run your experiment in the timeframe of three days, you only pay 3/30th of the monthly fees as you scale it up before you use it and scale it down after you use it. After you have created an account on Heroku, download and install the <a href="https://devcenter.heroku.com/articles/heroku-cli" target="_blank">Heroku Command Line Interface</a>. After installing the Heroku Command Line Interface, there are three ways to deploy experiments to Heroku: oTree Hub, GitHub, and using your command prompt or terminal (for Mac users). oTree Hub is the easiest way and requires least coding. However, convenience comes at a cost as you can have limited free project space and everything you deploy using oTree Hub becomes publicly available immediately, unless you pay. GitHub also does not require programming and you can even auto-deploy your experiment everytime you commit changes to GitHub. If you are not daunted by some programming you can use the command line to deploy your experiment to Heroku. Next, I will discuss how to deploy by each method separately.</p>

<h3 id="otreehub">oTree Hub</h3>

<p style="text-align:justify;">First, you can use [oTree Hub](https://www.otreehub.com/). Once you have registered at oTree Hub and connected oTree Hub with Heroku you can click on "Heroku Server Deployment". At the server deployment you can upload your project. If you set a project up for the first time you need to set up database management. To do so, go to your Heroku account and click on "Configure Add-ons". Subsequently, enable Heroku Postgres and Heroku Redis, as you don't want to spend money just yet start with the free package (hobby-dev). Now you are ready to go back to oTree Hub, where you can upload an .otreezip file. To create an oTree Zip file go to the path where your oTree project is located and use the command prompt:</p>

```bash
cd "[oTree project path]"
otree zip
```

<p style="text-align:justify;">After running this code in the command prompt, an .otreezip file is created in your oTree project environment (where also your Settings.py file is located). You can upload this .otreezip file to oTree Hub, and oTree Hub will automatically deploy it to the Heroku server. Once you have done so, you can click on "Reset DB". Make sure to save copies of your data because resetting the database will remove all existing data. Your experiment will not be available online at: https://[yourappnamehere].herokuapp.com.</p>

![oTree Hub Connect](/images/otreehub_connect.png)
<p align="center"><i>A screenshot of oTree Hub</i></p>

<h3 id="github">GitHub</h3>

<p style="text-align:justify;">Second, you can use [GitHub](https://github.com). If you are browsing this repository, this implies you are already on GitHub. If you have a GitHub account, you can integrate this with Heroku. In Heroku, create an app and click on "Deploy". Here, you can authorize Heroku to access your GitHub repositories. After authorizing Heroku, you can search for your GitHub repository and connect it to Heroku. You can either manually deploy your GitHub repository to Heroku or automatically deploy all pushes you make to GitHub. If you add new variables in your experiment, you should reset the database in Heroku by using the following code in the Command Prompt.</p>

```bash
heroku login
heroku run "otree reset db"
```
<p style="text-align:justify;"> Alternatively, you can go to your app in Heroku, click on Heroku Postgres, Settings, and Reset Database. </p>

![GitHub Connect](/images/github_connect.png)
<p align="center"><i>A screenshot of the GitHub integration in Heroku</i></p>

<h3 id="commandprompt">Command Prompt</h3>

<p style="text-align:justify;">The third option is to deploy your experiment to Heroku by using your command prompt (or Terminal for iOS users). In this case, you do not need any third-party software except Heroku. To use the command prompt you need to follow the following steps: </p>

<p style="text-align:justify;">Locate the project root folder (particular oTree instance).

```bash
cd '/Users/Name/Folder/'
```

<p style="text-align:justify;">If you have created a Heroku account, use the following command. If you do not have a Heroku account yet, you can create one [here](https://signup.heroku.com/login).</p>

```bash
heroku login
```

<p style="text-align:justify;">If the above command does not work, you probably have not installed Heroku CLI properly. Since you are already in the project root folder you can create the .git here.</p>

```bash
git init
```

<p style="text-align:justify;">Then, you can create a new Heroku-app, if you don't have one yet.</p>

```bash
heroku create my-app-name
```

<p style="text-align:justify;">You can push your code locally to Heroku. If you already have an app you can use '<span style="color:blue;>--your_appname</span>' to specifically refer to your app.</p>

```bash
git add .
git commit -am "the message you want to commit"
```

<p style="text-align:justify;">Finally push the local repository to the Heroku server.</p>

```bash
git push heroku master
```

<p style="style="text-align:justify;">If already used, reset the oTree database.</p>

```bash
heroku run "otree resetdb"
```

<p style="text-align:justify;">In order to view the Heroku app, enter the following command or enter the URL in your browser.</p>

```
heroku open
```

##

<p style="text-align:justify;">If you add new variables in the models.py, you should reset the database in Heroku.</p>

```bash
heroku login
heroku run "otree reset db"
```

<p style="text-align:justify;">Or do it manually in the Heroku app, simlarly to the way described earlier. A related blog post on how to deploy your experiment to a server can be found on [Accounting Experiments](https://www.accountingexperiments.com/post/server-deployment/).</p>

<h2 id="mturk">Publishing Your Experiment on Amazon Mechanical Turk</h2>

<p style="text-align:justify;">Now your oTree experiment is deployed to a server, you can make it available to participants.</p>

##

<h2 id="questions">Questions?</h2>

<p style="text-align:justify;">If you have questions or experience problems please use the `issues` tab of this repository. Also, [Victor van Pelt](http://victorvanpelt.com) and I have created [Accounting Experiments](https://www.accountingexperiments.com). [Accounting Experiments](https://www.accountingexperiments.com) is an online resource and community for sharing information about designing, programming, and analyzing data of accounting experiments.</p>

<h2 id="disclaimer">Disclaimer</h2>

<p style="text-align:justify;">In this repository, I highlight my own preferred setup to run online experiments. There are many other ways to run online experiments that each have advantages and disadvantages. oTree is opensource under the MIT license with the added requirement of a citation of [Chen, Schonger, and Wickens (2016)](https://doi.org/10.1016/j.jbef.2015.12.001). I have no financial or any stake in the software I recommend. Information may be obsolete or inaccurate as software is continuously updateing.</p>

<h2 id="license">License</h2>

[MIT](LICENSE) - Christian Peters - 2020

<p align = "center">
    <a href="https://www.buymeacoffee.com/lLgZJab19" target="_blank"><img src="https://bmc-cdn.nyc3.digitaloceanspaces.com/BMC-button-images/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>
</p>  
