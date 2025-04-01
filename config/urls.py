# This file is responsible for routing the requests to the respective applications
# Importing the path, include, static and settings modules from the django.urls module

from django.contrib import admin
from django.urls import path, include

# Importing the static and settings modules from the django.conf.urls module

from django.conf.urls.static import static
from django.conf import settings

# Importing the DefaultRouter from the rest_framework.routers module

from rest_framework.routers import DefaultRouter

# Importing the TokenObtainPairView and TokenRefreshView from the rest_framework_simplejwt.views module

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Importing the routers for the respective applications

from usuario.router import router as usuario_router
from uploader.router import router as uploader_router

# Importing the views for the API documentation

from drf_spectacular.views import(
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

# Importing viewsets for the respective models in the backendLivraria application
from backendLivraria.views.init import CategoriaViewSet, EditoraViewSet, AutorViewSet, LivroViewSet

# Creating a router object

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'editoras', EditoraViewSet)
router.register(r'autores', AutorViewSet)
router.register(r'livros', LivroViewSet)

# Creating a list of urlpatterns

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path("api/", include(router.urls)),
    
    path("api/token/",
         TokenObtainPairView.as_view(), 
         name="token_obtain_pair"
        ),
    path("api/token/refresh/", 
         TokenRefreshView.as_view(), 
         name="token_refresh"
        ),
    
    path("api/media/", include(uploader_router.urls)),
    
    path("api/schema/", 
         SpectacularAPIView.as_view(),
         name="schema"
        ),
    path("api/swagger/",
         SpectacularSwaggerView.as_view(url_name="schema"),
         name="swagger"
        ),
    path("api/redoc/",
         SpectacularRedocView.as_view(url_name="schema"),
         name="redoc"
        ),
]

# Adding the router urls to the urlpatterns list

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
