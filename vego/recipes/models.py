from django.db import models
from django.contrib.auth import get_user_model
# from users.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    steps = models.TextField()
    tags = models.ManyToManyField('Tag', related_name='recipes', blank=True)
    image = models.ImageField(upload_to='recipe_images/', blank=True)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='created_recipes')

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
# Arania web scrapy para obtener recetas, 