# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import BookViewSet  

# router = DefaultRouter()
# router.register(r'books', BookViewSet)

# urlpatterns = [
#     path('', include(router.urls)),

# ]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet  # Ensure correct import path

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]