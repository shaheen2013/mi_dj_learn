from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from drf.serializers import TodoSerializer
from drf.models import Todo
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class TodoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
