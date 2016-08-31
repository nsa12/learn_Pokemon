from django.shortcuts import render, redirect
from django.http import HttpResponse
import time

import os
from django.conf import settings

from random import randint, shuffle

from search.models import Pokedex

# Create your views here.

pokemon_data = {"Bulbasaur":"http://img.pokemondb.net/artwork/bulbasaur.jpg","Ivysaur":"http://img.pokemondb.net/artwork/ivysaur.jpg","Venusaur":"http://img.pokemondb.net/artwork/venusaur.jpg","Charmander":"http://img.pokemondb.net/artwork/charmander.jpg","Charmeleon":"http://img.pokemondb.net/artwork/charmeleon.jpg","Charizard":"http://img.pokemondb.net/artwork/charizard.jpg","Squirtle":"http://img.pokemondb.net/artwork/squirtle.jpg","Wartortle":"http://img.pokemondb.net/artwork/wartortle.jpg","Blastoise":"http://img.pokemondb.net/artwork/blastoise.jpg","Caterpie":"http://img.pokemondb.net/artwork/caterpie.jpg","Metapod":"http://img.pokemondb.net/artwork/metapod.jpg","Butterfree":"http://img.pokemondb.net/artwork/butterfree.jpg","Weedle":"http://img.pokemondb.net/artwork/weedle.jpg","Kakuna":"http://img.pokemondb.net/artwork/kakuna.jpg","Beedrill":"http://img.pokemondb.net/artwork/beedrill.jpg","Pidgey":"http://img.pokemondb.net/artwork/pidgey.jpg","Pidgeotto":"http://img.pokemondb.net/artwork/pidgeotto.jpg","Pidgeot":"http://img.pokemondb.net/artwork/pidgeot.jpg","Rattata":"http://img.pokemondb.net/artwork/rattata.jpg","Raticate":"http://img.pokemondb.net/artwork/raticate.jpg","Spearow":"http://img.pokemondb.net/artwork/spearow.jpg","Fearow":"http://img.pokemondb.net/artwork/fearow.jpg","Ekans":"http://img.pokemondb.net/artwork/ekans.jpg","Arbok":"http://img.pokemondb.net/artwork/arbok.jpg","Pikachu":"http://img.pokemondb.net/artwork/pikachu.jpg","Raichu":"http://img.pokemondb.net/artwork/raichu.jpg","Sandshrew":"http://img.pokemondb.net/artwork/sandshrew.jpg","Sandslash":"http://img.pokemondb.net/artwork/sandslash.jpg","Nidoran?":"http://img.pokemondb.net/artwork/nidoran?.jpg","Nidorina":"http://img.pokemondb.net/artwork/nidorina.jpg","Nidoqueen":"http://img.pokemondb.net/artwork/nidoqueen.jpg","Nidorino":"http://img.pokemondb.net/artwork/nidorino.jpg","Nidoking":"http://img.pokemondb.net/artwork/nidoking.jpg","Clefairy":"http://img.pokemondb.net/artwork/clefairy.jpg","Clefable":"http://img.pokemondb.net/artwork/clefable.jpg","Vulpix":"http://img.pokemondb.net/artwork/vulpix.jpg","Ninetales":"http://img.pokemondb.net/artwork/ninetales.jpg","Jigglypuff":"http://img.pokemondb.net/artwork/jigglypuff.jpg","Wigglytuff":"http://img.pokemondb.net/artwork/wigglytuff.jpg","Zubat":"http://img.pokemondb.net/artwork/zubat.jpg","Golbat":"http://img.pokemondb.net/artwork/golbat.jpg","Oddish":"http://img.pokemondb.net/artwork/oddish.jpg","Gloom":"http://img.pokemondb.net/artwork/gloom.jpg","Vileplume":"http://img.pokemondb.net/artwork/vileplume.jpg","Paras":"http://img.pokemondb.net/artwork/paras.jpg","Parasect":"http://img.pokemondb.net/artwork/parasect.jpg","Venonat":"http://img.pokemondb.net/artwork/venonat.jpg","Venomoth":"http://img.pokemondb.net/artwork/venomoth.jpg","Diglett":"http://img.pokemondb.net/artwork/diglett.jpg","Dugtrio":"http://img.pokemondb.net/artwork/dugtrio.jpg","Meowth":"http://img.pokemondb.net/artwork/meowth.jpg","Persian":"http://img.pokemondb.net/artwork/persian.jpg","Psyduck":"http://img.pokemondb.net/artwork/psyduck.jpg","Golduck":"http://img.pokemondb.net/artwork/golduck.jpg","Mankey":"http://img.pokemondb.net/artwork/mankey.jpg","Primeape":"http://img.pokemondb.net/artwork/primeape.jpg","Growlithe":"http://img.pokemondb.net/artwork/growlithe.jpg","Arcanine":"http://img.pokemondb.net/artwork/arcanine.jpg","Poliwag":"http://img.pokemondb.net/artwork/poliwag.jpg","Poliwhirl":"http://img.pokemondb.net/artwork/poliwhirl.jpg","Poliwrath":"http://img.pokemondb.net/artwork/poliwrath.jpg","Abra":"http://img.pokemondb.net/artwork/abra.jpg","Kadabra":"http://img.pokemondb.net/artwork/kadabra.jpg","Alakazam":"http://img.pokemondb.net/artwork/alakazam.jpg","Machop":"http://img.pokemondb.net/artwork/machop.jpg","Machoke":"http://img.pokemondb.net/artwork/machoke.jpg","Machamp":"http://img.pokemondb.net/artwork/machamp.jpg","Bellsprout":"http://img.pokemondb.net/artwork/bellsprout.jpg","Weepinbell":"http://img.pokemondb.net/artwork/weepinbell.jpg","Victreebel":"http://img.pokemondb.net/artwork/victreebel.jpg","Tentacool":"http://img.pokemondb.net/artwork/tentacool.jpg","Tentacruel":"http://img.pokemondb.net/artwork/tentacruel.jpg","Geodude":"http://img.pokemondb.net/artwork/geodude.jpg","Graveler":"http://img.pokemondb.net/artwork/graveler.jpg","Golem":"http://img.pokemondb.net/artwork/golem.jpg","Ponyta":"http://img.pokemondb.net/artwork/ponyta.jpg","Rapidash":"http://img.pokemondb.net/artwork/rapidash.jpg","Slowpoke":"http://img.pokemondb.net/artwork/slowpoke.jpg","Slowbro":"http://img.pokemondb.net/artwork/slowbro.jpg","Magnemite":"http://img.pokemondb.net/artwork/magnemite.jpg","Magneton":"http://img.pokemondb.net/artwork/magneton.jpg","Farfetch'd":"http://img.pokemondb.net/artwork/farfetch'd.jpg","Doduo":"http://img.pokemondb.net/artwork/doduo.jpg","Dodrio":"http://img.pokemondb.net/artwork/dodrio.jpg","Seel":"http://img.pokemondb.net/artwork/seel.jpg","Dewgong":"http://img.pokemondb.net/artwork/dewgong.jpg","Grimer":"http://img.pokemondb.net/artwork/grimer.jpg","Muk":"http://img.pokemondb.net/artwork/muk.jpg","Shellder":"http://img.pokemondb.net/artwork/shellder.jpg","Cloyster":"http://img.pokemondb.net/artwork/cloyster.jpg","Gastly":"http://img.pokemondb.net/artwork/gastly.jpg","Haunter":"http://img.pokemondb.net/artwork/haunter.jpg","Gengar":"http://img.pokemondb.net/artwork/gengar.jpg","Onix":"http://img.pokemondb.net/artwork/onix.jpg","Drowzee":"http://img.pokemondb.net/artwork/drowzee.jpg","Hypno":"http://img.pokemondb.net/artwork/hypno.jpg","Krabby":"http://img.pokemondb.net/artwork/krabby.jpg","Kingler":"http://img.pokemondb.net/artwork/kingler.jpg","Voltorb":"http://img.pokemondb.net/artwork/voltorb.jpg","Electrode":"http://img.pokemondb.net/artwork/electrode.jpg","Exeggcute":"http://img.pokemondb.net/artwork/exeggcute.jpg","Exeggutor":"http://img.pokemondb.net/artwork/exeggutor.jpg","Cubone":"http://img.pokemondb.net/artwork/cubone.jpg","Marowak":"http://img.pokemondb.net/artwork/marowak.jpg","Hitmonlee":"http://img.pokemondb.net/artwork/hitmonlee.jpg","Hitmonchan":"http://img.pokemondb.net/artwork/hitmonchan.jpg","Lickitung":"http://img.pokemondb.net/artwork/lickitung.jpg","Koffing":"http://img.pokemondb.net/artwork/koffing.jpg","Weezing":"http://img.pokemondb.net/artwork/weezing.jpg","Rhyhorn":"http://img.pokemondb.net/artwork/rhyhorn.jpg","Rhydon":"http://img.pokemondb.net/artwork/rhydon.jpg","Chansey":"http://img.pokemondb.net/artwork/chansey.jpg","Tangela":"http://img.pokemondb.net/artwork/tangela.jpg","Kangaskhan":"http://img.pokemondb.net/artwork/kangaskhan.jpg","Horsea":"http://img.pokemondb.net/artwork/horsea.jpg","Seadra":"http://img.pokemondb.net/artwork/seadra.jpg","Goldeen":"http://img.pokemondb.net/artwork/goldeen.jpg","Seaking":"http://img.pokemondb.net/artwork/seaking.jpg","Staryu":"http://img.pokemondb.net/artwork/staryu.jpg","Starmie":"http://img.pokemondb.net/artwork/starmie.jpg","Mr. Mime":"http://img.pokemondb.net/artwork/mr. mime.jpg","Scyther":"http://img.pokemondb.net/artwork/scyther.jpg","Jynx":"http://img.pokemondb.net/artwork/jynx.jpg","Electabuzz":"http://img.pokemondb.net/artwork/electabuzz.jpg","Magmar":"http://img.pokemondb.net/artwork/magmar.jpg","Pinsir":"http://img.pokemondb.net/artwork/pinsir.jpg","Tauros":"http://img.pokemondb.net/artwork/tauros.jpg","Magikarp":"http://img.pokemondb.net/artwork/magikarp.jpg","Gyarados":"http://img.pokemondb.net/artwork/gyarados.jpg","Lapras":"http://img.pokemondb.net/artwork/lapras.jpg","Ditto":"http://img.pokemondb.net/artwork/ditto.jpg","Eevee":"http://img.pokemondb.net/artwork/eevee.jpg","Vaporeon":"http://img.pokemondb.net/artwork/vaporeon.jpg","Jolteon":"http://img.pokemondb.net/artwork/jolteon.jpg","Flareon":"http://img.pokemondb.net/artwork/flareon.jpg","Porygon":"http://img.pokemondb.net/artwork/porygon.jpg","Omanyte":"http://img.pokemondb.net/artwork/omanyte.jpg","Omastar":"http://img.pokemondb.net/artwork/omastar.jpg","Kabuto":"http://img.pokemondb.net/artwork/kabuto.jpg","Kabutops":"http://img.pokemondb.net/artwork/kabutops.jpg","Aerodactyl":"http://img.pokemondb.net/artwork/aerodactyl.jpg","Snorlax":"http://img.pokemondb.net/artwork/snorlax.jpg","Articuno":"http://img.pokemondb.net/artwork/articuno.jpg","Zapdos":"http://img.pokemondb.net/artwork/zapdos.jpg","Moltres":"http://img.pokemondb.net/artwork/moltres.jpg","Dratini":"http://img.pokemondb.net/artwork/dratini.jpg","Dragonair":"http://img.pokemondb.net/artwork/dragonair.jpg","Dragonite":"http://img.pokemondb.net/artwork/dragonite.jpg","Mewtwo":"http://img.pokemondb.net/artwork/mewtwo.jpg","Mew":"http://img.pokemondb.net/artwork/mew.jpg"}

def oddish(request):
	return render(request, 'search/oddish.html')

def game(request):
	context_dict = {}
	pokemon_arr = Pokedex.objects.all()
	random_number = randint(0, len(pokemon_arr)-1)
	random_pokemon = pokemon_arr[random_number]
	context_dict['pokemon'] = random_pokemon
	return render(request, 'search/game.html', context_dict)

def search_pokemon(search_string, result_type='arr'):
	result_arr = []
	if search_string=='*' and result_type=='dict':
		for key,value in pokemon_data.iteritems():
			result_arr.append(dict(name=key, image_url=value))
		return result_arr

	if search_string=='*' and result_type=='arr':
		for key,value in pokemon_data.iteritems():
			result_arr.append([key,value])
		return result_arr

	for key,value in pokemon_data.iteritems():
		if key.lower().startswith(search_string.lower()):
			if result_type=='arr':
				result_arr.append([key,value])
			elif result_type=='dict':
				data_dict = dict(name=key, image_url=value)
				result_arr.append(data_dict)
	
	return result_arr

def edit(request, pokemon_id):
	if request.method=='POST':
		pokemon_name = request.POST.get('name')
		pokemon_type = request.POST.get('type')
		pokemon_image = request.POST.get('image')
		p = Pokedex.objects.get_or_create(id=pokemon_id)[0]
		p.pokemon_name = pokemon_name
		p.pokemon_type = pokemon_type
		p.pokemon_image = pokemon_image
		p.save()
		return HttpResponse('SAVED %s of type %s and imageurl %s'%(pokemon_name, pokemon_type, pokemon_image))
	else:
		context_dict = {}
		matching_pokemon = 'N/A'
		context_dict['pokemon_id'] = pokemon_id
		context_dict['pokedex'] = Pokedex.objects.all()
		for pokemon in Pokedex.objects.all():
			if pokemon_id == str(pokemon.id):		#id created by sqlite when entering data into database
				matching_pokemon = pokemon

		context_dict['matching_pokemon']=matching_pokemon

		return render(request, 'search/edit.html', context_dict)

def searchget(request):
	search_string = request.GET.get("searchstring") or ''
	context_dict={}
	context_dict['search_string']=search_string
	context_dict['result_arr']=search_pokemon(search_string)

	return render(request, 'search/searchGET.html', context_dict)				#To output a page on browser

def searchpost(request):
	search_string = request.POST.get("searchstring") or ''
	search_string = str(search_string)
	context_dict={}
	context_dict['search_string']=search_string
	context_dict['result_arr']=search_pokemon(search_string)

	return render(request, 'search/searchPOST.html', context_dict)				#To output a page on browser

def searchredirect(request, search_string):
	
	context_dict={}
	context_dict['search_string']=search_string
	context_dict['result_arr']=search_pokemon(search_string, result_type='dict')

	return render(request, 'search/searchREDIRECT.html', context_dict)

def searchlistjs(request):
	
	context_dict={}
	context_dict['result_arr']=search_pokemon('*', result_type='dict')

	return render(request, 'search/searchLISTJS.html', context_dict)

def index(request):
	context_dict = {}
	context_dict['date'] = time.ctime
	n = 10
	try:
		page_id = int(request.GET.get('page') or '1')
	except ValueError:
		page_id = 1
	if page_id > 150/n:
		page_id = 150/n
	context_dict['page'] = page_id
	data_arr = Pokedex.objects.all()
	try:
		context_dict['pokedex'] = data_arr[(page_id-1)*n : (page_id)*n]
	except AssertionError:
		context_dict['pokedex'] = data_arr[:n]
		page_id=1
	context_dict['prev'] = page_id-1
	context_dict['next'] = page_id+1
	#context_dict['iter_arr'] = range(1,150/n+1)
	context_dict['iter_arr'] = range(max(1,page_id-3),min(page_id+4,15))
	return render(request, 'search/index.html', context_dict)				#To output a page on browser

def index2(request, page_id):
	context_dict = {}
	context_dict['date'] = time.ctime
	n = 10
	try:
		#page_id = int(request.GET.get('page') or '1')
		page_id = int(page_id)
	except ValueError:
		page_id = 1
	if page_id > 150/n:
		page_id = 150/n
	context_dict['page'] = page_id
	data_arr = Pokedex.objects.all()
	try:
		context_dict['pokedex'] = data_arr[(page_id-1)*n : (page_id)*n]
	except AssertionError:
		context_dict['pokedex'] = data_arr[:n]
		page_id=1
	context_dict['prev'] = page_id-1
	context_dict['next'] = page_id+1
	#context_dict['iter_arr'] = range(1,150/n+1)
	context_dict['iter_arr'] = range(max(1,page_id-3), min(page_id+4, 16))
	return render(request, 'search/index.html', context_dict)				#To output a page on browser

def search_db(search_string):
	result_arr = []
	for pokemon in Pokedex.objects.all():
		if pokemon.pokemon_name.lower().startswith(search_string.lower()):
			result_arr.append(pokemon)

	return result_arr

def short_url(request, pokemon_id):
	try:
		pokemon = Pokedex.objects.get(id=pokemon_id)
	except:
		return redirect('/pokemon/156/Oddish')
	return redirect('/pokemon/%s/%s'%(pokemon_id, pokemon.pokemon_name))

def description(request, pokemon_id, pokemon_name):
	#pokemon_image = search_pokemon(pokemon_name)[0][1]		#Because this is a nested list- returns array of arrays
	#pokemon_image = search_db(pokemon_name)[0].pokemon_image
	try:
		pokemon = Pokedex.objects.get(id=pokemon_id, pokemon_name = pokemon_name)
	except:
		try:
			pokemon = Pokedex.objects.get(id=pokemon_id)
		except:
			return redirect('/pokemon/156/Oddish')
		return redirect('/pokemon/%s/%s'%(pokemon_id, pokemon.pokemon_name))
	context_dict = {}
	#context_dict['pokemon_id'] = pokemon_id
	#context_dict['pokemon_name'] = pokemon_name
	#context_dict['pokemon_image'] = pokemon_image
	context_dict['pokemon'] = pokemon
	return render(request, 'search/description.html', context_dict)

'''
def random(request):
	list_dir = os.listdir(os.path.join(settings.STATIC_PATH, 'images'))
	shuffle(list_dir)
	context_dict={}
	context_dict['list_dir'] = list_dir

	return render(request, 'search/random.html', context_dict)

def newIndex(request):
	today_date = time.ctime()
	context_dict = {}
	context_dict['date']=today_date
	list_dir = os.listdir(os.path.join(settings.STATIC_PATH, 'images'))
	shuffle(list_dir)
	context_dict['list_dir']=list_dir
	context_dict['pokedex']=Pokedex.objects.all()

	return render(request, 'search/newIndex.html', context_dict) 

def search2(request,foo):
	search_string = foo or 1
	list_dir = os.listdir(os.path.join(settings.STATIC_PATH, 'images'))
	result_arr = []
	for file_name in list_dir:
		if search_string in file_name:
			result_arr.append(file_name)
	context_dict={}
	context_dict['search_string']=search_string
	context_dict['result_arr']=result_arr
	return render(request, 'search/search.html', context_dict)				#To output a page on browser

'''