from rest_framework import viewsets
from api.serializers import dataSerializer
from api.models import data

class dataViewset(viewsets.ModelViewSet):
    http_method_names = ["get"]
    queryset = data.objects.all()
    serializer_class = dataSerializer
