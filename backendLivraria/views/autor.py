from rest_framework.viewsets import ModelViewSet
from backendLivraria.models.init import Autor
from backendLivraria.serializers.init import AutorSerializer

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer