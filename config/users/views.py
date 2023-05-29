from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from django.shortcuts import get_object_or_404


from .models import CustomUser
from .serializer import UserSerializer

# Create your views here.

class UserRegisterationView(APIView):
    def post(self,request):
        print('here')
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            print('wtf')
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            email = serializer.validated_data['email']
            user = CustomUser.objects.create_user(username=username, password=password,
                                            email=email, first_name=serializer.data['first_name'],
                                            last_name=serializer.data['last_name'])
            user.save()

            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST,data={'errors':serializer.errors})

class LogoutView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            print(request.headers['Authorization'])
            request.headers['Authorization'] = ''
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserRetrieveView(APIView):
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def get(self,request,pk):
        user = get_object_or_404(CustomUser, pk=pk)
        serializer = UserSerializer(user)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self,request,pk):
        serializer = UserSerializer(request.user,data=request.data,partial=True)
        if serializer.is_valid():
            user = get_object_or_404(CustomUser, pk=pk)
            user.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'erros' : serializer.errors})
