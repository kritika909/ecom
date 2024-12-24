from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkflowViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'workflows', WorkflowViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]