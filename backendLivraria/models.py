from django.db import models

# Models for the Livraria application, representing categories, publishers, authors, and books.


class Categoria(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Editora(models.Model):
    nome = models.CharField(max_length=255)
    site = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'
    
class Autor(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        
class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    quantidade = models.IntegerField(default=0, null=True, blank=True) 
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE, related_name='livros')
    
    def __str__(self):
        return f"{self.titulo} ({self.quantidade})"       
    
    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'