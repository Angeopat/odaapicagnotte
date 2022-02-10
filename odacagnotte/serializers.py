from rest_framework import serializers
from .models import*

class AcademicienSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academicien
        fields = '_all'

class MotifSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motif
        fields = '_all'

class PaiementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paiements
        fields = '_all'