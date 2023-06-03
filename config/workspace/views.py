from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .serializer import WorkspaceSerializer, MembershipSerializer, BoardSerializer
from users.models import CustomUser
from utils.custom_class_permissions import has_object_permission
from .models import Workspace, Membership, Board

# Create your views here.

class CreateWorkspaceView(APIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        serializer = WorkspaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':serializer.errors})


class RetrieveWorkspaceView(APIView):
    permission_classes = [IsAuthenticated]
    uthentication_classes = [JWTAuthentication]

    def get(self,request,pk):
        workspace = Workspace.objects.filter(pk=pk)
        if not has_object_permission(request=request.user,obj=workspace[0]):
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error':'permission denied!'})            
        if workspace.exists():
            serializer = WorkspaceSerializer(workspace, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':'User dose not have workspace!'})
    
    def put(self,request,pk):
        workspace = Workspace.objects.filter(pk=pk)
        if not has_object_permission(request=request.user,obj=workspace[0]):
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error':'permission denied!'})            
        serializer = WorkspaceSerializer(data=request.data)
        if serializer.is_valid():
            workspace.update(owner=request.data['owner'], subject=request.data['subject'],
                             description=request.data['description'])
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':serializer.errors})
    

class CreateBoardView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':serializer.errors})
        
    
class RetrieveBoardView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,pk):
        board = get_object_or_404(Board, pk=pk)
        workspace = get_object_or_404(Workspace, pk=board.workspace_id)
        if not has_object_permission(request=request.user,obj=workspace):
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error':'permission denied!'})
        serializer = BoardSerializer(board)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def put(self,request,pk):
        board = get_object_or_404(Board,pk=pk)
        workspace = get_object_or_404(Workspace,pk=board.workspace_id)
        if not has_object_permission(request=request.user,obj=workspace):
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error':'permission denied!'})
        serializer = BoardSerializer(board,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':serializer.errors})
        


class MembershipView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        workspace = get_object_or_404(Workspace,pk=request.data['workspace'])
        if not has_object_permission(request=request.user, obj=workspace[0]):
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error':'permission denied!'}) 
        
        obj = Membership.objects.filter(workspace=request.data['workspace'],
                                        user=request.data['user'])
        if obj.exists():
            return Response(status=status.HTTP_409_CONFLICT, data={'error':'User already is a member of Workspace'})
        serializer = MembershipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':serializer.errors})