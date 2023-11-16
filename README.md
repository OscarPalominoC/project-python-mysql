# Project MySQL and Python

This project was a mere test to connect Python and MySQL.

The project was based on an Note application.

## User Class
This class defines the ``user`` object and its methods. Also, it contains a different file named `actions.py`, which it contains all of the actions you'll see mostly on screen.

## Note Class
This class defines the `Note` object and its methods. Also, it contains a different file named `actions.py`, which it contains all of the actions you'll see mostly on screen.

## Environment variables

You will need a `.env` file. For that reason it exists `example.env`.

Within `example.env` it exists the environment variables already created, you just have to change its values and rename the file to `.env`.

## How to use it?

1. Download the repo. `git clone git@github.com:OscarPalominoC/project-python-mysql.git`
2. Enter the project folder! `cd project-python-mysql`
3. Create your python environment! `python -m venv <venv>` where `<venv>` is the name you want to create for your python environment
4. Enter into your Python environment!
    - Windows `<venv>\Scripts\activate`
    - Linux/MAC `source <venv>/bin/activate`
5. Install the ``requirements.txt`` into your python environment! `pip install -r requirements.txt`
6. Run the project! `python main.py`