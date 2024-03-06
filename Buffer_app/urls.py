from django.urls import path
from.import views
urlpatterns = [
    path('Buffer_app/',views.Buffer_app, name = 'Buffer_app'),
]