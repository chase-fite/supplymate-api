# SupplyMate API

## Steps to get This project started:

* Clone down the repo and `cd` into it

* Create your OSX virtual environment in Terminal:

  * `python -m venv supplymateEnv`
  * `source ./supplymateEnv/bin/activate`

* Or create your Windows virtual environment in Command Line:

  * `python -m venv supplymateEnv`
  * `source ./supplymateEnv/Scripts/activate`

* Install the app's dependencies:

  * `pip install -r requirements.txt`

* Build your database from the existing models:

  * `python manage.py makemigrations`
  * `python manage.py migrate`

* Fire up your dev server and get to work!

  * `python manage.py runserver`

## Client

Please also clone down the front-end part of this app and follow the instructions for setting up react for the full experience of this app.

https://github.com/chase-fite/supplymate-client

## ERD

![supplymate ERD](./assets/supplymate-erd.PNG)