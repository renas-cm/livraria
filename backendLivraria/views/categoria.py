from rest_framework.viewsets import ModelViewSet
from backendLivraria.models.init import Categoria
from backendLivraria.serializers.init import CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    #permission_classes = [IsAuthenticated]