from rest_framework.serializers import ModelSerializer
from backendLivraria.models.init import Categoria

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        