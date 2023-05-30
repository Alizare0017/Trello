from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializer import WorkpaceSerializer, MembershipSerializer
from users.models import CustomUser

from .models import Workspace, Membership

# Create your views here.

class CreateWorkspaceView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self,request):
        serializer = WorkpaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':serializer.errors})
    

class RetrieveWorkspace(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self,request,pk):
        workspace = Workspace.objects.filter(pk=pk)
        if workspace.exists():
            serializer = WorkpaceSerializer(workspace, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':'User dose not have workspace!'})
    

class MembershipView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self,request):
        obj = Membership.objects.filter(workspace=request.data['workspace'],
                                        user=request.data['user'])
        if obj.exists():
            return Response(status=status.HTTP_409_CONFLICT, data={'error':'User already has permission to workspace'})
        serializer = MembershipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':serializer.errors})