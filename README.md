# Guest Lecture Experiments

Want to learn how to build a state-of-the-art experiment and run it in an online participant pool? This repository will get you started.

<p align = "center">
  <span style='font-size: 15pt'><strong>Author:</strong> Christian Peters (<a href="https://www.tilburguniversity.edu/staff/c-p-h-peters">Profile</a>)</span>
</p>

## Connecting oTree to Heroku

In order to make the oTree instance accessible globally, a server is needed. We use the [Heroku](http://herokuapp.com). For this, the conducted the following steps:

Locate the project root folder (particular oTree instance).

```bash
cd '/Users/Christian/Dropbox/Christian/Auditor Task Selection/3. Instrument/TaskDiscretionExperiment/oTree_Task_Discretion'
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
