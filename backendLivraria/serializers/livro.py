from rest_framework.serializers import ModelSerializer
from backendLivraria.models.init import Livro

from rest_framework.serializers import ModelSerializer, SlugRelatedField

from uploader.models import  Image
from uploader.serializers import ImageSerializer

class LivroSerializer(ModelSerializer):
    capa_attchment_key = SlugRelatedField(
        source = "capa",
        queryset = Image.objects.all(),
        slug_field = "attchment_key",
        required = False,
        write_only = True
    )
    cap= ImageSerializer(required=False, read_only=True)
    
    class Meta:
        model = Livro
        fields = '__all__'
        


class LivroDetailSerializer(ModelSerializer):
    capa = ImageSerializer(required=False)
    
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

