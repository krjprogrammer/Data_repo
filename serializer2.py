from rest_framework import serializers

from .models import Data_Model

class DataModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data_Model
        fields = '__all__'