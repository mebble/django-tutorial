from django.contrib.auth.models import Group, User
from rest_framework import serializers

# class UserSerializer(serializers.ModelSerializer): # TRYOUT: see how the output response changes
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
