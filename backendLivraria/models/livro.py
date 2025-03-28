from django.db import models
from .init import Editora, Autor, Categoria

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    quantidade = models.IntegerField(default=0, null=True, blank=True) 
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='livros')
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE, related_name='livros')
    autores = models.ManyToManyField(Autor, related_name='livros')
    
    def __str__(self):
        return f"{self.titulo} ({self.quantidade})"       
    
    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'