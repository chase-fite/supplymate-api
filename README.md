# SupplyMate API (Nashville Software School final project)

SupplyMate is an inventory and logistics management system. It was designed as a tool for companies that maintain an inventory and also have employees pulling from that inventory. No more emails, phone calls, text messages, spreadsheets. SupplyMate streamlines the whole process.

## Setup

- This is assuming you have python installed, and you're using a terminal with Bash.
- From your terminal clone this repository into your directory of choice and `cd` into it.
- Run `python -m venv env`. This will create a virtual environment so the project can run the correct dependencies.
- If you're on a Mac run `source env/bin/activate`. If you're on windows run `source env/Scripts/activate`.
- Run `pip install -r requirements.txt` to install all dependencies.
- Run `python manage.py makemigrations` and `python manage.py migrate` to setup the database.
- Run `python manage.py loaddata roles.json` and `python manage.py loaddata statuses.json` to add initial data to the database.
- Lastly to start the api run `python manage.py runserver`.
- If you have not done so yet, be sure to setup the front-end for this app as well. https://github.com/chase-fite/supplymate-client

## Usage

- A user can register as either a logistics or remote employee.
- Logistics employees manage the inventory and supply requests. They can add, remove, or update items. They can also approve, cancel, or modify supply requests.
- Remote employees can create supply requests, selecting items and quantities directly from the inventory. They can also approve or cancel modified supply requests.

## ERD

![supplymate ERD](./assets/supplymate-erd.PNG)
