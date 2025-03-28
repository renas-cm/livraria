# here we have only one path, which is the admin path, which is the path to the admin site
# We will add the path to the application we created, which is the backendLivraria application.

from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from usuario.router import router as usuario_router

from django.conf import settings
from django.conf.urls.static import static

from uploader.router import router as uploader_router

# Importing viewsets for the respective models in the backendLivraria application
from backendLivraria.views.init import CategoriaViewSet, EditoraViewSet, AutorViewSet, LivroViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'editoras', EditoraViewSet)
router.register(r'autores', AutorViewSet)
router.register(r'livros', LivroViewSet)

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path("api/", include(usuario_router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/media/", include(uploader_router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
