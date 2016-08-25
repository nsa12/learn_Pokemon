import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PokemonGo.settings')

import django
django.setup()

from search.models import Pokedex
from search.views import search_pokemon

def populate():
	for pokemon in search_pokemon('*', result_type='dict'):
		add(pokemon_name=pokemon['name'], pokemon_image=pokemon['image_url'])

def showDB():
	for pokemon in Pokedex.objects.all():
		print pokemon

def add(pokemon_name,pokemon_image, pokemon_type='N/A'):
	try:
		p = Pokedex.objects.get_or_create(pokemon_name=pokemon_name, pokemon_image=pokemon_image, pokemon_type=pokemon_type)[0]		#get_or_create either updates it or creates it- even if we run the program multiple times, multiple copies of an object are not created
		p.save()
	except:
		print 'ERROR'
		print pokemon_name
		return
	
	showDB()

if __name__ == '__main__':
	populate()
	#print search_pokemon('*', 'dict')
	#populate()
	#showDB()