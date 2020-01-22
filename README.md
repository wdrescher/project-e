# project-e

## Get setup locally: 
Install 
 * [ ] pgadmin 
 * [ ] nodejs
 * [ ] python3.7

$ python3.7 -m venv ./env

$ pip install -r requirements/local.txt

$ createdb project-e -U postgres --password <password>

$ export DATABASE_URL=postgres://postgres:<password>@127.0.0.1:5432/project-e

$ python manage.py migrate

$ python manage.py runserver
for more help
https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#setting-up-development-environment

:License: Apache Software License 2.0

Running projcet
Build using

    npm run dev 
Setting Up Your Users
To create a normal user account, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

To create an superuser account, use this command::

    $ python manage.py createsuperuser
For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
Running type checks with mypy:

::

$ mypy project_e

Test coverage
To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html
Running tests with py.test
::

$ pytest