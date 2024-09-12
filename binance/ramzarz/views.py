from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import json


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


