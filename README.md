# DSA REST API Backend

This repository contains the code for the DSA website backend. 

## Running this bad boy
It is recommended that you create a new virtual environment for this project. 
Below you can find instructions on how to do that. Don't complain about stuff not working if you don't use a venv.

Install the requirements using `pip install -r requirements.txt`

Apply migrations with `python -m manage migrate`

You can run the server by using `python3 -m manage runserver` or `python -m manage runserver`

## Adding code
Please install the project in a virtual environment. 
This will help with keeping your system clean as well as making debugging and updating `requirements.txt` easier.

You can start creating a new app by running `python3 manage.py startapp <name>`. 
After that add the name of the app to the `INSTALLED_APPS` list in `dsa_api/settings.py` and add `path('', include('<name>.urls')),` to the urlpatterns list of `dsa_api/urls.py`. Then you can edit the files in the app to your liking. See the `activities` app as an example. 

Further instructions on how to do things are available on 
[the Django REST documentation site](https://www.django-rest-framework.org/)
and the [Django documentation site](https://docs.djangoproject.com/en/3.0/)

## Creating and using a virtual environment
This can be done in PyCharm in the interpreter settings of the project
or from the terminal by going to the root of this project and running `python3 -m venv ./venv` 
(or `python -m venv ./venv` on up to date Linux distro's). 
In PyCharm you will automatically use the venv, in the terminal you will first have to run `source venv/bin/activate` or 
`source venv/bin/activate.fish` if you're using fish. 
If all went well you should see `(venv)` in front of the text in the terminal. 
`python` should now automatically use the venv Python environment.
`pip` might not be correctly changed. In that case use `python -m pip` in place of pip. 

## A working flow for upgrading packages to latest
- Remove all version info (but not the package names) from requirements.txt
- `python -m pip install --upgrade -r requirements.txt`
- `pip freeze > requirements.txt`