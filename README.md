# Django tutorial

- [Django tutorial intro](https://docs.djangoproject.com/en/4.2/intro/)
    - Resume from: https://docs.djangoproject.com/en/4.2/intro/tutorial05/

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
deactivate
```

Create a new migration:

```
python manage.py makemigrations polls
```

Debugging:

```
python manage.py sqlmigrate polls 0001
python manage.py check
python manage.py shell
```

## References

- https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
- https://docs.djangoproject.com/en/4.2/ref/models/querysets/
- Tags and filters: https://docs.djangoproject.com/en/5.0/ref/templates/builtins/
