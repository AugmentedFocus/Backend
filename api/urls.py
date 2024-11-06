from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, CourseViewSet, UnitViewSet, ActivityViewSet, GradeViewSet, EventViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'units', UnitViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'grades', GradeViewSet)
router.register(r'events', EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
