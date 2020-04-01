
# dye ids
dye_black = "blackdye"
dye_maroon = "maroondye"
dye_green = "greendye"
dye_brown = "browndye"
dye_tan = "tandye"
dye_purple = "purpledye"
dye_teal = "tealdye"
dye_orange = "orangedye"
dye_gray = "graydye"
dye_red = "reddye"
dye_lime = "limedye"
dye_yellow = "yellowdye"
dye_blue = "bluedye"
dye_fuchsia = "fuchsiadye"
dye_aqua = "aquadye"
dye_white = "whitedye"

# list of dyes you're able to saturate your Slimeoid with
dye_list = []
dye_map = {}


hue_id_yellow = "yellow"
hue_id_orange = "orange"
hue_id_red = "red"
hue_id_pink = "pink"
hue_id_magenta = "magenta"
hue_id_purple = "purple"
hue_id_blue = "blue"
hue_id_cobalt = "cobalt"
hue_id_cyan = "cyan"
hue_id_teal = "teal"
hue_id_green = "green"
hue_id_lime = "lime"
hue_id_rainbow = "rainbow"
hue_id_white = "white"
hue_id_grey = "grey"
hue_id_black = "black"



# All color attributes in the game.
hue_list = [
	EwHue(
		id_hue = hue_id_white,
		alias = [
			"whitedye",
			"poketubers"
		],
		str_saturate = "It begins to glow a ghostly white!",
		str_name = "white",
		str_desc = "Its pale white body and slight luminescence give it a supernatural vibe."
	),
	EwHue(
		id_hue = hue_id_yellow,
		alias = [
			"yellowdye",
			"pulpgourds"
		],
		str_saturate = "It begins to shine a bright yellow!",
		str_name = "yellow",
		str_desc = "Its bright yellow hue is delightfully radiant.",
		effectiveness = {
			hue_id_orange: hue_analogous,
			hue_id_lime: hue_analogous,
			hue_id_purple: hue_atk_complementary,
			hue_id_cobalt: hue_special_complementary,
			hue_id_rainbow: hue_full_complementary
		}
	),
	EwHue(
		id_hue = hue_id_orange,
		alias = [
			"orangedye",
			"sourpotatoes"
		],
		str_saturate = "It turns a warm orange!",
		str_name= "orange",
		str_desc = "Its warm orange hue makes you want to cuddle up beside it with a nice book.",
		effectiveness = {
			hue_id_red: hue_analogous,
			hue_id_yellow: hue_analogous,
			hue_id_blue: hue_atk_complementary,
			hue_id_cyan: hue_special_complementary,
			hue_id_rainbow: hue_full_complementary
		}
	),
	EwHue(
		id_hue = hue_id_red,
		alias = [
			"reddye",
			"blood",
			"cabbage"
		],
		str_saturate = "It darkens a deep shade of crimson red!",
		str_name = "red",
		str_desc = "Its deep burgundy hue reminds you of a rare steak’s leaked myoglobin.",
		effectiveness = {
			hue_id_pink: hue_analogous,
			hue_id_orange: hue_analogous,
			hue_id_cobalt: hue_atk_complementary,
			hue_id_teal: hue_special_complementary,
			hue_id_rainbow: hue_full_complementary
		}
	),
	EwHue(
		id_hue = hue_id_magenta,
		alias = [
			"magentadye",
			"joybeans"
		],
		str_saturate = "It turns a vivid magenta!",
		str_name = "magenta",
		str_desc = "It’s vivid magenta that fills you with energy and excitement every time you see it.",
		effectiveness = {
			hue_id_pink: hue_analogous,
			hue_id_purple: hue_analogous,
			hue_id_teal: hue_atk_complementary,
			hue_id_lime: hue_special_complementary,
			hue_id_rainbow: hue_full_complementary
		}
	),
	EwHue(
		id_hue = hue_id_purple,
		alias = [
			"purpledye",
			"purplekilliflower",
			"killer"
		],
		str_saturate = "It turns a dark purple!",
		str_name = "purple",
		str_desc = "Its dark purple hue gives it a brooding, edgy appearance. It will huff and groan when given orders, like a teenage rebelling against his mom in the most flaccid way possible.",
		effectiveness = {
			hue_id_blue: hue_analogous,
			hue_id_magenta: hue_analogous,
			hue_id_green: hue_atk_complementary,
			hue_id_yellow: hue_special_complementary,
			hue_id_rainbow: hue_full_complementary
		}
	),
	EwHue(
		id_hue = hue_id_blue,
		alias = [
			"bluedye",
			"razornuts"
		],
		str_saturate = "It turns a deep blue!",
		str_name = "blue",
		str_desc = "Its deep blue hue reminds you of those “ocean” things you’ve heard so much of in the movies and video games that have washed ashore the coast of the Slime Sea.",
		effectiveness = {
			hue_id_cobalt: hue_analogous,
			hue_id_purple: hue_analogous,
			hue_id_lime: hue_atk_complementary,
			hue_id_orange: hue_special_complementary,
			hue_id_rainbow: hue_full_complementary
		}
	),
	EwHue(
		id_hue = hue_id_green,
		alias = [
			"greendye",
			"pawpaw",
			"juvie"
		],
		str_saturate = "It turns a shade of green that barely distinguishes itself from a Slimeoid’s standard hue.",
		str_name = "green",
		str_desc = "Its unimpressive green hue does nothing to separate itself from the swathes of the undyed Slimeoids of the working class.",
		effectiveness = {
			hue_id_lime: hue_analogous,
			hue_id_teal: hue_analogous,
			hue_id_pink: hue_atk_complementary,
			hue_id_purple: hue_special_complementary,
			hue_id_rainbow: hue_full_complementary
		}

	),
	EwHue(
		id_hue = hue_id_teal,
		alias = [
			"tealdye",
			"sludgeberries"
		],
		str_saturate = "It looks so purdy now!",
		str_name = "teal",
		str_desc = "Its caliginous teal hue gives you a sudden lust for prosecuting criminals in the legal system, before coming to your senses and realizing there is no legal system here.",
		effectiveness = {
			hue_id_green: hue_analogous,
			hue_id_cyan: hue_analogous,
			hue_id_red: hue_atk_complementary,
			hue_id_magenta: hue_special_complementary,
			hue_id_rainbow: hue_full_complementary
		}

	),
	EwHue(
		id_hue = hue_id_rainbow,
		alias = [
			"rainbowdye",
			"suganmanuts"
		],
		str_saturate = "It turns a fantastic shade of... well, everything!!",
		str_name = "***Rainbow***",
		str_desc = "Its ***Rainbow*** hue dazzles and amazes you. It comprises the whole color spectrum in an crude, Photoshop-tier gradient. It’s so obnoxious… and yet, decadent!"
	),
	EwHue(
		id_hue = hue_id_pink,
		alias = [
			"pinkdye",
			"pinkrowddishes"
		],
		str_saturate = "It turns a vibrant shade of  pink!",
		str_name = "pink",
		str_desc = "Its vibrant pink hue imbues the Slimeoid with an uncontrollable lust for destruction. You will often see it flailing about happily, before knocking down a mailbox or kicking some adult in the shin.",
		effectiveness = {
			hue_id_magenta: hue_analogous,
			hue_id_red: hue_analogous,
			hue_id_cyan: hue_atk_complementary,
			hue_id_green: hue_special_complementary,
			hue_id_rainbow: hue_full_complementary
		}

	),
	EwHue(
		id_hue = hue_id_grey,
		alias = [
			"greydye",
			"dankwheat"
		],
		str_saturate = "It turns a dull, somber grey.",
		str_name = "grey",
		str_desc = "Its dull grey hue depresses you, lulling you into inaction and complacency. "
	),
	EwHue(
		id_hue = hue_id_cobalt,
		alias = [
			"cobaltdye",
			"brightshade"
		],
		str_saturate = "It turns a shimmering cobalt!",
		str_name = "cobalt",
		str_desc = "Its shimmering cobalt hue can reflect images if properly polished.",
		effectiveness = {
			hue_id_cyan: hue_analogous,
			hue_id_blue: hue_analogous,
			hue_id_yellow: hue_atk_complementary,
			hue_id_red: hue_special_complementary,
			hue_id_rainbow: hue_full_complementary
		}

	),
	EwHue(
		id_hue = hue_id_black,
		alias = [
			"blackdye",
			"blacklimes"
		],
		str_saturate = "It turns pitch black!",
		str_name = "black",
		str_desc = "Its pitch black, nearly vantablack hue absorbs all the light around it, making this Slimeoid appear as though a hole was ripped right out of reality."
	),
	EwHue(
		id_hue = hue_id_lime,
		alias = [
			"limedye",
			"phosphorpoppies"
		],
		str_saturate = "It turns a heavily saturated lime!",
		str_name = "lime",
		str_desc = "Its heavily saturated lime hue assaults your eyes in a way not unlike the Slime Sea. That is to say, painfully.",
		effectiveness = {
			hue_id_yellow: hue_analogous,
			hue_id_green: hue_analogous,
			hue_id_magenta: hue_atk_complementary,
			hue_id_blue: hue_special_complementary,
			hue_id_rainbow: hue_full_complementary
		}

	),
	EwHue(
		id_hue = hue_id_cyan,
		alias = [
			"cyandye",
			"direapples"
		],
		str_saturate = "It turned a light cyan!",
		str_name = "cyan",
		str_desc = "Its light cyan hue imbues it with a slightly anxious demeanor, it is sure to avoid sewer manholes when walking down the street.",
		effectiveness = {
			hue_id_teal: hue_analogous,
			hue_id_cobalt: hue_analogous,
			hue_id_orange: hue_atk_complementary,
			hue_id_pink: hue_special_complementary,
			hue_id_rainbow: hue_full_complementary
		}

	),
]

# A map of id_hue to EwHue objects.
hue_map = {}

# A list of hue names
hue_names = []
