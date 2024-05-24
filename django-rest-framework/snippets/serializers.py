from rest_framework import serializers
from snippets.models import Snippet

"""
python manage.py shell -i ipython

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# 1. model -> serializer -> native python objects

snippet = Snippet(code='print("hello, world")\n')
snippet.save()

serializer = SnippetSerializer(snippet)
serializer.data  # [#] Native python objects (dicts and lists)

json = JSONRenderer().render(serializer.data)  # [#] JSON string

# 2. native python objects -> serializer -> model

serializer = SnippetSerializer(data=serializer.data)
serializer.is_valid()
serializer.validated_data

snippet = Snippet(**serializer.validated_data)
snippet.save()
"""

"""
print(repr(serializer))
"""

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
