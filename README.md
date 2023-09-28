<p align="center">
<a href="https://github.com/paulakaferreira/XIXauthors/actions/workflows/black.yml"><img src="https://github.com/paulakaferreira/XIXauthors/actions/workflows/black.yml/badge.svg"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

# French Authors from the 19th century

## Installation

Install graphviz:

`sudo apt-get install python3-dev graphviz libgraphviz-dev pkg-config`

Install all python dependencies:

`pip install -r requirements.txt`

## Docker Setup (for local development)  

1) Check if Docker Desktop is running  

2) Run `docker compose up --build --detach --remove-orphans` to initialize the docker container (if you're using old docker, you might need to use `docker-compose` with an hyphen)

3) Navigate to `http://localhost:8000` to check if everything is running smoothly  

4) Use the command `docker exec -it django sh` to open the command prompt inside the container you've just created!

## Django Setup (for local development)

*Inside the docker container:*

1) Run `migrate` to populate local database with required tables:

`python manage.py migrate`

2) Create your `superuser`:

`python manage.py createsuperuser`

3) Start Django debug server:

`python manage.py runserver`

4) Check if it works by accessing `localhost:8000` in your browser.

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

## Database Available At:

* **[Project Gutenberg](https://www.gutenberg.org/cache/epub/feeds/)**
