from rest_framework.exceptions import APIException
from rest_framework.response import Response
from django.shortcuts import render,redirect,get_object_or_404
from rest_framework import generics, viewsets,status 
from rest_framework.serializers import Serializer
from .permissions import IsAuthorOrReadOnly 
from .models import * 
from .serializers import * 

class MoodEntryView(generics.RetrieveDestroyAPIView): 

    def get_queryset(self):
        return moodEntry.objects.filter(created_by=self.request.user)

    queryset = moodEntry.objects.all()
    serializer_class = MoodEntrySerializer

    def post(self,request,pk): 
        #TODO add modd entry via post
        serializer = MoodEntrySerializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request,pk=None): 
        entry = get_object_or_404(moodEntry,id=pk)
        serializer = MoodEntrySerializer(entry)
        return Response(serializer.data)


    #TODO PATCH METHOD??
    
    #TODO DELETE METHD??? (complete CRUD)


#TODO MoodBoard View 


