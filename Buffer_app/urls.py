from django.urls import path
from.import views

from.views import PublicationBuffer
urlpatterns = [
    path('Buffer_app/',views.Buffer_app, name = 'Buffer_app'),
    path('PublicationBuffer/',PublicationBuffer, name = 'PublicationBuffer'),
]