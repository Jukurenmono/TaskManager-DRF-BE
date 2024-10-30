from django.urls import path
from .views import (TaskViewSet)

urlpatterns = [
    path('', TaskViewSet.as_view({
        'get' : 'list',
        'post' : 'post'
    })),
    path('<int:pk>', TaskViewSet.as_view({
        'patch' : 'patch',
        'get' : 'get',
        'delete' : 'delete'
    }))
]