from django.db import models

class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombres', max_length = 200, blank = False, null = False)
    apellidos = models.CharField('Apellidos', max_length = 220, blank = False, null = False)
    nacionalidad = models.CharField('Nacionalidad', max_length = 100, blank = False, null = False)
    descripcion = models.TextField('Descripción', blank = True, null = True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Título', max_length = 200, blank = False, null = False)
    fecha_publicacion = models.DateField('Fecha de plublicación', auto_now=False, auto_now_add=False, blank = False, null = False)
    autor_id = models.ManyToManyField(Autor, verbose_name = 'Autor(es)')

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return self.titulo