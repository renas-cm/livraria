from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
