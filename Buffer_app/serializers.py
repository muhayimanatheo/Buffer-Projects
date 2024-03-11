from rest_framework import serializers
from.models import *
class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        models = Publication
        fields = '__all__'