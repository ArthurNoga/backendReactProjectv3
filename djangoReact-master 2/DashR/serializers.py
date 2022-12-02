import http
import json

from rest_framework import serializers
from rest_framework_nested.relations import NestedHyperlinkedRelatedField

from .models import *


class dev_serializer(serializers.HyperlinkedModelSerializer):
    dev_id = models.IntegerField(primary_key=True)

    class Meta:
        model = Dev
        fields = ["id", "firstname", "lastname", "username", "password", "price","gloablEarnings"]


class client_serializer(serializers.HyperlinkedModelSerializer):
    client_id = models.IntegerField(primary_key=True)
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    mail = serializers.CharField()
    Tel = serializers.CharField()

    class Meta:
        model = Client
        fields = ["id", "firstname", "lastname", "mail", "Tel"]


class invoice_serializer(serializers.HyperlinkedModelSerializer):
    invoice_id = models.IntegerField(primary_key=True)

    class Meta:
        model = Invoice
        fields = '__all__'


class project_serializer(serializers.HyperlinkedModelSerializer):
    project_id = models.IntegerField(primary_key=True)
    client = client_serializer(read_only=True, allow_null=True)
    dev = dev_serializer(read_only=True, allow_null=True)

    class Meta:
        model = Project
        fields = ('__all__')


def create(self, validated_data):
    request = self.context['request']
    # Get DEV
    devjson = request.data.get("dev")
    username = devjson["username"];
    dev = Dev.objects.filter(username=username)[0]
    validated_data['dev'] = dev
    # Get USER
    clientJson = request.data.get("client")
    mail = clientJson["mail"]
    client = Client.objects.filter(mail=mail)[0]
    validated_data['client'] = client
    print(client)

    instance = super().create(validated_data)

    return instance
