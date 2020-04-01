
poi_list = [
	EwPoi( # 1
		id_poi = poi_id_downtown,
		alias = [
			"central",
			"dt",
		],
		str_name = "Downtown NLACakaNM",
		str_desc = "Skyscrapers and high-rise apartments tower above the jam-packed, bustling city streets below for as far as the eye can see. In this dense concrete jungle, your attention is constantly being divided among a thousand different things. Neon, fluorescent signs flash advertisements for all manner of amenities and businesses. The streets rumble with the sound of engines and metal scraping from the subway system deep underground. Hordes of men and women from every imaginable background walk these cruel streets, trying desperately to eke out a pitiful existence for themselves. This district never unwinds from its constant 24/7 slime-induced mania for even a moment, let alone sleep.\nDowntown is the beating heart of New Los Angeles City, aka Neo Milwaukee. With settlements in the area predating the emergence of slime, its prime location along the newly formed coastline naturally grew it into the cultural, economic, and literal center of the city. Due to its symbolic and strategic importance, it's home to the most intense gang violence of the city. Gunshots and screams followed by police sirens are background noises for this district. Some say that this propensity for violence is result of the sinister influence from an old obelisk in the center of town, ominously called ENDLESS WAR. You aren’t sure if you believe that, though.\n\nThis area contains ENDLESS WAR, SlimeCorp HQ, the Slime Stock Exchange and the Downtown Subway Station. To the north is Smogsburg. To the East is the Green Light District. To the South is the Rowdy Roughhouse. To the Southwest is Poudrin Alley. To the West is Krak Bay. To the Northwest is Cop Killtown.",
		coord = (28, 21),
		coord_alias = [
			(29, 21),
			(30, 21),
			(30, 22),
			(30, 23)
		],
		channel = "downtown",
		role = "Downtown",
		property_class = property_class_s,
		is_capturable = True
	),
	EwPoi( # 2
		id_poi = poi_id_smogsburg,
		alias = [
			"smog",
			"smogs",
			"sb"
		],
		str_name = "Smogsburg",
		str_desc = "In every direction, smokestacks belch out copious amounts of pollution into the atmosphere, creating a thick cloud that shrouds the district in sickening smog. It covers the district so completely that you can barely make out what time day it is. Your lungs can’t take much more of standing here, just do what you want to do and get out.\nSmogsburg is comprise of dozens of slime refineries and poudrin mills that turn unrefined, raw materials like the sludge from the city’s harbor into useful, pure slime. Functioning as the city’s premier industrial sector, it is by far the district hardest on the environment.\n\nThis area contains the Bazaar, the SlimeCorp Recycling Plant and the Smogsburg Subway Station. To the North is Arsonbrook. To the Northeast is Little Chernobyl. To the East is Old New Yonkers. To the South is Downtown NLACakaNM. To the West is Cop Killtown. To the Northwest is Astatine Heights.",
		coord = (28, 16),
		channel = "smogsburg",
		role = "Smogsburg",
		property_class = property_class_b,
		is_capturable = True
	),
	EwPoi( # 3
		id_poi = poi_id_copkilltown,
		alias = [
			"cop",
			"cops",
			"killers",
			"killer",
			"killtown",
			"copkt",
			"ck",
			"cct",
			"ckt",
			"cathedral"
		],
		str_name = "Cop Killtown",
		str_desc = "Edifices of various sinister architectural styles rise above the pavement. Gothic cathedrals, Victorian buildings, and New England brownstone apartments all dyed cool, dark colors. This district even hosts a miniature Japantown, featuring stores and restaurants that clutter your vision with densely packed fluorescent signage and other visual noise. Often cloaked in shadow from the height of these imposing buildings, the narrow, cobblestone streets of this district are perfect to brood and foster your angst in.\nCop Killtown is the gang base of the hardboiled, and calculating Killers. St. Ben’s Cathedral looms menacing on the horizon.\nhttps://discord.gg/xSQQD2M\n\nThis area contains the Cop Killtown Subway Station. To the North is Astatine Heights. To the East is Smogsburg. To the Southeast is Downtown NLACakaNM. To the Northwest is Gatlingsdale.",
		coord = (22, 18),
		channel = channel_copkilltown,
		role = "Cop Killtown",
		factions = [
			faction_killers
		],
		pvp = False,
		property_class = property_class_a,
		community_chest = chest_id_copkilltown
	),
	EwPoi( # 4
		id_poi = poi_id_krakbay,
		alias = [
			"krak",
			"kb"
		],
		str_name = "Krak Bay",
		str_desc = "Long street blocks are are densely packed with stores and restaurants, mixed in with townhouses and accompanied by modern skyscrapers and sprawling in-door shopping malls. These amenities and a scenic view of the River of Slime on its coast makes this district a favorite of a juvenile out on the town.\nKrak Bay is a bustling commercial district, featuring stores from across the retail spectrum. From economic, practical convenience stores to high-class, swanky restaurants, Krak Bay has it all. It is also home to some of the most recognizable fixtures of the city’s skyline, most notably the Poudrintial Tower and the shopping mall at its base which contains the city’s prized food court.\n\nThis area contains the Food Court, Bicarbonate Soda Fountain, and the Krak Bay Subway Station. To the East is Downtown NLACakaNM. To the Southeast is Poudrin Alley. To the South is Ooze Gardens. To the Southwest is South Sleezeborough. To the West is North Sleezeborough. To the Northwest is Glocksbury.",
		coord = (21, 24),
		channel = "krak-bay",
		role = "Krak Bay",
		property_class = property_class_a,
		is_capturable = True
	),
	EwPoi( # 5
		id_poi = poi_id_poudrinalley,
		alias = [
			"poudrin",
			"pa"
		],
		str_name = "Poudrin Alley",
		str_desc = "Densely packed, claustrophobic mazes of residential apartments stand above poorly planned roads with broken streetlights that spark and flicker over the cracked pavement. Only the locals know how to navigate the residential labyrinth effectively, by utilizing the interconnected, narrow alleyways the district is named for.\nPoudrin Alley is the principal residential district of the city, outfitted with enough low-rent apartments for the lower-middle class to house the entire city on its own. Sadly, for most of the impoverished dredges of the city, these low rents just aren’t low enough and the majority of the apartments go unused.\n\nThis area contains the 7-11. To the Northeast is Downtown NLACakaNM. To the East is the Rowdy Roughhouse. To the South is Cratersville. To the Southwest is Ooze Gardens. To the Northwest is Krak Bay.",
		coord = (24, 28),
		channel = "poudrin-alley",
		role = "Poudrin Alley",
		property_class = property_class_b,
		is_capturable = True
	),
	EwPoi( # 6
		id_poi = poi_id_rowdyroughhouse,
		alias = [
			"rowdy",
			"rowdys",
			"rowdies",
			"roughhouse",
			"rowdyrh",
			"rr",
			"rrh"
		],
		str_name = "Rowdy Roughhouse",
		str_desc = "Cheap townhouses and abandoned warehouses host graffiti art on basically every surface. An almost completely overrun slum, many of the deteriorated buildings have been painted a bright pink by the gangsters that seized them. Overpopulated and underhoused, the majority of the residents have constructed shanty houses for themselves and gather around trash can bonfires. Loud music blasts from bass-heavy speakers all hours of the night, fueling the seemingly constant parties this district is known for.\nRowdy Roughhouse is the gang base of the hot blooded, and reckless Rowdys. In the heart of the district stands the Rowdy Roughhouse, for which the district is named. Yes, it’s confusing, we know.\nhttps://discord.gg/JZ2AaJ2\n\nThis area contains the Rowdy Roughhouse Subway Station. To the North is Downtown NLACakaNM. To the South is Wreckington. To the Southwest is Cratersville. To the West is Poudrin Alley.",
		coord = (30, 26),
		channel = channel_rowdyroughhouse,
		role = "Rowdy Roughhouse",
		factions = [
			faction_rowdys
		],
		pvp = False,
		property_class = property_class_c,
		community_chest = chest_id_rowdyroughhouse
	),
	EwPoi( # 7
		id_poi = poi_id_greenlightdistrict,
		alias = [
			"greenlight",
			"gld"
		],
		str_name = "Green Light District",
		str_desc = "Animated neon, fluorescent signs dominate your vision, advertising all conceivable earthly pleasures. This district’s main street consists of a long, freshly-paved road with brothels, bars, casinos and other institutions of sin lining either side of it. Among these is the city-famous SlimeCorp Casino, where you can gamble away your hard-earned SlimeCoin playing various slime-themed games. The ground is tacky with some unknown but obviously sinful grime.\nThe Green Light District is well-known for its illegal activities, almost completely being comprised by amenities of ill repute and vice.\n\nThis area contains the SlimeCorp Casino and the Green Light District Subway Station. To the East is Vagrant's Corner. To the Southeast is Juvie's Row. To the West is Downtown NLACakaNM.",
		coord = (34, 19),
		channel = "green-light-district",
		role = "Green Light District",
		property_class = property_class_a,
		is_capturable = True,
		has_ads = True
	),
	EwPoi( # 8
		id_poi = poi_id_oldnewyonkers,
		alias = [
			"ony"
		],
		str_name = "Old New Yonkers",
		str_desc = "Rows of three-story brick condominiums with white marble moulding wind along lanes of old asphalt roads with faded markings. Spiked wrought-iron gates protect the lawn of the district’s principal institutions, like the senior center.\nOld New Yonkers is popular with the older citizens of the city, due to its incredibly boring, gentrified residential landscape. Modest outdoor malls sells useless shit like candles and soaps, and the elderly population fills up their lumpy, sagging bodies at chain restaurants like Applebee’s and fucking IHOP.\n\nThis area contains the Slimecorp Real Estate Agency. To the Northeast is New New Yonkers. To the Southeast is Vagrant's Corner. To the Southwest is Smogsburg. To the East is Little Chernobyl. To the Northwest is Brawlden.",
		coord = (37, 14),
		channel = "old-new-yonkers",
		role = "Old New Yonkers",
		property_class = property_class_a,
		is_capturable = True
	),
	EwPoi( # 9
		id_poi = poi_id_littlechernobyl,
		alias = [
			"chernobyl",
			"lilchernobyl",
			"lilchern",
			"lc"
		],
		str_name = "Little Chernobyl",
		str_desc = "Dilapidated office buildings overgrown with ivy and the bombed-out frames of unidentifiable structures comprise the majority of the housing for this sparsely populated district. Radioactive almost to the point of warding off thieves and vandals (but not quite), many people report seeing strange creatures and various cryptids roaming the abandoned power plant complex at night.\nLittle Chernobyl might not be much to look at or often discussed nowadays, but don’t be fooled by its current irrelevance. Long ago, it was home to Arizona's largest nuclear power plant. An electrical blackout caused a total safety system failure, leading in a cataclysmic nuclear meltdown. This caused nuclear waste to flood into the Grand Canyon and create the Slime Sea we know and love today.\n\nThis area contains Green Cake Cafe. To the North is Brawlden. To the East is Old New Yonkers. To the West is Arsonbrook.",
		coord = (30, 12),
		channel = "little-chernobyl",
		role = "Little Chernobyl",
		property_class = property_class_c,
		is_capturable = True
	),
	EwPoi( # 10
		id_poi = poi_id_arsonbrook,
		alias = [
			"arson",
			"ab"
		],
		str_name = "Arsonbrook",
		str_desc = "This district is seemingly eternally overcast, allowing the dark plumes of smoke from distant fires fade into the soft grey clouds. A thin layer of soot rests upon basically the entire district, providing nutrient-rich soil which the rural farmers in the north of the district take advantage of. In the south, enclaves of civilization have started to pop up, learning from the mistakes of previous generations and building out of brick instead of wood. Aesthetically, these settlements resemble a small mining town from the mountainous forests of the northwest, just replace the rugged terrain with flat land and the evergreens with burnt, charcoal frames of trees that used to be. A Starbucks tried to open here once.\nArsonbook is easily among the most peaceful districts of the city, as long as you count constant wildfires and destruction of property from arson as peaceful. The locals are used to that sort of thing though, so they’re pretty mellow. Kick back, relax, and don’t get too attached to your house if you plan on living here.\n\nThis area contains the Arsonbrook Farms and the Arsonbrook Subway Station. To the East is Brawlden. To the Southeast is Little Chernobyl. To the South is Smogsburg. To the West is Astatine Heights. To the North is Arsonbrook Outskirts.",
		coord = (26, 8),
		channel = "arsonbrook",
		role = "Arsonbrook",
		property_class = property_class_b,
		is_capturable = True
	),
	EwPoi( # 11
		id_poi = poi_id_astatineheights,
		alias = [
			"astatine",
			"heights",
			"ah"
		],
		str_name = "Astatine Heights",
		str_desc = "Swanky modern condominiums jut out of the steep hills to the north, while to the south rows of picture-perfect suburban homes with disgustingly well-maintained lawns constrict around freshly-laid roads. Luxury boutiques and high-class restaurants compete for the wallets of privileged, rich yuppies.\nAstatine Heights is the home to many of the wealthiest men and women of the city, with many of the residents forcing their fratty Republican sons to the prestigious college N.L.A.C.U. in neighboring Gatlingsdale. The difference between Astatine Heights and other affluent districts of the city is that the majority of residents have not passed onto the elysian fields of retirement, and thus have at least a sliver of personality and ambition left in their community, however gentrified it might be.\n\nThis area contains NLACakaNM Cinemas, the Red Mobster Seafood Restaurant and the Astatine Heights Subway Station. To the East is Arsonbrook. To the Southeast is Smogsburg. To the South is Cop Killtown. To the Southwest is Gatlingsdale. To the West is Toxington. To the North is Astatine Heights Outskirts.",
		coord = (22, 11),
		channel = "astatine-heights",
		role = "Astatine Heights",
		property_class = property_class_a,
		is_capturable = True
	),
	EwPoi( # 12
		id_poi = poi_id_gatlingsdale,
		alias = [
			"gatlings",
			"gatling",
			"gd"
		],
		str_name = "Gatlingsdale",
		str_desc = "Hundreds of small “nerdy” retail stores and ethnically-diverse restaurants are compact into a dense, bustling plaza just minutes from the prestigious N.L.A.C.U. college campus. Almost all of district is comprised of or controlled by the sprawling ivy league university. Featuring smoky cafes, vintage clothing boutiques, and independent bookstores, this district is perfectly catered to the pompous hipsters that flood its streets every day after class.\nGatlingsdale is a historic district, with many of its winding cobblestone roads and gaslamp streetlights dating back to the early days of the city.\n\nThis District contains New Los Angeles City University and the Gatlingsdale Subway Station. To the Northeast is Astatine Heights. To the Southeast is Cop Killtown. To the Southwest is Vandal Park. To the West is Polonium Hill. To the Northwest is Toxington.",
		coord = (18, 14),
		channel = "gatlingsdale",
		role = "Gatlingsdale",
		property_class = property_class_a,
		is_capturable = True
	),
	EwPoi( # 13
		id_poi = poi_id_vandalpark,
		alias = [
			"vandal",
			"park",
			"vp"
		],
		str_name = "Vandal Park",
		str_desc = "A laundry list of various sports amenities and public parks dot the landscape of this athletically minded district. These include soccer fields, skate parks, swimming pools, and of course the district’s famous Battle Arena.\nVandal Park’s numerous open spaces and its more-or-less clean air make it an attractive destination for juveniles seeking a stroll. Despite this you’ve still got to keep your wits about you here if you want to not get publicly executed against one of the pretty trees.\n\nThis area contains the Battle Arena. To the Northeast is Gatlingsdale. To the South is Glocksbury. To the Southwest is West Glocksbury. To the Northwest is Polonium Hill.",
		coord = (15, 17),
		channel = "vandal-park",
		role = "Vandal Park",
		property_class = property_class_b,
		is_capturable = True
	),
	EwPoi( # 14
		id_poi = poi_id_glocksbury,
		alias = [
			"glocks",
			"glock",
			"gb"
		],
		str_name = "Glocksbury",
		str_desc = "Semi-orderly residential neighborhoods with discolored white picket fences protecting unkempt lawns for as far as the eye can far. This district likes to pretend its a quiet suburb, but the regular screams and gunshots coupled with numerous chalk outlines of human bodies on the street make this hard to believe. You smell bacon. *Figurative* bacon. The cops must be lurking nearby somewhere.\nGlocksbury’s flaccid attempts at normalcy are fueled by it hosting the city’s police department, which is hilariously ineffectual and underfunded to the point of absurdity. In this city, the bumbling police act as target practice to the local gangs rather than actual authorities to be obeyed. But, they sure like to pretend they are.\n\nThis area contains Glocksbury Comics, and the Glocksbury Subway Station. To the North is Vandal Park. To the Southeast is Krak Bay. To the South is North Sleezeborough. To the West is West Glocksbury. To the West is West Glocksbury Outskirts.",
		coord = (14, 21),
		channel = "glocksbury",
		role = "Glocksbury",
		property_class = property_class_c,
		is_capturable = True
	),
	EwPoi( # 15
		id_poi = poi_id_northsleezeborough,
		alias = [
			"northsleezeboro",
			"nsleezeborough",
			"nsleezeboro",
			"nsleeze",
			"northsleeze",
			"nsb",
			"ns"
		],
		str_name = "North Sleezeborough",
		str_desc = "Sleepy brownstone apartments and about 50,000 different terrible pizza places populate this slow paced, gentrifying district. Outdoor malls have started to spring up here and there, mostly around the college campus of Neo Milwaukee State. Retired parents rest on benches, throwing crumbs of bread at birds and squandering the twilight years of their misspent life. Students with curious facial hair and suspenders lurk in vinyl record stores and horde ironic knick-knacks.\nNorth Sleezeborough residents really, really don't care about anything. It wouldn’t be fair to call them nihilistic, that implies self-reflection or philosophical quandary, they are just so lethargic that they might as well categorically be considered legally dead. Alongside these generally older occupants are younger students who have flocked to the dirt cheap public college of Neo Milwaukee State to continue their mediocre education.\n\nThis area contains Neo Milwaukee State and the North Sleezeborough Subway Station. To the North is Glocksbury. To the East is Krak Bay. To the South is South Sleezeborough.",
		coord = (16, 24),
		channel = "north-sleezeborough",
		role = "North Sleezeborough",
		property_class = property_class_b,
		is_capturable = True
	),
	EwPoi( # 16
		id_poi = poi_id_southsleezeborough,
		alias = [
			"southsleezeboro",
			"ssleezeborough",
			"ssleezeboro",
			"ssleeze",
			"southsleeze",
			"ssb",
			"ss"
		],
		str_name = "South Sleezeborough",
		str_desc = "Dreary townhouses and red brick apartments brush up against the embarrassingly inauthentic approximations oriental architectural styles of the city’s Chinatown. There, pagodas and dragon gates take up every square inch of land that asian restaurants and law firms don’t. From the streets it’s hard to make out the sky from the tacky lanterns and web of unintelligible business signs.\nSouth Sleezeborough’s residential streets are as boring as can be, but wade through them and you’ll have a fun time ordering popping bubble tea and lemon roll cakes from bakeries and sparing with your buddies at the Dojo.\n\nThis area contains the Dojo and the South Sleezeborough Subway Station. To the North is North Sleezeborough. To the Northeast is Krak Bay. To the East is Ooze Gardens. To the West is Crookline. To the South is South Sleezeborough Outskirts.",
		coord = (17, 27),
		channel = "south-sleezeborough",
		role = "South Sleezeborough",
		property_class = property_class_b,
		is_capturable = True
	),
	EwPoi( # 17
		id_poi = poi_id_oozegardens,
		alias = [
			"ooze",
			"gardens",
			"og"
		],
		str_name = "Ooze Gardens",
		str_desc = "Walking paths connect dozens of greenhouses and gardens featuring rare, exotic, and irradiated flora. This district is really just one big park, broken up into several sections hosting different types of botanical attractions, as well as several museums and even the city’s zoo. Musical concerts are often held in one of the several outdoor amphitheatres that are scattered across the district. Truly, an amusement park for lovers of nature and culture.\nOoze Gardens is a clear cultural outlier of the city. The residents of this district are largely pacifist, choosing music, love, and psychedelic drugs over violent crime. They make you sick.\n\nThis area contains the Ooze Gardens Farms. To the North is Krak Bay. To the Northeast is Poudrin Alley. To the East is Cratersville. To the West is South Sleezeborough. To the South is Ooze Gardens Outskirts.",
		coord = (19, 30),
		channel = "ooze-gardens",
		role = "Ooze Gardens",
		property_class = property_class_a,
		is_capturable = True
	),
	EwPoi( # 18
		id_poi = poi_id_cratersville,
		alias = [
			"craters",
			"cville",
			"cv"
		],
		str_name = "Cratersville",
		str_desc = "Crumbling infrastructure is commonplace here. The craters and smaller potholes that give this district its name are scattered liberally across the streets and sidewalks. Unruly miners have refused to limit their excavating to the designated mining sector and scavenge even the residential roads for meager drops of slime.\nCratersville really sucks to live in. I mean, obviously. Look at this place. Even aside from the huge fucking holes everywhere, you’ve still got to deal with the constant sound of mining and dynamite explosions underground.\n\nThis area contains the Cratersville Mines and the Cratersville Subway Station. To the North is Poudrin Alley. To the Northeast is the Rowdy Roughhouse. To the East is Wreckington. To the West is Ooze Gardens. To the South is Cratersville Outskirts.",
		coord = (24, 33),
		channel = "cratersville",
		role = "Cratersville",
		property_class = property_class_c,
		is_capturable = True
	),
	EwPoi( # 19
		id_poi = poi_id_wreckington,
		alias = [
			"wrecking",
			"wton",
			"ton",
			"wt"
		],
		str_name = "Wreckington",
		str_desc = "Piles of rubble and scrap metal lean against partially demolished buildings that barely remain standing. Sadly, these structures are often all the critically impoverished residents of Wreckington have to house themselves. Constant new construction projects promise new opportunities for the deteriorating district, but these promises are too often broken by lack of funding and interest. Jackhammers pummeling the asphalt and wrecking balls knocking down apartment complexes can be heard throughout the entire district, 24/7.\nWreckington isn’t completely barren however, its strategic location on the coast and cheap property makes its shipyard a favorite among unscrupulous sailors. It also features a ferry connection to Vagrant’s Corner, if you’re so inclined to visit the eastern districts.\n\nThis area contains the Smoker's Cough Diner, the Wreckington Ferry Port and the Wreckington Subway Station. To the North is the Rowdy Roughhouse. To the West is Cratersville. To the South is Wreckington Outskirts.",
		coord = (32, 29),
		channel = "wreckington",
		role = "Wreckington",
		property_class = property_class_c,
		is_capturable = True
	),
	EwPoi( # 20
		id_poi = poi_id_juviesrow,
		alias = [
			"juvies",
			"jrow",
			"jr"
		],
		str_name = "Juvie's Row",
		str_desc = "The landscape of this district is completely defined by it containing the city’s largest mineshafts. Almost the entire district is has been dug up, the earth overturned by a crazed populace trying to soak up every drop of slime it can get its hands on. There are few permanent structures here, and even less infrastructure. Swathes of juveniles have constructed shanty houses out of discarded building materials, suffering from the intense pollution and poor living conditions just to be closer to the mine shaft entrances that jut out of the otherwise useless, rugged terrain. Makeshift bazaars and other rudimentary amenities have popped up in the horribly overcrowded tent cities.\nJuvie’s Row might just be the most populous district of the city, with every ambitious juvenile spending at least some of their formative days toiling underground to eke out a pitiful existence. Seeing all the gang unaligned juvies here fills you with pity, as well as disgust.\n\nThis area contains the Juvie's Row Mines, the Juvie's Row Farms and the Juvie's Row Subway Station. To the Northeast is Vagrant's Corner. To the Northwest is the Green Light District.",
		coord = (37, 23),
		channel = "juvies-row",
		role = "Juvie's Row",
		pvp = False,
		property_class = property_class_b,
		community_chest = chest_id_juviesrow
	),
	EwPoi( # 21
		id_poi = poi_id_slimesend,
		alias = [
			"slimes",
			"send",
			"end",
			"se"
		],
		str_name = "Slime's End",
		str_desc = "There’s not much to see here, as this sparsely populated district is mainly comprised of small residential enclaves and barren terrain. Maybe a tree here and there, I don’t know.\nSlime’s End is a narrow peninsula is bordered on both sides by the Slime Sea. The phosphorescence illuminates the sky with an eerily green glow.\n\nThis area contains the Slime's End Cliffs. To the North is Vagrant's Corner.",
		coord = (45, 21),
		channel = "slimes-end",
		role = "Slime's End",
		property_class = property_class_b,
		is_capturable = True
	),
	EwPoi( # 22
		id_poi = poi_id_vagrantscorner,
		alias = [
			"vagrants",
			"vcorner",
			"vc"
		],
		str_name = "Vagrant's Corner",
		str_desc = "A foul, fishy smell pervades the entire district, emanating from the harbor. This wretched wharf is home to the seediest underbelly of the city, besides the neighboring Green Light District of course. Pirates and other seafaring scoundrels patron the local taverns and other haunts of ill repute while on shore leave. The harsh glow of the Slimea Sea illuminates the undersides of the innumerable docks that extend out from this district, as well as the heavy industrial equipment designed to pump slime into the cargo holds of outbound barges.\nVagrant’s Corner features the largest seaport of the city, with almost all seabound imports and exports funnel through it. It also features a ferry connection to Wreckington, if you’re so inclined to visit the southern districts.\n\nThis area contains The King's Wife's Son Speakeasy, and the Vagrant's Corner Ferry Port. To the North is New New Yonkers. To the Northeast is Assault Flats Beach. To the South is Slime's End. To the Southwest is Juvie's Row. To the West is the Green Light District. To the Northwest is Old New Yonkers.",
		coord = (42, 16),
		channel = "vagrants-corner",
		role = "Vagrant's Corner",
		property_class = property_class_c,
		is_capturable = True
	),
	EwPoi( # 23
		id_poi = poi_id_assaultflatsbeach,
		alias = [
			"assaultflats",
			"assault",
			"flats",
			"beach",
			"assflats",
			"afb"
		],
		str_name = "Assault Flats Beach",
		str_desc = "Colorfully painted wooden storefronts and towering condominium complexes peer out from the coastline of this scenic beach town. Most of the district is owned by the sprawling luxury resort the district is best known for, as well as virtually the entirety of the actual beach of Assault Flats Beach.\nAssault Flats Beach is by far one of if not the most expensive districts in the city to live in, due to its complete subjugation by the resort and accompanying security force, it is also the safest district to live in by a long shot. But, as you venture away from the coast you’ll begin to see more of the city’s standard crime rate return. Interestingly, the district is a favorite among archaeologists for its unprecedented density of jurassic fossils hidden deep underground. Some even say dinosaurs still roam the outskirts of the district to the north, but frankly that just seems ridiculous. I mean, we all know dinosaurs aren’t real.\n\nThis area contains the Resort, the Assault Flats Beach Blimp Tower and the Assault Flats Beach Subway Station. To the South is Vagrant's Corner. To the West is New New Yonkers. To the North is Assault Flats Beach Outskirts.",
		coord = (45, 11),
		channel = "assault-flats-beach",
		role = "Assault Flats Beach",
		property_class = property_class_s,
		is_capturable = True
	),
	EwPoi( # 24
		id_poi = poi_id_newnewyonkers,
		alias = [
			"nnewyonkers",
			"nnyonkers",
			"nny"
		],
		str_name = "New New Yonkers",
		str_desc = "Nightclubs and trendy restaurants have popped up in slick, modern buildings while the same old, reliable brownstones host arcades, bowling alleys and other teenage favorites. Featuring probably the best nightlife in the city, New New Yonkers is a favorite hangout spot among the juveniles of the city and consequently has an alarming crime rate. Many of the older residents want to see these fun times come to an end however, seeking to emulate the gentrified suburbia of Old New Yonkers to the south. This is adamantly resisted by the rough-and-tumble youth, those who’s to say if this district will remain the bastion of good times it is today.\nNew New Yonkers is the best district to hang out in on a weekend with your friends. Really, what else can a district aspire to?\n\nTo the East is Assault Flats Beach. To the South is Vagrant's Corner. To the Southwest is Old New Yonkers. To the West is Brawlden. To the North is New New Yonkers Outskirts.",
		coord = (41, 9),
		channel = "new-new-yonkers",
		role = "New New Yonkers",
		property_class = property_class_b,
		is_capturable = True
	),
	EwPoi( # 25
		id_poi = poi_id_brawlden,
		alias = [
			"den",
			"bd"
		],
		str_name = "Brawlden",
		str_desc = "Sturdy red brick apartments rise above the hard-knock streets. Gruff mechanics, plummers, and other workers of dirty jobs like to make their homes here, away from the pissy baby fucker fapper bullshit of the juvenile-populated inner districts. You can see them roaming the streets in their stained wife beaters, popping open the hoods of their cars and grunting dad noises. Sometimes they cross paths with one another and immediately upon locked eyesight engage in brutal fist fights. No one really knows why.\nBrawlden, despite being a largely rumble-and-tough inhabited primarily by dads is inexplicability the home of a high-tech laboratory run by SlimeCorp. Deep underground in an unassuming corner of this district lays a not-so-secret top secret laboratory dedicated to the study of Slimeoids. What are Slimeoids? You’ll just have to find out, buddy.\n\nThis area contains the Slimeoid Laboratory. To the East is New New Yonkers. To the Southeast is Old New Yonkers. To the South is Little Chernobyl. To the West is Arsonbrook. To the North is Brawlden Outskirts.",
		coord = (33, 8),
		channel = "brawlden",
		role = "Brawlden",
		property_class = property_class_c,
		is_capturable = True
	),
	EwPoi( # 26
		id_poi = poi_id_toxington,
		alias = [
			"tox",
			"tton",
			"ttn",
			"tt",
			"tx"
		],
		str_name = "Toxington",
		str_desc = "You cover your mouth in a futile attempt to avoid breathing in the toxins rising from the nearby lakes and mineshafts. A thick fog of this foul-smelling, poisonous gas shrouds the entire district, making the land virtually uninhabitable. But, where there’s slime, people will settle. Juveniles from across the city are happy to spend their short lives in this hellhole for a chance to strike it rich.\nToxington has no redeemable aspects, outside of its abundance of slime veins underground and its lovely fishing spots above.\n\nThis area contains the Toxington Mines and the Toxington Subway Station. To the East is Astatine Heights. To the Southeast is Gatlingsdale. To the South is Polonium Hill. To the East is Charcoal Park. To the North is Toxington Outskirts.",
		coord = (14, 9),
		channel = "toxington",
		role = "Toxington",
		property_class = property_class_c,
		is_capturable = True
	),
	EwPoi( # 27
		id_poi = poi_id_charcoalpark,
		alias = [
			"charcoal",
			"park2",
			"cpark",
			"awkwardinitials",
			"cp",
			"ch"
		],
		str_name = "Charcoal Park",
		str_desc = "A completely unremarkable, quiet retirement community. The citizens are fed up with slime, honestly. Pathetic little gardens rest in front of the uneven parking lots of corporate complexes housing dentists, fortune-tellers, real estate agencies, and other equally dull and pointless ventures.\nCharcoal Park is where boring people go to die. No one is happy to be here.\n\nTo the East is Toxington. To the South is Polonium Hill. To the Northwest is Charcoal Park Outskirts.",
		coord = (11, 7),
		channel = "charcoal-park",
		role = "Charcoal Park",
		property_class = property_class_c,
		is_capturable = True
	),
	EwPoi( # 28
		id_poi = poi_id_poloniumhill,
		alias = [
			"polonium",
			"hill",
			"phill",
			"ph"
		],
		str_name = "Polonium Hill",
		str_desc = "The gently rolling astroturf hills are sprinkled with hideous mansions that obviously cost a fortune but look like complete shit. This whole district feels like it tries way to hard to come across as high-society, when it's really just some residential district on the far-flung edges of the city.\nPolonium Hills residents really want you to think they're rich.\n\nTo the North is Charcoal Park. To the Northeast is Toxington. To the East is Gatlingsdale. To the Southeast is Vandal park. To the South is West Glocksbury. To the West is Polonium Hill Outskirts.",
		coord = (11, 14),
		channel = "polonium-hill",
		role = "Polonium Hill",
		property_class = property_class_b,
		is_capturable = True
	),
	EwPoi( # 29
		id_poi = poi_id_westglocksbury,
		alias = [
			"wglocksbury",
			"westglocks",
			"wglocks",
			"wglock",
			"wgb",
			"wg"
		],
		str_name = "West Glocksbury",
		str_desc = "Glocksbury-styled neighborhoods continue into its western counterpart, though liberated from the oppressive yolk of the city’s police department enforcing its poor attempts at enforcing societal values. This, coupled with its location on the outer edge of the city leads to some brutal, cruel crimes being perpetrated by maniacs with little grip on reality. Gunshots ring out regularly from somewhere in the distance, behind laundromats and barber shops.\nWest Glocksbury’s startlingly high violent crime rate may make even some of the most jaded residents of the city may get nervous.\n\nThis area contains the West Glocksbury Subway Station. To the North is Polonium Hill. To the Northeast is Vandal Park. To the East is Glocksbury.",
		coord = (9, 19),
		channel = "west-glocksbury",
		role = "West Glocksbury",
		property_class = property_class_c,
		is_capturable = True
	),
	EwPoi(  # 30
		id_poi = poi_id_jaywalkerplain,
		alias = [
			"jaywalker",
			"jay",
			"walker",
			"plain",
			"jp",
		],
		str_name = "Jaywalker Plain",
		str_desc = "Though about half of this district is made of up parks, don’t mistake this for a wealthy district. These neglected, overgrown open spaces only help to congest the poor communities of Jaywalker Plains into tightly packed slums. This, coupled with being a backwater on the edge of the city with nothing to do, has bred a district that leads the city only in amount of narcotics injected per capita. Everyone is on a bad trip in Jaywalker Plain. Maniacs roam the street, screaming obscenities and striping naked in public. Homeless men ramble incoherent nonsense while picking drunken fights with one another on the side of the street. Many strange and unusual crimes are perpetrated here and reported on by local news teams to the amusement of residents of neighboring districts. “Did you hear what that guy from Jaywalker Plain did the other day,” is a common conversation starter in the western districts.\nJaywalker Plain has actually become a common residential district for lower income students attending the nearby Neo Milwaukee State wanting to avoid the already cheap rates of apartments in North Sleezebrorough. Because of this, you’re guaranteed to see a lot of young artists and hipsters roaming this broken, nightmare hellscape of a district looking for cafes to leech Wi-Fi access off of. Good luck with that.\n\nThis area contains the Jaywalker Plain Subway Station. To the North is West Glocksbury. To the Northeast is Glocksbury. To the East is North Sleezeborough. To the Southwest is Crookline. To the South is Dreadford. To the West is Jaywalker Plain Outskirts.",
		coord = (9, 25),
		channel = "jaywalker-plain",
		role = "Jaywalker Plain",
		property_class = property_class_c,
		is_capturable = True
	),
	EwPoi(  # 31
		id_poi = poi_id_crookline,
		alias = [
			"crook",
			"line",
			"cl",
		],
		str_name = "Crookline",
		str_desc = "Most of this district is shrouded in total darkness, the unregulated construction of skyscrapers obstructing sunlight from ever reaching the streets far below them. Streetlights and the dense arrays of neon signs advertising speakeasy after speakeasy are the only illumination you’re provided with while traveling the narrow, twisting streets of this district. You’ll have to keep your wits about you if you want to leave here with your wallet, Crookline is perhaps most known for its hordes of petty thieves who specialise in stealing from clueless juveniles from the posher districts. Despite these hurdles, or possibly because of them, Crookline has a bustling nightlife heavily featuring those aforementioned speakeasies. No matter where you are in this district, you’re not more than a block or two from a jazz club. You sort of feel like you’re on the set of a film noir movie when you traverse these dark alleyways.\nCrookline was a historically rebellious settlement on the edge of New Los Angeles City aka Neo Milwaukee, resisting full annexation for years until it was fully culturally and economically dominated by the city. Because of this, the residents have always kept an independent streak, and remain vehemently opposed most aspects of slime past its purely utilitarian purposes. You get the feeling the denizens of this district would have been happier if there was gold discovered in the area rather than the green, morality obliterating substance they’re stuck with.\n\n To the North is Jaywalker Plain. To the Northeast is North Sleezeborough. To the East is South Sleezeborough. To the West is Dreadford. To the South is Crookline Outskirts.",
		coord = (14, 26),
		channel = "crookline",
		role = "Crookline",
		property_class = property_class_b,
		is_capturable = True
	),
	EwPoi(  # 32
		id_poi = poi_id_dreadford,
		alias = [
			"dread",
			"ford",
			"df",
		],
		str_name = "Dreadford",
		str_desc = "Neatly spaced colonial revival mansions and chapels are broken up by botches of thick, twisting woods. This district is largely rural and suburban, with a small town center with various necessities like Whole Foods and a cemetery. The residents of this district are very, very wealthy and meticulously maintain the gated community they’ve grown for themselves. Perhaps the most obvious example of this is the country club and its accompanying golf course, which comprises a large chunk of the district.\nDreadford is one of the oldest settlements of the area, being inhabited by humans as far back as 1988. The original founders were fleeing restrict criminals rights laws, and established the town of Dreadford in what was then a barren Arizonian desert. These first settlers had quite the pension of holding kangaroo courts, which often amounted to just reading the list of crimes the accused was charged with before hanging them immediately. Some nooses still hang on trees around the district, begging to be finally used.\n\n This area contains the Country Club and the Dreadford Blimp Tower. To the North is Jaywalker Plain. To the East is Crookline. To the Southwest is Dreadford Outskirts.",
		coord = (10, 28),
		channel = "dreadford",
		role = "Dreadford",
		property_class = property_class_s,
		is_capturable = True
	),
	EwPoi( # the-sewers
		id_poi = poi_id_thesewers,
		alias = [
			"drain",
			"sewers",
			"sewer",
			"ghost",
			"ghosts",
			"ts",
			"s",
			"loser"
		],
		str_name = "The Sewers",
		str_desc = "A vast subterranean maze of concrete tunnels, eternally echoing with the dripping of water and decayed slime runoff. All the waste of NLACakaNM eventually winds up here, citizens included.",
		channel = channel_sewers,
		life_states = [
			life_state_corpse
		],
		role = "Sewers",
		community_chest = chest_id_thesewers
	),
	EwPoi(  # ENDLESS WAR
		id_poi = poi_id_endlesswar,
		alias = [
			"obelisk",
			"war",
			"ew"
		],
		str_in = "at the base of",
		str_enter = "arrive at",
		str_name = "ENDLESS WAR",
		str_desc = "Its bright, neon green color nearly blinds you when observed from this close. You are overwhelmed by an acute, menacing aura as you crane your neck to observe the obelisk in its entirety. You almost thought you saw it looking back down at you, but it was probably just your imagination. You shouldn’t stay here any longer than you have to, you always get a weird feeling in the pit of your stomach when you stick around for too long.",
		channel = channel_endlesswar,
		role = "Endless War",
		is_subzone = True,
		mother_district = poi_id_downtown,
		max_degradation = 10000000,
	),
	EwPoi(  # slimecorp HQ
		id_poi = poi_id_slimecorphq,
		alias = [
			"slimecorp",
			"hq",
			"corp"
		],
		str_in = "in the lobby of",
		str_name = "SlimeCorp HQ",
		str_desc = "Here, businessmen carrying briefcases dripping with slime powerwalk from every direction to every other direction. They barely acknowledge your existence outside of muttering under their breath when they’re forced to sidestep around you and the other clueless juveniles loitering in their lobby. Above the first few floors begins the endless labyrinths of cubicles and office spaces that comprised the majority of the building. This corporate nightmare repeats itself for nearly every floor of the towering skyscraper. With its sleek, modern architecture and high-tech amenities, SlimeCorp HQ looks nothing like the rest of the city.\nPast countless receptionists' desks, waiting rooms, legal waivers, and at least one or two stainless steel vault doors, lay several slime donation rooms. All that wait for you in these secluded rooms is a reclined medical chair with an attached IV bag and the blinding light of a fluorescent light bulb. If you choose to !donate some of your slime, a SlimeCorp employee will take you to one of these rooms and inform you of the vast and varied uses of SlimeCoin, SlimeCorp’s hot new cryptocurrency.",
		channel = channel_slimecorphq,
		role = "SlimeCorp HQ",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_downtown
	),
	EwPoi( # stock-exchange
		id_poi = poi_id_stockexchange,
		alias = [
			"stocks",
			"stock",
			"exchange",
			"sexchange",
			"stockexchange",
			"slimecorpstockexchange",
			"sex",  # slime's end is "se"
			"sx",
			"scex",
			"scx",
			"findom"
		],
		str_name = "The SlimeCorp Stock Exchange",
		str_desc = "A huge, cluttered space bursting at the seams with teller booths and data screens designed to display market data, blasting precious economic insight into your retinas. Discarded punch cards and ticker tape as trampled on by the mass of investors and shareholders that are constantly screaming \"BUY, SELL, BUY, SELL,\" over and over again at no one in particular. Recently reopened, tents line the streets, filled with eager investors. \n\nExits into Downtown NLACakaNM.",
		channel = channel_stockexchange,
		role = "Stock Exchange",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_downtown
	),
	EwPoi( # the-bazaar
		id_poi = poi_id_bazaar,
		alias = [
			"bazaar",
			"market",
			"bz",
			"b"
		],
		str_name = "The Bazaar",
		str_desc = "An open-air marketplace where professional merchants and regular citizens alike can hock their wares. Its currently completely barren, but what does catch your eye is a stall some weirdo's set up. Apparently his services include prying things off of propstands and luring fish out of their tanks.\n\nExits into Brawlden.",
		channel = channel_bazaar,
		role = "Bazaar",
		pvp = False,
		vendors = [
			vendor_bazaar
		],
		is_subzone = True,
		mother_district = poi_id_smogsburg
	),
	EwPoi( # the-cinema
		id_poi = poi_id_cinema,
		alias = [
			"nlacakanmcinema",
			"cinema",
			"cinemas",
			"theater",
			"movie",
			"movies",
			"nc"
		],
		str_name = "NLACakaNM Cinemas",
		str_desc = "A delightfully run-down movie theater, with warm carpeted walls fraying ever so slightly. Films hand picked by the Rowdy Fucker and/or Cop Killer are regularly screened.\n\nExits into Astatine Heights.",
		channel = channel_cinema,
		role = "Cinema",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_astatineheights
	),
	EwPoi( # food-court
		id_poi = poi_id_foodcourt,
		alias = [
			"thenlacakanmfoodcourt",
			"food",
			"foodcourt",
			"food-court",
			"pizzahut",
			"tacobell",
			"kfc",
			"fcourt",
			"fc",
			"marketmanipulation"
		],
		str_name = "The NLACakaNM Food Court",
		str_desc = "Inside a large shopping mall lies the city’s prized food court. This large, brightly-lit area with tiled walls and floors and numerous clashing, "
				   "gaudy color schemes has probably not been renovated since the ‘90s, which is just the way you like it. You are surrounded on all sides by Yum! Brands "
				   "restaurants, specifically the area is one big combination Pizza Hut/Taco Bell/Kentucky Fried Chicken. In the court’s center lies the esteemed "
				   "Mountain Dew fountain, dispensing that glorious piss yellow elixir for all who patron it. Bustling with life, this is the happeningest place in New Los Angeles City "
				   "aka Neo Milwaukee for a hip juvenile such as yourself. So hang out with your fellow gangsters, soak in the outdated mall music and savor the moment. When you’re old "
				   "and brittle, you’ll wish you spent your time doing this more.\n\nExits into Krak Bay.",
		channel = channel_foodcourt,
		role = "Food Court",
		pvp = False,
		vendors = [
			vendor_pizzahut,
			vendor_tacobell,
			vendor_kfc,
			vendor_mtndew,
		],
		is_subzone = True,
		mother_district = poi_id_krakbay
	),
	EwPoi( # nlac-u
		id_poi = poi_id_nlacu,
		alias = [
			"nlacu",
			"university",
			"nlacuniversity",
			"uni",
			"nu",
			"school",
			"nlac"
		],
		str_name = "New Los Angeles City University",
		str_desc = "An expansive campus housing massive numbers of students and administrators, all here in pursuit of knowledge. The campus is open to visitors, but there's nobody here. **Use '!help' to get info on game mechanics, or '!order' if you want to purchase a game guide.**\n\nExits into Gatlingsdale.",
		channel = channel_nlacu,
		role = "NLAC U",
		pvp = False,
		vendors = [
			vendor_college
		],
		is_subzone = True,
		mother_district = poi_id_gatlingsdale,
		write_manuscript = True,
	),
	EwPoi( # battle-arena
		id_poi = poi_id_arena,
		alias = [
			"thearena",
			"arena",
			"battlearena",
			"a",
			"ba"
		],
		str_name = "The Battle Arena",
		str_desc = "A huge arena stadium capable of housing tens of thousands of battle enthusiasts, ringing a large field where Slimeoid Battles are held. All the seats are empty.\n\nExits into Vandal Park.",
		channel = channel_arena,
		role = "Arena",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_vandalpark
	),
	EwPoi( # the-dojo
		id_poi = poi_id_dojo,
		alias = [
			"dojo",
			"training",
			"sparring",
			"thedojo",
			"td",
			"d"
		],
		str_name = "The Dojo",
		str_desc = "A traditional, modest Dojo, containing all the facilities and armaments necessary for becoming a cold-blooded killing machine. It’s rustic wood presentation is accentuated by bamboo and parchment walls that separate the Dojo floor into large tatami-matted sections. Groups of juveniles gather here to increase their viability in combat. These sparring children are overseen by the owner of the Dojo, an elderly master of martial artists, fittingly known as the Dojo Master. He observes you train from a distance, brooding, and lamenting his lost youth.\n\nExits into South Sleezeborough.",
		channel = channel_dojo,
		role = "Dojo",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_southsleezeborough,
		vendors = [
			vendor_dojo
		]
	),
	EwPoi( # speakeasy
		id_poi = poi_id_speakeasy,
		alias = [
			"kingswifessonspeakeasy",
			"kingswifesson",
			"speakeasy",
			"bar",
			"sons",
			"sez",  # se is already slime's end
			"ez",
			"kws",
			"king",
			"kings"
		],
		str_name = "The King's Wife's Son Speakeasy",
		str_desc = "A rustic tavern with dark wooden walls and floor, bearing innumerable knickknacks on the walls and high wooden stools arranged in front of a bar made of patina'd copper. It is crowded with seedy lowlifes and other generally undesirables, such as yourself.\n\nExits into Vagrant's Corner.",
		channel = channel_speakeasy,
		role = "Speakeasy",
		pvp = False,
		vendors = [
			vendor_bar
		],
		is_subzone = True,
		mother_district = poi_id_vagrantscorner
	),
	EwPoi( # 7-11
		id_poi = poi_id_711,
		alias = [
			"outsidethe7-11",
			"outside7-11",
			"outside711",
			"7-11",
			"711",
			"seveneleven",
			"outsideseveneleven"
		],
		str_name = "Outside the 7-11",
		str_desc = "The darkened derelict 7-11 stands as it always has, a steadfast pillar of NLACakaNM culture. On its dirty exterior walls are spraypainted messages about \"patch notes\", \"github\", and other unparseable nonsense.\n\nExits into Poudrin Alley.",
		channel = channel_711,
		role = "7-11",
		pvp = False,
		vendors = [
			vendor_vendingmachine
		],
		is_subzone = True,
		mother_district = poi_id_poudrinalley
	),
	EwPoi( # the-labs
		id_poi = poi_id_slimeoidlab,
		alias = [
			"lab",
			"labs",
			"laboratory",
			"slimecorpslimeoidlaboratory",
			"slimecorpslimeoidlab",
			"slimecorplab",
			"slimecorplabs",
			"slimeoidlaboratory",
			"slimeoidlab",
			"slimeoidlabs",
			"slab",
			"sl",
			"slimeoid"
		],
		str_name = "SlimeCorp Slimeoid Laboratory",
		str_desc = "A nondescript building containing mysterious SlimeCorp industrial equipment. Large glass tubes and metallic vats seem to be designed to serve as incubators. There is a notice from SlimeCorp on the entranceway explaining the use of its equipment. Use !instructions to read it.\nPast countless receptionists' desks, Slimeoid incubation tubes, legal waivers, and down at least one or two secured elevator shafts, lay several mutation test chambers. All that wait for you in these secluded rooms is a reclined medical chair with an attached IV bag and the blinding light of a futuristic neon LED display which has a hundred different PoweShell windows open that are all running Discord bots. If you choose to tinker with mutations, a SlimeCorp employee will take you to one of these rooms and inform you of the vast and varied ways they can legally fuck with your body's chemistry.\n\nExits into Brawlden.",
		channel = channel_slimeoidlab,
		role = "Slimeoid Lab",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_brawlden
	),
	EwPoi( # the-mines
		id_poi = poi_id_mine,
		alias = [
			"mines",
			"mine",
			"m",
			"tm",
			"jrm"
		],
		str_name = "The Mines",
		str_desc = "A veritable slime-mine of slime, rejuvinated by the revival of ENDLESS WAR.\n\nExits into Juvie's Row.",
		channel = channel_mines,
		role = "Mines",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_juviesrow
	),
	EwPoi( # the-casino
		id_poi = poi_id_thecasino,
		alias = [
			"casino",
			"slimecasino",
			"theslimecasino",
			"tc",  # the casino
			"cas",
			"c",
			"scs"
		],
		str_name = "The SlimeCorp Casino",
		str_desc = "The casino is filled with tables and machines for playing games of chance, and garishly decorated wall-to-wall. Lights which normally flash constantly cover everything, but now they all sit unlit. What's worse, you can see Sherman, the SlimeCorp salaryman staring you down near the back.\n\nExits into Green Light District.",
		channel = channel_casino,
		role = "Casino",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_greenlightdistrict
	),
	EwPoi(  # cratersville mines
		id_poi = poi_id_cv_mines,
		alias = [
			"mines2",
			"cvmines",
			"cmines",
			"cvm",
			"cm",
			"cratersvillemine",
			"cratersvillem"
		],
		str_name = "The Cratersville Mines",
		str_desc = "A veritable slime-mine of slime, rejuvenated by the revival of ENDLESS WAR.\n\nExits into Cratersville.",
		channel = channel_cv_mines,
		role = "Cratersville Mines",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_cratersville
	),
	EwPoi(  # toxington mines
		id_poi = poi_id_tt_mines,
		alias = [
			"mines3",
			"ttmines",
			"ttm",
			"toxm",
			"toxingtonmine",
			"toxingtonm"
		],
		str_name = "The Toxington Mines",
		str_desc = "A veritable slime-mine of slime, rejuvinated by the revival of ENDLESS WAR.\n\nExits into Toxington.",
		channel = channel_tt_mines,
		role = "Toxington Mines",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_toxington
	),
	EwPoi( # smokers-cough
		id_poi = poi_id_diner,
		alias = [
			"diner",
			"smokers",
			"cough",
			"smc",
			"sc",
			"rf", #rowdy food
			"sm",
			"koff"
		],
		str_name = "The Smoker's Cough",
		str_desc = "A quaint hole-in-the-wall vintage diner. The wallpaper may be peeling and the ‘80s paint job might be faded, but you’ll be damned if this place didn’t make an aesthetic stomping grounds for cheapskate juveniles like yourself. All the staff know you by name, they’ve memorized your order, and frankly they love you. You’re like a ninth son to the inbred owner and his many, many wives. It’s a cramped space, only fitting about 20 people maximum. The fluorescent lighting from the ceiling lamps invade every nook and cranny of the cyan and purple diner, even when the natural daylight could easily illuminate it just as well. You think you can see some mold on certain corners of the floor. Oh man, so cool.\n\nExits into Wreckington.",
		channel = channel_diner,
		role = "Smoker's Cough",
		pvp = False,
		vendors = [
			vendor_diner
		],
		is_subzone = True,
		mother_district = poi_id_wreckington
	),
	EwPoi( # Red Mobster
		id_poi = poi_id_seafood,
		alias = [
			"seafood",
			"redmobster",
			"red",
			"mobster",
			"rm",
			"mob",
			"kf" #killer food
		],
		str_name = "Red Mobster Seafood",
		str_desc = "The last bastion of sophistication in this godforsaken city. A dimly lit, atmospheric fine dining restaurant with waiters and tables and archaic stuff like that. Upper crust juveniles and older fugitives make up the majority of the patrons, making you stick out like a sore thumb. Quiet, respectable murmurs pollute the air alongside the scrapping of silverware and the occasional hoity toity laugh. Everything about this place makes you sick.\n\nExits into Astatine Heights.",
		channel = channel_seafood,
		role = "Red Mobster Seafood",
		pvp = False,
		vendors = [
			vendor_seafood
		],
		is_subzone = True,
		mother_district = poi_id_astatineheights
	),
	EwPoi( # JR Farm
		id_poi = poi_id_jr_farms,
		alias = [
			"jrf", #juviesrow farms
			"jrp", #juviesrow plantation
			"jrfarms",
			"jrfarm",
			"jrplantation",
			"jrplant",
			"juviesrowf",
			"juviesrowfarm"
		],
		str_name = "The Juvie's Row Farms",
		str_desc = "An array of haphazardly placed farms dot the already dense, crowded areas between mining shaft entrances and impoverished juvenile housing. Pollution is rampant here, with the numerous trash heaps and sludge refineries enjoying the majority of earth under the smoke-smuggered stars. It’s soil is irradiated and barely arable, but it will do. It has to.\n\nExits into Juvie's Row.",
		channel = channel_jr_farms,
		role = "Juvie's Row Farms",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_juviesrow
	),
	EwPoi( # OG Farm
		id_poi = poi_id_og_farms,
		alias = [
			"ogf",  # OozeGardens farms
			"ogp",  # OozeGardens plantation
			"ogfarms",
			"ogfarm",
			"ogplantation",
			"ogplant",
			"oozegardenfarms",
			"oozegardenfarm",
			"oozegardensf",
			"oozegardensfarm"
		],
		str_name = "The Ooze Gardens Farms",
		str_desc = "An impressive host of unique and exotic flora are grown here. Originally on private property, the expansive greenhouses were the weekly meeting place for the city’s botanical society. They have since been seized by imminent domain and are now a public park. It’s type of soil is vast and varied depending on where you choose to plant. Surely, anything can grow here.\n\nExits into Ooze Gardens.",
		channel = channel_og_farms,
		role = "Ooze Gardens Farms",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_oozegardens
	),
	EwPoi( # AB Farm
		id_poi = poi_id_ab_farms,
		alias = [
			"abf", #ArsonBrook farms
			"abp", #ArsonBrook plantation
			"abfarms",
			"abfarm",
			"abplantation",
			"abplant",
			"arsonbrookf",
			"arsonbrookfarm"
		],
		str_name = "The Arsonbrook Farms",
		str_desc = "A series of reedy creeks interspersed with quiet farms and burnt, black trees. It’s overcast skies make the embers from frequent forest fires glow even brighter by comparison. It’s soil is fertile with copious amounts of soot and accompanying nutrients.\n\nExits into Arsonbrook.",
		channel = channel_ab_farms,
		role = "Arsonbrook Farms",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_arsonbrook
	),
	EwPoi(  # Neo Milwaukee State
		id_poi = poi_id_neomilwaukeestate,
		alias = [
			"neomilwaukee",
			"state",
			"college",
			"nms",
		],
		str_name = "Neo Milwaukee State",
		str_desc = "An abysmally funded public college, with a student body of high school has-beens and future gas station attendants. With nearly a 100% acceptance rate, it’s needless to say that the riff raff is not kept out of this seedy establishment. People are here to stumble through their meaningless lives, chasing normality and appeasing their poor parent’s ideas of success by enrolling in the first college they get accepted to and walking out four years later with thousands of dollars of debt and a BA in English. No one here is excited to learn, no one is excited to teach, no one is excited for anything here. They all just want to die, and thankfully they will someday. **Use '!help' to get info on game mechanics, or '!order' if you want to purchase a game guide.**\n\nExits into North Sleezeborough. ",
		channel = channel_neomilwaukeestate,
		role = "Neo Milwaukee State",
		pvp = False,
		vendors = [
			vendor_college
		],
		is_subzone = True,
		mother_district = poi_id_northsleezeborough,
		write_manuscript = True,
	),
	EwPoi(  # Assault Flats Beach Resort
		id_poi = poi_id_beachresort,
		alias = [
			"resort",
			"br",
			"r",
		],
		str_name = "The Resort",
		str_desc = "The interior is lavishly decorated with all manner of tropically-inspired furnishings, all beautifully maintained with nary a speck of grime staining it’s pristine off-white walls. Exotic potted plants and natural lighting fill the hallways, which all smell like the inside of a women’s body wash bottle. Palm trees seemingly occupy half of the outside land on the complex, averaging about 2 feet apart from one another at most to your calculations. Imported red sand of the beach stretches toward the horizon, lapped by gentle waves of slime. Couples enjoy slima coladas and tanning by the slime pool. This place fucking disgusts you. Is… is that a stegosaurus in the distance?\n\nExits into Assault Flats Beach.",
		channel = channel_beachresort,
		role = "Beach Resort",
		pvp = False,
		vendors = [
			vendor_beachresort
		],
		is_subzone = True,
		mother_district = poi_id_assaultflatsbeach
	),
	EwPoi(  # Dreadford Country Club
		id_poi = poi_id_countryclub,
		alias = [
			"country",
			"club",
			"cc",
		],
		str_name = "The Country Club",
		str_desc = "On top of a grassy hill, behind several wired/eletric fences, lies Dreadford’s famous country club. The lodge itself is a huge, old wooden lodge from the 1800s, with hundreds of knick-knacks, hunting trophies and historic photos hung up on the wall, and tacky rugs and furniture around a roaring fire in it’s center. Sprawling out from the club itself is the complex’s signature golf course, where all the pompous rich assholes go to waste their time and chit-chat with each other about cheating on their wives.\n\nExits into Dreadford.",
		channel = channel_countryclub,
		role = "Country Club",
		pvp = False,
		vendors = [
			vendor_countryclub
		],
		is_subzone = True,
		mother_district = poi_id_dreadford
	),
	EwPoi(  # SlimeCorp Recycling Plant
		id_poi = poi_id_recyclingplant,
		alias = [
			"slimecorprecyclingplant",
			"recyclingplant",
			"recycling",
			"recycle",
			"burntrash",
			"scrp",
			"rp",
		],
		str_name = "The SlimeCorp Recycling Plant",
		str_desc = "It looks like just another blocky building with a huge chimney contributing to Smogsburg's unique air quality, but the SlimeCorp marketing assures you that this plant in fact contains the latest in recycling technology, able to automatically sort and sustainably process any item. Whatever this technology may entail, it sure smells a lot like burning trash.\n\nExits into Smogsburg.",
		channel = channel_recyclingplant,
		role = "Recycling Plant",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_smogsburg
	),
	EwPoi(  # Toxington Pier
		id_poi = poi_id_toxington_pier,
		alias = [
			"toxingtonpier",
			"ttpier",
			"ttp",
		],
		str_name = "Toxington Pier",
		str_desc = "A rickety, decaying pier stretching over a bubbling lake of molten slime. Use of your olfactory organs in any capacity is not recommended, the toxic fumes this district is known for originate here, from these lakes. But, there are some pretty sicknasty fuckin’ fishes down there, you bet.\n\nExits into Toxington.",
		channel = channel_tt_pier,
		role = "Toxington Pier",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_toxington,
		is_pier = True,
		pier_type = fish_slime_freshwater
	),
	EwPoi(  # Jaywalker Plain Pier
		id_poi = poi_id_jaywalkerplain_pier,
		alias = [
			"jaywalkerplainpier",
			"jppier",
			"jpp",
		],
		str_name = "Jaywalker Plain Pier",
		str_desc = "An old, sundrenched pier stretching over a lake overgrown with reeds and similar vegetation. It’s just one of the many natural beauties overlooked by the district’s perpetually twisted (a colloquialism for being drunk and high at the same time) population.\n\nExits into Jaywalker Plain.",
		channel = channel_jp_pier,
		role = "Jaywalker Plain Pier",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_jaywalkerplain,
		is_pier = True,
		pier_type = fish_slime_freshwater

	),
	EwPoi(  # Crookline Pier
		id_poi = poi_id_crookline_pier,
		alias = [
			"crooklinepier",
			"clpier",
			"clp",
		],
		str_name = "Crookline Pier",
		str_desc = "A dark, modern pier stretching over a large lake on the outskirts of the district. Bait shops and other aquatic-based stores surround the water, with the occasional restaurant breaking up the monotony.\n\nExits into Crookline.",
		channel = channel_cl_pier,
		role = "Crookline Pier",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_crookline,
		is_pier = True,
		pier_type = fish_slime_freshwater

	),
	EwPoi(  # Assault Flats Beach Pier
		id_poi = poi_id_assaultflatsbeach_pier,
		alias = [
			"assaultflatsbeachpier",
			"afbpier",
			"afbp",
		],
		str_name = "Assault Flats Beach Pier",
		str_desc = "A white, picturesque wooden pier stretching far out into the Slime Sea. This famous landmark is a common destination for robber barons on vacation, with a various roller coasters and rides occupying large parts of the pier. It’s really fucking lame, and you feel sick thinking about the astronomical slime the yuppies around you have ontained solely through inhereitance. You vow to piss on the ferris wheel if you get the proper mutations.\n\nExits into Assault Flats Beach.",
		channel = channel_afb_pier,
		role = "Assault Flats Beach Pier",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_assaultflatsbeach,
		is_pier = True,
		pier_type = fish_slime_saltwater

	),
	# EwPoi(  # Vagrant's Corner Pier
	# 	id_poi = poi_id_vagrantscorner_pier,
	# 	alias = [
	# 		"vagrantscornerpier",
	# 		"vcpier",
	# 		"vcpr",
	# 	],
	# 	str_name = "Vagrant's Corner Pier",
	# 	str_desc = "One of many long, seedy wooden piers stretching out into the Slime Sea from the Vagrant’s Corner wharf. Fishermen and sailors off-duty all fish and get drunk around you, singing jaunty tunes and cursing loudly for minor inconveniences. A few fights break out seemingly just for fun. This is your kinda place!\n\nExits into Vagrant's Corner.",
	# 	channel = channel_vc_pier,
	# 	role = "Vagrant's Corner Pier",
	# 	pvp = False,
	# 	is_subzone = True,
	# 	mother_district = poi_id_vagrantscorner,
	# 	is_pier = True,
	# 	pier_type = fish_slime_saltwater
	#
	# ),
	EwPoi(  # Juvie's Row Pier
		id_poi = poi_id_juviesrow_pier,
		alias = [
			"juviesrowpier",
			"jrpier",
			"jrpr",
		],
		str_name = "Juvie's Row Pier",
		str_desc = "One of many long, seedy wooden piers stretching out into the Slime Sea from the Juvie's Row wharf. A few fishermen and off-duty sailors from nearby Vagrant's Corner all fish and get drunk around you, singing jaunty tunes and cursing loudly. A few fights break out seemingly just for fun. This is your kinda place!\n\nExits into Juvie's Row.",
		channel = channel_jr_pier,
		role = "Juvie's Row Pier",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_juviesrow,
		is_pier = True,
		pier_type = fish_slime_saltwater

	),
	EwPoi(  # Slime's End Pier
		id_poi = poi_id_slimesend_pier,
		alias = [
			"slimesendpier",
			"sepier",
			"sep",
		],
		str_name = "Slime's End Pier",
		str_desc = "A lonesome pier at the very end of the Slime’s End peninsula, stretching out into the Slime Sea. From here, you’re able to clearly make out Downtown in the distance, pumping light pollution into the normally polluted air. You’re itching to get back there and punch some grandmas once you’re done wringing slime out of fish.\n\nExits into Slime's End.",
		channel = channel_se_pier,
		role = "Slime's End Pier",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_slimesend,
		is_pier = True,
		pier_type = fish_slime_saltwater

	),
	EwPoi( # Slime Sea
		id_poi = poi_id_slimesea,
		str_name = "The Slime Sea",
		str_desc = "Slime as far as the eye can see.",
		channel = channel_slimesea,
		role = "Slime Sea",
		pvp = True
	),
	EwPoi(  # Wreckington Ferry Port
		id_poi = poi_id_wt_port,
		alias = [
			"wreckingtonport",
			"wtport",
			"wreckingtonferry",
			"wtferry",
			"wtp",
			"wtfp",
			"wf"
		],
		str_name = "The Wreckington Ferry Port",
		str_desc = "Caddy corner to Wreckington’s iconic junkyard lies its less famous shipyard, filled mostly with dozens upon dozens of different garbage barges dumping off metric tons of trash every day but also hosting this very terminal! The ferry takes you from here to Vagrant’s Corner, so just head there like you would any other district and you’ll hop on the ferry. Nifty!\n\nExits into Wreckington.",
		channel = channel_wt_port,
		role = "Wreckington Port",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_wreckington,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Vagrant's Corner Ferry Port
		id_poi = poi_id_vc_port,
		alias = [
			"vagrantscornerport",
			"vagrantsport",
			"vcport",
			"vagrantscornerferry",
			"vcferry",
			"vcp",
			"vcfp",
			"vf"
		],
		str_name = "The Vagrant's Corner Ferry Port",
		str_desc = "Down one of hundreds of piers on the crowded Vagrant’s Corner wharf sits this dingy dinghy terminal. The ferry takes you from here to Wreckington, so just head there like you would any other district and you’ll hop on the ferry. Nifty!\n\nExits into Vagrant's Corner.",
		channel = channel_vc_port,
		role = "Vagrant's Corner Port",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_vagrantscorner,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Toxington Subway Station
		id_poi = poi_id_tt_subway_station,
		alias = [
			"toxingtonsubway",
			"toxingtonsub",
			"toxingtonstation",
			"toxsubwaystation",
			"toxsubway",
			"toxsub",
			"toxstation",
			"ttsubwaystation",
			"ttsubway",
			"ttsub",
			"ttstation",
			"toxs",
			"tts"
		],
		str_name = "The Toxington Subway Station",
				str_desc = str_red_subway_station_description + "\n\nExits into Toxington.",
		channel = channel_tt_subway_station,
		role = "Toxington Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_toxington,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Astatine Heights Subway Station
		id_poi = poi_id_ah_subway_station,
		alias = [
			"astatineheightssubway",
			"astatineheightssub",
			"astatineheightsstation",
			"astatinesubwaystation",
			"astatinesubway",
			"astatinesub",
			"astatinestation",
			"ahsubwaystation",
			"ahsubway",
			"ahsub",
			"ahstation",
			"astatines",
			"ahs"
		],
		str_name = "The Astatine Heights Subway Station",
		str_desc = str_red_subway_station_description + "\n\nExits into Astatine Heights.",
		channel = channel_ah_subway_station,
		role = "Astatine Heights Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_astatineheights,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Gatlingsdale Subway Station
		id_poi = poi_id_gd_subway_station,
		alias = [
			"gatlingsdalesubway",
			"gatlingsdalesub",
			"gatlingsdalestation",
			"gatlingssubwaystation",
			"gatlingssubway",
			"gatlingssub",
			"gatlingsstation",
			"gdsubwaystation",
			"gdsubway",
			"gdsub",
			"gdstation",
			"gatlingss",
			"gds"
		],
		str_name = "The Gatlingsdale Subway Station",
		str_desc = str_red_subway_station_description + "\n\nExits into Gatlingsdale.",
		channel = channel_gd_subway_station,
		role = "Gatlingsdale Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_gatlingsdale,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Arsonbrook Subway Station
		id_poi = poi_id_ab_subway_station,
		alias = [
			"arsonbrooksubway",
			"arsonbrooksub",
			"arsonbrookstation",
			"arsonsubwaystation",
			"arsonsubway",
			"arsonsub",
			"arsonstation",
			"absubwaystation",
			"absubway",
			"absub",
			"abstation",
			"arsons",
			"abs"
		],
		str_name = "The Arsonbrook Subway Station",
		str_desc = str_yellow_subway_station_description + "\n\nExits into Arsonbrook.",
		channel = channel_ab_subway_station,
		role = "Arsonbrook Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_arsonbrook,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Cop Killtown Subway Station
		id_poi = poi_id_ck_subway_station,
		alias = [
			"copkilltownsubway",
			"copkilltownsub",
			"copkilltownstation",
			"copkillsubwaystation",
			"copkillsubway",
			"copkillsub",
			"copkillstation",
			"cksubwaystation",
			"cksubway",
			"cksub",
			"ckstation",
			"copkills",
			"cks",
			"cs"
		],
		str_name = "The Cop Killtown Subway Station",
		str_desc = str_red_subway_station_description + "\n\nExits into Cop Killtown.",
		channel = channel_ck_subway_station,
		role = "Cop Killtown Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_copkilltown,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Smogsburg Subway Station
		id_poi = poi_id_sb_subway_station,
		alias = [
			"smogsburgsubway",
			"smogsburgsub",
			"smogsburgstation",
			"smogssubwaystation",
			"smogssubway",
			"smogssub",
			"smogsstation",
			"sbsubwaystation",
			"sbsubway",
			"sbsub",
			"sbstation",
			"smogss",
			"sbs"
		],
		str_name = "The Smogsburg Subway Station",
		str_desc = str_green_subway_station_description + \
						"\n\n" + str_subway_connecting_sentence.format("yellow") + \
						"\n\n" + str_yellow_subway_station_description \
			+ "\n\nExits into Smogsburg.",
		channel = channel_sb_subway_station,
		role = "Smogsburg Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_smogsburg,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Downtown Subway Station
		id_poi = poi_id_dt_subway_station,
		alias = [
			"downtownsubway",
			"downtownsub",
			"downtownstation",
			"dtsubwaystation",
			"dtsubway",
			"dtsub",
			"dtstation",
			"dts"
		],
		str_name = "The Downtown NLACakaNM Subway Station",
		str_desc = str_downtown_station_description,
		channel = channel_dt_subway_station,
		role = "Downtown Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_downtown,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Krak Bay Subway Station
		id_poi = poi_id_kb_subway_station,
		alias = [
			"krakbaysubway",
			"krakbaysub",
			"krakbaystation",
			"kraksubwaystation",
			"kraksubway",
			"kraksub",
			"krakstation",
			"kbsubwaystation",
			"kbsubway",
			"kbsub",
			"kbstation",
			"kraks",
			"kbs"
		],
		str_name = "The Krak Bay Subway Station",
		str_desc = str_green_subway_station_description + \
						"\n\n" + str_subway_connecting_sentence.format("yellow") + \
						"\n\n" + str_yellow_subway_station_description + \
			"\n\nExits into Krak Bay.",
		channel = channel_kb_subway_station,
		role = "Krak Bay Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_krakbay,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Glocksbury Subway Station
		id_poi = poi_id_gb_subway_station,
		alias = [
			"glocksburysubway",
			"glocksburysub",
			"glocksburystation",
			"glockssubwaystation",
			"glockssubway",
			"glockssub",
			"glocksstation",
			"gbsubwaystation",
			"gbsubway",
			"gbsub",
			"gbstation",
			"glockss",
			"gbs"
		],
		str_name = "The Glocksbury Subway Station",
		str_desc = str_green_subway_station_description + "\n\nExits into Glocksbury.",
		channel = channel_gb_subway_station,
		role = "Glocksbury Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_glocksbury,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # West Glocksbury Subway Station
		id_poi = poi_id_wgb_subway_station,
		alias = [
			"westglocksburysubway",
			"westglocksburysub",
			"westglocksburystation",
			"westglockssubwaystation",
			"westglockssubway",
			"westglockssub",
			"westglocksstation",
			"wgbsubwaystation",
			"wgbsubway",
			"wgbsub",
			"wgbstation",
			"westglockss",
			"wgbs"
		],
		str_name = "The West Glocksbury Subway Station",
		str_desc = str_green_subway_station_description + "\n\nExits into West Glocksbury.",
		channel = channel_wgb_subway_station,
		role = "West Glocksbury Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_westglocksbury,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Jaywalker Plain Subway Station
		id_poi = poi_id_jp_subway_station,
		alias = [
			"jaywalkerplainsubway",
			"jaywalkerplainsub",
			"jaywalkerplainstation",
			"jaywalkersubwaystation",
			"jaywalkersubway",
			"jaywalkersub",
			"jaywalkerstation",
			"jpsubwaystation",
			"jpsubway",
			"jpsub",
			"jpstation",
			"jaywalkers",
			"jps"
		],
		str_name = "The Jaywalker Plain Subway Station",
		str_desc = str_green_subway_station_description + "\n\nExits into Jaywalker Plain.",
		channel = channel_jp_subway_station,
		role = "Jaywalker Plain Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_jaywalkerplain,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # North Sleezeborough Subway Station
		id_poi = poi_id_nsb_subway_station,
		alias = [
			"northsleezeboroughsubwaystation",
			"northsleezeboroughsubway",
			"northsleezeboroughsub",
			"northsleezeboroughstation",
			"northsleezesubwaystation",
			"northsleezesubway",
			"northsleezesub",
			"northsleezestation",
			"nsbsubwaystation",
			"nsbsubway",
			"nsbsub",
			"nsbstation",
			"northsleezes",
			"nsbs"
		],
		str_name = "The North Sleezeborough Subway Station",
		str_desc = str_green_subway_station_description + "\n\nExits into North Sleezeborough.",
		channel = channel_nsb_subway_station,
		role = "North Sleezeborough Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_northsleezeborough,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # South Sleezeborough Subway Station
		id_poi = poi_id_ssb_subway_station,
		alias = [
			"southsleezeboroughsubwaystation",
			"southsleezeboroughsubway",
			"southsleezeboroughsub",
			"southsleezeboroughstation",
			"southsleezesubwaystation",
			"southsleezesubway",
			"southsleezesub",
			"southsleezestation",
			"ssbsubwaystation",
			"ssbsubway",
			"ssbsub",
			"ssbstation",
			"southsleezes",
			"ssbs"
		],
		str_name = "The South Sleezeborough Subway Station",
		str_desc = str_yellow_subway_station_description + "\n\nExits into South Sleezeborough.",
		channel = channel_ssb_subway_station,
		role = "South Sleezeborough Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_southsleezeborough,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Cratersville Subway Station
		id_poi = poi_id_cv_subway_station,
		alias = [
			"cratersvillesubway",
			"cratersvillesub",
			"cratersvillestation",
			"craterssubwaystation",
			"craterssubway",
			"craterssub",
			"cratersstation",
			"cvsubwaystation",
			"cvsubway",
			"cvsub",
			"cvstation",
			"craterss",
			"cvs"
		],
		str_name = "The Cratersville Subway Station",
		str_desc = str_red_subway_station_description + "\n\nExits into Cratersville.",
		channel = channel_cv_subway_station,
		role = "Cratersville Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_cratersville,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Wreckington Subway Station
		id_poi = poi_id_wt_subway_station,
		alias = [
			"wreckingtonsubway",
			"wreckingtonsub",
			"wreckingtonstation",
			"wrecksubwaystation",
			"wrecksubway",
			"wrecksub",
			"wreckstation",
			"wtsubwaystation",
			"wtsubway",
			"wtsub",
			"wtstation",
			"wrecks",
			"wts"
		],
		str_name = "The Wreckington Subway Station",
		str_desc = str_red_subway_station_description + "\n\nExits into Wreckington.",
		channel = channel_wt_subway_station,
		role = "Wreckington Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_wreckington,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Rowdy Roughhouse Subway Station
		id_poi = poi_id_rr_subway_station,
		alias = [
			"rowdyroughhousesubway",
			"rowdyroughhousesub",
			"rowdyroughhousestation",
			"rowdysubwaystation",
			"rowdysubway",
			"rowdysub",
			"rowdystation",
			"rrsubwaystation",
			"rrsubway",
			"rrsub",
			"rrstation",
			"rrs"
		],
		str_name = "The Rowdy Roughhouse Subway Station",
		str_desc = str_red_subway_station_description + "\n\nExits into Rowdy Roughhouse.",
		channel = channel_rr_subway_station,
		role = "Rowdy Roughhouse Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_rowdyroughhouse,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Green Light District Subway Station
		id_poi = poi_id_gld_subway_station,
		alias = [
			"greenlightdistrictsubwaystation",
			"greenlightdistrictsubway",
			"greenlightdistrictsub",
			"greenlightdistrictstation",
			"greenlightsubwaystation",
			"greenlightsubway",
			"greenlightsub",
			"greenlightstation",
			"gldsubwaystation",
			"gldsubway",
			"gldsub",
			"gldstation",
			"greenlights",
			"glds"
		],
		str_name = "The Green Light District Subway Station",
		str_desc = str_blue_subway_station_description + "\n\nExits into Green Light District.",
		channel = channel_gld_subway_station,
		role = "Green Light District Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_greenlightdistrict,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Juvie's Row Subway Station
		id_poi = poi_id_jr_subway_station,
		alias = [
			"juviesrowsubway",
			"juviesrowsub",
			"juviesrowstation",
			"juviessubwaystation",
			"juviessubway",
			"juviessub",
			"juviesstation",
			"jrsubwaystation",
			"jrsubway",
			"jrsub",
			"jrstation",
			"juviess",
			"jrs"
		],
		str_name = "The Juvie's Row Subway Station",
		str_desc = str_blue_subway_station_description + "\n\nExits into Juvie's Row.",
		channel = channel_jr_subway_station,
		role = "Juvie's Row Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_juviesrow,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Vagrant's Corner Subway Station
		id_poi = poi_id_vc_subway_station,
		alias = [
			"vagrantscornersubway",
			"vagrantscornersub",
			"vagrantscornerstation",
			"vagrantssubwaystation",
			"vagrantssubway",
			"vagrantssub",
			"vagrantsstation",
			"vcsubwaystation",
			"vcsubway",
			"vcsub",
			"vcstation",
			"vagrantss",
			"vcs"
		],
		str_name = "The Vagrant's Corner Subway Station",
		str_desc = str_blue_subway_station_description + "\n\nExits into Vagrant's Corner.",
		channel = channel_vc_subway_station,
		role = "Vagrant's Corner Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_vagrantscorner,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Assault Flats Beach Subway Station
		id_poi = poi_id_afb_subway_station,
		alias = [
			"assaultflatsbeachsubwaystation",
			"assaultflatsbeachsubway",
			"assaultflatsbeachsub",
			"assaultflatsbeachstation",
			"assaultflatssubwaystation",
			"assaultflatssubway",
			"assaultflatssub",
			"assaultflatsstation",
			"beachsubwaystation",
			"beachsubway",
			"beachsub",
			"beachstation",
			"afbsubwaystation",
			"afbsubway",
			"afbsub",
			"afbstation",
			"assaultflatss",
			"afbs"
		],
		str_name = "The Assault Flats Beach Subway Station",
		str_desc = str_blue_subway_station_description + "\n\nExits into Assault Flats Beach.",
		channel = channel_afb_subway_station,
		role = "Assault Flats Beach Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_assaultflatsbeach,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Dreadford Blimp Tower
		id_poi = poi_id_df_blimp_tower,
		alias = [
			"dreadfordblimptower",
			"dreadfordhblimp",
			"dreadfordtower",
			"dreadblimptower",
			"dreadblimp",
			"dreadtower",
			"dfblimptower",
			"dfblimp",
			"dftower"
		],
		str_name = "The Dreadford Blimp Tower",
		str_desc = str_blimp_tower_description + "\n\nExits into Dreadford.",
		channel = channel_df_blimp_tower,
		role = "Dreadford Blimp Tower",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_dreadford,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Assault Flats Beach Blimp Tower
		id_poi = poi_id_afb_blimp_tower,
		alias = [
			"assaultflatsbeachblimptower",
			"assaultflatsbeachblimp",
			"assaultflatsbeachtower",
			"assaultflatsblimptower",
			"assaultflatsblimp",
			"assaultflatstower",
			"beachblimptower",
			"beachblimp",
			"beachtower",
			"afbblimptower",
			"afbblimp",
			"afbtower"
		],
		str_name = "The Assault Flats Beach Blimp Tower",
		str_desc = str_blimp_tower_description + "\n\nExits into Assault Flats Beach.",
		channel = channel_afb_blimp_tower,
		role = "Assault Flats Beach Blimp Tower",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_assaultflatsbeach,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi( # realestate
		id_poi = poi_id_realestate,
		alias = [
			"realestate",
			"rea",
			"realtor",
			"landlord",
			"scre",
			"apartmentagency",
			"realestateagent"
		],
		str_name = "SlimeCorp Real Estate Agency",
		str_desc = "The sleek glass walls and cold, green tile flooring give the place an intimidating presence. That is, if it weren't for the disheveled drunk fellow sitting on the reception desk ahead of you. A huge 3-D SlimeCorp logo hangs off the ceiling above his head.\n\nExits into Old New Yonkers.",
		pvp = False,
		channel = channel_realestateagency,
		role = "Real Estate Agency",
		mother_district = poi_id_oldnewyonkers,
		is_subzone = True
	),
	EwPoi( # Glocksbury Comics
		id_poi = poi_id_glocksburycomics,
		alias = [
			"gbc",
			"gc",
			"glocksburycomics",
			"comicstore",
			"comics",
			"cardshop",
			"card shop",
		],
		str_name = "Glocksbury Comics",
		str_desc = "The walls and booths are plastered with various Secreature:tm: paraphernalia, ranging from comic books, to music CDs, to cheap plastic figurines, and of course, trading cards. This place has it all, and then some. The store itself seems to have a very labyrinthian structure, with different sections of the store devoted to secreatures merging with each other, like some kind of modern day winchester house. Near the front register, manned by a balding gentleman almost certainly in his early-to-mid 30s, you notice that they're also selling... slimecorp-brand body spray? You dread the thought of the stench such a thing emits.\n\nExits into Glocksbury.",
		pvp = False,
		vendors = [vendor_glocksburycomics],
		channel = "glocksbury-comics",
		role = "Glocksbury Comics",
		mother_district = poi_id_glocksbury,
		is_subzone = True,
		write_manuscript = True,
	),
	EwPoi( # Slimy Persuits
		id_poi=poi_id_slimypersuits,
		alias=[
			"sp",
			"slimypersuits",
			"slimeypersuits",
			"candystore",
			"candyshop",
			"candy store",
			"candy shop",
		],
		str_name="Slimy Persuits",
		str_desc="It's a vintage style candy store, and on top of that an ice-cream parlour. Sugary delicacies line the displays, giving the whole place an inviting presence and sweet scent. One of the signs on the walls tells of their signature product, the Slime Sours. Apprently they're made almost entirely by hand, and a lot of the other products in the store seem to fit that bill as well. In a post-apocalyptic hellscape like NLACakaNM, it seems some traditions have still survived.\n\nExits into New New Yonkers.",
		pvp=False,
		vendors=[vendor_slimypersuits],
		channel="slimy-persuits",
		role="Slimy Persuits",
		mother_district=poi_id_newnewyonkers,
		is_subzone=True
	),
	EwPoi(  # Green Cake Cafe
		id_poi=poi_id_greencakecafe,
		alias=[
			"gcc",
			"cafe",
			"greencake",
			"green",
			"cake"
		],
		str_name="Green Cake Cafe",
		str_desc="Deeply nestled in the vandalized, sparsely populated buildings of Little Chernobyl lays a stubby building covered in vines, spray paint, and posters for criminals and concerts that have both long since passed. It seems the recently realized population of authors in the city has taken this irradiated little dump to be a safe haven from the general noisiness of the other districts in the city. Little do they know, the consequences of spending most of your time in Little Chernobyl will far exceed tinnitus in the long-term, but for now the Green Cake Cafe is where hipsters of all varieties want to write their zine opus while drinking a fresh cup of goolong tea served by the seven-eyed waitress.\n\nExits into Little Chernobyl.",
		pvp=False,
		vendors=[vendor_greencakecafe],
		channel="green-cake-cafe",
		role="Green Cake Cafe",
		mother_district=poi_id_littlechernobyl,
		is_subzone=True,
		write_manuscript=True,
	),
	EwPoi(
		id_poi=poi_id_sodafountain,
		alias=[
			"tsf",
			"soda",
			"fountain",
			"bicarbonate",
			"newgameplus"
		],
		str_name="The Bicarbonate Soda Fountain",
		str_desc="A sickening display of worship recently and secretly installed by those who wish to pay tribute to that blue cartoon, the one that's plagued our city for Slime Invictus knows HOW long. Legends say you can offer up your slime and !purify yourself with the deadly waters that fluctuate in, out, and around the fountain. Even THINKING about the act of doing such a thing makes you SICK... or, maybe not? There's no shame in trying something you've never tried before, you think to yourself.\n\nExits into Krak Bay.",
		pvp=False,
		channel=channel_sodafountain,
		role="The Bicarbonate Soda Fountain",
		mother_district=poi_id_krakbay,
		is_subzone=True
	),
	EwPoi(  # Ferry
		id_poi = poi_id_ferry,
		alias = [
			"boat",
			"f"
		],
		str_name = "The Ferry",
		str_desc = "A modest two-story passenger ferry, built probably 80 years ago. Its faded paint is starting to crack and its creaky wood benches aren’t exactly comfortable. Though it’s not much to look at, you still love riding it. Out here, all you have to think about is the cool wind in your hair, the bright green glow of the Slime Sea searing your eyes, and the New Los Angeles City aka Neo Milwaukee skyline in the distance. You plug in earbuds to drown out the sea captain’s embarrassing Jungle Cruise-tier commentary over the microphone. Good times.",
		channel = channel_ferry,
		role = "Ferry",
		pvp = True,
		is_transport = True,
		transport_type = transport_type_ferry,
		default_line = transport_line_ferry_wt_to_vc,
		default_stop = poi_id_wt_port,
		is_pier = True,
		pier_type = fish_slime_saltwater

	),
	EwPoi(  # Subway train on the red line
		id_poi = poi_id_subway_red01,
		str_name = "A Red Line Subway Train",
		str_desc = str_red_subway_description,
		channel = channel_subway_red01,
		role = "Subway Train R-01",
		pvp = True,
		is_transport = True,
		transport_type = transport_type_subway,
		default_line = transport_line_subway_red_northbound,
		default_stop = poi_id_cv_subway_station
	),
	EwPoi(  # Subway train on the red line
		id_poi = poi_id_subway_red02,
		str_name = "A Red Line Subway Train",
		str_desc = str_red_subway_description,
		channel = channel_subway_red02,
		role = "Subway Train R-02",
		pvp = True,
		is_transport = True,
		transport_type = transport_type_subway,
		default_line = transport_line_subway_red_southbound,
		default_stop = poi_id_tt_subway_station
	),
	EwPoi(  # Subway train on the yellow line
		id_poi = poi_id_subway_yellow01,
		str_name = "A Yellow Line Subway Train",
		str_desc = str_yellow_subway_description,
		channel = channel_subway_yellow01,
		role = "Subway Train Y-01",
		pvp = True,
		is_transport = True,
		transport_type = transport_type_subway,
		default_line = transport_line_subway_yellow_northbound,
		default_stop = poi_id_ssb_subway_station
	),
	EwPoi(  # Subway train on the yellow line
		id_poi = poi_id_subway_yellow02,
		str_name = "A Yellow Line Subway Train",
		str_desc = str_yellow_subway_description,
		channel = channel_subway_yellow02,
		role = "Subway Train Y-02",
		pvp = True,
		is_transport = True,
		transport_type = transport_type_subway,
		default_line = transport_line_subway_yellow_southbound,
		default_stop = poi_id_ab_subway_station
	),
	EwPoi(  # Subway train on the green line
		id_poi = poi_id_subway_green01,
		str_name = "A Green Line Subway Train",
		str_desc = str_green_subway_description,
		channel = channel_subway_green01,
		role = "Subway Train G-01",
		pvp = True,
		is_transport = True,
		transport_type = transport_type_subway,
		default_line = transport_line_subway_green_eastbound,
		default_stop = poi_id_wgb_subway_station
	),
	EwPoi(  # Subway train on the green line
		id_poi = poi_id_subway_green02,
		str_name = "A Green Line Subway Train",
		str_desc = str_green_subway_description,
		channel = channel_subway_green02,
		role = "Subway Train G-02",
		pvp = True,
		is_transport = True,
		transport_type = transport_type_subway,
		default_line = transport_line_subway_green_westbound,
		default_stop = poi_id_sb_subway_station
	),
	EwPoi(  # Subway train on the blue line
		id_poi = poi_id_subway_blue01,
		str_name = "A Blue Line Subway Train",
		str_desc = str_blue_subway_description,
		channel = channel_subway_blue01,
		role = "Subway Train B-01",
		pvp = True,
		is_transport = True,
		transport_type = transport_type_subway,
		default_line = transport_line_subway_blue_eastbound,
		default_stop = poi_id_dt_subway_station
	),
	EwPoi(  # Subway train on the blue line
		id_poi = poi_id_subway_blue02,
		str_name = "A Blue Line Subway Train",
		str_desc = str_blue_subway_description,
		channel = channel_subway_blue02,
		role = "Subway Train B-02",
		pvp = True,
		is_transport = True,
		transport_type = transport_type_subway,
		default_line = transport_line_subway_blue_westbound,
		default_stop = poi_id_afb_subway_station
	),
	# EwPoi(  # Subway train on the white line
	# 	id_poi = poi_id_subway_white01,
	# 	str_name = "A Subway Train",
	# 	str_desc = str_generic_subway_description, # TODO: add description
	# 	channel = channel_subway_white01,
	# 	role = "Subway Train W-01",
	# 	pvp = False,
	# 	is_transport = True,
	# 	transport_type = transport_type_subway,
	# 	default_line = transport_line_subway_white_eastbound,
	# 	default_stop = poi_id_dt_subway_station
	# ),
	EwPoi(  # Blimp
		id_poi = poi_id_blimp,
		alias = [
			"zeppelin",
			"airship"
		],
		str_name = "The Blimp",
		str_desc = str_blimp_description,
		channel = channel_blimp,
		role = "Blimp",
		pvp = True,
		is_transport = True,
		transport_type = transport_type_blimp,
		default_line = transport_line_blimp_df_to_afb,
		default_stop = poi_id_df_blimp_tower
	),

	EwPoi( # apt
		id_poi = poi_id_apt,
		alias = [
		],
		str_name = "an apartment",
		str_desc = "",
		channel = channel_apt,
		role = "Apartments",
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-downtown
		id_poi = poi_id_apt_downtown,
		alias = [
			"apt",
		],
		str_name = "a Downtown apartment",
		str_desc = "",
		channel = channel_apt_downtown,
		role = "Downtown Apartments",
		is_apartment = True,
		mother_district = poi_id_downtown,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-smogsburg
		id_poi = poi_id_apt_smogsburg,
		alias = [
			"apt",
		],
		str_name = "a Smogsburg apartment",
		str_desc = "",
		channel = channel_apt_smogsburg,
		role = "Smogsburg Apartments",
		is_apartment = True,
		mother_district = poi_id_smogsburg,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-krakbay
		id_poi = poi_id_apt_krakbay,
		alias = [
			"apt",
		],
		str_name = "a Krak Bay apartment",
		str_desc = "",
		channel = channel_apt_krakbay,
		role = "Krak Bay Apartments",
		is_apartment = True,
		mother_district = poi_id_krakbay,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-poudrinalley
		id_poi = poi_id_apt_poudrinalley,
		alias = [
			"apt",
		],
		str_name = "a Poudrin Alley apartment",
		str_desc = "",
		channel = channel_apt_poudrinalley,
		role = "Poudrin Alley Apartments",
		is_apartment = True,
		mother_district = poi_id_poudrinalley,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-green-light-district
		id_poi = poi_id_apt_greenlightdistrict,
		alias = [

		],
		str_name = "a Green Light District apartment",
		str_desc = "",
		channel = channel_apt_greenlightdistrict,
		role = "Green Light District Apartments",
		is_apartment = True,
		mother_district = poi_id_greenlightdistrict,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-old-new-yonkers
		id_poi = poi_id_apt_oldnewyonkers,
		alias = [

		],
		str_name = "an Old New Yonkers apartment",
		str_desc = "",
		channel = channel_apt_oldnewyonkers,
		role = "Old New Yonkers Apartments",
		is_apartment = True,
		mother_district = poi_id_oldnewyonkers,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-little-chernobyl
		id_poi = poi_id_apt_littlechernobyl,
		alias = [

		],
		str_name = "a Little Chernobyl apartment",
		str_desc = "",
		channel = channel_apt_littlechernobyl,
		role = "Little Chernobyl Apartments",
		is_apartment = True,
		mother_district = poi_id_littlechernobyl,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-arsonbrook
		id_poi = poi_id_apt_arsonbrook,
		alias = [

		],
		str_name = "an Arsonbrook apartment",
		str_desc = "",
		channel = channel_apt_arsonbrook,
		role = "Arsonbrook Apartments",
		is_apartment = True,
		mother_district = poi_id_arsonbrook,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-astatine-heights
		id_poi = poi_id_apt_astatineheights,
		alias = [

		],
		str_name = "an Astatine Heights apartment",
		str_desc = "",
		channel = channel_apt_astatineheights,
		role = "Astatine Heights Apartments",
		is_apartment = True,
		mother_district = poi_id_astatineheights,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-gatlingsdale
		id_poi = poi_id_apt_gatlingsdale,
		alias = [

		],
		str_name = "a Gatlingsdale apartment",
		str_desc = "",
		channel = channel_apt_gatlingsdale,
		role = "Gatlingsdale Apartments",
		is_apartment = True,
		mother_district = poi_id_gatlingsdale,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-vandal-park
		id_poi = poi_id_apt_vandalpark,
		alias = [

		],
		str_name = "a Vandal Park apartment",
		str_desc = "",
		channel = channel_apt_vandalpark,
		role = "Vandal Park Apartments",
		is_apartment = True,
		mother_district = poi_id_vandalpark,
		pvp = False,
		is_subzone = False,
	),
	EwPoi(  # apt-glocksbury
		id_poi=poi_id_apt_glocksbury,
		alias=[

		],
		str_name="your Glocksbury apartment",
		str_desc="",
		channel=channel_apt_glocksbury,
		role="Glocksbury Apartments",
		is_apartment = True,
		mother_district = poi_id_glocksbury,
		pvp=False,
		is_subzone=False,
	),
	EwPoi(  # apt-north-sleezeborough
		id_poi=poi_id_apt_northsleezeborough,
		alias=[

		],
		str_name="your North Sleezeborough apartment",
		str_desc="",
		channel=channel_apt_northsleezeborough,
		role="North Sleezeborough Apartments",
		is_apartment=True,
		mother_district = poi_id_northsleezeborough,
		pvp=False,
		is_subzone=False,
	),
	EwPoi( # apt-south-sleezeborough
		id_poi = poi_id_apt_southsleezeborough,
		alias = [

		],
		str_name = "a South Sleezeborough apartment",
		str_desc = "",
		channel = channel_apt_southsleezeborough,
		role = "South Sleezeborough Apartments",
		is_apartment=True,
		mother_district = poi_id_southsleezeborough,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # ooze-gardens
		id_poi = poi_id_apt_oozegardens,
		alias = [

		],
		str_name = "an Ooze Gardens apartment",
		str_desc = "",
		channel = channel_apt_oozegardens,
		role = "Ooze Gardens Apartments",
		is_apartment=True,
		mother_district = poi_id_oozegardens,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-cratersville
		id_poi = poi_id_apt_cratersville,
		alias = [

		],
		str_name = "a Cratersville apartment",
		str_desc = "",
		channel = channel_apt_cratersville,
		role = "Cratersville Apartments",
		is_apartment=True,
		mother_district = poi_id_cratersville,
		pvp = False,
		is_subzone = False,
	),
	EwPoi(  # apt-wreckington
		id_poi=poi_id_apt_wreckington,
		alias=[

		],
		str_name="your Wreckington apartment",
		str_desc="",
		channel=channel_apt_wreckington,
		role="Wreckington Apartments",
		is_apartment=True,
		mother_district = poi_id_wreckington,
		pvp=False,
		is_subzone=False,
	),
	EwPoi( # apt-slimes-end
		id_poi = poi_id_apt_slimesend,
		alias = [

		],
		str_name = "a Slime's End apartment",
		str_desc = "",
		channel = channel_apt_slimesend,
		role = "Slime's End Apartments",
		is_apartment=True,
		mother_district = poi_id_slimesend,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-vagrants-corner
		id_poi = poi_id_apt_vagrantscorner,
		alias = [

		],
		str_name = "a Vagrant's Corner apartment",
		str_desc = "",
		channel = channel_apt_vagrantscorner,
		role = "Vagrant's Corner Apartments",
		is_apartment=True,
		mother_district = poi_id_vagrantscorner,
		pvp = False,
		is_subzone = False,
	),
	EwPoi(  # apt-afbr
		id_poi=poi_id_apt_assaultflatsbeach,
		alias=[

		],
		str_name="your Assault Flats Beach apartment",
		str_desc="",
		channel=channel_apt_assaultflatsbeach,
		role="Assault Flats Beach Apartments",
		is_apartment=True,
		mother_district = poi_id_assaultflatsbeach,
		pvp=False,
		is_subzone=False,
	),
	EwPoi(  # apt-new-new-yonkers
		id_poi=poi_id_apt_newnewyonkers,
		alias=[

		],
		str_name="your New New Yonkers apartment",
		str_desc="",
		channel=channel_apt_newnewyonkers,
		role="New New Yonkers Apartments",
		is_apartment=True,
		mother_district = poi_id_newnewyonkers,
		pvp=False,
		is_subzone=False,
	),
	EwPoi( # apt-brawlden
		id_poi = poi_id_apt_brawlden,
		alias = [

		],
		str_name = "a Brawlden apartment",
		str_desc = "",
		channel = channel_apt_brawlden,
		role = "Brawlden Apartments",
		is_apartment=True,
		mother_district = poi_id_brawlden,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-toxington
		id_poi = poi_id_apt_toxington,
		alias = [

		],
		str_name = "a Toxington apartment",
		str_desc = "",
		channel = channel_apt_toxington,
		role = "Toxington Apartments",
		is_apartment=True,
		mother_district = poi_id_toxington,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-charcoal-park
		id_poi = poi_id_apt_charcoalpark,
		alias = [

		],
		str_name = "a Charcoal Park apartment",
		str_desc = "",
		channel = channel_apt_charcoalpark,
		role = "Charcoal Park Apartments",
		is_apartment=True,
		mother_district = poi_id_charcoalpark,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # polonium-hill
		id_poi = poi_id_apt_poloniumhill,
		alias = [

		],
		str_name = "a Polonium Hill apartment",
		str_desc = "",
		channel = channel_apt_poloniumhill,
		role = "Polonium Hill Apartments",
		is_apartment=True,
		mother_district = poi_id_poloniumhill,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-west-glocksbury
		id_poi = poi_id_apt_westglocksbury,
		alias = [

		],
		str_name = "a West Glocksbury apartment",
		str_desc = "",
		channel = channel_apt_westglocksbury,
		role = "West Glocksbury Apartments",
		is_apartment=True,
		mother_district = poi_id_westglocksbury,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-jaywalker-plain
		id_poi = poi_id_apt_jaywalkerplain,
		alias = [

		],
		str_name = "a Jaywalker Plain apartment",
		str_desc = "",
		channel = channel_apt_jaywalkerplain,
		role = "Jaywalker Plain Apartments",
		is_apartment=True,
		mother_district = poi_id_jaywalkerplain,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-crookline
		id_poi = poi_id_apt_crookline,
		alias = [

		],
		str_name = "a Crookline apartment",
		str_desc = "",
		channel = channel_apt_crookline,
		role = "Crookline Apartments",
		is_apartment=True,
		mother_district = poi_id_crookline,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-dreadford
		id_poi = poi_id_apt_dreadford,
		alias = [

		],
		str_name = "a Dreadford apartment",
		str_desc = "",
		channel = channel_apt_dreadford,
		role = "Dreadford Apartments",
		is_apartment=True,
		mother_district = poi_id_dreadford,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # slime's end cliffs
		id_poi = poi_id_slimesendcliffs,
		alias = [
			"sec",
			"cliffs",
			"secliffs",
			"cliff"
		],
		str_name = "Slime's End Cliffs",
		str_desc = "You stand in the Slime's End Cliffs. Grassy, windswept fields overlook a harrowing drop into the vast Slime Sea. Even from this height you faintly hear its crashing waves. Countless people have used the isolation of this place to rid themselves of personal baggage and bagged persons. Keep that in mind when you stop for a picnic or a leisurely cig. Someone's got their eyes on you. Exits into Slime's End.",
		channel = channel_slimesendcliffs,
		role = "Slime's End Cliffs",
		mother_district = poi_id_slimesend,
		pvp = True,
		is_subzone = True,
	),

	EwPoi(  # Outskirts - 1
		id_poi=poi_id_south_outskirts,
		alias=[
			"southoutskirts",
			"soutskirts",
			"so",
		],
		str_name="Southern Outskirts",
		str_desc="{} These outskirts lay just beyond the boundaries of Wreckington, Cratersville, and Ooze Gardens. If you kept wandering, you could probably wind up in the Southwestern Outskirts too.".format(str_generic_outskirts_description),
		coord = (19, 37),
		coord_alias = [
			(20, 37),
			(21, 37)
		],
		channel="south-outskirts",
		role="Southern Outskirts",
		pvp=True,
		is_capturable=False,
		is_outskirts=True
	),
	EwPoi(  # Outskirts - 2
		id_poi=poi_id_southwest_outskirts,
		alias=[
			"southwesternoutskirts",
			"swoutskirts",
			"swo",
		],
		str_name="Southwestern Outskirts",
		str_desc="{} These outskirts lay just beyond the boundaries of South Sleezeborough, Crookline, and Dreadford. If you kept wandering, you could probably wind up in the Western or Southern Outskirts too.".format(str_generic_outskirts_description),
		coord = (6, 37),
		coord_alias = [
			(7, 37),
			(8, 37),
			(9, 37),
			(10, 37)
		],
		channel="southwest-outskirts",
		role="Southwestern Outskirts",
		pvp=True,
		is_capturable=False,
		is_outskirts=True
	),
	EwPoi(  # Outskirts - 3
		id_poi=poi_id_west_outskirts,
		alias=[
			"westernoutskirts",
			"woutskirts",
			"wo",
		],
		str_name="Western Outskirts",
		str_desc="{} These outskirts lay just beyond the boundaries of Jaywalker Plain, West Glocksbury, and Polonium Hill. If you kept wandering, you could probably wind up in the Southwestern or Northwestern Outskirts too.".format(str_generic_outskirts_description),
		coord = (3, 10),
		coord_alias = [
			(3, 11),
			(3, 12),
			(3, 13),
			(3, 14),
		],
		channel="west-outskirts",
		role="Western Outskirts",
		pvp=True,
		is_capturable=False,
		is_outskirts=True
	),
	EwPoi(  # Outskirts - 4
		id_poi=poi_id_northwest_outskirts,
		alias=[
			"northwesternoutskirts",
			"nwoutskirts",
			"nwo",
		],
		str_name="Northwestern Outskirts",
		str_desc="{} These outskirts lay just beyond the boundaries of Charcoal Park, Toxington, and Astatine Heights. If you kept wandering, you could probably wind up in the Western or Northern Outskirts too.".format(str_generic_outskirts_description),
		coord = (22, 2),
		coord_alias = [
			(21, 2),
			(20, 2),
			(19, 2),
			(18, 2),
		],
		channel="northwest-outskirts",
		role="Northwestern Outskirts",
		pvp=True,
		is_capturable=False,
		is_outskirts=True
	),
	EwPoi(  # Outskirts - 5
		id_poi=poi_id_north_outskirts,
		alias=[
			"northernoutskirts",
			"noutskirts",
			"no",
		],
		str_name="North Outskirts",
		str_desc="{}  These outskirts lay just beyond the boundaries of Arsonbrook, Brawlden, and New New Yonkers. If you kept wandering, you could probably wind up in the Northwestern Outskirts or the Nuclear Beach too.".format(str_generic_outskirts_description),
		coord = (37, 2),
		coord_alias = [
			(36, 2),
			(35, 2),
			(34, 2),
			(33, 2)
		],
		channel="north-outskirts",
		role="Northern Outskirts",
		pvp=True,
		is_capturable=False,
		is_outskirts=True
	),
	EwPoi( # Outskirts - 6
		id_poi=poi_id_nuclear_beach,
		alias=[
			"nuclearbeach",
			"nuclearbeachoutskirts",
			"nb",
			"nbeach",
			"afbo",
			"afboutskirts",
		],
		str_name="Nuclear Beach",
		str_desc="{}  A place only the fiercest secreatures call home, right next to Assault Flats Beach. Stay around too long, and you'll wind up in the jaws of god knows what lurks around here.".format(str_generic_outskirts_description),
		coord = (47, 6),
		coord_alias = [
			(47, 7)
		],
		channel="nuclear-beach",
		role="Nuclear Beach",
		pvp=True,
		is_capturable=False,
		is_outskirts=True
	),
	# EwPoi(  # Outskirts - 6
	# 	id_poi=poi_id_dreadford_outskirts,
	# 	alias=[
	# 		"dreadfordoutskirts",
	# 		"dfoutskirts",
	# 		"dfo",
	# 	],
	# 	str_name="Dreadford Outskirts",
	# 	str_desc="{} To the Northeast is Dreadford. To the North is Jaywalker Plain Outskirts. To the East is Crookline Outskirts.".format(str_generic_outskirts_description),
	# 	coord=(2, 51),
	# 	channel="dreadford-outskirts",
	# 	role="Dreadford Outskirts",
	# 	pvp=True,
	# 	is_capturable=False,
	# 	is_outskirts=True
	# ),
	# EwPoi(  # Outskirts - 7
	# 	id_poi=poi_id_jaywalkerplain_outskirts,
	# 	alias=[
	# 		"jaywalkerplainoutskirts",
	# 		"jpoutskirts",
	# 		"jpo",
	# 	],
	# 	str_name="Jaywalker Plain Outskirts",
	# 	str_desc="{} To the East is Jaywalker Plain. To the South is Dreadford Outskirts. To the North is West Glocksbury Outskirts.".format(str_generic_outskirts_description),
	# 	coord=(5, 44),
	# 	channel="jaywalker-plain-outskirts",
	# 	role="Jaywalker Plain Outskirts",
	# 	pvp=True,
	# 	is_capturable=False,
	# 	is_outskirts=True
	# ),
	# EwPoi(  # Outskirts - 8
	# 	id_poi=poi_id_westglocksbury_outskirts,
	# 	alias=[
	# 		"westglocksburyoutskirts",
	# 		"wgboutskirts",
	# 		"wgbo"
	# 	],
	# 	str_name="West Glocksbury Outskirts",
	# 	str_desc="{} To the East is West Glocksbury. To the South is Jaywalker Plain Outskirts. To the North is Polonium Hill Outskirts.".format(str_generic_outskirts_description),
	# 	coord=(6, 32),
	# 	channel="west-glocksbury-outskirts",
	# 	role="West Glocksbury Outskirts",
	# 	pvp=True,
	# 	is_capturable=False,
	# 	is_outskirts=True
	# ),
	# EwPoi(  # Outskirts - 9
	# 	id_poi=poi_id_poloniumhill_outskirts,
	# 	alias=[
	# 		"poloniumhilloutskirts",
	# 		"phoutskirts",
	# 		"pho",
	# 	],
	# 	str_name="Polonium Hill Outskirts",
	# 	str_desc="{} To the East is Polonium Hill. To the South is West Glocksbury Outskirts. To the North is Charcoal Park Outskirts.".format(str_generic_outskirts_description),
	# 	coord=(7, 18),
	# 	channel="polonium-hill-outskirts",
	# 	role="Polonium Hill Outskirts",
	# 	pvp=True,
	# 	is_capturable=False,
	# 	is_outskirts=True
	# ),
	# EwPoi(  # Outskirts - 10
	# 	id_poi=poi_id_charcoalpark_outskirts,
	# 	alias=[
	# 		"charcoalparkoutskirts",
	# 		"cpoutskirts",
	# 		"cpo",
	# 	],
	# 	str_name="Charcoal Park Outskirts",
	# 	str_desc="{} To the Southeast is Charcoal Park. To the South is Polonium Hill Outskirts. To the East is Toxington Outskirts.".format(str_generic_outskirts_description),
	# 	coord=(15, 4),
	# 	channel="charcoal-park-outskirts",
	# 	role="Charcoal Park Outskirts",
	# 	pvp=True,
	# 	is_capturable=False,
	# 	is_outskirts=True
	# ),
	# EwPoi(  # Outskirts - 11
	# 	id_poi=poi_id_toxington_outskirts,
	# 	alias=[
	# 		"toxingtonoutskirts",
	# 		"ttoutskirts",
	# 		"tto",
	# 	],
	# 	str_name="Toxington Outskirts",
	# 	str_desc="{} To the South is Toxington. To the West is Charcoal Park Outskirts. To the East is Astatine Heights Outskirts.".format(str_generic_outskirts_description),
	# 	coord=(27, 4),
	# 	channel="toxington-outskirts",
	# 	role="Toxington Outskirts",
	# 	pvp=True,
	# 	is_capturable=False,
	# 	is_outskirts=True
	# ),
	# EwPoi(  # Outskirts - 12
	# 	id_poi=poi_id_astatineheights_outskirts,
	# 	alias=[
	# 		"astatineheightsoutskirts",
	# 		"ahoutskirts",
	# 		"aho",
	# 	],
	# 	str_name="Astatine Heights Outskirts",
	# 	str_desc="{} To the South is Astatine Heights. To the West is Toxington Outskirts. To the East is Arsonbrook Outskirts.".format(str_generic_outskirts_description),
	# 	coord=(46, 10),
	# 	channel="astatine-heights-outskirts",
	# 	role="Astatine Heights Outskirts",
	# 	pvp=True,
	# 	is_capturable=False,
	# 	is_outskirts=True
	# ),
	# EwPoi(  # Outskirts - 13
	# 	id_poi=poi_id_arsonbrook_outskirts,
	# 	alias=[
	# 		"arsonbrookoutskirts",
	# 		"aboutskirts",
	# 		"abo",
	# 	],
	# 	str_name="Arsonbrook Outskirts",
	# 	str_desc="{} To the South is Arsonbrook. To the West is Astatine Heights Outskirts. To the East is Brawlden Outskirts.".format(str_generic_outskirts_description),
	# 	coord=(54, 2),
	# 	channel="arsonbrook-outskirts",
	# 	role="Arsonbrook Outskirts",
	# 	pvp=True,
	# 	is_capturable=False,
	# 	is_outskirts=True
	# ),
	# EwPoi(  # Outskirts - 14
	# 	id_poi=poi_id_brawlden_outskirts,
	# 	alias=[
	# 		"brawldenoutskirts",
	# 		"bdoutskirts",
	# 		"bdo",
	# 	],
	# 	str_name="Brawlden Outskirts",
	# 	str_desc="{} To the South is Brawlden. To the West is Arsonbrook Outskirts. To the East is New New Yonkers Outskirts.".format(str_generic_outskirts_description),
	# 	coord=(71, 2),
	# 	channel="brawlden-outskirts",
	# 	role="Brawlden Outskirts",
	# 	pvp=True,
	# 	is_capturable=False,
	# 	is_outskirts=True
	# ),
	# EwPoi(  # Outskirts - 15
	# 	id_poi=poi_id_newnewyonkers_outskirts,
	# 	alias=[
	# 		"newnewyonkersoutskirts",
	# 		"nnyoutskirts",
	# 		"nnyo",
	# 	],
	# 	str_name="New New Yonkers Outskirts",
	# 	str_desc="{} To the South is New New Yonkers. To the West is Brawlden Outskirts. To the East is Assault Flats Beach Outskirts.".format(str_generic_outskirts_description),
	# 	coord=(89, 6),
	# 	channel="new-new-yonkers-outskirts",
	# 	role="New New Yonkers Outskirts",
	# 	pvp=True,
	# 	is_capturable=False,
	# 	is_outskirts=True
	# ),
	# EwPoi(  # Outskirts - 16
	# 	id_poi=poi_id_assaultflatsbeach_outskirts,
	# 	alias=[
	# 		"assaultflatsbeachoutskirts",
	# 		"afboutskirts",
	# 		"afbo",
	# 	],
	# 	str_name="Assault Flats Beach Outskirts",
	# 	str_desc="{} To the South is Assault Flats Beach. To the West is New New Yonkers Outskirts.".format(str_generic_outskirts_description),
	# 	coord=(99, 8),
	# 	channel="assault-flats-beach-outskirts",
	# 	role="Assault Flats Beach Outskirts",
	# 	pvp=True,
	# 	is_capturable=False,
	# 	is_outskirts=True
	# ),
	EwPoi(  # Tutorial - 1
		id_poi = poi_id_tutorial_classroom,
		channel="classroom",
		role="Classroom",
		is_tutorial = True,
	),
	EwPoi(  # Tutorial - 2
		id_poi = poi_id_tutorial_hallway,
		channel="hallway",
		role="Hallway",
		is_tutorial = True,
	),
	EwPoi(  # Tutorial - 3
		id_poi = poi_id_tutorial_ghostcontainment,
		channel="ghost-containment",
		role="Ghost Containment",
		is_tutorial = True,
	),
	EwPoi(  # For containing people while server-wide renovations are transpiring.
		id_poi = poi_id_thesphere,
		str_name = "The Sphere",
		str_desc = "A nebulous defined space for containing hazardous waste. You can't tell what's happening on the outside, but it's probably not good.",
		coord = (54, 39),
		channel = "the-sphere",
		role = "The Sphere",
		is_subzone = True
	),
]

debugroom = ewdebug.debugroom
debugroom_short = ewdebug.debugroom_short
debugpiers = ewdebug.debugpiers
debugfish_response = ewdebug.debugfish_response
debugfish_goal = ewdebug.debugfish_goal

id_to_poi = {}
coord_to_poi = {}
chname_to_poi = {}
alias_to_coord = {}
capturable_districts = []
transports = []
transport_stops = []
transport_stops_ch = []
piers = []
outskirts = []
tutorial_pois = []
zine_mother_districts = []
