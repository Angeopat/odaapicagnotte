from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import*

class Motif(APIView):

    def post(self, request):
        serializer = MotifSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    def get(self,request):
        motif = Motif.objects.all()
        serializer = MotifSerializer(motif, many=True)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data)


