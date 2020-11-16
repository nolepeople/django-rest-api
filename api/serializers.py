from rest_framework import serializers
from api.models import data

class dataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = data
        fields = (
                "positif",
                "sembuh",
                "meninggal",
                "dirawat",
                )
      
