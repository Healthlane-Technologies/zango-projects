# Zango Project

This is a fully functional project made with Zango framework using manual setup. The best part is, there are 3 apps(or projects) inside this one project so that you dont have to start a new project from scratch everytime. Also, you can host all of these three apps on a single cloud and all the new apps that you create under this project will be hosted on the same cloud, saving cost, time and extra efforts requried to host projects.

## Project structure
```
root                        # root where this readme file is located.
|
+-- zango_projects          # main zango_projects folder which contains everything related to our project.
|   |               
|   +-- workspaces          # all the apps are create dynamically inside this folder.
    |   |
    |   +-- todo_app        # todo app directory, detailed app structure is present inside the app directory.
        |   |
        |   +-- Readme.md   # app readme, contains app structure and other app specific details.
            .
            .
        +-- portfolio       # portfolio app directory, detailed app structure is present inside the app directory.
        |   |
        |   +-- Readme.md   # app readme, contains app structure and other app specific details.
            .
            .
        +-- issue_tracker   # issue tracker app directory, detailed app structure is present inside the app directory.
        |   |
        |   +-- Readme.md   # app readme, contains app structure and other app specific details.
            .
            .
    +-- zango_projects      # contains all the zango platform configuration files.
    |   |
    |   +-- asgi.py
        +-- settings.py     # contains all the project settings, just like django.
        +-- urls_public.py  # contains config for urls of zango platform.
        +-- urls_tenants.py # contains config for urls of apps present inside project.
        +-- urls.py
        +-- wsgi.py
    +-- manage.py           # same manage.py which is there in traditional django projects.
+-- Readme.md               # The file which you are reading right now.
+-- .gitignore
+-- .env                    # This is required for running the project.
+-- venv
```

## How to setup and run zango platform
To setup the zango platform (manually) there are a few steps that needs to be followed. We are going to run postgres and redis database using docker container and then run the project using runserver command, celery worker and celery beat.

### 1. Database setup

**For setting up and running the postgres database follow the steps below:**

a. Download [docker desktop](https://www.docker.com/products/docker-desktop/) as per your operating system.

b. The first step after that is to pull the Postgres Docker image from the Docker Hub repository. This is done by running the following command in a new terminal window:
```
docker pull postgres
```
  
c. Next, we need to create a Docker volume to persist our Postgres data. This is done by running the following command:
```
docker volume create postgres_data
```
    
d. Now we can run the Postgres Docker container using the following command:
```
docker run --name postgres_container -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 -v postgres_data:/var/lib/postgresql/data postgres
```
    
e. You can confirm that postgres db container is up and running by using `docker ps` command.

**For setting up and running the redis database follow the steps below:**

a. Assuming you already downloaded docker desktop in above guide, run the following command in the terminal:
```
docker run -d -p 6379:6379 redis:latest
```

This will run the latest redis image on port 6379 .


### 2. Downloading this project and setting up

Below are the steps for setting up the zango platform. To setup the specific app (like todo), checkout the readme files in the project directory, i.e, inside: `zango_projects/workspaces/app_name/`.

a. Download this project and create a python virtual env in the root directory.

b. Now activate the virtual env and install zango using:
```
pip install zango
```

c. Now, you'll have to delete the workspaces folder present inside `zango_projects` directory initially because it will be created dynamically from the zango platform and then you can paste the code of that project from this repository. Suppose you created `todo_app` from the zango platform, zango will automatically generate todo_app directory with some config files inside `zango_projects/workspaces` and then you can replace all the files inside `zango_project/workspaces/todo_app` with the files present in this repository. This is because zango creates schema of the app(todo_app) only when we create it dynamically(from zango platform).

d. After you have deleted the workspaces folder, go inside the zango_projects directory (where manage.py file is located) and run the `zango initialize-project zango_projects` command to initialize the project database and create a platform user.

e. After the platform user has been created, run the following commands inside zango_projects directory:

- Start the project using traditional django command:
```
python manage.py runserver
```
- In another terminal window, start celery worker using command:
```
celery -A zango_projects worker -l INFO
```
- In one more terminal window, start celery beat using command:
```
celery -A zango_projects beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

g. Then go to `localhost:8000/platform` where you'll see a login screen. Congratulations! You have successfully setup the zango platform. Now its time to create some projects using zango.

Please head over to the [readme of todo_app](https://github.com/Healthlane-Technologies/zango-projects/tree/main/zango_projects/workspaces/todo_app/Readme.md) for a detailed guide on creating and getting todo_app up and running.