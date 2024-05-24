from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

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

class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)  # [Q]: does this mean we can POST a snippet with our own ID?
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
