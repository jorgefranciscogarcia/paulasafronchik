from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='projects')
    link = models.URLField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    # Pasos para convertir al español las palabras en el admin
    # class Meta:
    #     verbose_name = 'proyecto'
    #     verbose_name_plural = 'proyectos'
    #     ordering = ['-created']
    #
    # Para que muestre el título del proyecto en el link desde el admin
    def __str__(self):
        return self.title