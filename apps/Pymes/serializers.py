from rest_framework import serializers
from .models import Producto,Pyme

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class PymeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pyme
        fields = '__all__'
