# AUDL-App

See the app at https://audl-stats-explorer.herokuapp.com/

TODO:

* Update README
* Choose new font that's on Mac by default
* Create script that creates all of the files needed for the app
* Figure out how to combine players from 2021 to 2022

## How to Run App Locally

1. Open a terminal in this directory and create a virtual environment `virtualenv --python=<path to python version 3.7.11> venv`
1. Activate the venv `source venv/bin/activate` and install the requirements `pip install -r requirements.txt`
1. `python run.py`

## How to Deploy

These steps outline the process for pushing an updated app to Heroku.

1. Set up Heroku on your computer according to this [guide](https://devcenter.heroku.com/articles/getting-started-with-python#set-up).
1. Make sure the requirements file is updated with the latest commit of the [audl-advanced-stats](https://github.com/JohnLithio/AUDL-Advanced-Stats) module.
1. Push the changes to Github and the changes will automatically deploy to Heroku.