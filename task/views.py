from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import TaskSerializer
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        task = self.serializer_class.Meta.model.objects.get(pk=pk)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk, format=None):
        try:
            task = self.serializer_class.Meta.model.objects.get(id=pk)
            serializer = self.serializer_class(task)
            return Response(serializer.data)
        except self.serializer_class.Meta.model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk, *args, **kwargs):
        try:
            self.serializer_class.Meta.model.objects.get(pk=pk).delete()
            return Response(status=status.HTTP_200_OK)
        except self.serializer_class.Meta.model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
