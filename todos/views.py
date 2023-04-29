from rest_framework.generics import get_object_or_404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from todos.models import TodoList
from todos.serializers import TodoListCompleteSerializer, TodoListSerializer, TodoListCreateSerializer
# Create your views here.


class TodoListView(APIView):# serializer 수정? 꾸미기?
    def get(self, request):
        todo_list = TodoList.objects.all()
        serializer = TodoListSerializer(todo_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class TodoListCreateView(APIView):
    def post(self, request):
        serializer = TodoListCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response("todo_list 작성 완료!", status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class TodoListEditView(APIView):
    def put(self, request, todo_list_id):
        todo_list = get_object_or_404(TodoList, id=todo_list_id)
        serializer = TodoListCreateSerializer(todo_list, data=request.data)
        if request.user == todo_list.user:
            serializer = TodoListCreateSerializer(todo_list, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이없습니다.", status=status.HTTP_403_FORBIDDEN)
        
    def delete(self, request, todo_list_id):
        todo_list = get_object_or_404(TodoList, id=todo_list_id)
        if request.user == todo_list.user:
            todo_list.delete()
            return Response("삭제완료!",status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이없습니다.", status=status.HTTP_403_FORBIDDEN)


class TodoListCompleteView(APIView):
    def put(self, request, todo_list_id):
        todo_list = get_object_or_404(TodoList, id=todo_list_id)
        serializer = TodoListCompleteSerializer(todo_list, data=request.data)
        if request.user == todo_list.user:
            serializer = TodoListCompleteSerializer(todo_list, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이없습니다.", status=status.HTTP_403_FORBIDDEN)