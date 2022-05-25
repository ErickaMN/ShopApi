
from rest_framework.routers import SimpleRouter
from . import views
from django.urls import path, include


router = SimpleRouter()
router.register('products',views.ProductViewSet)
router.register('categories', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls))

]