from rest_framework.routers import DefaultRouter
from django.urls import path, include
from pulse.views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
  path('', include(router.urls)),
]