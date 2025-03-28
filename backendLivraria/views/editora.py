from rest_framework.viewsets import ModelViewSet
from backendLivraria.models.init import Editora
from backendLivraria.serializers.init import EditoraSerializer

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer