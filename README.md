# Guest Lecture Experiments

Want to learn how to build a state-of-the-art experiment and run it in an online participant pool? This repository will get you started.

<p align = "center">
  <span style='font-size: 15pt'><strong>Author:</strong> Christian Peters (<a href="https://www.tilburguniversity.edu/staff/c-p-h-peters">Profile</a>)</span>
</p>

<p align = "center">
   <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
</p>  

## Building your Experiment in oTree

## Connecting oTree to Heroku

In order to make the oTree instance accessible globally, a server is needed. We use [Heroku](http://herokuapp.com). There are two ways of For this, we conducted the following steps:

Locate the project root folder (particular oTree instance).

```bash
cd '/Users/Name/Folder/'
```

If you have created a Heroku account, use the following command. If you do not have a Heroku account yet, you can create one [here](https://signup.heroku.com/login).

```bash
heroku login
```

Since you are already in the project root folder you can create the .git here.

```bash
git init
```

Then, you can create a new Heroku-app if you don't have one yet. 

```bash
heroku create my-app-name
# Or in the case you already created an app you want to edit:
cd myapp
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

You can connect Heroku with GitHub to deploy respositories automatically.

##

If you add columns (variables in the models.py), you should reset the database in Heroku.

```bash
heroku login
heroku run "otree reset db"
```

Or do it manually in the Heroku app. It is then important to upload a new version of the instance.

## Publishing your Experiment on Amazon Mechanical Turk


##

<h2 id="questions">Questions?</h2>

If you have questions or experience problems please use the `issues` tab of this repository.

<h2 id="license">License</h2>

[MIT](LICENSE) - Christian Peters - 2019

<p align = "center">
    <a href="https://www.buymeacoffee.com/lLgZJab19" target="_blank"><img src="https://bmc-cdn.nyc3.digitaloceanspaces.com/BMC-button-images/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>
</p>  
