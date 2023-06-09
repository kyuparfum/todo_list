from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import users
from users.models import User
from users.serializers import CustomTokenObtainPairSerializer, UserCreateSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView




class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"massage":"가입완료"}, status=status.HTTP_200_OK)
        else:
            return Response({"massage":f"{serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserCreateSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class LoginView(APIView):# 로그인확인용
    permission_classes=[permissions.IsAuthenticated]# 로그인됐을 때만 작업가능.
    def get(self, request):
        return Response("get test")

class UserEditView(APIView):
    def put(self,request,user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserCreateSerializer(user, data=request.data)
        if request.user == user:
            serializer = UserCreateSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)
        
    def delete(self,request,user_id):
        user = get_object_or_404(User, id=user_id)
        if request.user == user:
            user.delete()
            return Response("탈퇴 되었습니다.", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)
        
