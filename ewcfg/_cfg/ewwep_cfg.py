
# Weapon related config

# A Weapon Effect Function for "revolver". Takes an EwEffectContainer as ctn.
def wef_revolver(ctn = None):
	ctn.slimes_damage = int(ctn.slimes_damage * 0.8)
	aim = (random.randrange(10) + 1)
	user_mutations = ctn.user_data.get_mutations()
	ctn.sap_damage = 2

	if aim <= (1 + int(10 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.miss = True
		else:
			ctn.miss = True

	elif aim >= (10 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2

# weapon effect function for "dualpistols"
def wef_dualpistols(ctn = None):
	aim = (random.randrange(10) + 1)
	user_mutations = ctn.user_data.get_mutations()
	ctn.sap_damage = 2

	if aim <= (4 + int(10 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.miss = True
		else:
			ctn.miss = True

	elif aim >= (9 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage = int(ctn.slimes_damage * 2)

# weapon effect function for "shotgun"
def wef_shotgun(ctn = None):
	ctn.slimes_damage = int(ctn.slimes_damage * 1.65)
	ctn.slimes_spent = int(ctn.slimes_spent * 1.5)
	ctn.sap_damage = 5

	aim = (random.randrange(10) + 1)
	user_mutations = ctn.user_data.get_mutations()

	if aim <= (1 + int(10 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.miss = True
		else:
			ctn.miss = True

	elif aim >= (10 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2
		ctn.sap_damage *= 2

# weapon effect function for "rifle"
def wef_rifle(ctn = None):
	ctn.slimes_damage = int(ctn.slimes_damage * 1.25)
	ctn.slimes_spent = int(ctn.slimes_spent * 1.25)
	aim = (random.randrange(10) + 1)
	ctn.sap_ignored = 10
	ctn.sap_damage = 2

	if aim >= (9 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2
		ctn.sap_damage += 2
		ctn.sap_ignored += 10

# weapon effect function for "smg"
def wef_smg(ctn = None):
	dmg = int(ctn.slimes_damage * 0.4)
	ctn.slimes_damage = 0
	jam = (random.randrange(10) + 1)
	user_mutations = ctn.user_data.get_mutations()

	if jam <= 2:
		ctn.weapon_item.item_props["jammed"] = "True"
		ctn.jammed = True
	else:
		for count in range(6):
			aim = (random.randrange(100) + 1)
			if aim > (25 + int(100 * ctn.miss_mod)):
				ctn.strikes += 1

				if aim >= (95 - int(100 * ctn.crit_mod)):
					ctn.slimes_damage += int(dmg * 1.5)
				else:
					ctn.slimes_damage += int(dmg * 0.5)
			elif mutation_id_sharptoother in user_mutations:
				if random.random() < 0.5:
					ctn.strikes += 1

					if aim >= (95 - int(100 * ctn.crit_mod)):
						ctn.slimes_damage += int(dmg * 1.5)
					else:
						ctn.slimes_damage += int(dmg * 0.5)

		if ctn.strikes == 0:
			ctn.miss = True

	ctn.sap_damage = ctn.strikes

# weapon effect function for "minigun"
def wef_minigun(ctn = None):
	dmg = 0.8 * ctn.slimes_damage
	ctn.slimes_damage = 0
	user_mutations = ctn.user_data.get_mutations()

	for count in range(10):
		aim = (random.randrange(10) + 1)

		if aim > (5 + int(10 * ctn.miss_mod)):
			ctn.strikes += 1

			if aim >= (10 - int(10 * ctn.crit_mod)):
				ctn.slimes_damage += dmg * 2
			else:
				ctn.slimes_damage += dmg
		elif mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.strikes += 1

				if aim >= 10 - int(10 * ctn.crit_mod):
					ctn.slimes_damage += dmg * 2
				else:
					ctn.slimes_damage += dmg

	if ctn.strikes == 0:
		ctn.miss = True

	ctn.sap_damage = 2 * ctn.strikes

# weapon effect function for "bat"
def wef_bat(ctn = None):
	aim = (random.randrange(0, 13) - 2)
	user_mutations = ctn.user_data.get_mutations()
	dmg = ctn.slimes_damage
	ctn.sap_damage = 2

	# Increased miss chance if attacking within less than two seconds after last attack
	time_lastattack = ctn.time_now - (float(ctn.weapon_item.item_props.get("time_lastattack")) if ctn.weapon_item.item_props.get("time_lastattack") != None else ctn.time_now)
	ctn.miss_mod += (((3 - min(time_lastattack, 3)) / 3) ** 2) / 13 * 10

	ctn.slimes_damage = int(ctn.slimes_damage * ((aim/5) + 0.5) )

	if aim <= (-2 + int(13 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.backfire = True
				ctn.backfire_damage = ctn.slimes_damage
		else:
			ctn.backfire = True
			ctn.backfire_damage = ctn.slimes_damage

	elif aim <= (-1 + int(13 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.miss = True
		else:
			ctn.miss = True

	elif aim >= (10 - int(13 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage = int(dmg * 4)

# weapon effect function for "brassknuckles"
def wef_brassknuckles(ctn = None):
	last_attack = (float(ctn.weapon_item.item_props.get("time_lastattack")) if ctn.weapon_item.item_props.get("time_lastattack") != None else 0)
	successful_timing = 2.1 > (ctn.time_now - last_attack) > 1.9
	user_mutations = ctn.user_data.get_mutations()
	ctn.strikes = 0

	damage_min = ctn.slimes_damage / 10

	if last_attack > 0:
		ctn.slimes_damage = damage_min * ((min(last_attack, 2) / 2)**0.5  * 10)
	else:
		ctn.slimes_damage = damage_min

	ctn.slimes_damage = int(max(ctn.slimes_damage, damage_min))

	consecutive_hits = (int(ctn.weapon_item.item_props.get("consecutive_hits")) if ctn.weapon_item.item_props.get("consecutive_hits") != None else 0)
	if consecutive_hits == 2 and successful_timing:
		ctn.crit = True
		ctn.sap_damage = 5
		ctn.slimes_damage *= 3
		ctn.weapon_item.item_props["consecutive_hits"] = 0

	else:
		aim1 = (random.randrange(10) + 1)
		aim2 = (random.randrange(10) + 1)
		whiff1 = 1
		whiff2 = 1

		if aim1 <= (2 + int(10 * ctn.miss_mod)):
			if mutation_id_sharptoother in user_mutations:
				if random.random() < 0.5:
					whiff1 = 0
			else:
				whiff1 = 0
		if aim2 <= (2 + int(10 * ctn.miss_mod)):
			if mutation_id_sharptoother in user_mutations:
				if random.random() < 0.5:
					whiff2 = 0
			else:
				whiff2 = 0

		if whiff1 == 0 and whiff2 == 0:
			ctn.miss = True
		else:
			ctn.strikes = whiff1 + whiff2
			ctn.slimes_damage = (ctn.slimes_damage * whiff1) + (ctn.slimes_damage * whiff2)
			if successful_timing:
				ctn.weapon_item.item_props["consecutive_hits"] = consecutive_hits + 1
			else:
				ctn.weapon_item.item_props["consecutive_hits"] = 0



# weapon effect function for "katana"
def wef_katana(ctn = None):
	ctn.slimes_damage = int(ctn.slimes_damage * 1.3)
	ctn.slimes_spent = int(ctn.slimes_spent * 1.3)
	ctn.sap_damage = 0

	# Decreased damage if attacking within less than four seconds after last attack
	time_lastattack = ctn.time_now - (float(ctn.weapon_item.item_props.get("time_lastattack")) if ctn.weapon_item.item_props.get("time_lastattack") != None else ctn.time_now)

	damage_min = ctn.slimes_damage / 10


	if time_lastattack > 0:
		ctn.slimes_damage = damage_min * ((min(time_lastattack, 5) / 5)**0.5  * 10)
	else:
		ctn.slimes_damage = damage_min

	ctn.slimes_damage = int(max(ctn.slimes_damage, damage_min))

	if 5.2 > time_lastattack > 4.8:
		ctn.sap_ignored = 10


	weapons_held = ewitem.inventory(
		id_user = ctn.user_data.id_user,
		id_server = ctn.user_data.id_server,
		item_type_filter = it_weapon
	)

	#lucky lucy's lucky katana always crits
	if ctn.user_data.life_state == life_state_lucky:
		ctn.crit = True
		ctn.slimes_damage *= 7.77

	elif len(weapons_held) == 1:
		ctn.crit = True
		ctn.slimes_damage *= 2
		ctn.sap_ignored *= 1.5

# weapon effect function for "broadsword"
def wef_broadsword(ctn = None):
	ctn.slimes_spent = int(ctn.slimes_spent * 5)
	dmg = ctn.slimes_damage
	ctn.slimes_damage *= 3
	aim = (random.randrange(10) + 1)
	user_mutations = ctn.user_data.get_mutations()
	ctn.sap_damage = 5
	ctn.sap_ignored = 20

	ctn.slimes_damage += int( dmg * (min(10, int(ctn.weapon_item.item_props.get("kills"))) / 2) )

	if aim <= (2 + int(10 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.backfire = True
				ctn.backfire_damage = ctn.slimes_damage
		else:
			ctn.backfire = True
			ctn.backfire_damage = ctn.slimes_damage

	elif aim <= (3 + int(10 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.miss = True
		else:
			ctn.miss = True

	elif aim >= (9 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.sap_damage *= 2
		ctn.slimes_damage *= 2

# weapon effect function for "nun-chucks"
def wef_nunchucks(ctn = None):
	ctn.strikes = 0
	dmg = ctn.slimes_damage
	ctn.slimes_damage = 0
	user_mutations = ctn.user_data.get_mutations()

	time_lastattack = ctn.time_now - (float(ctn.weapon_item.item_props.get("time_lastattack")) if ctn.weapon_item.item_props.get("time_lastattack") != None else ctn.time_now)
	ctn.miss_mod += (((3 - min(time_lastattack, 3)) / 3) ** 2) / 100 * 55

	for count in range(4):
		if (random.randrange(100) + 1) > (25 + int(100 * ctn.miss_mod)):
			ctn.strikes += 1
			ctn.slimes_damage += int(dmg * 0.25)
		elif mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.strikes += 1
				ctn.slimes_damage += int(dmg * 0.25)

	if ctn.strikes == 4:
		ctn.crit = True
		# extra hit that deals 2* base damage
		ctn.strikes = 5
		ctn.slimes_damage += dmg * 2

	elif ctn.strikes == 0:
		ctn.backfire = True
		ctn.backfire_damage = dmg * 2

	ctn.sap_damage = ctn.strikes

# weapon effect function for "scythe"
def wef_scythe(ctn = None):
	ctn.slimes_spent = int(ctn.slimes_spent * 3)
	ctn.slimes_damage = int(ctn.slimes_damage * 0.5)
	user_mutations = ctn.user_data.get_mutations()
	ctn.sap_damage = 0

	try:
		target_kills = ewstats.get_stat(user = ctn.shootee_data, metric = stat_kills)
	except:
		target_kills = 4

	ctn.slimes_damage = ctn.slimes_damage * max(1, min(target_kills, 10))
	ctn.sap_ignored = 3 * min(target_kills, 10)

	# Decreased damage if attacking within less than three seconds after last attack
	time_lastattack = ctn.time_now - (float(ctn.weapon_item.item_props.get("time_lastattack")) if ctn.weapon_item.item_props.get("time_lastattack") != None else ctn.time_now)
	damage_min = ctn.slimes_damage / 10
	if time_lastattack > 0:
		ctn.slimes_damage = damage_min * ((min(time_lastattack, 3)/3)**0.5 * 10)
	else:
		ctn.slimes_damage = damage_min

	ctn.slimes_damage = int(max(ctn.slimes_damage, damage_min))

	aim = (random.randrange(10) + 1)

	if aim <= (1 + int(10 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.miss = True
		else:
			ctn.miss = True

	elif aim >= (10 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2

# weapon effect function for "yo-yos"
def wef_yoyo(ctn = None):
	base_dmg = ctn.slimes_damage
	ctn.slimes_damage = ctn.slimes_damage * 0.5
	user_mutations = ctn.user_data.get_mutations()

	time_lastattack = ctn.time_now - (float(ctn.weapon_item.item_props.get("time_lastattack")) if ctn.weapon_item.item_props.get("time_lastattack") != None else ctn.time_now)

	#Consecutive hits only valid for a minute
	if time_lastattack < 60:
		ctn.slimes_damage += (base_dmg * (int(ctn.weapon_item.item_props.get("consecutive_hits")) * 0.25))
	else:
		ctn.weapon_item.item_props["consecutive_hits"] = 0

	damage_min = ctn.slimes_damage / 10

	if time_lastattack > 0:
		ctn.slimes_damage = damage_min * ((min(time_lastattack, 2)/2) ** 0.5 * 10)
	else:
		ctn.slimes_damage = damage_min

	ctn.slimes_damage = int(max(ctn.slimes_damage, damage_min))

	if time_lastattack >= 2:
		ctn.sap_damage = 1

	ctn.weapon_item.item_props["consecutive_hits"] = int(ctn.weapon_item.item_props["consecutive_hits"]) + 1
	aim = (random.uniform(0, 100))

	if aim <= (18.75 + (100 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.miss = True
		else:
			ctn.miss = True

	elif aim >= (90 - (100 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2


# weapon effect function for "knives"
def wef_knives(ctn = None):
	ctn.slimes_spent = int(ctn.slimes_spent * 0.25)
	ctn.slimes_damage = int(ctn.slimes_damage * 0.5)
	user_mutations = ctn.user_data.get_mutations()
	ctn.sap_damage = 0

	aim = (random.randrange(10) + 1)

	if aim <= (1 + int(10 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.miss = True
		else:
			ctn.miss = True

	elif aim >= (10 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage = int(ctn.slimes_damage * 2)

# weapon effect function for "molotov"
def wef_molotov(ctn = None):
	dmg = ctn.slimes_damage
	ctn.slimes_damage = int(ctn.slimes_damage * 0.75)
	ctn.slimes_spent *= 1
	user_mutations = ctn.user_data.get_mutations()
	ctn.sap_damage = 0
	ctn.sap_ignored = 10

	aim = (random.randrange(10) + 1)

	ctn.bystander_damage = dmg * 0.5

	if aim <= (2 + int(10 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.backfire = True
				ctn.backfire_damage = dmg
		else:
			ctn.backfire = True
			ctn.backfire_damage = dmg

	elif aim > 2 and aim <= (3 + int(10 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.miss = True
		else:
			ctn.miss = True

	else:
		if aim >= (10 - int(10 * ctn.crit_mod)):
			ctn.crit = True
			ctn.slimes_damage *= 2

# weapon effect function for "grenade"
def wef_grenade(ctn = None):
	dmg = ctn.slimes_damage
	ctn.slimes_damage = int(ctn.slimes_damage * 0.75)
	ctn.slimes_spent *= 1
	ctn.bystander_damage = int(dmg * 0.3)
	user_mutations = ctn.user_data.get_mutations()
	ctn.sap_damage = 5

	aim = (random.randrange(10) + 1)

	if aim <= (1 + int(10 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.miss = True
				ctn.bystander_damage = 0
		else:
			ctn.miss = True
			ctn.bystander_damage = 0

	elif aim > 1 and aim <= (2 + int(10 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.backfire = True
				ctn.backfire_damage = ctn.slimes_damage
		else:
			ctn.backfire = True
			ctn.backfire_damage = ctn.slimes_damage

	elif aim >= (10 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage = dmg * 4

# weapon effect function for "garrote"
def wef_garrote(ctn = None):
	ctn.slimes_damage *= 15
	ctn.sap_damage = 0
	ctn.sap_ignored = ctn.shootee_data.hardened_sap

	user_mutations = ctn.user_data.get_mutations()
	aim = (random.randrange(100) + 1)
	if aim <= int(100 * ctn.miss_mod):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.miss = True
		else:
			ctn.miss = True

	elif aim <= (1 - int(100 * ctn.crit_mod)):
		ctn.slimes_damage *= 10
		ctn.crit = True

	if ctn.miss == False:
		#Stop movement
		ewutils.moves_active[ctn.user_data.id_user] = 0
		#Stun player for 5 seconds
		ctn.user_data.applyStatus(id_status=status_stunned_id, value=(int(ctn.time_now) + 5))
		#Start strangling target
		ctn.shootee_data.applyStatus(id_status=status_strangled_id, source=ctn.user_data.id_user)

# weapon effect function for all weapons which double as tools.
def wef_tool(ctn = None):
	ctn.slimes_damage *= 0.2
	ctn.sap_damage = 0

	aim = (random.randrange(10) + 1)
	user_mutations = ctn.user_data.get_mutations()

	if aim == 1:
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.miss = True
				ctn.slimes_damage = 0
		else:
			ctn.miss = True
			ctn.slimes_damage = 0

	elif aim == 10:
		ctn.crit = True
		ctn.slimes_damage *= 2

# weapon effect function for "bass"
def wef_bass(ctn = None):
	aim = (random.randrange(0, 13) - 2)
	user_mutations = ctn.user_data.get_mutations()
	dmg = ctn.slimes_damage
	ctn.sap_damage = 1
	ctn.sap_ignored = 5

	# Increased miss chance if attacking within less than two seconds after last attack
	time_lastattack = ctn.time_now - (float(ctn.weapon_item.item_props.get("time_lastattack")) if ctn.weapon_item.item_props.get("time_lastattack") != None else ctn.time_now)
	ctn.miss_mod += (((3 - min(time_lastattack, 3)) / 3) ** 2) / 13 * 10

	ctn.slimes_damage = int(ctn.slimes_damage * ((aim/5) + 0.5) )

	if aim <= (-2 + int(13 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.miss = True
		else:
			ctn.miss = True

	elif aim >= (9 - int(13 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage = int(dmg * 4)

# A Weapon Effect Function for "umbrella". Takes an EwEffectContainer as ctn.
def wef_umbrella(ctn = None):
	ctn.slimes_damage = int(ctn.slimes_damage * 0.5)
	aim = (random.randrange(10) + 1)
	user_mutations = ctn.user_data.get_mutations()
	ctn.sap_damage = 1

	if aim <= (1 + int(10 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.miss = True
		else:
			ctn.miss = True

	elif aim >= (10 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2
# weapon effect function for "minecraft bow"
def wef_bow(ctn = None):
	aim = (random.randrange(0, 13) - 2)
	user_mutations = ctn.user_data.get_mutations()
	dmg = ctn.slimes_damage
	ctn.sap_damage = 1
	ctn.sap_ignored = 8

	time_lastattack = ctn.time_now - (float(ctn.weapon_item.item_props.get("time_lastattack")) if ctn.weapon_item.item_props.get("time_lastattack") != None else ctn.time_now)
	ctn.miss_mod += (((10 - min(time_lastattack, 10)) / 10) ** 2) / 13 * 10

	ctn.slimes_damage = int(ctn.slimes_damage * 3)

	if aim <= (-2 + int(13 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.miss = True
		else:
			ctn.miss = True

	elif aim >= (9 - int(16 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage = int(dmg * 6)

# weapon effect function for "Dragon Claw"

def wef_dclaw(ctn = None):
	aim = (random.randrange(0, 13) - 2)
	user_mutations = ctn.user_data.get_mutations()
	dmg = ctn.slimes_damage
	if mutation_id_fastmetabolism in user_mutations or mutation_id_lightasafeather in user_mutations:
		ctn.slimes_damage = int(ctn.slimes_damage * 1.2)
		ctn.slimes_spent *= 0.5
	else:
		ctn.slimes_damage = int(ctn.slimes_damage * 1.5)
		ctn.slimes_spent *= 1

	ctn.bystander_damage = int(dmg * 0.5)

	#less slime cost and less damage = attacking faster I guess?
	ctn.sap_damage = 5
	ctn.sap_ignored = 10
	time_lastattack = ctn.time_now - (float(ctn.weapon_item.item_props.get("time_lastattack")) if ctn.weapon_item.item_props.get("time_lastattack") != None else ctn.time_now)
	ctn.miss_mod += (((5 - min(time_lastattack, 5)) / 5) ** 2) / 13 * 5
	if aim <= (-2 + int(13 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.3:
				ctn.miss = True
		else:
			ctn.miss = True
	elif aim >= (9 - int(13 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage = int(dmg * 4)
