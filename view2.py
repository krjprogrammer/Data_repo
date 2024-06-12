from django.shortcuts import render
import csv
import sqlite3
from io import StringIO
from django.db.models import Q
from django.core.serializers import serialize
from django.urls import reverse
from django.http import JsonResponse,FileResponse,HttpResponse
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import zipfile
import tempfile,time
from rest_framework.response import Response
import re
from io import BytesIO
from pathlib import Path
import os,json
import pdfplumber
from django.forms.models import model_to_dict
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from .models import MappingData,Column_mapping_data,company_onbording_payment,sub_company_onbording_payment,vendor_onbording_payment,ban_onboarding_payment,UserLogs,otp_verification_table
from .serializers import post_mapping_serializer,get_mapping_serializer,column_serializer,company_onbording_payment_serializer,sub_company_onbording_payment_serializer,vendor_onbording_payment_serializer,ban_onbording_payment_serializer
from rest_framework import status
from .models import Data_Model
from .serializers import DataModelSerializer

class EditDataModel(APIView):
    def get_object(self, id):
        try:
            return Data_Model.objects.get(id=id)
        except Data_Model.DoesNotExist:
            return Response({"error": "record not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        data_model = self.get_object(id)
        serializer = DataModelSerializer(data_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteDataModel(APIView):
    def delete(self, request, id):
        try:
            instance = Data_Model.objects.get(id=id)
        except Data_Model.DoesNotExist:
            return Response({"error": "record not found"}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response({"success": "Record Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)

class CreateDataModel(APIView):
    def post(self, request):
        serializer = DataModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GetDataModel(APIView):
    def get(self, request):
        data_models = Data_Model.objects.all()
        serializer = DataModelSerializer(data_models, many=True)
        return Response(serializer.data)
