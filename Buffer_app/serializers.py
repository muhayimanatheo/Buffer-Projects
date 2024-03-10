from rest_framework import serializers
from.models import *
class PublicationsSerializer(serializers.ModelSerializer):
    class Meta:
        models = Publications
        fields = '__all__'