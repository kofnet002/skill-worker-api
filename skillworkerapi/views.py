from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

from django.http import HttpResponse

# Create your views here.
class Home(APIView):
    def get(self, request):
        data = User.objects.all()
        serializer_data = UserSerializer(data, many=True)
        return Response(serializer_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialzer = UserSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(request, status=status.HTTP_201_CREATED)
        return Response(request, status=status.HTTP_400_BAD_REQUEST)