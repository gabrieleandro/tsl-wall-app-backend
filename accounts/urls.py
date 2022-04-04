from django.urls import path

from .views import UserList, UserDetail

urlpatterns = [
    path('users/', UserList.as_view(), name='users-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-details'),
]