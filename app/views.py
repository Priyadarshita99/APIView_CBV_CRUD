from django.shortcuts import render

# Create your views here.
from app.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import APIView

class ProductCrud(APIView):
    def get(self,request,id):
        PDO=Product.objects.all()         #ORM
        #PDO=Product.objects.get(id=id)      #for id url

        PJO=ProductModelSerializer(PDO,many=True)     #Json
        #PJO=ProductModelSerializer(PDO)                #for one id details
        return Response(PJO.data)
    
    def post(self,request,id):            #url(id) u can write anyid
        JDO=request.data
        PDO=ProductModelSerializer(data=JDO)
        if PDO.is_valid():
            PDO.save()
            return Response({'Insert':'Data is inserted Successfully'})   #Error-Single quote,','
        else:
            return Response({'Error':'Data is not inserted'})   
        
    def put(self,request,id):            #url(id) u can write the id which u want to update
        PO=Product.objects.get(id=id)
        UPDO=ProductModelSerializer(PO,data=request.data)
        if UPDO.is_valid():
            UPDO.save()
            return Response({'Update':'Updation done successfully'})
        else:
            return Response({'Error':'Updation unsuccessful'})
        
    def patch(self,request,id):            #url(id) u can write the id which u want to update
        PO=Product.objects.get(id=id)
        UPDO=ProductModelSerializer(PO,data=request.data,partial=True)
        if UPDO.is_valid():
            UPDO.save()
            return Response({'Update':'Updation done successfully'})
        else:
            return Response({'Error':'Updation unsuccessful'})
        
    def delete(self,request,id):
        DO=Product.objects.get(id=id).delete()
        return Response({'Delete':'Data deleted Successfully'})
    