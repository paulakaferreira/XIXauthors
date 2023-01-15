<p align="center">
<a href="https://github.com/paulakaferreira/XIXauthors/actions/workflows/black.yml"><img src="https://github.com/paulakaferreira/XIXauthors/actions/workflows/black.yml/badge.svg"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

# French Authors from the 19th century

## Installation

Install graphviz:

`sudo apt install graphviz`

Install all python dependencies:

`pip install -r requirements.txt`

## Django Setup (for local development)

Run `migrate` to populate local database with required tables:

`python manage.py migrate`

Create your `superuser`:

`python manage.py createsuperuser`

Start Django debug server:

`python manage.py runserver`

Check if it works by accessing `localhost:8000` in your browser.

Welcome to the Django!


**⚠️PS: if you want to go straight to django-admin, try `localhost:8000/admin` instead.⚠️**

## Create an EDR graph

For a png file run:

`python manage.py graph_models bibliotheque -o edr.png`

For a svg file run:

`python manage.py graph_models bibliotheque -o edr.svg`


## Collaborators
* **[Paula Ferreira](https://github.com/paulakaferreira)** 
* **[Tiago Lima](https://github.com/til021)**
* **[Arthur Alves](https://github.com/sprezz-arthur)**
* **[Amélia Galvão](https://github.com/ameliagalvao)**
