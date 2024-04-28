# Your First Django App

Initial project setup:

```
python3 -m venv env
git init .
source env/bin/activate
python -m pip install django
django-admin startproject mypollsite
cd mypollsite
python manage.py startapp polls
python manage.py migrate
```

Environment:

```
source env/bin/activate
pip install -r requirements.txt
deactivate
```

Create a new migration:

```
python manage.py makemigrations polls
```

Development:

```
python manage.py runserver
```

Debugging:

```
python manage.py sqlmigrate polls 0001
python manage.py check
python manage.py shell
```

Testing:

```
python manage.py test <app>
```

## References

- https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
- https://docs.djangoproject.com/en/4.2/ref/models/querysets/
- Tags and filters: https://docs.djangoproject.com/en/5.0/ref/templates/builtins/

## Notes

### Tutorial 5:

> It doesn’t matter. Let them grow. For the most part, you can write a test once and then forget about it. It will continue performing its useful function as you continue to develop your program.

> At worst, as you continue developing, you might find that you have some tests that are now redundant. Even that’s not a problem; in testing redundancy is a good thing.

### Tutorial 6:

> You should always use relative paths to link your static files between each other, because then you can change STATIC_URL
