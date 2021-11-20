from django.db import models
from django.db.models import query
from django.http import response
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from django.shortcuts import get_object_or_404

#TODO Build Abstract user Views


class ListMoodEntryView(APIView): 
    queryset = MoodEntry.objects.all().order_by("-date_created")
    serializer = MoodEntrySerializer


class MoodView(APIView): 

    def get(self,request,id=None):
        if id:
            entry = get_object_or_404(MoodEntry,id=id)
            serializer = MoodEntrySerializer(entry)
            return Response({"status": "success", "data": serializer.data},status=status.HTTP_200_OK)
        else: 
            entry = MoodEntry.objects.all()
            serializer = MoodEntrySerializer(entry,many=True)
            return Response({"status": "success","data": serializer.data},status=status.HTTP_200_OK)

    def post(self,request): 
        serializer = MoodEntrySerializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response({"status": "success","data": serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({"status": "error","data": serializer.errors},status=status.HTTP_400_BAD_REQUEST) 

    def delete(self,request,id=None): 
        entry = get_object_or_404(MoodEntry,id=id)
        entry.delete() 
        return Response({"status": "success","data": "Mood Entry Removed"})

