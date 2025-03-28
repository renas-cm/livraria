from rest_framework.serializers import ModelSerializer
from backendLivraria.models.init import Editora

class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'