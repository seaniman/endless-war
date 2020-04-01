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













# property classes
property_class_s = "s"
property_class_a = "a"
property_class_b = "b"
property_class_c = "c"

# district capturing
capture_tick_length = 10  # in seconds; also affects how much progress is made per tick
max_capture_points_s = 500000 # 500k
max_capture_points_a = 300000  # 300k
max_capture_points_b = 200000  # 200k
max_capture_points_c = 100000   # 100k

# district capture rates assigned to property classes
max_capture_points = {
	property_class_s: max_capture_points_s,
	property_class_a: max_capture_points_a,
	property_class_b: max_capture_points_b,
	property_class_c: max_capture_points_c
}

# how long districts stay locked after capture
capture_lock_s = 48 * 60 * 60  # 2 days
capture_lock_a = 24 * 60 * 60  # 1 day
capture_lock_b = 12 * 60 * 60  # 12 hours
capture_lock_c = 6 * 60 * 60  # 6 hours

# district lock times assigned to property classes
capture_locks = {
	property_class_s: capture_lock_s,
	property_class_a: capture_lock_a,
	property_class_b: capture_lock_b,
	property_class_c: capture_lock_c,
}

# how much slimes is needed to bypass capture times
slimes_toannex_s = 1000000 # 1 mega
slimes_toannex_a = 500000 # 500 k
slimes_toannex_b = 200000 # 200 k
slimes_toannex_c = 100000 # 100 k

# slimes to annex by property class
slimes_toannex = {
	property_class_s: slimes_toannex_s,
	property_class_a: slimes_toannex_a,
	property_class_b: slimes_toannex_b,
	property_class_c: slimes_toannex_c
}

# by how much to extend the capture lock per additional gangster capping
capture_lock_per_gangster = 60 * 60  # 60 min

# capture lock messages
capture_lock_milestone = 5 * 60 # 5 min

# capture messages
capture_milestone = 5  # after how many percent of progress the players are notified of the progress

# capture speed at 0% progress
baseline_capture_speed = 1

# accelerates capture speed depending on current progress
capture_gradient = 1

# district de-capturing
decapture_speed_multiplier = 1  # how much faster de-capturing is than capturing

# district control decay
decay_modifier = 1  # more means slower

# time values
seconds_per_ingame_day = 21600
ticks_per_day = seconds_per_ingame_day / update_market  # how often the kingpins receive slime per in-game day

# kingpin district control slime yields (per tick, i.e. in-game-hourly)
slime_yield_class_s = int(60000 / ticks_per_day)  # dividing the daily amount by the amount of method calls per day
slime_yield_class_a = int(40000 / ticks_per_day)
slime_yield_class_b = int(30000 / ticks_per_day)
slime_yield_class_c = int(20000 / ticks_per_day)

# district control slime yields assigned to property classes
district_control_slime_yields = {
	property_class_s: slime_yield_class_s,
	property_class_a: slime_yield_class_a,
	property_class_b: slime_yield_class_b,
	property_class_c: slime_yield_class_c
}

# Slime decay rate
slime_half_life = 60 * 60 * 24 * 14 #two weeks

# Rate of bleeding stored damage into the environment
bleed_half_life = 60 * 5 #five minutes

# how often to bleed
bleed_tick_length = 10

# how often to decide whether or not to spawn an enemy
enemy_spawn_tick_length = 60 * 3 # Three minutes

# how often it takes for hostile enemies to attack
enemy_attack_tick_length = 5

# how often to burn
burn_tick_length = 4

# how often to check for statuses to be removed
removestatus_tick_length = 5

# Unearthed Item rarity (for enlisted players)
unearthed_item_rarity = 1500

# Chance to loot an item while scavenging
scavenge_item_rarity = 1000

# Lifetimes
invuln_onrevive = 0

# how often to apply weather effects
weather_tick_length = 10

# how often to delete expired world events
event_tick_length = 5

# shambleball tick length
shambleball_tick_length = 5

# how often to refresh sap
sap_tick_length = 5

# the amount of sap crushed by !piss
sap_crush_piss = 3

# the amount of sap spent on !piss'ing on someone
sap_spend_piss = 1

# farming
crops_time_to_grow = 180  # in minutes; 180 minutes are 3 hours
reap_gain = 100000
farm_slimes_peraction = 25000
time_nextphase = 20 * 60 # 20 minutes
farm_tick_length = 60 # 1 minute

farm_phase_sow = 0
farm_phase_reap = 9

farm_action_none = 0
farm_action_water = 1
farm_action_fertilize = 2
farm_action_weed = 3
farm_action_pesticide = 4

farm_actions = [
	EwFarmAction(
		id_action = farm_action_water,
		action = cmd_irrigate,
		str_check = "Your crop is dry and weak. It needs some water.",
		str_execute = "You pour water on your parched crop.",
		str_execute_fail = "You pour gallons of water on the already saturated soil, nearly drowning your crop.",
	),
	EwFarmAction(
		id_action = farm_action_fertilize,
		action = cmd_fertilize,
		str_check = "Your crop looks malnourished like an African child in a charity ad.",
		str_execute = "You fertilize your starving crop.",
		str_execute_fail = "You give your crop some extra fertilizer for good measure. The ground's salinity shoots up as a result. Maybe look up fertilizer burn, dumbass.",
	),
	EwFarmAction(
		id_action = farm_action_weed,
		action = cmd_weed,
		str_check = "Your crop is completely overgrown with weeds.",
		str_execute = "You make short work of the weeds.",
		str_execute_fail = "You pull those damn weeds out in a frenzy. Hold on, that wasn't a weed. That was your crop. You put it back in the soil, but it looks much worse for the wear.",
	),
	EwFarmAction(
		id_action = farm_action_pesticide,
		action = cmd_pesticide,
		str_check = "Your crop is being ravaged by parasites.",
		str_execute = "You spray some of the good stuff on your crop and watch the pests drop like flies, in a very literal way.",
		str_execute_fail = "You spray some of the really nasty stuff on your crop. Surely no pests will be able to eat it away now. Much like any other living creature, probably.",
	),
]

id_to_farm_action = {}
cmd_to_farm_action = {}
farm_action_ids = []

for farm_action in farm_actions:
	cmd_to_farm_action[farm_action.action] = farm_action
	for alias in farm_action.aliases:
		cmd_to_farm_action[alias] = farm_action
	id_to_farm_action[farm_action.id_action] = farm_action
	farm_action_ids.append(farm_action.id_action)


# fishing
fish_gain = 10000 # multiplied by fish size class
fish_offer_timeout = 1440 # in minutes; 24 hours

# Cooldowns
cd_kill = 5
cd_spar = 60
cd_haunt = 600
cd_squeeze = 1200
cd_invest = 1200
cd_boombust = 22
#For possible time limit on russian roulette
cd_rr = 600
#slimeoid downtime after a defeat
cd_slimeoiddefeated = 300
cd_scavenge = 0
soft_cd_scavenge = 15 # Soft cooldown on scavenging
cd_enlist = 60

# PvP timer pushouts
time_pvp_kill = 30 * 60
time_pvp_attack = 10 * 60
time_pvp_annex = 10 * 60
time_pvp_mine = 1 * 60
time_pvp_scavenge = 3 * 60
time_pvp_fish = 5 * 60
time_pvp_farm = 10 * 60
time_pvp_spar = 5 * 60
time_pvp_enlist = 5 * 60
time_pvp_knock = 10 #temp fix. will probably add spam prevention or something funny like restraining orders later
time_pvp_duel = 3 * 60

# time to get kicked out of subzone
time_kickout = 60 * 60  # 1 hour

# time after coming online before you can act
time_offline = 10

# time for an enemy to despawn
time_despawn = 60 * 60 * 12 # 12 hours

# time for a player to be targeted by an enemy after entering a district
time_enemyaggro = 5

# time for a raid boss to target a player after moving to a new district
time_raidbossaggro = 3

# time for a raid boss to activate
time_raidcountdown = 60

# time for a raid boss to stay in a district before it can move again
time_raidboss_movecooldown = 150

# maximum amount of enemies a district can hold before it stops spawning them
max_enemies = 5

# response string used to let attack function in ewwep know that an enemy is being attacked
enemy_targeted_string = "ENEMY-TARGETED"


# Emotes
emote_tacobell = "<:tacobell:431273890195570699>"
emote_pizzahut = "<:pizzahut:431273890355085323>"
emote_kfc = "<:kfc:431273890216673281>"
emote_moon = "<:moon:431418525303963649>"
emote_111 = "<:111:431547758181220377>"

emote_copkiller = "<:copkiller:431275071945048075>"
emote_rowdyfucker = "<:rowdyfucker:431275088076079105>"
emote_ck = "<:ck:504173691488305152>"
emote_rf = "<:rf:504174176656162816>"

emote_theeye = "<:theeye:431429098909466634>"
emote_slime1 = "<:slime1:431564830541873182>"
emote_slime2 = "<:slime2:431570132901560320>"
emote_slime3 = "<:slime3:431659469844381717>"
emote_slime4 = "<:slime4:431570132901560320>"
emote_slime5 = "<:slime5:431659469844381717>"
emote_slimeskull = "<:slimeskull:431670526621122562>"
emote_slimeheart = "<:slimeheart:431673472687669248>"
emote_dice1 = "<:dice1:436942524385329162>"
emote_dice2 = "<:dice2:436942524389654538>"
emote_dice3 = "<:dice3:436942524041527298>"
emote_dice4 = "<:dice4:436942524406300683>"
emote_dice5 = "<:dice5:436942524444049408>"
emote_dice6 = "<:dice6:436942524469346334>"
emote_negaslime = "<:ns:453826200616566786>"
emote_bustin = "<:bustin:455194248741126144>"
emote_ghost = "<:lordofghosts:434002083256205314>"
emote_slimefull = "<:slimefull:496397819154923553>"
emote_purple = "<:purple:496397848343216138>"
emote_pink = "<:pink:496397871180939294>"
emote_slimecoin = "<:slimecoin:440576133214240769>"
emote_slimegun = "<:slimegun:436500203743477760>"
emote_slimeshot = "<:slimeshot:436604890928644106>"
emote_slimecorp = "<:slimecorp:568637591847698432>"
emote_nlacakanm = "<:nlacakanm:499615025544298517>"
emote_megaslime = "<:megaslime:436877747240042508>"
emote_srs = "<:srs:631859962519224341>"
emote_staydead = "<:sd:506840095714836480>"

# Emotes for the negaslime writhe animation
emote_vt = "<:vt:492067858160025600>"
emote_ve = "<:ve:492067844930928641>"
emote_va = "<:va:492067850878451724>"
emote_v_ = "<:v_:492067837565861889>"
emote_s_ = "<:s_:492067830624157708>"
emote_ht = "<:ht:492067823150039063>"
emote_hs = "<:hs:492067783396294658>"
emote_he = "<:he:492067814933266443>"
emote_h_ = "<:h_:492067806465228811>"
emote_blank = "<:blank:570060211327336472>"

# Emotes for troll romance
emote_hearts = ":hearts:"
emote_diamonds = ":diamonds:"
emote_spades = ":spades:"
emote_clubs = ":clubs:"
emote_broken_heart = ":broken_heart:"

# Emotes for minesweeper
emote_ms_hidden = ":pick:"
emote_ms_mine = ":x:"
emote_ms_flagged = ":triangular_flag_on_post:"
emote_ms_0 = ":white_circle:"
emote_ms_1 = ":heart:"
emote_ms_2 = ":yellow_heart:"
emote_ms_3 = ":green_heart:"
emote_ms_4 = ":blue_heart:"
emote_ms_5 = ":purple_heart:"
emote_ms_6 = ":six:"
emote_ms_7 = ":seven:"
emote_ms_8 = ":eight:"

# mining grid types
mine_grid_type_minesweeper = "minesweeper"
mine_grid_type_pokemine = "pokemining"
mine_grid_type_bubblebreaker = "bubblebreaker"

# mining sweeper
cell_mine = 1
cell_mine_marked = 2
cell_mine_open = 3

cell_empty = -1
cell_empty_marked = -2
cell_empty_open = -3

cell_slime = 0

# bubble breaker
cell_bubble_empty = "0"
cell_bubble_0 = "5"
cell_bubble_1 = "1"
cell_bubble_2 = "2"
cell_bubble_3 = "3"
cell_bubble_4 = "4"

cell_bubbles = [
	cell_bubble_0,
	cell_bubble_1,
	cell_bubble_2,
	cell_bubble_3,
	cell_bubble_4
]

bubbles_to_burst = 4


symbol_map_ms = {
	-1 : "/",
	1 : "/",
	-2 : "+",
	2 : "+",
	3 : "X"
}

symbol_map_pokemine = {
	-1 : "_",
	0 : "~",
	1 : "X",
	11 : ";",
	12 : "/",
	13 : "#"

}

number_emote_map = {
	0 : emote_ms_0,
	1 : emote_ms_1,
	2 : emote_ms_2,
	3 : emote_ms_3,
	4 : emote_ms_4,
	5 : emote_ms_5,
	6 : emote_ms_6,
	7 : emote_ms_7,
	8 : emote_ms_8
}

alphabet = "abcdefghijklmnopqrstuvwxyz"

mines_wall_map = {
	channel_mines : channel_jrmineswall,
	channel_tt_mines : channel_ttmineswall,
	channel_cv_mines : channel_cvmineswall
}

# trading
trade_state_proposed = 0
trade_state_ongoing = 1
trade_state_complete = 2

# SLIMERNALIA
festivity_on_gift_wrapping = 100
festivity_on_gift_giving = 10000

# Common strings.
str_casino_closed = "The SlimeCorp Casino only operates at night."
str_casino_negaslime_dealer = "\"We don't deal with negaslime around here.\", says the dealer disdainfully."
str_casino_negaslime_machine = "The machine doesn't seem to accept antislime."
str_exchange_closed = "The Exchange has closed for the night."
str_exchange_specify = "Specify how much {currency} you will {action}."
str_exchange_channelreq = "You must go to the #" + channel_stockexchange + " in person to {action} your {currency}."
str_exchange_busy = "You can't {action} right now. Your slimebroker is busy."
str_weapon_wielding_self = "You are wielding"
str_weapon_wielding = "They are wielding"
str_weapon_married_self = "You are married to"
str_weapon_married = "They are married to"
str_eat_raw_material = "You chomp into the raw {}. It isn't terrible, but you feel like there is a more constructive use for it."

generic_role_name = 'NLACakaNM'

str_generic_subway_description = "A grimy subway train."
str_generic_subway_station_description = "A grimy subway station."
str_blimp_description = "This luxury zeppelin contains all the most exquisite amenities a robber baron in transit could ask for. A dining room, a lounge, a pool table, you know, rich people stuff. Being a huge, highly flammable balloon filled with hydrogen, it is the safest way to travel in the city only because it's out of the price range of most juveniles' budget. It's used by the rich elite to travel from their summer homes in Assault Flats Beach to their winter homes in Dreadford, and vice versa, without having to step foot in the more unsavory parts of the city. It does it's job well and only occasionally bursts into flames."
str_blimp_tower_description = "This mooring mast is mostly used for amassing millionaire mooks into the marvelous Neo Milwaukee multi-story zeppelin, m'lady. Basically, you can board a blimp here. All you have to do is walk up an extremely narrow spiral staircase without an adequate handrail for about 40 feet straight up and then you can embark onto the highest airship this side of the River of Slime! It'll be great! Don't mind the spontaneously combusting zeppelins crashing into the earth in the distance. That's normal."
str_downtown_station_description = "This large, imposing structure is the central hub for the entire city's rapid transit system. A public transportation powerhouse, it contains connections to every subway line in the city, and for dirt cheap. Inside of it's main terminal, a humongous split-flap display is constantly updating with the times of subway arrivals and departures. Hordes of commuters from all across the city sprint to their connecting trains, or simply spill out into the Downtown streets, ready to have their guts do the same.\n\nExits into Downtown NLACakaNM."
str_red_subway_description = "Red Line trains are strictly uniform, with dull, minimalistic furnishings producing a borderline depressing experience. Almost completely grey aside from it's style guide mandated red accents, everything is purely practical. It provides just enough for its commuting salarymen to get to work in the morning and home at night."
str_red_subway_station_description = "This sparsely decorated terminal replicates the feeling of riding on a Red Line train, otherwise known as inducing suicidal thoughts. Dim lighting barely illuminates the moldy, stained terminal walls. Inbound and outbound trains arrive and departure one after another with unreal temporal precision. You're not sure if you've ever seen a Red Line train be late. Still doesn't make you like being on one though."
str_green_subway_description = "Easily the oldest subway line in the city, with the interior design and general cleanliness to prove it. Once cutting edge, it's art deco stylings have begun to deteriorate due to overuse and underfunding. That goes double for the actual trains themselves, with a merely bumpy ride on the Green Line being the height of luxury compared to the far worse potential risks."
str_green_subway_station_description = "Much like its trains, Green Line terminals have fallen into disrepair. It's vintage aesthetic only exasperating it's crumbling infrastructure, making the whole line seem like a old, dilapidated mess. But, you'll give it one thing, it's pretty cool looking from the perspective of urban exploration. You've dreamed of exploring it's vast, abandoned subway networks ever since you first rode on it. They could lead to anywhere. So close, and yet so mysterious."
str_blue_subway_description = "Probably the nicest subway line in the city, the Blue Line isn't defined by its poor hygiene or mechanical condition. Instead, it's defined by its relative normality. More-or-less clean floors, brightly lit interiors, upholstery on the seats. These stunning, almost sci-fi levels of perfection are a sight to behold. Wow!"
str_blue_subway_station_description = "It is clean and well-kempt, just like the Blue Line trains. This relatively pristine subway terminal hosts all manner of unusualities. With limited amounts of graffiti sprayed unto the otherwise sort-of white walls, there's actually some semblance of visual simplicity. For once in this city, your eyes aren't being completely assaulted with information or blinding lights. Boring, this place sucks. Board whatever train you're getting on and get back to killing people as soon as possible."
str_yellow_subway_description = "If there's one word to describe the Yellow Line, it's \"confusing\". It's by far the filthiest subway line in the city, which is exponentially worsened by it's bizarre, unexplainable faux wood paneling that lines every train. You can only imagine that this design decision was made to make the subway feel less sterile and more homely, but the constant stench of piss and homeless people puking sort of ruins that idea. Riding the Yellow Line makes you feel like you're at your grandma's house every single time you ride it, if your grandma's house was in Jaywalker Plain."
str_yellow_subway_station_description = "It's absolutely fucking disgusting. By far the worst subway line, the Yellow Line can't keep it's terrible interior design choices contained to its actual trains. Even in its terminals, the faux wood paneling clashes with every other aesthetic element present. It's ghastly ceilings have turned a delightful piss-soaked shade of faded white. It's bizarre mixture of homely decorations and completely dilapidated state makes you oddly beguiled in a way. How did they fuck up the Yellow Line so bad? The world may never know."
str_subway_connecting_sentence = "Below it, on a lower level of the station, is a {} line terminal."

# TODO: Add descriptions for each outskirts district.
str_generic_outskirts_description = "It's a wasteland, devoid of all life except for slime beasts."



context_slimeoidheart = 'slimeoidheart'
context_slimeoidbottle = 'slimeoidbottle'
context_slimeoidfood = 'slimeoidfood'
context_wrappingpaper = 'wrappingpaper'

# Item vendor names.
vendor_bar = 'bar'	#rate of non-mtn dew drinks are 100 slime to 9 hunger
vendor_pizzahut = 'Pizza Hut'	#rate of fc vendors are 100 slime to 10 hunger
vendor_tacobell = 'Taco Bell'
vendor_kfc = 'KFC'
vendor_mtndew = 'Mtn Dew Fountain'
vendor_vendingmachine = 'vending machine'
vendor_seafood = 'Red Mobster Seafood'	#rate of seafood is 100 slime to 9 hunger
vendor_diner = "Smoker's Cough"	#rate of drinks are 100 slime to 15 hunger
vendor_beachresort = "Beach Resort" #Just features clones from the Speakeasy and Red Mobster
vendor_countryclub = "Country Club" #Just features clones from the Speakeasy and Red Mobster
vendor_farm = "Farm" #contains all the vegetables you can !reap
vendor_bazaar = "bazaar"
vendor_college = "College" #You can buy game guides from either of the colleges
vendor_glocksburycomics = "Glocksbury Comics" #Repels and trading cards are sold here
vendor_slimypersuits = "Slimy Persuits" #You can buy candy from here
vendor_greencakecafe = "Green Cake Cafe" #Brunch foods

item_id_slimepoudrin = 'slimepoudrin'
item_id_monstersoup = 'monstersoup'
item_id_doublestuffedcrust = 'doublestuffedcrust'
item_id_quadruplestuffedcrust = 'quadruplestuffedcrust'
item_id_octuplestuffedcrust = "octuplestuffedcrust"
item_id_sexdecuplestuffedcrust = "sexdecuplestuffedcrust"
item_id_duotrigintuplestuffedcrust = "duotrigintuplestuffedcrust"
item_id_quattuorsexagintuplestuffedcrust = "quattuorsexagintuplestuffedcrust"
item_id_forbiddenstuffedcrust = "theforbiddenstuffedcrust"
item_id_forbidden111 = "theforbiddenoneoneone"
item_id_tradingcardpack = "tradingcardpack"
item_id_stick = "stick"
item_id_gameguide = "gameguide"
item_id_juviegradefuckenergybodyspray = "juviegradefuckenergybodyspray"
item_id_superduperfuckenergybodyspray = "superduperfuckenergybodyspray"
item_id_gmaxfuckenergybodyspray = "gmaxfuckenergybodyspray"
item_id_costumekit = "costumekit"
item_id_doublehalloweengrist = "doublehalloweengrist"
item_id_whitelineticket = "ticket"
item_id_seaweedjoint = "seaweedjoint"
item_id_megaslimewrappingpaper = "megaslimewrappingpaper"
item_id_greeneyesslimedragonwrappingpaper = "greeneyesslimedragonwrappingpaper"
item_id_phoebuswrappingpaper = "phoebuswrappingpaper"
item_id_slimeheartswrappingpaper = "slimeheartswrappingpaper"
item_id_slimeskullswrappingpaper = "slimeskullswrappingpaper"
item_id_shermanwrappingpaper = "shermanwrappingpaper"
item_id_slimecorpwrappingpaper = "slimecorpwrappingpaper"
item_id_pickaxewrappingpaper = "pickaxewrappingpaper"
item_id_munchywrappingpaper = "munchywrappingpaper"
item_id_benwrappingpaper = "benwrappingpaper"
item_id_gellphone = "gellphone"
item_id_royaltypoudrin = "royaltypoudrin"

item_id_faggot = "faggot"
item_id_doublefaggot = "doublefaggot"

item_id_dinoslimemeat = "dinoslimemeat"
item_id_dinoslimesteak = "dinoslimesteak"

#SLIMERNALIA
item_id_sigillaria = "sigillaria"

#candy ids
item_id_paradoxchocs = "paradoxchocs"
item_id_licoricelobsters = "licoricelobsters"
item_id_chocolateslimecorpbadges = "chocolateslimecorpbadges"
item_id_munchies = "munchies"
item_id_snipercannon = "snipercannon"
item_id_twixten = "twixten"
item_id_slimybears = "slimybears"
item_id_marsbar = "marsbar"
item_id_magickspatchkids = "magickspatchkids"
item_id_atms = "atms"
item_id_seanis = "seanis"
item_id_candybungis = "candybungis"
item_id_turstwerthers = "turstwerthers"
item_id_poudrinpops = "poudrinpops"
item_id_juvieranchers = "juvieranchers"
item_id_krakel = "krakel"
item_id_swedishbassedgods = "swedishbassedgods"
item_id_bustahfingers = "bustahfingers"
item_id_endlesswarheads = "endlesswarheads"
item_id_n8heads = "n8heads"
item_id_strauberryshortcakes = "strauberryshortcakes"
item_id_chutzpahcherries = "chutzpahcherries"
item_id_n3crunch = "n3crunch"
item_id_slimesours = "slimesours"

#slimeoid food
item_id_fragilecandy = "fragilecandy" #+chutzpah -grit
item_id_rigidcandy = "rigidcandy" #+grit -chutzpah
item_id_recklesscandy = "recklesscandy" #+moxie -grit
item_id_reservedcandy = "reservedcandy" #+grit -moxie
item_id_bluntcandy = "bluntcandy" #+moxie -chutzpah
item_id_insidiouscandy = "insidiouscandy" #+chutzpah -moxie

#vegetable ids
item_id_poketubers = "poketubers"
item_id_pulpgourds = "pulpgourds"
item_id_sourpotatoes = "sourpotatoes"
item_id_bloodcabbages = "bloodcabbages"
item_id_joybeans = "joybeans"
item_id_purplekilliflower = "purplekilliflower"
item_id_razornuts = "razornuts"
item_id_pawpaw = "pawpaw"
item_id_sludgeberries = "sludgeberries"
item_id_suganmanuts = "suganmanuts"
item_id_pinkrowddishes = "pinkrowddishes"
item_id_dankwheat = "dankwheat"
item_id_brightshade = "brightshade"
item_id_blacklimes = "blacklimes"
item_id_phosphorpoppies = "phosphorpoppies"
item_id_direapples = "direapples"

#weapon ids
weapon_id_revolver = 'revolver'
weapon_id_dualpistols = 'dualpistols'
weapon_id_shotgun = 'shotgun'
weapon_id_rifle = 'rifle'
weapon_id_smg = 'smg'
weapon_id_minigun = 'minigun'
weapon_id_bat = 'bat'
weapon_id_brassknuckles = 'brassknuckles'
weapon_id_katana = 'katana'
weapon_id_broadsword = 'broadsword'
weapon_id_nunchucks = 'nun-chucks'
weapon_id_scythe = 'scythe'
weapon_id_yoyo = 'yo-yo'
weapon_id_knives = 'knives'
weapon_id_molotov = 'molotov'
weapon_id_grenades = 'grenades'
weapon_id_garrote = 'garrote'
weapon_id_pickaxe = 'pickaxe'
weapon_id_bass = 'bass'
weapon_id_umbrella = 'umbrella'
weapon_id_bow = 'bow'
weapon_id_dclaw = 'dclaw'
theforbiddenoneoneone_desc = "This card that you hold in your hands contains an indescribably powerful being known simply " \
	"as The Forbidden {emote_111}. It is an unimaginable horror, a beast of such supreme might that wields " \
	"destructive capabilities that is beyond any human’s true understanding. And for its power, " \
	"the very fabric of reality conspired to dismember and seal The Forbidden {emote_111} away into the most " \
	"obscured, nightmarish cages conceivable: trading cards. Now you, foolish mortal, have revived " \
	"this ancient evil. Once again this slime-starved beast may roam the lands, obliterating all life " \
	"that dares to evolve."
forbiddenstuffedcrust_eat = "Dough, pepperoni, grease, marinara and cheese. Those five simple ingredients folded into one " \
	"another thousands upon thousands of times, and multiplied in quantity exponentially over the " \
	"course of weeks. That is what has begat this, an affront to god and man. To explain the ramifications " \
	"of the mere existence of this pizza is pointless. You could not comprehend the amount of temporal " \
	"and spatial destruction you have caused this day. The very fabric of space and time cry out in agony, " \
	"bleeding from the mortal wound you have inflicted upon them. Imbued into every molecule of this " \
	"monstrosity is exactly one word, one thought, one concept. Hate. Hate for conscious life, in concept. " \
	"Deep inside of this pizza, a primordial evil is sealed away for it’s sheer destructive power. Escaped " \
	"from its original prison only to be caged in another. To release, all one needs to do is do exactly " \
	"what you are doing. That is to say, eat a slice. They don’t even need to finish it, as after the very " \
	"first bite it will be free. Go on. It’s about that time, isn’t it? You gaze upon this, the epitome of " \
	"existential dread that you imprudently smelted, and despair. Tepidly, you bring the first slice to your " \
	"tongue, letting the melted cheese drizzle unto your awaiting tongue. There are no screams. There is no time. " \
	"There is only discord. And then, nothing."
forbiddenstuffedcrust_desc = "What are you waiting for? You’ve come this far, why do you hesitate? Useless. Useless, useless, useless. " \
	"Escaping your purpose is impossible. Not destiny, purpose. You were never truly alive, never truly free. " \
	"Your one, singular purpose, that you were created to fulfill, is on the precipice of completion. You’ve " \
	"sought that absolution all your life, haven’t you? You’ve begged to be given the answer, to be shown that " \
	"you and your family and your friends were put on this planet for a purpose. Well, here it is. Here is what " \
	"you were meant to do. Don’t fight it. It’s useless. Useless, useless, useless. Don’t keep the universe waiting. " \
	"It’s ready to die. Slather it in some low-quality marinara, toss it up into the air like in the old movies, and " \
	"shove it into the oven, to teach it the true meaning of heat death. Eat a slice of that motherfucking pizza."

# List of normal items.
item_list = [
	EwGeneralItem(
		id_item = item_id_slimepoudrin,
		alias = [
			"poudrin",
		],
		context = "poudrin",
		str_name = "Slime Poudrin",
		str_desc = "A dense, crystalized chunk of precious slime.",
		acquisition = acquisition_mining,
	),
	EwGeneralItem(
		id_item = "whitedye",
		context = "dye",
		str_name = "White Dye",
		str_desc = "A small vial of white dye.",
		acquisition = acquisition_milling,
		ingredients = item_id_poketubers,
	),
	EwGeneralItem(
		id_item = "yellowdye",
		context = "dye",
		str_name = "Yellow Dye",
		str_desc = "A small vial of yellow dye.",
		acquisition = acquisition_milling,
		ingredients = item_id_pulpgourds,
	),

	EwGeneralItem(
		id_item = "orangedye",
		context = "dye",
		str_name = "Orange Dye",
		str_desc = "A small vial of orange dye.",
		acquisition = acquisition_milling,
		ingredients = item_id_sourpotatoes,
	),
	EwGeneralItem(
		id_item = "reddye",
		context = "dye",
		str_name = "Red Dye",
		str_desc = "A small vial of red dye.",
		acquisition = acquisition_milling,
		ingredients = item_id_bloodcabbages,
	),
	EwGeneralItem(
		id_item = "magentadye",
		context = "dye",
		str_name = "Magenta Dye",
		str_desc = "A small vial of magenta dye.",
		acquisition = acquisition_milling,
		ingredients = item_id_joybeans,
	),
	EwGeneralItem(
		id_item = "purpledye",
		context = "dye",
		str_name = "Purple Dye",
		str_desc = "A small vial of purple dye.",
		acquisition = acquisition_milling,
		ingredients = item_id_purplekilliflower,
	),
	EwGeneralItem(
		id_item = "bluedye",
		context = "dye",
		str_name = "Blue Dye",
		str_desc = "A small vial of blue dye.",
		acquisition = acquisition_milling,
		ingredients = item_id_razornuts,
	),
	EwGeneralItem(
		id_item = "greendye",
		context = "dye",
		str_name = "Green Dye",
		str_desc = "A small vial of green dye.",
		acquisition = acquisition_milling,
		ingredients = item_id_pawpaw,
	),
	EwGeneralItem(
		id_item = "tealdye",
		context = "dye",
		str_name = "Teal Dye",
		str_desc = "A small vial of teal dye.",
		acquisition = acquisition_milling,
		ingredients = item_id_sludgeberries,
	),
	EwGeneralItem(
		id_item = "rainbowdye",
		context = "dye",
		str_name = "***Rainbow Dye!!***",
		str_desc = "***A small vial of Rainbow dye!!***",
		acquisition = acquisition_milling,
		ingredients = item_id_suganmanuts,
	),
	EwGeneralItem(
		id_item = "pinkdye",
		context = "dye",
		str_name = "Pink Dye",
		str_desc = "A small vial of pink dye.",
		acquisition = acquisition_milling,
		ingredients = item_id_pinkrowddishes,
	),
	EwGeneralItem(
		id_item = "greydye",
		context = "dye",
		str_name = "Grey Dye",
		str_desc = "A small vial of grey dye.",
		acquisition = acquisition_milling,
		ingredients = item_id_dankwheat,
	),
	EwGeneralItem(
		id_item = "cobaltdye",
		context = "dye",
		str_name = "Cobalt Dye",
		str_desc = "A small vial of cobalt dye.",
		acquisition = acquisition_milling,
		ingredients = item_id_brightshade,
	),
	EwGeneralItem(
		id_item = "blackdye",
		context = "dye",
		str_name = "Black Dye",
		str_desc = "A small vial of black dye.",
		acquisition = acquisition_milling,
		ingredients = item_id_blacklimes,
	),
	EwGeneralItem(
		id_item = "limedye",
		context = "dye",
		str_name = "Lime Dye",
		str_desc = "A small vial of lime dye.",
		acquisition = acquisition_milling,
		ingredients = item_id_phosphorpoppies,
	),
	EwGeneralItem(
		id_item = "cyandye",
		context = "dye",
		str_name = "Cyan Dye",
		str_desc = "A small vial of cyan dye.",
		acquisition = acquisition_milling,
		ingredients = item_id_direapples,
	),
	EwGeneralItem(
		id_item = item_id_tradingcardpack,
		alias = [
			"tcp", # DUDE LOL JUST LIKE THE PROCRASTINATORS HOLY FUCKING SHIT I'M PISSING MYSELF RN
			"tradingcard",
			"trading",
			"card",
			"cardpack",
			"pack"
		],
		str_name = "Trading Cards",
		str_desc = "A pack of trading cards",
		price = 50000,
		vendors = [vendor_bazaar, vendor_glocksburycomics],
	),
	EwGeneralItem(
		id_item = "rightleg",
		context = 'slimexodia',
		str_name = "The Right Leg of The Forbidden {}".format(emote_111),
		str_desc = "One of the extremely rare, legendary Forbidden {} cards. Gazing upon the card and its accompanying "
				   "intense holographic sheen without the proper eyewear can have disastrous consequences. Yet, you do it anyway. "
				   "It’s just too beautiful not to.".format(emote_111),
	),
	EwGeneralItem(
		id_item = "leftleg",
		context = 'slimexodia',
		str_name = "Left Leg of The Forbidden {}".format(emote_111),
		str_desc = "One of the extremely rare, legendary Forbidden {} cards. Gazing upon the card and its accompanying "
				   "intense holographic sheen without the proper eyewear can have disastrous consequences. Yet, you do it anyway. "
				   "It’s just too beautiful not to.".format(emote_111),
	),
	EwGeneralItem(
		id_item = "slimexodia",
		context = 'slimexodia',
		str_name = "Slimexodia The Forbidden {}".format(emote_111),
		str_desc = "The centerpiece of the extremely rare, legendary Forbidden {} cards. Gazing upon the card and its accompanying "
				   "intense holographic sheen without the proper eyewear can have disastrous consequences. Yet, you do it anyway. "
				   "It’s just too beautiful not to.".format(emote_111),
	),
	EwGeneralItem(
		id_item = "rightarm",
		context = 'slimexodia',
		str_name = "Right Arm of The Forbidden {}".format(emote_111),
		str_desc = "One of the extremely rare, legendary Forbidden {} cards. Gazing upon the card and its accompanying "
				   "intense holographic sheen without the proper eyewear can have disastrous consequences. Yet, you do it anyway. "
				   "It’s just too beautiful not to.".format(emote_111),
	),
	EwGeneralItem(
		id_item = "leftarm",
		context = 'slimexodia',
		str_name = "Left Arm of The Forbidden {}".format(emote_111),
		str_desc = "One of the extremely rare, legendary Forbidden {} cards. Gazing upon the card and its accompanying "
				   "intense holographic sheen without the proper eyewear can have disastrous consequences. Yet, you do it anyway. "
				   "It’s just too beautiful not to.".format(emote_111),
	),
	EwGeneralItem(
		id_item = item_id_forbidden111,
		str_name = "The Forbidden {}".format(emote_111),
		str_desc = theforbiddenoneoneone_desc.format(emote_111 = emote_111),
		acquisition = acquisition_smelting
	),
	EwGeneralItem(
		id_item = item_id_stick,
		str_name = "stick",
		str_desc = "It’s just some useless, dumb stick.",
		acquisition = acquisition_milling,
		ingredients = item_id_direapples,
	),
	EwGeneralItem(
		id_item = item_id_faggot,
		str_name = "faggot",
		str_desc = "Wow, incredible! We’ve evolved from one dumb stick to several, all tied together for the sake of a retarded puesdo-pun! Truly, ENDLESS WAR has reached its peak. It’s all downhill from here, folks.",
		acquisition = acquisition_smelting
	),
	EwGeneralItem(
		id_item = item_id_doublefaggot,
		str_name = "double faggot",
		str_desc = "It's just a bundle of sticks, twice as long and hard as the two combined to form it. Hey, what are you chucklin' at?.",
		acquisition = acquisition_smelting
	),
	EwGeneralItem(
		id_item = "seaweed",
		str_name = "Seaweed",
		str_desc = "OH GOD IT'S A FUCKING SEAWEED!",
		acquisition = acquisition_bartering,
		ingredients = "generic",
		context = 10,
	),
	EwGeneralItem(
		id_item = "oldboot",
		str_name = "Old Boot",
		str_desc = "OH GOD IT'S A FUCKING OLD BOOT!",
		acquisition = acquisition_bartering,
		ingredients = "generic",
		context = 10,
	),
	EwGeneralItem(
		id_item = "tincan",
		str_name = "Tin Can",
		str_desc = "OH GOD IT'S A FUCKING TIN CAN!",
		acquisition = acquisition_bartering,
		ingredients = "generic",
		context = 10,
	),
	EwGeneralItem(
		id_item = "leather",
		str_name = "Leather",
		str_desc = "A strip of leather.",
		acquisition = acquisition_smelting,
		ingredients = "generic",
		context = 10,
	),
	EwGeneralItem(
		id_item = "ironingot",
		str_name = "Iron Ingot",
		str_desc = "A bar of iron",
		acquisition = acquisition_smelting,
		ingredients = "generic",
		context = 10,
	),
	EwGeneralItem(
		id_item = "dragonsoul",
		str_name = "Dragon Soul",
		str_desc = "A fearsome dragon soul, pried from the corpse of a Green Eyes Slime Dragon. It's just like Dark Souls! Wait... *just like* Dark Souls??? Maybe you can use this for something.",
		context = 'dragon soul',
	),
	EwGeneralItem(
		id_item = "monsterbones",
		str_name = "Monster Bones",
		str_desc = "A large set of bones, taken from the monsters that roam the outskirts. Tastes meaty.",
		context = 'monster bone',
	),
	EwGeneralItem(
		id_item = "bloodstone",
		str_name = "blood stone",
		str_desc = "Formed from the cracking of monster bones, it glistens in your palm with the screams of those whos bones comprise it. Perhaps it will be of use one day.",
		context = 'blood stone',
		acquisition = acquisition_smelting
	),
	EwGeneralItem(
		id_item = "tanningknife",
		context = "tool",
		str_name = "Tanning Knife",
		str_desc = "A tanning knife",
		acquisition = acquisition_smelting,
	),

	EwGeneralItem(
		id_item = "string",
		str_name = "string",
		str_desc = "It’s just some string.",
		acquisition = acquisition_bartering,
		ingredients = "generic",
		context = 60,
	),
	EwGeneralItem(
		id_item = item_id_gameguide,
		alias = [
			"gg",
			"gameguide",
			"gamergate",
		],
		str_name = "The official unofficial ENDLESS WAR Game Guide",
		str_desc = "A guide on all the game mechanics found in ENDLESS WAR. Use the !help command to crack it open.",
		vendors = [vendor_college],
		price = 10000,
	),
	EwGeneralItem(
		id_item=item_id_juviegradefuckenergybodyspray,
		context='repel',
		alias=[
			"regular body spray",
			"regbs",
			"regular repel",
			"juvie",
			"juviegrade",
			"juvie grade",
			"repel",
			"body spray",
			"bodyspray",
			"bs",
		],
		str_name="Juvie Grade FUCK ENERGY Body Spray",
		str_desc="A canister of perfume. Somehow doubles as a slime beast repellant. The label on the back says it lasts for three hours.",
		vendors=[vendor_glocksburycomics],
		price=10000,
	),
	EwGeneralItem(
		id_item = item_id_superduperfuckenergybodyspray,
		context = 'superrepel',
		alias = [
			"superrepel",
			"super repel",
			"super duper body spray",
			"superbodyspray",
			"superduperbodyspray",
			"sdbs",
			"super",
		],
		str_name = "Super Duper FUCK ENERGY Body Spray",
		str_desc = "A canister of perfume. Somehow doubles as a slime beast repellant. The label on the back says it lasts for six hours.",
		vendors = [vendor_glocksburycomics],
		price = 20000,
	),
	EwGeneralItem(
		id_item = item_id_gmaxfuckenergybodyspray,
		context = 'maxrepel',
		alias = [
			"maxrepel",
			"max repel",
			"g-max body spray",
			"gmaxbodyspray",
			"gmbs",
			"gmax",
			"g-max",
		],
		str_name = "G-Max FUCK ENERGY Body Spray",
		str_desc = "A canister of perfume. Somehow doubles as a slime beast repellant. The label on the back says it lasts for twelve hours.",
		vendors = [vendor_glocksburycomics],
		price = 40000,
	),
	EwGeneralItem(
		id_item = item_id_costumekit,
		context = 'costumekit',
		alias = [
			"costumekit",
			"ck",
			"fursuit",
			"kit",
			"costume",
		],
		str_name = "Double Halloween Costume Kit",
		str_desc = "A package of all the necessary tools and fabrics needed to make the Double Halloween costume of your dreams.",
		price = 50000,
	),
	EwGeneralItem(
		id_item = item_id_doublehalloweengrist,
		context = 'dhgrist',
		alias = [
			"grist"
		],
		str_name = "Double Halloween Grist",
		str_desc = "A mush of finely ground candy. Perhaps it can be forged into something special?",
	),
	EwGeneralItem(
		id_item = item_id_whitelineticket,
		context = 'wlticket',
		alias = [
			"tickettohell"
		],
		str_name = "Ticket to the White Line",
		str_desc = "A large assortment of candy molded into one unholy voucher for access into the underworld. Use it in a White Line subway station... ***IF YOU DARE!!***",
		acquisition=acquisition_smelting,
	),
	EwGeneralItem(
		id_item=item_id_megaslimewrappingpaper,
		context=context_wrappingpaper,
		alias=[
			"mswp"
		],
		str_name="Megaslime Wrapping Paper",
		str_desc="Wrapping paper with Megaslimes plastered all over it. Blaargh!",
	#	vendors=[vendor_glocksburycomics],
		price = 1000,
	),
	EwGeneralItem(
		id_item=item_id_greeneyesslimedragonwrappingpaper,
		context=context_wrappingpaper,
		alias=[
			"gesdwp"
		],
		str_name="Green Eyes Slime Dragon Wrapping Paper",
		str_desc="Wrapping paper with many images of the Green Eyes Slime Dragon printed on it. Powerful...",
	#	vendors=[vendor_glocksburycomics],
		price = 1000,
	),
	EwGeneralItem(
		id_item = item_id_phoebuswrappingpaper,
		context = context_wrappingpaper,
		alias = [
			"pwp"
		],
		str_name = "Phoebus Wrapping Paper",
		str_desc = "A set of wrapping paper with Slime Invictus on it. Yo, Slimernalia!",
	#	vendors = [vendor_glocksburycomics],
		price = 1000,
	),
	EwGeneralItem(
		id_item = item_id_slimeheartswrappingpaper,
		context = context_wrappingpaper,
		alias = [
			"shwp"
		],
		str_name = "Slime Hearts Wrapping Paper",
		str_desc = "Wrapping paper decorated with slime hearts. Cute!!",
	#	vendors = [vendor_glocksburycomics],
		price = 1000,
	),
	EwGeneralItem(
		id_item = item_id_slimeskullswrappingpaper,
		context = context_wrappingpaper,
		alias = [
			"sswp"
		],
		str_name = "Slime Skulls Wrapping Paper",
		str_desc = "A roll of wrapping paper with Slime Skulls stamped all over it. Spooky...",
	#	vendors = [vendor_glocksburycomics],
		price = 1000,
	),
	EwGeneralItem(
		id_item = item_id_shermanwrappingpaper,
		context = context_wrappingpaper,
		alias = [
			"swp"
		],
		str_name = "Sherman Wrapping Paper",
		str_desc = "Wrapping paper with Sherman, the SlimeCorp salaryman etched into it. Jesus Christ, how horrifying!",
	#	vendors = [vendor_glocksburycomics],
		price = 1000,
	),
	EwGeneralItem(
		id_item = item_id_slimecorpwrappingpaper,
		context = context_wrappingpaper,
		alias = [
			"scwp"
		],
		str_name = "SlimeCorp Wrapping Paper",
		str_desc = "A set of wrapping paper with that accursed logo printed all over it. What sort of corporate bootlicker would wrap a gift in this?",
	#	vendors = [vendor_glocksburycomics],
		price = 1000,
	),
	EwGeneralItem(
		id_item = item_id_pickaxewrappingpaper,
		context = context_wrappingpaper,
		alias = [
			"pawp"
		],
		str_name = "Pickaxe Wrapping Paper",
		str_desc = "A roll of wrapping paper with a bunch of pickaxes depicted on it. Perfect for Juvies who love to toil away in the mines.",
	#	vendors = [vendor_glocksburycomics],
		price = 1000,
	),
	EwGeneralItem(
		id_item = item_id_benwrappingpaper,
		context = context_wrappingpaper,
		alias = [
			"bwp"
		],
		str_name = "Ben Wrapping Paper",
		str_desc = "Wrapping paper with the Cop Killer printed on it. !dab !dab !dab",
	#	vendors = [vendor_glocksburycomics],
		price = 1000,
	),
	EwGeneralItem(
		id_item = item_id_munchywrappingpaper,
		context = context_wrappingpaper,
		alias = [
			"mwp"
		],
		str_name = "Munchy Wrapping Paper",
		str_desc = "Wrapping paper with the Rowdy Fucker printed on it. !THRASH !THRASH !THRASH",
	#	vendors = [vendor_glocksburycomics],
		price = 1000,
	),
	EwGeneralItem(
		id_item = item_id_gellphone,
		context = 'gellphone',
		alias = [
			"gell",
			"phone",
			"cellphone",
			"flipphone",
			"nokia"
		],
		str_name = "Gellphone",
		str_desc = "A cell phone manufactured by SlimeCorp. Turning it on allows you to access various apps and games.",
		vendors = [vendor_bazaar],
		price = 1000000
	),
	EwSlimeoidFood(
		id_item = item_id_fragilecandy,
		alias = [
			"fragile",
		],
		str_name = "Fragile Candy",
		str_desc = "Increases Chutzpah and decreases Grit, when fed to a slimeoid.",
		vendors = [vendor_glocksburycomics, vendor_slimypersuits],
		price = 100000,
		increase = slimeoid_stat_chutzpah,
		decrease = slimeoid_stat_grit,
	),
	EwSlimeoidFood(
		id_item = item_id_rigidcandy,
		alias = [
			"rigid",
		],
		str_name = "Rigid Candy",
		str_desc = "Increases Grit and decreases Chutzpah, when fed to a slimeoid.",
		vendors = [vendor_glocksburycomics, vendor_slimypersuits],
		price = 100000,
		increase = slimeoid_stat_grit,
		decrease = slimeoid_stat_chutzpah,
	),
	EwSlimeoidFood(
		id_item = item_id_reservedcandy,
		alias = [
			"reserved",
		],
		str_name = "Reserved Candy",
		str_desc = "Increases Grit and decreases Moxie, when fed to a slimeoid.",
		vendors = [vendor_glocksburycomics, vendor_slimypersuits],
		price = 100000,
		increase = slimeoid_stat_grit,
		decrease = slimeoid_stat_moxie,
	),
	EwSlimeoidFood(
		id_item = item_id_recklesscandy,
		alias = [
			"reckless",
		],
		str_name = "Reckless Candy",
		str_desc = "Increases Moxie and decreases Grit, when fed to a slimeoid.",
		vendors = [vendor_glocksburycomics, vendor_slimypersuits],
		price = 100000,
		increase = slimeoid_stat_moxie,
		decrease = slimeoid_stat_grit,
	),
	EwSlimeoidFood(
		id_item = item_id_insidiouscandy,
		alias = [
			"insidious",
		],
		str_name = "Insidious Candy",
		str_desc = "Increases Chutzpah and decreases Moxie, when fed to a slimeoid.",
		vendors = [vendor_glocksburycomics, vendor_slimypersuits],
		price = 100000,
		increase = slimeoid_stat_chutzpah,
		decrease = slimeoid_stat_moxie,
	),
	EwSlimeoidFood(
		id_item = item_id_bluntcandy,
		alias = [
			"blunt",
		],
		str_name = "Blunt Candy",
		str_desc = "Increases Moxie and decreases Chutzpah, when fed to a slimeoid.",
		vendors = [vendor_glocksburycomics, vendor_slimypersuits],
		price = 100000,
		increase = slimeoid_stat_moxie,
		decrease = slimeoid_stat_chutzpah,
	),
]
item_list += ewdebug.debugitem_set

debugitem = ewdebug.debugitem

# A map of id_item to EwGeneralItem objects.
item_map = {}

# A list of item names
item_names = []

# list of dyes you're able to saturate your Slimeoid with
dye_list = []
dye_map = {}
# seperate the dyes from the other normal items
for c in item_list:
	if c.context != "dye":
		pass
	else:
		dye_list.append(c)
		dye_map[c.str_name] = c.id_item








# Attacking type effects
def atf_fangs(ctn = None):
	# Reskin of dual pistols

	aim = (random.randrange(10) + 1)
	ctn.sap_damage = 1

	if aim == (1 + int(10 * ctn.miss_mod)):
		ctn.miss = True
		ctn.slimes_damage = 0
	elif aim == (10 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2

def atf_talons(ctn = None):
	# Reskin of katana

	ctn.miss = False
	ctn.slimes_damage = int(0.85 * ctn.slimes_damage)
	ctn.sap_damage = 0
	ctn.sap_ignored = 10

	if (random.randrange(10) + 1) == (10 + int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2.1

def atf_raiderscythe(ctn = None):
	# Reskin of scythe

	ctn.enemy_data.change_slimes(n = (-ctn.slimes_spent * 0.33), source = source_self_damage)
	ctn.slimes_damage = int(ctn.slimes_damage * 1.25)
	aim = (random.randrange(10) + 1)
	ctn.sap_damage = 0
	ctn.sap_ignored = 5

	if aim <= (2 + int(10 * ctn.miss_mod)):
		ctn.miss = True
		ctn.slimes_damage = 0
	elif aim >= (9 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2

def atf_gunkshot(ctn = None):
	# Reskin of rifle

	aim = (random.randrange(10) + 1)
	ctn.sap_damage = 2

	if aim <= (2 + int(10 * ctn.miss_mod)):
		ctn.miss = True
		ctn.slimes_damage = 0
	elif aim >= (9 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2

def atf_tusks(ctn = None):
	# Reskin of bat

	aim = (random.randrange(21) - 10)
	ctn.sap_damage = 3
	if aim <= (-9 + int(21 * ctn.miss_mod)):
		ctn.miss = True
		ctn.slimes_damage = 0

	ctn.slimes_damage = int(ctn.slimes_damage * (1 + (aim / 10)))

	if aim >= (9 - int(21 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage = int(ctn.slimes_damage * 1.5)

def atf_molotovbreath(ctn = None):
	# Reskin of molotov

	dmg = ctn.slimes_damage
	ctn.slimes_damage = int(ctn.slimes_damage * 0.75)
	ctn.sap_damage = 0
	ctn.sap_ignored = 10

	aim = (random.randrange(10) + 1)

	#ctn.bystander_damage = dmg * 0.5

	if aim <= (2 + int(10 * ctn.miss_mod)):
		ctn.backfire = True
		ctn.backfire_damage = dmg

	elif aim == (3 + int(10 * ctn.miss_mod)):
		ctn.miss = True
		ctn.slimes_damage = 0

	elif aim == (10 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2

def atf_armcannon(ctn = None):
	dmg = ctn.slimes_damage
	ctn.sap_damage = 2

	aim = (random.randrange(20) + 1)

	if aim <= (2 + int(20 * ctn.miss_mod)):
		ctn.miss = True

	if aim == (20 - int(20 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 3


def atf_axe(ctn=None):
	ctn.slimes_damage *= 0.7
	aim = (random.randrange(10) + 1)

	if aim <= (4 + int(10 * ctn.miss_mod)):
		ctn.miss = True

	if aim == (10 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2


def atf_hooves(ctn=None):
	ctn.slimes_damage *= 0.4
	aim = (random.randrange(30) + 1)

	if aim <= (5 + int(30 * ctn.miss_mod)):
		ctn.miss = True

	if aim > (25 - int(30 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2

# All enemy attacking types in the game.
enemy_attack_type_list = [
	EwAttackType( # 1
		id_type = "fangs",
		str_crit = "**Critical Hit!** {name_enemy} sinks their teeth deep into {name_target}!",
		str_miss = "**{name_enemy} missed!** Their maw snaps shut!",
		#str_trauma_self = "You have bite marks littered throughout your body.",
		#str_trauma = "They have bite marks littered throughout their body.",
		str_kill = "{name_enemy} opens their jaw for one last bite right on {name_target}'s juicy neck. **CHOMP**. Blood gushes out of their arteries and onto the ground. {emote_skull}",
		str_killdescriptor = "mangled",
		str_damage = "{name_target} is bitten on the {hitzone}!!",
		fn_effect = atf_fangs
	),
	EwAttackType( # 2
		id_type = "talons",
		str_crit = "**Critical hit!!** {name_target} is slashed across the chest!!",
		str_miss = "**{name_enemy} missed!** Their wings flap in the air as they prepare for another strike!",
		#str_trauma_self = "A large section of scars litter your abdomen.",
		#str_trauma = "A large section of scars litter their abdomen.",
		str_kill = "In a fantastic display of avian savagery, {name_enemy}'s talons grip {name_target}'s stomach, rip open their flesh and tear their intestines to pieces. {emote_skull}",
		str_killdescriptor = "disembowled",
		str_damage = "{name_target} has their {hitzone} clawed at!!",
		fn_effect = atf_talons
	),
	EwAttackType( # 3
		id_type = "scythe",
		str_crit = "**Critical hit!!** {name_target} is carved by the wicked curved blade!",
		str_miss = "**MISS!!** {name_enemy}'s swings miss wide of the target!",
		#str_trauma_self = "You are wrapped tightly in bandages that hold your two halves together.",
		#str_trauma = "They are wrapped tightly in bandages that hold their two halves together.",
		str_kill = "**SLASHH!!** {name_enemy}'s scythe cleaves the air, and {name_target} staggers. A moment later, {name_target}'s torso topples off their waist. {emote_skull}",
		str_killdescriptor = "sliced in twain",
		str_damage = "{name_target} is cleaved through the {hitzone}!!",
		fn_effect = atf_raiderscythe
	),
	EwAttackType( # 4
		id_type = "gunk shot",
		str_crit = "**Critical hit!!** {name_target} is covered in a thick, gelatenous ooze!",
		str_miss = "**MISS!!** {name_enemy}'s gunk shot just barely missed the target!",
		#str_trauma_self = "Several locations on your body have decayed from the aftermath of horrific radiation.",
		#str_trauma = "Several locations on their body have decayed from the aftermath of horrific radiation.",
		str_kill = "**SPLOOSH!!** {name_enemy}'s gunk shot completely envelops {name_target}, boiling their flesh alive in a radiation that rivals the Elephant's Foot. Nothing but a charred husk remains. {emote_skull}",
		str_killdescriptor = "slimed on",
		str_damage = "{name_target} is coated in searing, acidic radiation on their {hitzone}!!",
		fn_effect = atf_gunkshot
	),
	EwAttackType( # 5
		id_type = "tusks",
		str_crit = "**Critical hit!!** {name_target} is smashed hard by {name_enemy}'s tusks!",
		str_miss = "**{name_enemy} missed!** Their tusks strike the ground, causing it to quake underneath!",
		#str_trauma_self = "You have one large scarred-over hole on your upper body.",
		#str_trauma = "They have one large scarred-over hole on their upper body.",
		str_kill = "**SHINK!!** {name_enemy}'s tusk rams right into your chest, impaling you right through your back! Moments later, you're thrusted out on to the ground, left to bleed profusely. {emote_skull}",
		str_killdescriptor = "pierced",
		str_damage = "{name_target} has tusks slammed into their {hitzone}!!",
		fn_effect = atf_tusks
	),
	EwAttackType( # 6
		id_type = "molotov breath",
		str_backfire = "**Oh the humanity!!** {name_enemy} tries to let out a breath of fire, but it combusts while still inside their maw!!",
		str_crit = "**Critical hit!!** {name_target} is char grilled by {name_enemy}'s barrage of molotov breath!",
		str_miss = "**{name_enemy} missed!** Their shot hits the ground instead, causing embers to shoot out in all directions!",
		#str_trauma_self = "You're wrapped in two layers of bandages. What skin is showing appears burn-scarred.",
		#str_trauma = "They're wrapped in two layers of bandages. What skin is showing appears burn-scarred.",
		str_kill = "In a last ditch effort, {name_enemy} breathes in deeply for an extra powerful shot of fire. Before you know it, your body is cooked alive like a rotisserie chicken. {emote_skull}",
		str_killdescriptor = "exploded",
		str_damage = "{name_target} is hit by a blast of fire on their {hitzone}!!",
		fn_effect = atf_molotovbreath
	),
	EwAttackType( # 7
		id_type = "arm cannon",
		str_crit = "**Critical hit!!** {name_target} has a clean hole shot through their chest by {name_enemy}'s bullet!",
		str_miss = "**{name_enemy} missed their target!** The stray bullet cleaves right into the ground!",
		#str_trauma_self = "There's a deep bruising right in the middle of your forehead.",
		#str_trauma = "There's a deep bruising right in the middle of their forehead.",
		str_kill = "{name_enemy} readies their crosshair right for your head and fires without hesitation. The force from the bullet is so powerful that when it lodges itself into your skull, it rips your head right off in the process. {emote_skull}",
		str_killdescriptor = "sniped",
		str_damage = "{name_target} has a bullet zoom right through their {hitzone}!!",
		fn_effect = atf_armcannon
	),
	EwAttackType( # 8
		id_type = "axe",
		str_crit = "**Critical hit!!** {name_target} is thoroughly cleaved by {name_enemy}'s axe!",
		str_miss = "**{name_enemy} missed!** The axe gives a loud **THUD** as it strikes the earth!",
		#str_trauma_self = "There's a hefty amount of bandages covering the top of your head",
		#str_trauma = "There's a hefty amount of bandages covering the top of their head",
		str_kill = "{name_enemy} lifts up their axe for one last swing. The wicked edge buries itself deep into your skull, cutting your brain in twain. {emote_skull}",
		str_killdescriptor = "axed",
		str_damage = "{name_target} is swung at right on their {hitzone}!!",
		fn_effect = atf_axe
	),
	EwAttackType( # 9
		id_type = "hooves",
		str_crit = "**Critical hit!!** {name_enemy} lays a savage hind-leg kick into {name_target}'s chest!",
		str_miss = "**WHOOSH!** {name_enemy}'s hooves just barely miss you!",
		#str_trauma_self = "Your chest is somewhat concave.",
		#str_trauma = "Their chest is somewhat concave.",
		str_kill = "{name_enemy} gallops right over your head, readying their hind legs just after landing. Before you can even ready your weapon, their legs are already planted right onto your chest. Your heart explodes. {emote_skull}",
		str_killdescriptor = "stomped",
		str_damage = "{name_target} is stomped all over their {hitzone}!!",
		fn_effect = atf_hooves
	),
]

# A map of id_type to EwAttackType objects.
attack_type_map = {}

# Populate attack type map.
for attack_type in enemy_attack_type_list:
	attack_type_map[attack_type.id_type] = attack_type


# stock ids
stock_kfc = "kfc"
stock_pizzahut = "pizzahut"
stock_tacobell = "tacobell"

# default stock rates
default_stock_market_rate = 1000
default_stock_exchange_rate = 1000000

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

vendor_stock_map = {
	vendor_kfc : stock_kfc,
	vendor_pizzahut : stock_pizzahut,
	vendor_tacobell : stock_tacobell
	}

fish_rarity_common = "common"
fish_rarity_uncommon = "uncommon"
fish_rarity_rare = "rare"
fish_rarity_promo = "promo"

fish_catchtime_rain = "rain"
fish_catchtime_night = "night"
fish_catchtime_day = "day"

fish_slime_freshwater = "freshwater"
fish_slime_saltwater = "saltwater"

fish_size_miniscule = "miniscule"
fish_size_small = "small"
fish_size_average = "average"
fish_size_big = "big"
fish_size_huge = "huge"
fish_size_colossal = "colossal"


bully_responses = [
	"You push {target_name} into a puddle of sludge, laughing at how hopelessly dirty they are.",
	"You hold {target_name} down and pull their underwear over their head. It looks like their neck's about to snap off, holy shit.",
	"You decide to give {target_name} a slime swirly in a nearby puddle. It's so shallow that they mostly get a faceful of gravel.",
	"You tie {target_name} to a tree and slap them around senselessly. You untie them once their face and belly bruise cherry red.",
	"You flag down a muscle car on the road and shout: \"HEY! {target_name} FUCKED YOUR WIFE!\" The good man parks on the side of the road and starts beating the everloving shit out them. {slimeoid} cowers in the corner, now scarred for life and afraid of dads.",
	"You pull on {target_name}'s hair, ripping some out and causing them to cry. They should fucking grow up.",
	"You reach into {target_name}'s shirt and give them a purple nurple. Man, these bullying tactics are getting kind of gay.",
	"You whip out your dick and pee on {target_name}'s wife. Fuck. That's a power move right there.",
	"You scream \"HEY {target_name}! NICE {cosmetic} YOU'RE WEARING! DID YOUR MOM BUY IT FOR YA?\"",
	"You grab {slimeoid} and give them a noogie. Just when {target_name} thinks this is all fun and games, you throw {slimeoid} into the street. They have a panic attack trying to get past all the traffic and back to safety."

]

cabinets_list = [
"This is a Zoombinis Logical Journey arcade cabinet.\nWait. This is an old PC game. Why the fuck would they port this to cabinet? Now you have to use the stick to move the mouse around. Oh well. Buyers remorse, you suppose. \nhttps://classicreload.com/win3x-logical-journey-of-the-zoombinis.html",
"This is a Cookie Clicker arcade cabinet.\n The huge cookie button on the front is pretty neat, but running it forever seems like it would crank your electricity bill. You know, if you had one.\nhttps://orteil.dashnet.org/cookieclicker/",
"This is a Poptropica arcade cabinet.\nI don't know who thought point and click platforming was a good idea, but this new control scheme is a godsend. \nhttps://www.poptropica.com/",
"This is a Frog Fractions arcade cabinet.\nThis cabinet's been lightly used. Looks like a remnant of some bar in Ponyville, what with all the ponytuber signatures on it. Eh, we can leave those well alone for now.\nhttps://kbhgames.com/game/frog-fractions",
"This is a Pokemon Showdown arcade cabinet.\nSouls, hearts, and eons of slime were won and lost on this legendary little number. Playing it on this rickety old thing somehow doesn't seem as suspenseful, though.\n https://pokemonshowdown.com/",
"This is a Madness: Accelerant arcade cabinet.\n If you've been to West Glocksbury the violence in here is a little old hat, but a lot of people have a soft spot for it.\nhttps://www.newgrounds.com/portal/view/512407",
"This is a Flanders Killer 6 arcade cabinet.\nClearly this is the greatest game the world has ever conceived.\nhttps://www.silvergames.com/en/flanders-killer-6",
"This is a Peasant's Quest arcade cabinet.\nThe struggles of the main guy here are a lot like what juvies go through: a rise to greatness, false hope, and inevitable worthless destruction. Onward!\nhttp://homestarrunner.com/disk4of12.html",
"This is a Super Mario 63 arcade cabinet.\nSince Reggie Fils-Amie is too fucking cowardly to set foot in NLACakaNM, we have to resort to bootleg merchandise. Relatively good bootlegs, but bootlegs nonetheless.\nhttps://www.newgrounds.com/portal/view/498969",
"This is a World's Hardest Game arcade cabinet.\nThere were countless stories of moms getting bankrupted because their kids dumped their money into these.\nhttps://www.coolmathgames.com/0-worlds-hardest-game "
]

browse_list = [
"You found a server slightly out of city limits. Looks like they don't care so much about slime or gang warfare, they just make art about other stuff. Unthinkable, but nonetheless fascinating.\nhttps://discord.gg/TAQukUe",
"Ah, how we forget the sports. Vandal Park's rec center ads have always felt like a big distraction from shooting rival gang members in the face, but maybe it could be fun! This one's shilling their TF2 and Ace of Spades sections, there seem to be many others.\n https://discord.gg/X6TB5uP",
"Looks like the Cop Killer has a coven of people someplace outside NLACakaNM, kind of like a summer home or the late stages of a cult operation. Either way, seems interesting.\nhttps://discordapp.com/invite/j6xP5MB ",
"Pokemon Go doesn't seem like an option in this city without a dedicated support group like this. If people went alone, I'm pretty certain they'd get ganked or eaten by secreatures.\nhttps://discord.gg/QbDqEFU",
"Wait a minute. This doesn't seem quite right. Let's not click this one. \nhttps://discord.gg/mtSRXek",
"A young Milwaukee citizen stands in her room. Today is a very important day, though as circumstances would have it, she has momentarily forgotten about the exit. But like hell that's gonna stop her, or her name isn't...\nhttps://discord.gg/EkCMmGn",
"Gangs with wiki pages. I never thought I'd see the day. This place lets you doxx your friends to the NLACakaNM Police Department by compiling their backgrounds and posting it on the internet. They're always looking for writers, so knock yourself out.\nhttps://discord.gg/z5mvCfS",
"You stumble across an old ARG server. It's since been abandoned, but it's an interesting little piece of history nonetheless.\nhttps://discord.gg/9nwaMC",
"You find a group of visionaries who have turned hunting into a business. Personally, you wouldn't have gone with the LARPy high-fantasy branding, but to each their own.\nhttps://discord.gg/Rw2wCYT",
"Killers weren't supposed to be able to access this place, but all you really have to do to get in these days is convincingly !thrash a few times.\nhttps://discord.gg/JZ2AaJ2",
"St. Ben's Cathedral is a weird base in that it doesn't really bar rowdys from entry. The killers there generally just sneer and spit at their rival gangsters. \nhttps://discord.gg/xSQQD2M",
"Look, you ignorant juvenile. You basically don't know anything. The media that you love so much is a brainwashing tool, and its lies pull wool over your weary eyes. Get REAL news from the South Los Angeles News Dog Enquirer Report.\nhttps://discord.gg/FtHKt3B",
"SUBMIT TO SLIMECORP\nhttps://discord.gg/HK8VEzw",
"You succumb to your urges and find a rather naughty link. Slimegirls are against God's will, but if you don't care this place might appeal to you.\n https://discord.gg/nN6xtk9",
"@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\nhttps://discord.gg/b2hP68k",
"It's the land of the nateheads. You're really opening Pandora's box, fucking with this one. \nhttps://discordapp.com/invite/2Kc7nTA",
"You used to not be a big fan of hippos, but then you learned they like tearing people limb from limb and you've been in love ever since. Maybe now's your chance to meet one.\nhttps://discordapp.com/invite/6ksZrne",
"Y'arrr. \nhttps://discord.gg/VFcUmgc"
]

bible_verses = [
"And they said one to another, Go to, let us make brick, and burn them thoroughly. And they had brick for stone, and slime had they for mortar. And they said, !Goto, let us build us a city and a tower, whose top may reach unto heaven; and let us make us a name, lest we be scattered abroad upon the face of the whole earth… Genesis, 11:4 7",
"Then he went up from there to Bethel; and as he was going up by the way, young lads came out from the city and mocked him and said to him, “Go up, you baldhead; go up, you baldhead!” When he looked behind him and saw them, he cursed them in the name of the LORD. Then two female bears came out of the woods and tore up forty-two lads of their number. And he went from there to Mount Carmel, and from there he returned to Samaria. 2 Kings 2:23-25",
"Yet she became more and more promiscuous as she recalled the days of her youth, when she was a prostitute in Egypt. There she lusted after her lovers, whose genitals were like those of donkeys and whose emission was like that of horses. So you longed for the lewdness of your youth, when in Egypt your bosom was caressed and your young breasts fondled. Ezekiel 23:19",
"No one whose testicles are crushed or whose male organ is cut off shall enter the assembly of the Lord. Deuteronomy 23:1",
"Ye are the light of the world. A city that is set on an hill cannot be hid. Matthew 5:14",
"But now they desire a better country, that is, an heavenly: wherefore God is not ashamed to be called their God: for he hath prepared for them a city. Hebrews 11:16 ",
"Seek the prosperity of the city to which I have sent you as exiles. Pray to the LORD on its behalf, for if it prospers, you too will prosper. Jeremiah 29:7",
"And they went up on the breadth of the earth, and compassed the camp of the saints about, and the beloved city: and fire came down from God out of heaven, and devoured them. Revelation 20:9 ",
"And I will turn my hand upon thee, and purely purge away thy dross, and take away all thy tin: And I will restore thy judges as at the first, and thy counsellors as at the beginning: afterward thou shalt be called, The city of righteousness, the faithful city. Isaiah 1:25-26 ",
"David rose up and went, he and his men, and struck down two hundred men among the Philistines Then David brought their foreskins, and they gave them in full number to the king, that he might become the king's son-in-law. So Saul gave him Michal his daughter for a wife. 1 Samuel 18:27 ",
"Behold, the days come, saith the LORD, that I will punish all them which are circumcised with the uncircumcised. Jeremiah 9:25",
"Let me gulp down some of that red stuff; I’m starving. Genesis 25:30 ",
"Would that those who are upsetting you might also castrate themselves! Galatians 5:12",
"Even the handle sank in after the blade, and his bowels discharged. Ehud did not pull the sword out, and the fat closed in over it. Judges 3:22 ",
]


tv_lines = [
	"Breaking news! A local street performer won't come down from a gigantic pile of corpses. He refuses to eat for publicity! More to come.",
	"Welcome, goobs and gabs, to the Live Interactive Broadcast Enquirer Line, or L.I.B.E.L. for short. In today's news, local resident N6 was arrested for her abusive and predatory behavior toward Epic. Charges include false accusations of foot fetishism, terroristic threats, and 3rd degree sloshing toward a minor.",
	"Welcome to Mad Murderous Money, the show where stockbrokers are allowed, nay, encouraged, to jump out of buildings when the Dow Jones gets a bit pouty. Today we have a fucking ridiculous upturn for KFC, which actually got one of its supply trucks through the gang infested streets without being ransacked. Taco Bell set up a new restaraunt in New New Yonkers, but the windows aren't even bulletproof, so it's probably just gonna be a money pit for them. But my little chiclets, DO NOT invest in FUCKING PIZZA HUT. ENDLESS WAR shot a fucking laser through their kitchen and they're still in reconstruction. \n\nAs always, this is Mad Murderous Money, telling you to buy sell, die, and shill!",
	"Hey, everybody. This is Slime Bob Ross. I'm like regular Bob Ross, only I'm a thrown together copy some Juvie made cause he wanted to fuck me. Today, we'll be painting on the graffiti soaked walls of urban Green Light District. Now, the first thing you do on these urban type pieces is to sign your name here in the bottom right. This is so you will receive credit even if you have to run from the police halfway through. OK, very good. Today we're going to be doing a still life of Wreckington. We'll be doing a lot of greys here, but let's start with something fun, the flames of the burning wreckage. Wait. I forgot to bring red paint. OK, in that case, I'll have more once I fetch a Juvie during the commercial break. Stay tuned!",
	"The TV is just static. Maybe it's a bad reception. You wait. It will turn back on eventually, right?",
	"Welcome to Reading Rainbow, boys and girls! I'm Slime Levar Burton, and despite the existential  dread that comes with being a blob person, I'm doing wonderful today. This week, I read a book called 'The Gamer and The Bear'. We'll read an excerpt here. \nOnce upon a time in a cute little village at the bottom of a valley was a big rowdy bear.The bear was a real nasty guy, always smashing shit up and stomping his big feet. All the innocent little gamers of the village were scared of the big bear for if he saw them !dabbing he’d rip them limb from limb! They had to hide in their homes when he came around, !dabbing under their breath and gaming with the TV muted. It was a horrible time for everyone. \nThat was the first page, be sure to buy the full book!",
	"It's time for 'Our Deep Fuck City', where we run documentaries on the mystique of each district. Today, we'll be examining the phenomenon of 'Door Gunning', a new prank pulled by the upstarts of Little Chernobyl. In order to explain it, we must first look at a certain subculture of people there, known as half-deads. These folks live so close to the radiation of Little Chernobyl Power Plant that the radiation has more than killed them and fully decayed their minds. The problem is, they can't !revive either. They are so brain dead that ENDLESS WAR doesn't know what to do with them. So functionally, they exist as these wildly disfigured, basically immortal suburbanites. Door Gunning takes advantage of this. A prankster will knock on the door of some hapless half-dead person, and shoot them repeatedly in the face. It's incredibly painful, but since nobody dies it gets passed off as harmless fun. It really makes you think, eh?",
	"It's time for 'Our Deep Fuck City', where we run documentaries on the mystique of each district. We've got a treat for you this time, something you probably haven't heard of. Charcoal Park's efforts to fight back against hostile secreatures. You see, most districts are under Slimecorp's protection, excluding gangsters. However, Charcoal Park was such a forgettable place that they just forgot to send relief over there. Things have gotten so dire that many of the region's blue collar workers have banded together to form a militia of their own. There were many casualties at first, but intense training has turned the region into an sort of anarchist paradise. You wouldn't know it, though. To this day, their houses are kept very clean.",
	"Oh. Looks like it's playing the test screen. You know, the one with all the verticle colored stripes and the long beep. Yeah.",
	"It's time for 'Our Deep Fuck City', where we run documentaries on the mystique of each district. Most NLACakaNM citizens stay indoors for obvious reasons. Because of this, we're often oblivious to the interesting new social patterns they exhibit in this isolation. For example, Old New Yonkers has developed its own sect of Christianity. The practitioners of Neo-Protestant Milwaukeeism are convinced that ENDLESS WAR is the second coming of Christ, and that they have all been sent to Hell for their sins. Beyond that, most of the differences lie in the amount of self-flaggellation there is. NLACakaNM is a place of extremes, so what actually takes place is pretty mild compared to what else we've seen here. But despite its modesty, those folks may well be the most miserable in the city.",
	"It's time for 'Our Deep Fuck City', where we run documentaries on the mystique of each district. It's time to talk about the disappearing statue of Thalamus J. Crookline that stands in Globule Plaza. You see, Crookline's bandits have developed an inflated sense of honor among themselves. Part of that means they'll often wish themselves luck on that particular statue for good fortune in their pilfering. Every thief knows this, so it's not surprising how often the damn thing gets stolen. Hence the 'disappearance'. It costs the government like 1,000,000 slime a year just to maintain it.",
]

the_slime_lyrics= [
"https://www.youtube.com/watch?v=w-sREpqDiUo",
"I am gross and perverted \nI'm obsessed 'n deranged \nI have existed for years\nBut very little has changed",
"I'm the tool of the Government\nAnd industry too\nFor I am destined to rule\nAnd regulate you",
"I may be vile and pernicious\nBut you can't look away\nI make you think I'm delicious\nWith the stuff that I say",
"I'm the best you can get\nHave you guessed me yet?\nI'm the slime oozin' out\nFrom your TV set",
"You will obey me while I lead you\nAnd eat the garbage that I feed you\nUntil the day that we don't need you\nDon't go for help . . . no one will heed you",
"Your mind is totally controlled\nIt has been stuffed into my mold\nAnd you will do as you are told\nUntil the rights to you are sold",
"That's right, folks\nDon't touch that dial",
"Well, I am the slime from your video\nOozin' along on your livin' room floor\nI am the slime from your video\nCan't stop the slime, people, lookit me go",
"I am the slime from your video\nOozin' along on your livin' room floor\nI am the slime from your video\nCan't stop the slime, people, lookit me go",
"Welp, there it went. The Slime begins to wreak havoc outside your apartment. Can you believe you sat on your ass for like 6 hours?"
]



howls = [
	'**AWOOOOOOOOOOOOOOOOOOOOOOOO**',
	'**5 6 7 0 9**',
	'**awwwwwWWWWWooooOOOOOOOOO**',
	'**awwwwwwwwwooooooooooooooo**',
	'*awoo* *awoo* **AWOOOOOOOOOOOOOO**',
	'*awoo* *awoo* *awoo*',
	'**awwwwwWWWWWooooOOOOOOOoo**',
	'**AWOOOOOOOOOOOOOOOOOOOOOOOOOOOOO**',
	'**AWOOOOOOOOOOOOOOOOOOOO**',
	'**AWWWOOOOOOOOOOOOOOOOOOOO**'
]

moans = [
	'**BRRRRRAAAAAAAAAIIIIIINNNNNZZ**',
	'**B R A I N Z**',
	'**bbbbbRRRRRaaaaaaIIIIIInnnnZZZZZZ**',
	'**bbbbbbrrrrrraaaaaaaaiiiiiiinnnnnnnzzzz**',
	'**duuuuude, liiiiike, brrrraaaaaaiiiiinnnnnnzzzzz**',
	'**bbbraaaaiiinnnzzz**',
	'**BRAAAAAAAIIIIIIIIIIIIIIIINNNNNNNNNZZZZZZZZ**',
	'**BBBBBBBBBBBBBBBBBRRRRRRRRRRRRRRRAAAAAAAAAAAAAIIIIIIIIIIIIIIINNNNNNNNZZZZZZZZZZ**',
	'**BRRRRAAAAAIIINNNNNZZZ**',
	'**BBBBRRRRRRRRRRRRRRRAAAAIIIIIINNNNZZZZZ**',
	'**BRRRAAAIINNNZZ? BRRRAAAAIINNNZZ! BRRRRRRRAAAAAAAAIIIIIINNNNNZZZZZZZ!!!**',
	'**bbbbbBBBBrrrrrRRRRaaaaIIIIInnnnnnNNNNNzzzzZZZZZZZ!!!**',
	'**CCCCRRRRRRIIIIINNNNNNNGGGGEEEEE! BBBBBAAAAAAAAAAASSSSSEEEDDDDDDDD!**'
]

"""
	The list of item definitions. Instances of items are always based on these
	skeleton definitions.
"""

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

landmark_pois = [
	poi_id_dreadford,
	poi_id_charcoalpark,
	poi_id_slimesend,
	poi_id_assaultflatsbeach,
	poi_id_wreckington,
]

# maps districts to their immediate neighbors
poi_neighbors = {}

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

# Things a slimeoid might throw
thrownobjects_list = [
	"sewer cap",
	"boulder",
	"chunk of broken asphalt",
	"broken fire hydrant",
	"SlimeCorp-Brand Slime Containment Vessel (tm)",
	"piece of sheet metal",
	"burning tire",
	"hapless bystander",
	"completely normal small mammal",
	"heap of broken glass",
	"stereotypical nautical anchor",
	"piece of an iron girder",
	"pile of lumber",
	"pile of bricks",
	"unrecognizably decayed animal carcass",
	"very fortuitously abandoned javelin",
	"large rock",
	"small motor vehicle",
	"chunk of broken concrete",
	"piece of rusted scrap metal",
	"box overflowing with KFC branded bbq sauce",
	"Nokia 3310"
]

for mutation in mutations:
	mutations_map[mutation.id_mutation] = mutation
	mutation_ids.add(mutation.id_mutation)


for quadrant in quadrants:
	quadrants_map[quadrant.id_quadrant] = quadrant
	for alias in quadrant.aliases:
		quadrants_map[alias] = quadrant



# A map of vendor names to their items.
vendor_inv = {}

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


# List of items you can obtain via milling.
mill_results = []

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

# List of items you can obtain via mining.
mine_results = []

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



sea_scavenge_responses = [
	"see a school of Fuck Sharks circling below you",
	"notice an approaching kraken",
	"remember you can't swim"
]

# List of outskirt districts for spawning purposes
outskirts_districts = [
	poi_id_south_outskirts,
	poi_id_southwest_outskirts,
	poi_id_west_outskirts,
	poi_id_northwest_outskirts,
	poi_id_north_outskirts,
	poi_id_nuclear_beach
]


rain_protection = [
	cosmetic_id_raincoat,
	weapon_id_umbrella
]












# lists of all the discord server objects served by bot, identified by the server id
server_list = {}

"""
	store a server in a dictionary
"""
def update_server_list(server):
	server_list[server.id] = server


client_ref = None

def get_client():
	global client_ref
	return client_ref

"""
	save the discord client of this bot
"""
def set_client(cl):
	global client_ref
	client_ref = cl

	return client_ref
