# DRF Quickstart

## Scaffolding

```
python3 -m venv env
source env/bin/activate

pip install django
pip install djangorestframework

django-admin startproject firstdrf .
cd firstdrf
django-admin startapp quickstart
cd ..
```

## Development


Shell:

```
python3 manage.py shell -i ipython
```

Curls

```
# GET requests
curl http://127.0.0.1:8000/api-snippets/snippets/
curl http://127.0.0.1:8000/api-snippets/snippets/2

# POST
# [#] "id" is ignored
curl -X POST http://127.0.0.1:8000/api-snippets/snippets/ \
    -H 'Content-Type: application/json' \
    -d '{"id": 999, "title": "another one", "code": "let x = 43"}'

curl -X POST http://127.0.0.1:8000/api-snippets/snippets/ \
    -H 'Content-Type: application/json' \
    -d '{"id": 999, "title": "another one", "foo": "bar"}'

curl -X POST http://127.0.0.1:8000/api-snippets/snippets/ \
    -H 'Content-Type: application/json' \
    -d '{invalid json}'

# PUT
curl -X PUT http://127.0.0.1:8000/api-snippets/snippets/2 \
    -H 'Content-Type: application/json' \
    -d '{"title": "another one", "code": "let y = 123"}'

curl -X PUT http://127.0.0.1:8000/api-snippets/snippets/2 \
    -H 'Content-Type: application/json' \
    -d '{"title": "another one", "foo": "bar"}'

# DELETE
curl -X DELETE http://127.0.0.1:8000/api-snippets/snippets/2
```

## Resources

- https://www.django-rest-framework.org/api-guide/serializers/#baseserializer
