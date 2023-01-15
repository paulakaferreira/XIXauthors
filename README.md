# French Authors from the 19th century

## Installation

Install all python dependencies:

`pip install -r requirements.txt`

## Docker Setup (for local development)  

1) Check if Docker Desktop is running  

2) Run `docker-compose up` to initialize the docker container  

3) Navigate to `http://localhost:8000` to check if everything is running smoothly  

4) Use the command `docker exec -it xixi_container sh` to open the command prompt inside the container you've just created!

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


## Collaborators
* **[Paula Ferreira](https://github.com/paulakaferreira)** 
* **[Tiago Lima](https://github.com/til021)**
* **[Arthur Alves](https://github.com/sprezz-arthur)**
* **[Amélia Galvão](https://github.com/ameliagalvao)**

## Database Available At:

* **[Project Gutenberg](https://www.gutenberg.org/cache/epub/feeds/)**
