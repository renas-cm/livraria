from rest_framework.viewsets import ModelViewSet
from backendLivraria.models.init import Livro
from backendLivraria.serializers.init import LivroSerializer, LivroDetailSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    
    def  get_serializer_class(self):
        if self.action in ['list', 'retrive']:
            return LivroDetailSerializer
        return LivroSerializer
        