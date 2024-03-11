from rest_framework import serializers
from.models import *
class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ['name', 'image', 'header', 'description']