from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateWorkspaceView.as_view(), name='create_workspace'),
    path('<int:pk>/', views.RetrieveWorkspace.as_view(), name='retrieve_workspace'),
    path('add/', views.MembershipView.as_view(), name='add_member'),
]