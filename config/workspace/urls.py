from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateWorkspaceView.as_view(), name='create_workspace'),
    path('<int:pk>/', views.RetrieveWorkspaceView.as_view(), name='retrieve_workspace'),
    path('add/', views.MembershipView.as_view(), name='add_member'),
    path('board/', views.CreateBoardView.as_view(), name='create_board'),
    path('board/<int:pk>/', views.RetrieveBoardView.as_view(), name='retrieve_board'),
]