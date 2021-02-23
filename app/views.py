from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from app.models import ProductModel
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from app.serializers import ProductSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(csrf_exempt,name="dispatch")
class Product(View):
    def post(self,request):
        binary_data = request.body
        st_data = io.BytesIO(binary_data)
        dict_data = JSONParser().parse(st_data)

        ps = ProductSerializer(data=dict_data)
        if ps. is_valid():
            ps.save()
            message = {"message":"Product is saved"}
        else:
            message = {"error":ps.errors}

        json_data = JSONRenderer().render(message)
        return HttpResponse(json_data,content_type="application/json")

class Viewproducts(View):
    def get(self,request):
        result = ProductModel.objects.all()
        ps = ProductSerializer(result,many=True)
        json_data = JSONRenderer().render(ps.data)
        return HttpResponse(json_data,content_type="application/json")