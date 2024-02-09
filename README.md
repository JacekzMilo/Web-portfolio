# WebPortfolio
This project showcases my data science projects on a deployed website.

**Latest update**: copyrights added.


## Table of Contents
1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [To Do](#todo)
4. [File Descriptions](#descriptions)

## Installation
The code requires Python versions of 3.* and general libraries available through the Anaconda package. 
In addition, psycopg2 for the PostgreSQL database, Flask, Werkzeug, Django, django-heroku and gunicorn need to be 
installed to be able to deploy the website. In order for this app to work correctly it also needs
django-extensions, django-excel, PILLow and whitenoise. Please refer to the requirements.txt file for more 
details on dependencies.

## Project Motivation <a name="motivation"></a>
I always wanted to have my own space where I can store my projects in proper way, 
with links to their code. This site also helps me to keep track on my progress.

## To Do <a name="todo"></a>
1. TODO: See if cards are good choice, try to standardize their height
2. TODO: Check why root body etc are loaded multiple times
3. TODO: Check the disallowance crawlers to index this website
4. TODO: add homepage button after resetting password
 
## File Description <a name="descriptions"></a>

The templates folder contains all html pages that will be accessible through the site. 
The static folder is made up of the images displayed on my website as well as 
the css stylesheet and .json file. Procfile and requirements.txt are required by heroku in order to start the app. 

