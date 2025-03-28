from rest_framework.serializers import ModelSerializer
from backendLivraria.models.init import Autor

class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'