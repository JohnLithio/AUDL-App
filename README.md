# AUDL-App

See the app at https://audl-stats-explorer.herokuapp.com/

TODO:

* Create script that creates all of the files needed for the app
* Set up daily data refresh with Google Cloud

## How to Run App Locally

1. Open a terminal in this directory and create a virtual environment `virtualenv --python=<path to python version 3.7.11> venv`
1. Activate the venv `source venv/bin/activate` and install the requirements `pip install -r requirements.txt`
1. `python run.py`

## How to Deploy

These steps outline the process for pushing an updated app to Heroku.

1. Set up Heroku on your computer according to this [guide](https://devcenter.heroku.com/articles/getting-started-with-python#set-up).
1. If you have not set the Heroku remote, use `heroku git:remote -a audl-stats-explorer`
1. Make sure the requirements file is updated with the latest commit of the [audl-advanced-stats](https://github.com/JohnLithio/AUDL-Advanced-Stats) module.
1. Push the changes to Github and the changes will automatically deploy to Heroku. If this does not work, use the following steps.
1. `git push heroku main`
1. If there's an error, you can view the logs with `heroku logs --tail`
1. If the app is not currently running, `heroku ps:scale web=1`
1. To open it up, `heroku open` or go to https://audl-stats-explorer.herokuapp.com/