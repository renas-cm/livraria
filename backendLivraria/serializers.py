# Description: Serializers for the models of the application.
# That will transform the data(obj) into JSON format.

from rest_framework.serializers import ModelSerializer

from .models import Categoria, Editora, Autor, Livro

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        
class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'

class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'


class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'


class LivroDetailSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'
        depth = 1

class LivroListSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = ['id','titulo','preco']
        
        def get_serializer_class(self):
            if self.action == 'list':
                return LivroListSerializer
            elif self.action == 'retrieve':
                return LivroDetailSerializer
            return LivroSerializer

