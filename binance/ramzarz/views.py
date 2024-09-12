from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from .serializer import ShartSerializer
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView
from rest_framework.permissions import IsAuthenticated
from .models import Shart
import requests
import json


class Login(TokenObtainPairView):
    pass



class MyAPI(APIView):
    def post(self , request):
        ramzarz = request.data.get("ramzarz")
        url = "https://api.nobitex.ir/market/stats?srcCurrency="+ ramzarz +"&dstCurrency=rls"
        response = requests.get(url)
        return Response(json.loads(response.content)["stats"][f"{ramzarz}-rls"]["latest"])


class History(APIView):
    def post(self , request):
        ramzarz = request.data.get("ramzarz")
        url = "https://api.nobitex.ir/market/stats?srcCurrency="+ ramzarz +"&dstCurrency=rls"
        response = requests.get(url)
        return Response(json.loads(response.content)["stats"][f"{ramzarz}-rls"]["dayChange"])


class NewShart(CreateAPIView):
    queryset = Shart.object.all()
    serializer_class = ShartSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)
    
