smelting_recipe_list = [
	EwSmeltingRecipe(
		id_recipe = "cosmetic",
		str_name = "a cosmetic",
		alias = [
			"hat",
		],
		ingredients = {
			item_id_slimepoudrin : 2
		},
		products = cosmetic_names
	),
	EwSmeltingRecipe(
		id_recipe = item_id_quadruplestuffedcrust,
		str_name = "a Quadruple Stuffed Crust",
		alias = [
			"qsc",
			"quadruple",
			"quadruplestuffed",
		],
		ingredients = {
			item_id_doublestuffedcrust : 2
		},
		products = [item_id_quadruplestuffedcrust],
	),
        EwSmeltingRecipe(
		id_recipe = "knightarmor",
		str_name = "Knight Armor",
                alias = [
			"armor",
		],
		ingredients = {
			"ironingot" : 2
		},
		products = ["knightarmor"]
	),
	EwSmeltingRecipe(
		id_recipe = item_id_monstersoup,
		str_name = "a bowl of Monster Soup",
		alias = [
			"soup",
			"meatsoup",
			"stew",
			"meatstew",
			"monstersoup",
			"monster soup"
		],
		ingredients = {
			"monsterbones" : 5,
			item_id_dinoslimemeat : 1
		},
		products = [item_id_monstersoup],
	),
	EwSmeltingRecipe(
		id_recipe = item_id_octuplestuffedcrust,
		str_name = "an Octuple Stuffed Crust",
		alias = [
			"osc",
			"octuple",
			"octuplestuffed",
		],
		ingredients = {
			item_id_quadruplestuffedcrust : 2
		},
		products = [item_id_octuplestuffedcrust],
	),
	EwSmeltingRecipe(
		id_recipe = item_id_sexdecuplestuffedcrust,
		str_name = "a Sexdecuple Stuffed Crust",
		alias = [
			"sdsc",
			"sexdecuple",
			"sexdecuplestuffed",
		],
		ingredients = {
			item_id_octuplestuffedcrust : 2
		},
		products = [item_id_sexdecuplestuffedcrust],
	),
	EwSmeltingRecipe(
		id_recipe = item_id_duotrigintuplestuffedcrust,
		str_name = "a Duotrigintuple Stuffed Crust",
		alias = [
			"dtsc",
			"duotrigintuple",
			"duotrigintuplestuffed",
		],
		ingredients = {
			item_id_sexdecuplestuffedcrust : 2
		},
		products = [item_id_duotrigintuplestuffedcrust],
	),
	EwSmeltingRecipe(
		id_recipe = item_id_quattuorsexagintuplestuffedcrust,
		str_name = "a Quattuorsexagintuple Stuffed Crust",
		alias = [
			"qssc",
			"quattuorsexagintuple",
			"quattuorsexagintuplestuffed",
		],
		ingredients = {
			item_id_duotrigintuplestuffedcrust : 2
		},
		products = [item_id_quattuorsexagintuplestuffedcrust],
	),
	EwSmeltingRecipe(
		id_recipe = item_id_forbiddenstuffedcrust,
		str_name = "a Forbidden Stuffed Crust",
		alias = [
			"fsc",
			"forbiddenstuffedcrust",
		],
		ingredients = {
			item_id_quattuorsexagintuplestuffedcrust : 2,
			item_id_forbidden111 : 1
		},
		products = [item_id_forbiddenstuffedcrust],
	),
	EwSmeltingRecipe(
		id_recipe = item_id_forbidden111,
		str_name = "The Forbidden {}".format(emote_111),
		alias = [
			"forbiddenone",
			"forbidden",
			"sealed",
			"exodia",
			"oneoneone",
			"forbidden111",
			":111:",
		],
		ingredients = {'leftleg' : 1,
			'rightleg' : 1,
			'slimexodia' : 1,
			'rightarm' : 1,
			'leftarm' : 1
		},
		products = [item_id_forbidden111]
	),
	EwSmeltingRecipe(
		id_recipe = "pickaxe",
		str_name = "a Poudrin Pickaxe",
		alias = [
			"pp", # LOL
			"poudrinpick",
			"poudrinpickaxe",
			"pick"
		],
		ingredients = {
			item_id_slimepoudrin : 3,
			item_id_stick : 2
		},
		products = ['pickaxe']
	),
	EwSmeltingRecipe(
		id_recipe = "faggot",
		str_name = "a Faggot",
		alias = [
			"f",
			"fag",
		],
		ingredients = {
			item_id_stick : 3

		},
		products = ['faggot']
	),
	EwSmeltingRecipe(
		id_recipe = "doublefaggot",
		str_name = "a Double Faggot",
		alias = [
			"df",
			"dfag",
		],
		ingredients = {
			item_id_faggot : 2
		},
		products = ['doublefaggot']
	),
	EwSmeltingRecipe(
		id_recipe = "dinoslimesteak",
		str_name = "a cooked piece of Dinoslime meat",
		alias = [
			"cookedmeat",
			"dss"
		],
		ingredients = {
			item_id_faggot : 1,
			item_id_dinoslimemeat : 1
		},
		products = ['dinoslimesteak']
	),
	EwSmeltingRecipe(
		id_recipe = "fishingrod",
		str_name = "a fishing rod",
		alias = [
			"fish",
			"fishing",
			"rod",
			"fr"
		],
		ingredients = {
			'string': 2,
			'stick': 3
		},
		products = ['fishingrod']
	),
    EwSmeltingRecipe(
		id_recipe = "bass",
		str_name = "a Bass Guitar",
		alias = [
			"bassguitar"
		],
		ingredients = {
			'thebassedgod' : 1,
			'string':4
		},
		products = ['bass']
    ),
    EwSmeltingRecipe(
		id_recipe = "bow",
		str_name = "a Minecraft Bow",
		alias = [
			"minecraft bow"
		],
		ingredients = {
			'stick' : 3,
			'string':3
		},
		products = ['bow']
    ),
	    EwSmeltingRecipe(
		id_recipe = "ironingot",
		str_name = "an Iron Ingot",
		alias = [
			"ingot"
			"metal",
			"ironingot",
			"iron ingot"
		],
		ingredients = {
			'tincan':10,
			'faggot':1
		},
		products = ['ironingot']
    ),
	    EwSmeltingRecipe(
		id_recipe = "tanningknife",
		str_name = "a small tanning knife",
		alias = [
			"knife",
			"tanningknife",
			"tanning"
		],
		ingredients = {
			'ironingot':1
		},
		products = ['tanningknife']
    ),
	    EwSmeltingRecipe(
		id_recipe = "leather",
		str_name = "a piece of leather",
		alias = [
			"leather"
		],
		ingredients = {
			'oldboot':10,
			'tanningknife':1
		},
		products = ['leather']
    ),
	    EwSmeltingRecipe(
		id_recipe = "bloodstone",
		str_name = "a chunk of bloodstone",
		alias = [
			"bloodstone",
			"bstone"
		],
		ingredients = {
			'monsterbones':100,
			'faggot':1
		},
		products = ['bloodstone']
    ),
	    EwSmeltingRecipe(
		id_recipe = "dclaw",
		str_name = "a Dragon Claw",
		alias = [
			"dragonclaw",
			"claw",
			"dclaw"
		],
		ingredients = {
			'dragonsoul' : 1,
			item_id_slimepoudrin : 5,
			'ironingot':1,
			'leather':1
		},
		products = ['dclaw']
    ),

	EwSmeltingRecipe(
		id_recipe = "leathercouch",
		str_name = "a leather couch",
		alias = [
			"humancouch"
		],
		ingredients = {
			'couch': 1,
			'scalp': 10
		},
		products = ['leathercouch']
	),
	EwSmeltingRecipe(
		id_recipe = "leatherchair",
		str_name = "a leather chair",
		alias = [
			"humanchair"
		],
		ingredients = {
			'chair': 1,
			'scalp': 5
		},
		products = ['leatherchair']
	),
	EwSmeltingRecipe(
		id_recipe = "leatherlamp",
		str_name = "a leather coated lamp",
		alias = [
			"humanlamp"
		],
		ingredients = {
			'lamp': 1,
			'scalp': 3
		},
		products = ['leatherlamp']
	),
	EwSmeltingRecipe(
		id_recipe = "leatherdesk",
		str_name = "a leather desk",
		alias = [
			"humandesk"
		],
		ingredients = {
			'desk': 1,
			'scalp': 4
		},
		products = ['leatherdesk']
	),
	EwSmeltingRecipe(
		id_recipe = "leatherbed",
		str_name = "a leather bed",
		alias = [
			"humanbed"
		],
		ingredients = {
			'bed': 1,
			'scalp': 12
		},
		products = ['leatherbed']
	),
	EwSmeltingRecipe(
		id_recipe = "seaweedjoint",
		str_name = "a seaweed joint",
		alias = [
			"joint",
			"seaweed",
			"weed",
			"doobie",
			"blunt"
		],
		ingredients = {
			'seaweed' : 3,
			'dankwheat': 1,
			item_id_slimepoudrin : 1,
		},
		products = ['seaweedjoint']
	),
	EwSmeltingRecipe(
		id_recipe = "slimepoudrin",
		str_name = "a slime poudrin",
		alias = [
			"poudrin",
			"poud",
			"pou",
			"poodrin",
		],
		ingredients = {
			'royaltypoudrin': 2
		},
		products = ['slimepoudrin']
	),
EwSmeltingRecipe(
		id_recipe = "humancorpse",
		str_name = "a corpse",
		alias = [
			"stiff",
			"corpse",
			"deadperson",
			"cadaver",
		],
		ingredients = {
			'scalp': 20,
			'dinoslimemeat':2,
			'string':2
		},
		products = ['humancorpse']
	),
EwSmeltingRecipe(
		id_recipe = "popeonarope",
		str_name = "pope on a rope",
		alias = [
			"pope",
			"francis",
			"deadpope",
			"sacrilege",
		],
		ingredients = {
			'humancorpse': 1,
			'diadem':1,
			'scarf':1,
			'confessionbooth':1
		},
		products = ['popeonarope']
	),
EwSmeltingRecipe(
		id_recipe = "reanimatedcorpse",
		str_name = "reanimated corpse",
		alias = [
			"frankenstein",
			"reanimate",
			"revenant",
		],
		ingredients = {
			'humancorpse': 1,
			'soul':1,
		},
		products = ['reanimatedcorpse']
	),
EwSmeltingRecipe(
		id_recipe = "soul",
		str_name = "soul",
		alias = [
			"spirit",
			"essence",
			"hippiebullshit",
		],
		ingredients = {
			'reanimatedcorpse': 1,
		},
		products = ['soul']
	),
EwSmeltingRecipe(
		id_recipe = "handmadechair",
		str_name = "handmade chair",
		alias = [
			"woodchair",
			"carvedchair",
			"woodenchair",
			"ornatechair",
		],
		ingredients = {
			'stick': 5,
			'bat':2,
		},
		products = ['ornatechair', 'shittychair']
	),
EwSmeltingRecipe(
		id_recipe = "handmadebench",
		str_name = "handmade bench",
		alias = [
			"woodbench",
			"carvedbench",
			"woodenbench",
			"ornatebench",
		],
		ingredients = {
			'stick': 10,
			'bat':4,
		},
		products = ['ornatebench', 'shittybench']
	),
EwSmeltingRecipe(
		id_recipe = "handmadebed",
		str_name = "handmade bed",
		alias = [
			"woodbed",
			"carvedbed",
			"woodenbed",
			"ornatebed",
		],
		ingredients = {
			'stick': 12,
			'bat':3,
		},
		products = ['ornatebed', 'shittybed']
	),
EwSmeltingRecipe(
		id_recipe = "handmadedesk",
		str_name = "handmade desk",
		alias = [
			"wooddesk",
			"carveddesk",
			"woodendesk",
			"ornatedesk",
		],
		ingredients = {
			'stick': 4,
			'bat':1,
		},
		products = ['ornatedesk', 'shittydesk']
	),
EwSmeltingRecipe(
		id_recipe = "clarinet",
		str_name = "clarinet",
		alias = [
			"flute",
			"bennygoodmanthing",
			"vuvuzela",
		],
		ingredients = {
			'bat': 1,
			'razornuts':1,
			'knives':1,
			'blacklimes':1,
			'direappleciderfuckenergy':1,
			'sweetfish':1,

		},
		products = ['craftsmansclarinet', 'woodenvuvuzela']
	),
EwSmeltingRecipe(
		id_recipe = "guitar",
		str_name = "solid poudrin guitar",
		alias = [
			"poudringuitar",
			"electricguitar",
			"solidpoudringuitar",
		],
		ingredients = {
			'slimepoudrin': 150,
			'string':6,
		},
		products = ['solidpoudringuitar']
	),
EwSmeltingRecipe(
		id_recipe = "drums",
		str_name = "beast skin drums",
		alias = [
			"beastskindrums",
			"drumset",
			"drum",
		],
		ingredients = {
			'dinoslimemeat': 25,
			'dinoslimesteak' : 5,
			'scalp': 5,
			'string' : 3,
			'stick' : 2
		},
		products = ['beastskindrums']
	),
EwSmeltingRecipe(
		id_recipe = "xylophone",
		str_name = "fish bone xylophone",
		alias = [
			"xylo",
			"metallophone",
			"fishbonexylophone",
		],
		ingredients = {
			'nuclearbream' : 1,
			'largebonedlionfish' : 2,
			'plebefish':3,
			'sweetfish':1,
			'stick':1
		},
		products = ['fishbonexylophone']
	),
EwSmeltingRecipe(
		id_recipe = "maracas",
		str_name = "gourd maracas",
		alias = [
			"gourdmaracas",
			"shakers",
			"rattle",
		],
		ingredients = {
			'pulpgourds' : 1,
			'suganmanuts' : 1,
			'sludgeberries':1,
			'razornuts':1,
			'joybeans':1,
			'phosphorpoppies':1
		},
		products = ['gourdmaracas']
	),
]


# A map of id_recipe to EwSmeltingRecipe objects.
smelting_recipe_map = {}

# A list of recipe names
recipe_names = []