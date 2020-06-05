<h2>Running Online Experiments</h2>

<p>
Want to learn how to build a state-of-the-art experiment and run it in an online participant pool? This repository will get you started.
</p>

<p align = "center">
  <span style='font-size: 15pt'><strong>Author:</strong> Christian Peters (<a href="https://www.tilburguniversity.edu/staff/c-p-h-peters">Profile</a>)</span>
</p>

<p align = "center">
   <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
</p>  

## Table of Contents

* [Introduction](#introduction)
* [Installation](#installation)
* [Building your Experiment in oTree](#otree)
* [Connecting oTree to Heroku](#heroku)
* [Publishing your Experiment on Amazon Mechanical Turk](#mturk)
* [Questions?](#questions)
* [Disclaimer](#disclaimer)
* [License](#license)

<h2 id="introduction">Introduction</h2>

<h2 id="installation">Installation</h2>

<h2 id="otree">Building Your Experiment in oTree</h2>

<h2 id="heroku">Connecting oTree to Heroku</h2>

In order to make the oTree instance accessible globally, a server is needed. We use [Heroku](http://herokuapp.com). Heroku is a cloud hosting server that provides a platform for apps, including app management and instant scaling (i.e., you pay for what you use). You can deploy an experiment to Heroku for free. However, if you run an experiment with a substantial number of participants, you must upgrade to a paid server. As you can immediately scale the server capacity it is not expensive to use. For instance, if you run your experiment in the timeframe of three days, you only pay 3/30th of the monthly fees as you scale it up before you use it and scale it down after you use it. After you have created an account on Heroku, download and install the [Heroku Command Line Interface](https://devcenter.heroku.com/articles/heroku-cli). After installing the Heroku Command Line Interface, there are three ways to deploy experiments to Heroku: oTree Hub, GitHub, and using your command prompt or terminal (for Mac users). oTree Hub is the easiest way and requires least coding. However, convenience comes at a cost as you can have limited free project space and everything you deploy using oTree Hub becomes publicly available immediately, unless you pay. GitHub also does not require programming and you can even auto-deploy your experiment everytime you commit changes to GitHub. If you are not daunted by some programming you can use the command line to deploy your experiment to Heroku. Next, I will discuss how to deploy by each method separately.

First, you can use [oTree Hub](https://www.otreehub.com/). Once you have registered at oTree Hub and connected oTree Hub with Heroku you can click on "Heroku Server Deployment". At the server deployment you can upload your project. If you set a project up for the first time you need to set up database management. To do so, go to your Heroku account and click on "Configure Add-ons". Subsequently, enable Heroku Postgres and Heroku Redis, as you don't want to spend money just yet start with the free package (hobby-dev). Now you are ready to go back to oTree Hub, where you can upload an .otreezip file. To create an oTree Zip file go to the path where your oTree project is located and use the command prompt:

```bash
cd "[oTree project path]"
otree zip
```

After running this code in the command prompt, an .otreezip file is created in your oTree project environment (where also your Settings.py file is located). You can upload this .otreezip file to oTree Hub, and oTree Hub will automatically deploy it to the Heroku server. Once you have done so, you can click on "Reset DB". Make sure to save copies of your data because resetting the database will remove all existing data. Your experiment will not be available online at: https://[yourappnamehere].herokuapp.com.

Second, you can use [GitHub](https://github.com). If you are browsing this repository, this implies you are already on GitHub. If you have a GitHub account, you can integrate this with Heroku. In Heroku, create an app and click on "Deploy". Here, you can authorize Heroku to access your GitHub repositories. After authorizing Heroku, you can search for your GitHub repository and connect it to Heroku. You can either manually deploy your GitHub repository to Heroku or automatically deploy all pushes you make to GitHub. If you add new variables in your experiment, you should reset the database in Heroku by using the following code in the Command Prompt.

```bash
heroku login
heroku run "otree reset db"
```
Alternatively, you can go to your app in Heroku, click on Heroku Postgres, Settings, and Reset Database.

The third option is to deploy your experiment to Heroku by using your command prompt. In this case, you do not need any third-party software except Heroku. To use the command prompt you need to follow the following steps:

Locate the project root folder (particular oTree instance).

```bash
cd '/Users/Name/Folder/'
```

If you have created a Heroku account, use the following command. If you do not have a Heroku account yet, you can create one [here](https://signup.heroku.com/login).

```bash
heroku login
```

If the above command does not work, you probably have not installed Heroku CLI properly. Since you are already in the project root folder you can create the .git here.

```bash
git init
```

Then, you can create a new Heroku-app, if you don't have one yet.

```bash
heroku create my-app-name
```

You can push your code locally to Heroku.

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
heroku run "otree resetdb"
```

In order to view the Heroku app, enter the following command or enter the URL in your browser.

```
heroku open
```

##

If you add new variables in the models.py, you should reset the database in Heroku.

```bash
heroku login
heroku run "otree reset db"
```

Or do it manually in the Heroku app, simlarly to the way described earlier. A related blog post on how to deploy your experiment to a server can be found on [Accounting Experiments](https://www.accountingexperiments.com/post/server-deployment/).

<h2 id="mturk">Publishing Your Experiment on Amazon Mechanical Turk</h2>

Now your oTree experiment is deployed to a server, you can make it available to participants.

##

<h2 id="questions">Questions?</h2>

If you have questions or experience problems please use the `issues` tab of this repository.

<h2 id="disclaimer">Disclaimer</h2>

In this repository, I highlight my own preferred setup to run online experiments. There are many other ways to run online experiments that each have advantages and disadvantages. I have no financial or any stake in the software I recommend.

<h2 id="license">License</h2>

[MIT](LICENSE) - Christian Peters - 2020

<p align = "center">
    <a href="https://www.buymeacoffee.com/lLgZJab19" target="_blank"><img src="https://bmc-cdn.nyc3.digitaloceanspaces.com/BMC-button-images/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>
</p>  
