from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from.models import Publication
from.serializers import PublicationSerializer
import json
# from django.views.decorators.csrf import csrf_exempt
from .import views
from rest_framework.parsers import JSONParser



def Buffer_app(request):
    return HttpResponse("Hello world!")

# @csrf_exempt
def PublicationBuffer(request):
    if request.method == 'GET':
        selectedData = Publication.objects.all()
        serializer = PublicationSerializer(selectedData, many=True)
        return JsonResponse(data=serializer.data, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'})
