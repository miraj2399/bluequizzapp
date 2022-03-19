import email
from rest_framework import serializers
from django.contrib.auth.models import User
from django.db import models

class registerSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

class loginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()