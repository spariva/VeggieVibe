from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from recipes.models import Recipe

class Profile(models.Model):
    # Asocio el perfil con un usuario, así 
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # Campos adicionales que hay en profile y no en user
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='users/static/users/images/', blank=True)

# Decorator para que si un usuario se crea, se crea un perfil asociado, y lo mismo para cuando actualiza.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
#* from django.contrib.auth.models import AbstrUser

# * class CustomUser(AbstractUser): 
# # Extender el modelo de usuario de Django, no sobreescribirlo
#     # Agregar campos personalizados si es necesario
#     bio = models.TextField(blank=True)
#     profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
#     favourite_recipes = models.ManyToManyField('recipes.Recipe', related_name='favorited_by', blank=True)

    
# ? Modelo de recetas favoritas del user
class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'recipe')
        verbose_name = 'fav_recipe'
        verbose_name_plural = 'fav_recipes'
    
    def __str__(self):
        return f'{self.user.username} likes: {self.recipe.title}'