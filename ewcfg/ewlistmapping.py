import random

import ewutils
import ewstats
import ewitem
import random
from ewcosmeticitem import EwCosmeticItem
from ewsmelting import EwSmeltingRecipe
from ewwep import EwWeapon
from ewhunting import EwAttackType
from ewweather import EwWeather
from ewfood import EwFood
from ewitem import EwItemDef, EwGeneralItem
from ewmap import EwPoi
from ewmutation import EwMutationFlavor
from ewslimeoid import EwBody, EwHead, EwMobility, EwOffense, EwDefense, EwSpecial, EwBrain, EwHue, EwSlimeoidFood
from ewquadrants import EwQuadrantFlavor
from ewtransport import EwTransportLine
from ewstatuseffects import EwStatusEffectDef
from ewfarm import EwFarmAction
from ewfish import EwFish
from ewapt import EwFurniture

from ewworldevent import EwEventDef
from ewdungeons import EwDungeonScene
from ewtrauma import EwTrauma, EwHitzone

# seperate the dyes from the other normal items
for c in item_list:
	if c.context != "dye":
		pass
	else:
		dye_list.append(c)
		dye_map[c.str_name] = c.id_item


# Populate attack type map.
for attack_type in enemy_attack_type_list:
	attack_type_map[attack_type.id_type] = attack_type


# A map of name to EwWeather objects.
weather_map = {}
for weather in weather_list:
	weather_map[weather.name] = weather

# seperate the crops from the normal foods
for v in food_list:
	if v.vendors != [vendor_farm]:
		pass
	else:
		vegetable_list.append(v)

for poi in poi_list:
	if poi.coord != None:
		# Populate the map of coordinates to their point of interest, for looking up from the map.
		coord_to_poi[poi.coord] = poi

		# Populate the map of coordinate aliases to the main coordinate.
		for coord_alias in poi.coord_alias:
			alias_to_coord[coord_alias] = poi.coord
			coord_to_poi[coord_alias] = poi

	# Populate the map of point of interest names/aliases to the POI.
	id_to_poi[poi.id_poi] = poi
	for alias in poi.alias:
		id_to_poi[alias] = poi

	# if it's a district and not RR, CK, or JR, add it to a list of capturable districts
	if poi.is_capturable:
		capturable_districts.append(poi.id_poi)

	if poi.is_transport:
		transports.append(poi.id_poi)

	if poi.is_transport_stop:
		transport_stops.append(poi.id_poi)
		transport_stops_ch.append(poi.channel)

	if poi.is_pier:
		piers.append(poi.id_poi)

	if poi.is_outskirts:
		outskirts.append(poi.id_poi)

	if poi.is_tutorial:
		tutorial_pois.append(poi.id_poi)

	if poi.write_manuscript:
		zine_mother_districts.append(id_to_poi.get(poi.mother_district))

	chname_to_poi[poi.channel] = poi


for line in transport_lines:
	id_to_transport_line[line.id_line] = line
	for alias in line.alias:
		id_to_transport_line[alias] = line

	for poi in transport_stops:
		poi_data = id_to_poi.get(poi)
		if (poi in line.schedule.keys()) or (poi == line.last_stop):
			poi_data.transport_lines.add(line.id_line)

# Populate recipe map, including all aliases.
for recipe in smelting_recipe_list:
	smelting_recipe_map[recipe.id_recipe] = recipe
	recipe_names.append(recipe.id_recipe)

	for alias in recipe.alias:
		smelting_recipe_map[alias] = recipe

# Populate body map, including all aliases.
for body in body_list:
	body_map[body.id_body] = body
	body_names.append(body.id_body)

	for alias in body.alias:
		body_map[alias] = body


# Populate mobility map, including all aliases.
for mobility in mobility_list:
	mobility_map[mobility.id_mobility] = mobility
	mobility_names.append(mobility.id_mobility)

	for alias in mobility.alias:
		mobility_map[alias] = mobility


# Populate offense map, including all aliases.
for offense in offense_list:
	offense_map[offense.id_offense] = offense
	offense_names.append(offense.id_offense)

	for alias in offense.alias:
		offense_map[alias] = offense

# Populate defense map, including all aliases.
for defense in defense_list:
	defense_map[defense.id_defense] = defense
	defense_names.append(defense.id_defense)

	for alias in defense.alias:
		defense_map[alias] = defense

# Populate special map, including all aliases.
for special in special_list:
	special_map[special.id_special] = special
	special_names.append(special.id_special)

	for alias in special.alias:
		special_map[alias] = special

# Populate brain map, including all aliases.
for brain in brain_list:
	brain_map[brain.id_brain] = brain
	brain_names.append(brain.id_brain)

	for alias in brain.alias:
		brain_map[alias] = brain

# Populate hue map, including all aliases.
for hue in hue_list:
	hue_map[hue.id_hue] = hue
	hue_names.append(hue.id_hue)

	for alias in hue.alias:
		hue_map[alias] = hue# A map of id_hue to EwHue objects.



for mutation in mutations:
	mutations_map[mutation.id_mutation] = mutation
	mutation_ids.add(mutation.id_mutation)


for quadrant in quadrants:
	quadrants_map[quadrant.id_quadrant] = quadrant
	for alias in quadrant.aliases:
		quadrants_map[alias] = quadrant





# Populate item map, including all aliases.
for item in item_list:
	item_map[item.id_item] = item
	item_names.append(item.id_item)

	# Add item to its vendors' lists.
	for vendor in item.vendors:
		vendor_list = vendor_inv.get(vendor)

		if vendor_list == None:
			vendor_list = []
			vendor_inv[vendor] = vendor_list

		vendor_list.append(item.id_item)

	for alias in item.alias:
		item_map[alias] = item

# Populate food map, including all aliases.
for food in food_list:
	food_map[food.id_food] = food
	food_names.append(food.id_food)

	# Add food to its vendors' lists.
	for vendor in food.vendors:
		vendor_list = vendor_inv.get(vendor)

		if vendor_list == None:
			vendor_list = []
			vendor_inv[vendor] = vendor_list

		vendor_list.append(food.id_food)

	for alias in food.alias:
		food_map[alias] = food

# Populate fish map, including all aliases.
for fish in fish_list:
	fish_map[fish.id_fish] = fish
	fish_names.append(fish.id_fish)

	# Add fish to its vendors' lists.
	for vendor in fish.vendors:
		vendor_list = vendor_inv.get(vendor)

		if vendor_list == None:
			vendor_list = []
			vendor_inv[vendor] = vendor_list

		vendor_list.append(fish.id_fish)

	for alias in fish.alias:
		fish_map[alias] = fish

# Populate cosmetic map.
for cosmetic in cosmetic_items_list:
	cosmetic_map[cosmetic.id_cosmetic] = cosmetic
	cosmetic_names.append(cosmetic.id_cosmetic)

	# Add food to its vendors' lists.
	for vendor in cosmetic.vendors:
		vendor_list = vendor_inv.get(vendor)

		if vendor_list == None:
			vendor_list = []
			vendor_inv[vendor] = vendor_list

		vendor_list.append(cosmetic.id_cosmetic)


for furniture in furniture_list:
	furniture_map[furniture.id_furniture] = furniture
	furniture_names.append(furniture.id_furniture)
	if furniture.furn_set == "haunted":
		furniture_haunted.append(furniture.id_furniture)
	elif furniture.furn_set == "high class":
		furniture_highclass.append(furniture.id_furniture)
	elif furniture.furn_set == "lgbt":
		furniture_lgbt.append(furniture.id_furniture)
	elif furniture.furn_set == "leather":
		furniture_leather.append(furniture.id_furniture)
	elif furniture.furn_set == "church":
		furniture_church.append(furniture.id_furniture)
	elif furniture.furn_set == "pony":
		furniture_pony.append(furniture.id_furniture)
	elif furniture.furn_set == "blackvelvet":
		furniture_blackvelvet.append(furniture.id_furniture)
	elif furniture.furn_set == "seventies":
		furniture_seventies.append(furniture.id_furniture)
	elif furniture.furn_set == "slimecorp":
		furniture_slimecorp.append(furniture.id_furniture)
	elif furniture.furn_set == "shitty":
		furniture_shitty.append(furniture.id_furniture)
	elif furniture.furn_set == "instrument":
		furniture_instrument.append(furniture.id_furniture)
	elif furniture.furn_set == "specialhue":
		furniture_specialhue.append(furniture.id_furniture)


	for vendor in furniture.vendors:
		vendor_list = vendor_inv.get(vendor)
		if vendor_list == None:
			vendor_list = []
			vendor_inv[vendor] = vendor_list
		vendor_list.append(furniture.id_furniture)


# Populate weapon map, including all aliases.
for weapon in weapon_list:
	weapon_map[weapon.id_weapon] = weapon
	weapon_names.append(weapon.id_weapon)

	for vendor in weapon.vendors:
		vendor_list = vendor_inv.get(vendor)

		if vendor_list == None:
			vendor_list = []
			vendor_inv[vendor] = vendor_list

		vendor_list.append(weapon.id_weapon)

	for alias in weapon.alias:
		weapon_map[alias] = weapon


# Gather all items that can be the result of milling.
for m in item_list:
	if m.acquisition == acquisition_milling:
		mill_results.append(m)
	else:
		pass

for m in food_list:
	if m.acquisition == acquisition_milling:
		mill_results.append(m)
	else:
		pass

for m in cosmetic_items_list:
	if m.acquisition == acquisition_milling:
		mill_results.append(m)
	else:
		pass

# List of items you can obtain via appraisal.
appraise_results = []

# Gather all items that can be the result of bartering.
for a in item_list:
	if a.acquisition == acquisition_bartering:
		appraise_results.append(a)
	else:
		pass

for a in food_list:
	if a.acquisition == acquisition_bartering:
		appraise_results.append(a)
	else:
		pass

for a in cosmetic_items_list:
	if a.acquisition == acquisition_bartering:
		appraise_results.append(a)
	else:
		pass

# List of items you can obtain via smelting.
smelt_results = []

# Gather all items that can be the result of smelting.
for s in item_list:
	if s.acquisition == acquisition_smelting:
		smelt_results.append(s)
	# So poudrins can be smelted with 2 royalty poudrins (this is obviously half-assed but i can't think of a better solution)
	elif s.id_item == item_id_slimepoudrin:
		smelt_results.append(s)
	else:
		pass

for s in food_list:
	if s.acquisition == acquisition_smelting:
		smelt_results.append(s)
	else:
		pass

for s in cosmetic_items_list:
	if s.acquisition == acquisition_smelting:
		smelt_results.append(s)
	else:
		pass

for s in weapon_list:
	if s.acquisition == acquisition_smelting:
		smelt_results.append(s)
	else:
		pass

for s in furniture_list:
	if s.acquisition == acquisition_smelting:
		smelt_results.append(s)
	else:
		pass


# Gather all items that can be the result of mining.
for m in item_list:
	if m.acquisition == acquisition_mining:
		mine_results.append(m)
	else:
		pass

for m in food_list:
	if m.acquisition == acquisition_mining:
		mine_results.append(m)
	else:
		pass

for m in cosmetic_items_list:
	if m.acquisition == acquisition_mining:
		mine_results.append(m)
	else:
		pass

# Gather all the items that can be the result of trick-or-treating.
trickortreat_results = []

for t in food_list:
	if t.acquisition == acquisition_trickortreating:
		trickortreat_results.append(t)
	else:
		pass

slimexodia_parts = []

# Gather all parts of slimexodia.
for slimexodia in item_list:
	if slimexodia.context == 'slimexodia':
		slimexodia_parts.append(slimexodia)
	else:
		pass



for status in status_effect_list:
	status_effects_def_map[status.id_status] = status

stackable_status_effects = [
	status_burning_id,
	status_repelled_id,
	status_repelaftereffects_id,
]



for hz in hitzones:
	hitzone_list.append(hz.name)
	hitzone_map[hz.name] = hz

	for alias in hz.aliases:
		hitzone_list.append(alias)
		hitzone_map[alias] = hz

	hitzone_map[hz.id_injury] = hz


for trauma in trauma_list:
	trauma_map[trauma.id_trauma] = trauma

# Shitty bait that always yields Plebefish while fishing.
plebe_bait = []

# Gather all shitty bait.
for bait in food_list:
	if bait.price == None or bait.price <= 1000:
		plebe_bait.append(bait.id_food)
	else:
		pass

# List of outskirt districts for spawning purposes
outskirts_districts = [
	poi_id_south_outskirts,
	poi_id_southwest_outskirts,
	poi_id_west_outskirts,
	poi_id_northwest_outskirts,
	poi_id_north_outskirts,
	poi_id_nuclear_beach
]


