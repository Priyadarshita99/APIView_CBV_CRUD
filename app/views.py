from django.shortcuts import render

# Create your views here.
from app.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import APIView

class ProductCrud(APIView):
    def get(self,request):
        PDO=Product.objects.all()  #ORM
        PJO=ProductModelSerializer(PDO,many=True)  #Json
        return Response(PJO.data)
    
    def post(self,request):
        JDO=request.data
        PDO=ProductModelSerializer(data=JDO)
        if PDO.is_valid():
            PDO.save()
            return Response({'Insert':'Data is inserted Successfully'})
        else:
            return Response({'Error':'Data is not inserted'})   #Error-Single quote,','
        