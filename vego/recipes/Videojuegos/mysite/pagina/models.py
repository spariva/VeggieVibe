from audioop import reverse
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Genero(models.Model):
    genero_text = models.CharField(max_length=30)

    def __str__(self):
        return self.genero_text

class Juego(models.Model):
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)  
    juego_text = models.CharField(max_length=30)
    pub_date = models.DateField("date published")  
    valoracion = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) 
    votos = models.IntegerField(default=0)

    def __str__(self):
        return f"Juego: {self.juego_text}, \
        Genero: {self.genero}, \
        Fecha de publicación: {self.pub_date}, \
        Valoración: {self.valoracion}"   
        
class Descripcion(models.Model):
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    descripcion_text = models.TextField()
    #imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)

    def __str__(self):
        return self.descripcion_text
        #return f"Juego: {self.juego}, \
        #Descripción: {self.descripcion_text}, \

