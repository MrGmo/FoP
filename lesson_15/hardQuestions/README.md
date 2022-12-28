# Django - Hard Questions

Today we walked through how to create a fullstack application using some JSON data and Django. Your task is to create a Django project from scratch that is not about polls, yours will deal with hard questions. Your home page will look like this:

Hard Questions

1. Is a hotdog a sandwich?
2. Is cereal soup?

You should be able to click on these questions and choose an answer. Each question must have four answer choices. Upon voting you should see a count of how many people have chosen that answer just like our polls app. Your application should also have a vote again button and a reset count button that resets the respective answer choice counts to zero and returns you to the main page. This application should be centered on the page and use Bootstrap for styling: https://getbootstrap.com/docs/5.3/getting-started/introduction/.

You will have to create a data.py file for your project, you will not be given one (hint: look at the data.py file we used for our polls_app).

Please create your project from scratch and don't just edit the project we have built together, this is about practice and getting you comfortable with our new technologies.

Here are some notes to help you get started:


## How to Create Django Project

Our first step will be to create a Django project. This is something that requires a number of steps, so let's make sure we walk through these steps together here:

0. Navigate into your project directory (if not already in there) in VS Code's terminal

1. Create a virtual environment

$> python -m venv .venv

- This will create a new virtual environment in a folder called `.venv`.

2. Load virtual environment

$> source .venv/bin/activate

- This is the command (for MacOS) to get into the virtual environment. You should see the virtual environment name (".venv") added to your command prompt message.

3. Install Django

$> pip install django

- This command will install the latest Django version into your virtual environment.

4. Save dependency version (optional)

$> pip freeze > requirements.txt

- This command will create a new file and store the results of pip freeze into it.

5. Create Django project

$> django-admin startproject hard_questions .

- This command will initialize a new Django project folder with files, and the all important `manage.py`. The "." at the end of the command prevents having nested folders.

6. Create Django app

$> python manage.py startapp hard_questions_app

- This command will initialize a new Django application folder with files.

7. Update Django project settings with app name

# hard_questions/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hard_questions_app', # added the name of our app
]

- This will tell our Django project to also use our newly create app

8. Apply migrations (optional)

$> python manage.py migrate

- This is optional right now, but will remove the warning about "unapplied migrations" when we run our server. You don't need to worry about what this is really doing right now (we'll cover it later on).

9. Launch Server

$> python manage.py runserver

- You should see a message in your terminal stating something like "Starting development server at http://127.0.0.1:8000/"

10. Open a browser and navigate to `http://localhost:8000/`

- If everything worked correctly, you should see a Django rocket lifting off! (This is the default Django landing page.)

**Your project is ready, get started! :)**