from rest_framework.exceptions import APIException
from rest_framework.response import Response
from django.shortcuts import render,redirect,get_object_or_404
from rest_framework import generics, viewsets,status 
from rest_framework.serializers import Serializer
from .permissions import IsAuthor
from .models import * 
from .serializers import * 

class MoodEntryView(generics.RetrieveDestroyAPIView): 

    def get_queryset(self):
        return moodEntry.objects.filter(created_by=self.request.user)

    queryset = moodEntry.objects.all()
    serializer_class = MoodEntrySerializer

    def get(self,request,pk=None): 
        entry = get_object_or_404(moodEntry,id=pk)
        serializer = self.serializer_class(entry)
        return Response(serializer.data)

    def delete(self,request,pk=None):
        entry = get_object_or_404(moodEntry,id=pk)
        entry.delete()
        return Response({'message': f'Entry {pk} Sucessfully Deleted'},status=status.HTTP_200_OK)
    

class MoodListView(generics.ListCreateAPIView): 
    def get_queryset(self):
        return moodEntry.objects.filter(created_by=self.request.user)

    queryset = moodEntry.objects.all()
    serializer_class = MoodEntrySerializer

    '''
    def post(self,request,pk): 
        if serializer.is_valid(): 
            serializer.ob
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    '''

    #TODO PATCH METHOD??

class MoodBoardView(viewsets.ModelViewSet): 
   
    def get_queryset(self):
        return get_user_model().objects.filter(username=self.request.user.username)

    queryset = get_user_model().objects.all()
    serializer_class = MoodBoardSerializer



    

#TODO MoodBoard View 


