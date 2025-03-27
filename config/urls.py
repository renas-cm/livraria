# here we have only one path, which is the admin path, which is the path to the admin site
# We will add the path to the application we created, which is the backendLivraria application.

from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

# Importing viewsets for the respective models in the backendLivraria application
from backendLivraria.views import CategoriaViewSet, EditoraViewSet, AutorViewSet, LivroViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'editoras', EditoraViewSet)
router.register(r'autores', AutorViewSet)
router.register(r'livros', LivroViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
