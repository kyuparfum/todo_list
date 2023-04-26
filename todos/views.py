from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
# from todos.serializers import CustomTokenObtainPairSerializer, UserSerializer
# Create your views here.


class TodoView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        pass
