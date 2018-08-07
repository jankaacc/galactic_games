from rest_framework import serializers


from . import models


class GladiatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Gladiator
        fields = ['name',
                  'profession',
                  'species',
                  'race']
        depth = 1
