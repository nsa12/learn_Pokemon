from django.db import models

# Create your models here.
class Pokedex(models.Model):			#Used to define structure of database
	pokemon_name = models.CharField(max_length=128, unique=True)
	pokemon_type = models.CharField(max_length=128)
	pokemon_image = models.CharField(max_length=128)

	def __unicode__ (self):			#called when print instance is called
		return self.pokemon_name