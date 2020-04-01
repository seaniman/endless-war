
# Hunting and Enemy related config

# combatant ids to differentiate players and NPCs in combat
combatant_type_enemy = "enemy"

# Enemy life states
enemy_lifestate_dead = 0
enemy_lifestate_alive = 1
enemy_lifestate_unactivated = 2

# Enemy attacking types (aka 'weapons')
enemy_attacktype_unarmed = 'unarmed'
enemy_attacktype_fangs = 'fangs'
enemy_attacktype_talons = 'talons'
enemy_attacktype_tusks = 'tusks'
enemy_attacktype_raiderscythe = 'scythe'
enemy_attacktype_gunkshot = 'gunk shot'
enemy_attacktype_molotovbreath = 'molotov breath'
enemy_attacktype_armcannon = 'arm cannon'
enemy_attacktype_axe = 'axe'
enemy_attacktype_hooves = 'hooves'

# Enemy weather types. In the future enemies will make use of this in tandem with the current weather, but for now they can just resist the rain.
enemy_weathertype_normal = 'normal'
enemy_weathertype_rainresist = 'rainresist'

# Enemy types
# Common enemies
enemy_type_juvie = 'juvie'
enemy_type_dinoslime = 'dinoslime'
# Uncommon enemies
enemy_type_slimeadactyl = 'slimeadactyl'
enemy_type_desertraider = 'desertraider'
enemy_type_mammoslime = 'mammoslime'
# Rare enemies
enemy_type_microslime = 'microslime'
enemy_type_slimeofgreed = 'slimeofgreed'
# Raid bosses
enemy_type_megaslime = 'megaslime'
enemy_type_slimeasaurusrex = 'slimeasaurusrex'
enemy_type_greeneyesslimedragon = 'greeneyesslimedragon'
enemy_type_unnervingfightingoperator = 'unnervingfightingoperator'

# Sandbag (Only spawns in the dojo, doesn't attack)
enemy_type_sandbag = 'sandbag'

# Double Halloween bosses. Could be brought back as enemies later on, for now will only spawn in the underworld.
enemy_type_doubleheadlessdoublehorseman = 'doubleheadlessdoublehorseman'
enemy_type_doublehorse = 'doublehorse'

# Enemy ai types
enemy_ai_sandbag = 'Sandbag'
enemy_ai_coward = 'Coward'
enemy_ai_attacker_a = 'Attacker-A'
enemy_ai_attacker_b = 'Attacker-B'
enemy_ai_defender = 'Defender'

# List of enemies sorted by their spawn rarity.
common_enemies = [enemy_type_sandbag, enemy_type_juvie, enemy_type_dinoslime]
uncommon_enemies = [enemy_type_slimeadactyl, enemy_type_desertraider, enemy_type_mammoslime]
rare_enemies = [enemy_type_microslime, enemy_type_slimeofgreed]
raid_bosses = [enemy_type_megaslime, enemy_type_slimeasaurusrex, enemy_type_greeneyesslimedragon, enemy_type_unnervingfightingoperator]

# List of enemies that spawn in the Nuclear Beach
pre_historic_enemies = [enemy_type_slimeasaurusrex, enemy_type_dinoslime, enemy_type_slimeadactyl, enemy_type_mammoslime]

# List of raid bosses sorted by their spawn rarity.
raid_boss_tiers = {
	"Micro": [enemy_type_megaslime],
	"Monstrous": [enemy_type_slimeasaurusrex, enemy_type_unnervingfightingoperator],
	"Mega": [enemy_type_greeneyesslimedragon],
	# This can be left empty until we get more raid boss ideas.
	#"Nega": [],
}

# List of enemies that are simply too powerful to have their rare variants spawn
overkill_enemies = [enemy_type_doubleheadlessdoublehorseman, enemy_type_doublehorse]

# List of enemies that have other enemies spawn with them
enemy_group_leaders = [enemy_type_doubleheadlessdoublehorseman]

# Dict of enemy spawn groups. The leader is the key, which correspond to which enemies to spawn, and how many.
enemy_spawn_groups = {
	enemy_type_doubleheadlessdoublehorseman: [[enemy_type_doublehorse, 1]]
}

# Enemy drop tables. Values are sorted by the chance to the drop an item, and then the minimum and maximum amount of times to drop that item.
enemy_drop_tables = {
	enemy_type_sandbag: [{"poudrin": [100, 1, 1]}],
	enemy_type_juvie: [{"poudrin": [50, 1, 2]}, {"pleb": [10, 1, 1]}, {"crop": [30, 1, 1]}, {"card": [20, 1, 1]}],
	enemy_type_dinoslime: [{"poudrin": [100, 2, 4]}, {"pleb": [40, 1, 2]},  {"meat": [33, 1, 2]}, {"monsterbones": [100, 3, 5]}],
	enemy_type_slimeadactyl: [{"poudrin": [100, 3, 5]}, {"pleb": [40, 1, 2]}, {"monsterbones": [100, 3, 5]}],
	enemy_type_microslime: [{"patrician": [100, 1, 1]}],
	enemy_type_slimeofgreed: [{"poudrin": [100, 2, 2]}],
	enemy_type_desertraider: [{"poudrin": [100, 1, 2]}, {"pleb": [100, 1, 1]},  {"crop": [50, 3, 6]}, {"monsterbones": [100, 3, 5]}],
	enemy_type_mammoslime: [{"poudrin": [75, 5, 6]},  {"patrician": [60, 1, 2]}, {"monsterbones": [100, 1, 3]}],
	enemy_type_doubleheadlessdoublehorseman: [{"poudrin": [100, 22, 22]}, {"pleb": [100, 22, 22]}, {"patrician": [100, 22, 22]}, {"crop": [100, 22, 22]}, {"meat": [100, 22, 22]}, {"card": [100, 22, 22]}],
	enemy_type_doublehorse: [{"poudrin": [100, 22, 22]}],
	enemy_type_megaslime: [{"poudrin": [100, 4, 8]}, {"pleb": [100, 1, 3]}, {"patrician": [33, 1, 1]}],
	enemy_type_slimeasaurusrex: [{"poudrin": [100, 8, 15]}, {"pleb": [75, 3, 3]}, {"patrician": [50, 1, 2]},  {"meat": [100, 3, 4]}, {"monsterbones": [100, 3, 5]}],
	enemy_type_greeneyesslimedragon: [{"dragonsoul": [100, 1, 1]},{"poudrin": [100, 15, 20]}, {"patrician": [100, 2, 4]}, {"monsterbones": [100, 5, 10]}],
	enemy_type_unnervingfightingoperator: [{"poudrin": [100, 1, 1]}, {"crop": [100, 1, 1]}, {"meat": [100, 1, 1]}, {"card": [100, 1, 1]}]
}

# Template. Use this when making a new enemy, as they need all these values filled out.
# {"slimerange": , "ai": , "attacktype": , "displayname": , "raredisplayname": , "aliases": },

# Enemy data tables. Slime is stored as a range from min to max possible slime upon spawning.
enemy_data_table = {
	enemy_type_sandbag: {"slimerange": [1000000000, 1000000000], "ai": enemy_ai_sandbag, "attacktype": enemy_attacktype_unarmed, "displayname": "Sand Bag", "raredisplayname": "Durable Sand Bag", "aliases": ["sandbag", "bag o sand", "bag of sand"]},
	enemy_type_juvie: {"slimerange": [10000, 50000], "ai": enemy_ai_coward, "attacktype": enemy_attacktype_unarmed, "displayname": "Lost Juvie", "raredisplayname": "Shellshocked Juvie", "aliases": ["juvie","greenman","lostjuvie", "lost"]},
	enemy_type_dinoslime: {"slimerange": [250000, 500000], "ai": enemy_ai_attacker_a, "attacktype": enemy_attacktype_fangs, "displayname": "Dinoslime", "raredisplayname": "Voracious Dinoslime", "aliases": ["dino","slimeasaur"]},
	enemy_type_slimeadactyl: {"slimerange": [500000, 750000], "ai": enemy_ai_attacker_b, "attacktype": enemy_attacktype_talons, "displayname": "Slimeadactyl", "raredisplayname": "Predatory Slimeadactyl", "aliases": ["bird","dactyl"]},
	enemy_type_desertraider: {"slimerange": [250000, 750000], "ai": enemy_ai_attacker_b, "attacktype": enemy_attacktype_raiderscythe, "displayname": "Desert Raider", "raredisplayname": "Desert Warlord", "aliases": ["raider","scytheboy","desertraider", "desert"]},
	enemy_type_mammoslime: {"slimerange": [650000, 950000], "ai": enemy_ai_defender, "attacktype": enemy_attacktype_tusks, "displayname": "Mammoslime", "raredisplayname": "Territorial Mammoslime", "aliases": ["mammoth","brunswick"]},
	enemy_type_microslime: {"slimerange": [10000, 50000], "ai": enemy_ai_defender, "attacktype": enemy_attacktype_unarmed, "displayname": "Microslime", "raredisplayname": "Irridescent Microslime", "aliases": ["micro","pinky"]},
	enemy_type_slimeofgreed: {"slimerange": [20000, 100000], "ai": enemy_ai_defender, "attacktype": enemy_attacktype_unarmed, "displayname": "Slime Of Greed", "raredisplayname": "Slime Of Avarice", "aliases": ["slime","slimeofgreed","pot","potofgreed","draw2cards"]},
	enemy_type_doubleheadlessdoublehorseman: {"slimerange": [100000000, 150000000], "ai": enemy_ai_attacker_b, "attacktype": enemy_attacktype_axe, "displayname": "Double Headless Double Horseman", "raredisplayname": "Quadruple Headless Quadruple Horseman", "aliases": ["doubleheadlessdoublehorseman", "headlesshorseman", "demoknight", "horseman"]},
	enemy_type_doublehorse: {"slimerange": [50000000, 75000000], "ai": enemy_ai_attacker_a, "attacktype": enemy_attacktype_hooves, "displayname": "Double Headless Double Horseman's Horse", "raredisplayname": "Quadruple Headless Quadruple Horseman's Horse", "aliases": ["doublehorse", "horse", "pony", "lilbit"]},
	enemy_type_megaslime: {"slimerange": [1000000, 1000000], "ai": enemy_ai_attacker_a, "attacktype": enemy_attacktype_gunkshot, "displayname": "Megaslime", "raredisplayname": "Rampaging Megaslime", "aliases": ["mega","smooze","muk"]},
	enemy_type_slimeasaurusrex: {"slimerange": [1750000, 3000000], "ai": enemy_ai_attacker_b, "attacktype": enemy_attacktype_fangs, "displayname": "Slimeasaurus Rex", "raredisplayname": "Sex Rex", "aliases": ["rex","trex","slimeasaurusrex","slimeasaurus"]},
	enemy_type_greeneyesslimedragon: {"slimerange": [3500000, 5000000], "ai": enemy_ai_attacker_a, "attacktype": enemy_attacktype_molotovbreath, "displayname": "Green Eyes Slime Dragon", "raredisplayname": "Green Eyes JPEG Dragon", "aliases": ["dragon","greeneyes","greeneyesslimedragon","green"]},
	enemy_type_unnervingfightingoperator: {"slimerange": [1000000, 3000000], "ai": enemy_ai_attacker_b, "attacktype": enemy_attacktype_armcannon, "displayname": "Unnerving Fighting Operator", "raredisplayname": "Unyielding Fierce Operator", "aliases": ["ufo", "alien","unnervingfightingoperator","unnvering"]},
}

# Raid boss names used to avoid raid boss reveals in ewutils.formatMessage
raid_boss_names = [
	enemy_data_table[enemy_type_megaslime]["displayname"],
	enemy_data_table[enemy_type_megaslime]["raredisplayname"],
	enemy_data_table[enemy_type_slimeasaurusrex]["displayname"],
	enemy_data_table[enemy_type_slimeasaurusrex]["raredisplayname"],
	enemy_data_table[enemy_type_greeneyesslimedragon]["displayname"],
	enemy_data_table[enemy_type_greeneyesslimedragon]["raredisplayname"],
	enemy_data_table[enemy_type_unnervingfightingoperator]["displayname"],
	enemy_data_table[enemy_type_unnervingfightingoperator]["raredisplayname"],
]

# Responses given by cowardly enemies when a non-ghost user is in their district.
coward_responses = [
	"The {} calls out to you: *H-Hello. Are you one of those Gangsters everyone seems to be talking about?*",
	"The {} calls out to you: *You wouldn't hurt a {}, would you?*",
	"The {} calls out to you: *Why.. uh.. hello there? What brings you to these parts, stranger?*",
	"The {} calls out to you: *L-look at how much slime I have! I'm not even worth it for you to kill me!*",
	"The {} calls out to you: *I'm just a good little {}... never hurt nobody anywhere...*",
]

# Responses given by cowardly enemies when hurt.
coward_responses_hurt = [
	"\nThe {} cries out in pain!: *Just wait until the Juvenile Enrichment Center hears about this!!*",
	"\nThe {} cries out in pain!: *You MONSTER!*",
	"\nThe {} cries out in pain!: *What the H-E-double-hockey-sticks is your problem?*",
]


# Letters that an enemy can identify themselves with
identifier_letters = [
	'A', 'B', 'C', 'D', 'E',
	'F', 'G', 'H', 'I', 'J',
	'K', 'L', 'M', 'N', 'O',
	'P', 'Q', 'R', 'S', 'T',
	'U', 'V', 'W', 'X', 'Y', 'Z'
]
