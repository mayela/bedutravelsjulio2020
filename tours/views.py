from rest_framework import viewsets

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Tour, User, Zona
from .serializers import TourSerializer, UserSerializer, ZonaSerializer

@login_required
def index(request):
    """ Vista para atender la petición de la url / """
    # Obteniendo los datos mediantes consultas
    tours = Tour.objects.all()

    return render(request, "tours/index.html", {"tours":tours})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ZonaViewSet(viewsets.ModelViewSet):
    queryset = Zona.objects.all()
    serializer_class = ZonaSerializer


class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer