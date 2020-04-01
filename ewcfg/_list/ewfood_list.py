
# All food items in the game.
food_list = [
	EwFood(
		id_food = "slimentonic",
		alias = [
			"tonic",
		],
		recover_hunger = 18,
		price = 200,
		inebriation = 2,
		str_name = 'slime n\' tonic',
		vendors = [vendor_bar, vendor_countryclub],
		str_eat = "You stir your slime n' tonic with a thin straw before chugging it lustily.",
		str_desc = "The drink that has saved more juveniles’ lives than any trip to the nurse’s office could.",
	),
	EwFood(
		id_food = "slimacolada",
		alias = [
			"colada",
		],
		recover_hunger = 27,
		price = 300,
		inebriation = 2,
		str_name = 'slima colada',
		vendors = [vendor_bar, vendor_beachresort],
		str_eat = "You slurp down the delicious tropical delicacy and you are temporarily immobilized by a severly, splitting brain freeze. You double down to numb the pain.",
		str_desc = "Perfect for if you like getting caught in the acid raid, training at the dojo, have half a megaslime, "
				   "or like gunning down juvies at midnight in the dunes of the Mojave. Not great for much else, though."
	),
	EwFood(
		id_food = "slimekashot",
		alias = [
			"shot",
			"slimeka",
		],
		recover_hunger = 9,
		price = 100,
		inebriation = 2,
		str_name = 'shot of slimeka',
		vendors = [vendor_bar],
		str_eat = "You toss back the glowing, hissing substance, searing the back of your throat and tearing up a bit. You might need to see a doctor.",
		str_desc = "Made with pure, unrefined sludge from the city’s harbor. Just about as damaging to the colon as a sawed-off shotgun blast."
	),
	EwFood(
		id_food = "cabernetslimeignon",
		alias = [
			"wine",
			"cabernet",
			"slimeignon",
			"bottle",
		],
		recover_hunger = 36,
		price = 9999,
		inebriation = 4,
		str_name = 'bottle of vintage cabernet slimeignon',
		vendors = [vendor_bar],
		str_eat = "Ahh, you have a keen eye. 19XX was an excellent year. You pop the cork and gingerly have a sniff. "
				  "Then you gulp the whole bottle down in seconds, because fuck it.",
		str_desc = "A sophisticated drink for a sophisticated delinquent such as yourself. You're so mature for your age.",
		time_expir = (12 * 3600 * 84) # 6 weeks
	),
	EwFood(
		id_food = "slimynipple",
		alias = [
			"nipple",
		],
		recover_hunger = 9,
		price = 100,
		inebriation = 2,
		str_name = 'slimy nipple',
		vendors = [vendor_bar],
		str_eat = "You gulp down the green, creamy beverage with little care to its multi-layered presentation.",
		str_desc = "Of all the drinks with shitty names, this one tastes the worst."
	),
	EwFood(
		id_food = "slimeonthebeach",
		alias = [
			"beach",
		],
		recover_hunger = 27,
		price = 300,
		inebriation = 2,
		str_name = 'slime on the beach',
		vendors = [vendor_bar],
		str_eat = "You look pretty stupid drinking this fluorescent drink with a lil umbrella in it, but you don't care. Bottoms up!",
		str_desc = "When you told the bartender you wanted slime on the beach, about a dozen other guys at the bar chuckled under their breath and "
				   "hilariously added “Yeah, wouldn’t we all,” before beating the shit out of you outside afterward."
	),
		EwFood(
		id_food = "goobalibre",
		alias = [
			"goo",
		],
		recover_hunger = 27,
		price = 300,
		inebriation = 2,
		str_name = 'gooba libre',
		vendors = [vendor_bar],
		str_eat = "You sip the slime and soft drink concoction, causing it to ooze tartly down your throat. Sorta nasty, but you still like it!",
		str_desc = "A sickening, bright green marriage of slime and Mountain Dew. Last time you attempted to ordered it you had tried to convince the bartender you were over 21 "
				   "for half an hour, before finally giving up and just ordering the Dew."
	),
		EwFood(
		id_food = "manhattanproject",
		alias = [
			"manhattan",
			"mp",
		],
		recover_hunger = 45, #hehe dude like 1945 like when we bombed japan haha fuck yeah dude up high
		price = 500,
		inebriation = 8,
		str_name = 'manhattan project',
		vendors = [vendor_bar],
		str_eat = "You guzzle your drink before slamming it back down on the countertop. Your courage soars as the alcohol hits your bloodstream with the force of an atomic bomb.",
		str_desc = "We got tired of waiting for the bombs to drop so we made our own."
	),
	EwFood(
		id_food = "slimymary",
		alias = [
			"mary",
		],
		recover_hunger = 27,
		price = 300,
		inebriation = 2,
		str_name = 'slimy mary',
		vendors = [vendor_bar],
		str_eat = "This drink smells pretty nasty even by NLACakaNM standards. But what are you gonna do, NOT drink it?",
		str_desc = "This drink contains an easter egg. To find it, all you have to do is stand in your bathroom with the lights off and your back turned from the mirror. "
				   "Say it’s name three times, turn around and open your eyes. Congratulations! Your wallets missing and I’m fucking your girlfriend."
	),
	EwFood(
		id_food = "slimestout",
		alias = [
			"stout",
			"beer",
		],
		recover_hunger = 36,
		price = 400,
		inebriation = 2,
		str_name = 'stein of dark slime stout',
		vendors = [vendor_bar],
		str_eat = "You chug the heavy liquor with moderate vigor. It’s strong taste causes you to flinch, but in the end your thirst is quenched. "
				  "You’ve won this bout with the mighty slime stout. Thank you, goodnight.",
		str_desc = "A rich, dark green slime stout straight from the tap, with a head so thick you could rest a SlimeCoin on it. If it were a physical currency, which it isn’t. "
				   "It’s a cryptocurrency. Duh, idiot. Maybe SlimeCorp will release a limited edition physical release for all those freak coin collectors out there one day."
	),
	EwFood(
		id_food = "water",
		alias = [
			"h20",
		],
		recover_hunger = 0,
		price = 0,
		inebriation = 0,
		str_name = 'glass of water',
		vendors = [vendor_bar, vendor_bazaar],
		str_eat = "The bartender sighs as he hands you a glass of water. You drink it. You're not sure why you bothered, though.",
		str_desc = "It’s a room temperature glass of tap water. Abstaining from drinking calories has never tasted this adequate!"
	),
	EwFood(
		id_food = "razornutspacket",
		alias = [
			"rn",
			"razor",
			"nuts",
			"packet"
		],
		recover_hunger = 50,
		price = 800,
		inebriation = 0,
		str_name = 'packet of salted razornuts',
		vendors = [vendor_bar],
		str_eat = "You tear into the packet and eat the small, pointy nuts one at a time, carefully avoiding any accidental lacerations.",
		str_desc = "It's a packet of locally-grown razornuts, roasted and salted to perfection. Perfect for snacking!"
	),
	EwFood(
		id_food = "breadsticks",
		alias = [
			"sticks",
		],
		recover_hunger = 20,
		price = 200,
		inebriation = 0,
		str_name = 'bundle of five breadsticks',
		vendors = [vendor_pizzahut],
		str_eat = "You gnaw on each stale breadstick like a dog chews on his bone, that is to say for hours and with little purpose. You let it soak underneath a nearby soda machine, "
				  "allowing the carbonation to eat away at the carbohydrate rod. You swallow the soggy appetizer whole, in one long gulp with no chewing necessary. Nasty!!",
		str_desc = "A hard slab of five breadsticks, all stuck together to form a stale brick of cheap bread and even cheaper pre-grated parmesan and oregano flakes. "
				   "Eating this is going to require some creative thinking. Hell, you might as well !equip it, you could probably drop it from a two story building and "
				   "split someone’s fucking skull open with it like an anvil in an old cartoon."
	),
	EwFood(
		id_food = "pizza",
		alias = [
			"cheese",
			"slice",
		],
		recover_hunger = 40,
		price = 400,
		inebriation = 0,
		str_name = 'slice of cheese pizza',
		vendors = [vendor_pizzahut],
		str_eat = "You nab a hot, greasy slice of that cheesy pie and cram it into your eager craw! Radical, dude!!",
		str_desc = "A supposedly hot slice of cheese pizza. Some of it’s pre-grated cheese hasn't fully melted yet, and it’s crust is hard and chewy. Reality is a cruel mistress."
	),
	EwFood(
		id_food = "pepperoni",
		alias = [
			"peperoni",
			"pep"
		],
		recover_hunger = 60,
		price = 600,
		inebriation = 0,
		str_name = 'slice of pepperoni pizza',
		vendors = [vendor_pizzahut],
		str_eat = "You chomp right into the salty, spicy sausage slice, bro! Cowabunga, my dude!!",

		str_desc = "An apparently appetizing slice of pepperoni pizza. It’s crust is limp and soggy from the excess grease it's slathered in, which is about the only thing you can taste on it. Pure Bliss."

	),
	EwFood(
		id_food = "meatlovers",
		alias = [
			"meatlovers",
			"meat"
		],
		recover_hunger = 80,
		price = 800,
		inebriation = 0,
		str_name = 'slice of Meat Lover\'s® pizza',
		vendors = [vendor_pizzahut],
		str_eat = "You happily scarf down this carnivore's delight! You’re neausiating both metaphorically and literally by the sheer volume of animal fat you're ingesting! Tubular!! Hell yes!!",
		str_desc = "A thoroughly revolting slice Meat Lover's® pizza. You like meat, but you aren't sure if you're ready to love again."
	),
	EwFood(
		id_food = "wings",
		alias = [
			"buffalowings",
			"hotwings",
		],
		recover_hunger = 120,
		price = 1200,
		inebriation = 0,
		str_name = 'box of twelve buffalo wings',
		vendors = [vendor_pizzahut],
		str_eat = "Hell yeah, bro! Your mouth burns with passion! Your lips are in agony! You accidentally wiped away a tear with a sauce salthered finger and now you’re blind! You’ve never felt so alive!!",
		str_desc = "Best eaten with several of your closest bros, forming a spicy pact that elevates your meager friendship to the highest form of union one can have with their bros. "
				   "Forged while eating the hottest chicken wings available and preferably crying in the process, the camaraderie experienced while sweating through the agony together lasts a lifetime. "
				   "It is a form of matrimony unparalleled in sentimentality, and it is not to be trifled with lightly. Nothing can break a spicy bro pact. Nothing."
	),
	EwFood(
		id_food = "taco",
		alias = [
			"softtaco",
		],
		recover_hunger = 10,
		price = 100,
		inebriation = 0,
		str_name = 'soft taco',
		vendors = [vendor_tacobell],
		str_eat = "You bite into the taco. Pretty good, you guess. It’s missing something… a blast of flavor, perhaps?",
		str_desc = "A limp, pitiful soft-shelled taco. Mirroring its own flabby, flaccid facade, it is the perfect food for weak-willed men without "
				   "the strong moral character needed to tame the wild, wicked blast of flavor found in more iconic Taco Bell tacos."
	),
	EwFood(
		id_food = "nachocheesetaco",
		alias = [
			"nachocheese",
			"nachotaco"
		],
		recover_hunger = 30,
		price = 300,
		inebriation = 0,
		str_name = 'Nacho Cheese taco',
		vendors = [vendor_tacobell],
		str_eat = "You slam your mouth into a cheesy blast of that iconic Nacho Cheese flavor!! **YEEAAAHHHH!!!!**",
		str_desc = "This flavor…!! It’s an explosion of artificial cheese flavors and shrapnel sized bits of soggy shell that vaguely reminds you of world famous Nacho Cheese Doritos!!"
	),
	EwFood(
		id_food = "coolranchtaco",
		alias = [
			"coolranch",
			"ranchtaco",
			"cr"
		],
		recover_hunger = 30,
		price = 300,
		inebriation = 0,
		str_name = 'Cool Ranch taco',
		vendors = [vendor_tacobell],
		str_eat = "You crash your teeth into an explosion of that dark horse Cool Ranch flavor!! Uhhhh... yeeaaahhhh!!",
		str_desc = "This flavor…?? It’s a mushy mess of poorly seasoned mystery meat and pre-grated cheese trapped in a miserable shell that unfortunately reminds you of Doritos’ *other flavor* that isn't Nacho Cheese."
	),
	EwFood(
		id_food = "quesarito",
		alias = [
			"qsr",
		],
		recover_hunger = 50,
		price = 500,
		inebriation = 0,
		str_name = 'chicken quesarito',
		vendors = [vendor_tacobell],
		str_eat = "You bite into a burrito, or something. It's got cheese in it. Whatever. You eat it and embrace nothingness.",
		str_desc = "This travesty reminds you of your favorite My Little Pony: Friendship is Magic character Fluttershy for reasons you can’t quite remember..."
	),
	EwFood(
		id_food = "steakvolcanoquesomachorito",
		alias = [
			"machorito",
			"quesomachorito"
			"svqmr",
			"volc"
		],
		recover_hunger = 130,
		price = 1300,
		inebriation = 0,
		str_name = 'SteakVolcanoQuesoMachoRito',
		vendors = [vendor_tacobell],
		str_eat = "It's a big fucking mess of meat, vegetables, tortilla, cheese, and whatever else happened to be around. You gobble it down greedily!!",
		str_desc = "This pound of greasy, soggy, and flavorless artificially flavored fast food just broke through the damp, leaking paper bag they doubled wrapped it in. "
				   "Guess you're going to have to eat it off the floor."
	),
	EwFood(
		id_food = "coleslaw",
		alias = [
			"slaw",
			"op",
			"ghst"

		],
		recover_hunger = 10,
		price = 100,
		inebriation = 0,
		str_name = 'tub of cole slaw',
		vendors = [vendor_kfc],
		str_eat = "You lap at the cup of some gross white cabbage swimming in watery mayo. Why the fuck would you order this?",
		str_desc = "This side is so horrific you might just start being able to shoot dead people if you eat it."
	),
	EwFood(
		id_food = "biscuitngravy",
		alias = [
			"biscuit",
			"gravy"
		],
		recover_hunger = 20,
		price = 200,
		inebriation = 0,
		str_name = 'biscuit with a side of gravy',
		vendors = [vendor_kfc],
		str_eat = "You dip the stale biscuit into the miniature bucket of gravy, scarf it down, and then chug the rest. *Burp.*",
		str_desc = "A cold biscuit that could break the glass if you threw it at window and scalding hot gravy that they let burn away the filth and grime in their pots so they don't have to clean them."
	),
	EwFood(
		id_food = "chickenbucket",
		alias = [
			"bucket",
			"cucket", #kraks favorite
			"chicken"
		],
		recover_hunger = 320,
		price = 3200,
		inebriation = 0,
		str_name = '8-piece bucket of fried chicken',
		vendors = [vendor_kfc],
		str_eat = "You stuff your face on the eight pieces of juicy limbs and hot, crispy skin carved from a winged beast. It’s calorie-rich flesh arouses your base instincts as a human, "
				  "triggering growls and snarls to all approach you while you feed. Your fingers and tongue are scalded and you don't give a shit.",
		str_desc = "An obscure amount of calories in a simple bucket, a convenient trough for you to consume your dystopian meal. While children are starving in third world countries, "
				   "you crush these family meals often and without remorse. Well, to be fair I don’t think even the starving African children would touch KFC. That shit is nasty. You have a problem."
	),
	EwFood(
		id_food = "famousbowl",
		alias = [
			"bowl",
		],
		recover_hunger = 40,
		price = 400,
		inebriation = 0,
		str_name = 'Famous Mashed Potato Bowl',
		vendors = [vendor_kfc],
		str_eat = "You scarf down a shitty plastic bowl full of jumbled-up bullshit. It really hits the spot!",
		str_desc = "It’s just not a meal unless it’s a potato-based meal with a calorie count in the six digits."
	),
	EwFood(
		id_food = "barbecuesauce",
		alias = [
			"bbq",
			"sauce",
			"saucepacket",
		],
		recover_hunger = 1,
		price = 0,
		inebriation = 0,
		str_name = 'packet of BBQ Sauce',
		vendors = [vendor_kfc],
		str_eat = "You discard what little is left of your dignity and steal a packet of barbeque sauce to slurp down. What is wrong with you?",
		str_desc = "You're not alone. Confidential help is available for free."
	),
	EwFood(
		id_food = "mtndew",
		alias = [
			"dew",
			"mountaindew",
			"greendew"
		],
		recover_hunger = 10,
		price = 100,
		inebriation = 0,
		str_name = 'Mtn Dew',
		vendors = [vendor_mtndew, vendor_vendingmachine],
		str_eat = "You fill your jumbo fountain drink vessel with vivid green swill and gulp it down.",
		str_desc = "Ah, a nice cold brew resembling a mix between battery acid and artificial various citrus flavorings. Sick!!"
	),
	EwFood(
		id_food = "bajablast",
		alias = [
			"bluedew",
		],
		recover_hunger = 10,
		price = 100,
		inebriation = 0,
		str_name = 'Mtn Dew Baja Blast',
		vendors = [vendor_mtndew, vendor_vendingmachine],
		str_eat = "You fill your jumbo fountain drink vessel with light bluish swill and gulp it down.",
		str_desc = "Ah, a nice cold brew resembling a mix between battery acid and artificial lime flavoring. Cool!!"
	),
	EwFood(
		id_food = "codered",
		alias = [
			"reddew",
		],
		recover_hunger = 10,
		price = 100,
		inebriation = 0,
		str_name = 'Mtn Dew Code Red',
		vendors = [vendor_mtndew, vendor_vendingmachine],
		str_eat = "You fill your jumbo fountain drink vessel with red swill and gulp it down.",
		str_desc = "Ah, a nice cold brew resembling a mix between battery acid and artificial cherry flavoring. Sweet!!"
	),
	EwFood(
		id_food = "pitchblack",
		alias = [
			"blackdew",
		],
		recover_hunger = 10,
		price = 100,
		inebriation = 0,
		str_name = 'Mtn Dew Pitch Black',
		vendors = [vendor_mtndew, vendor_vendingmachine],
		str_eat = "You fill your jumbo fountain drink vessel with dark purple swill and gulp it down.",
		str_desc = "Ah, a nice cold brew resembling a mix between battery acid and artificial grape flavoring. Gnarly!!"
	),
	EwFood(
		id_food = "whiteout",
		alias = [
			"whitedew",
		],
		recover_hunger = 10,
		price = 100,
		inebriation = 0,
		str_name = 'Mtn Dew White-Out',
		vendors = [vendor_mtndew, vendor_vendingmachine],
		str_eat = "You fill your jumbo fountain drink vessel with pale cloudy swill and gulp it down.",
		str_desc = "Ah, a nice cold brew resembling a mix between battery acid and artificial lemon flavoring. Bodacious!!"
	),
	EwFood(
		id_food = "livewire",
		alias = [
			"orangedew",
		],
		recover_hunger = 10,
		price = 100,
		inebriation = 0,
		str_name = 'Mtn Dew Livewire',
		vendors = [vendor_mtndew, vendor_vendingmachine],
		str_eat = "You fill your jumbo fountain drink vessel with orange swill and gulp it down.",
		str_desc = "Ah, a nice cold brew resembling a mix between battery acid and artificial orange flavoring. Tubular!!"
	),
	EwFood(
		id_food = "shrimpcocktail",
		alias = [
			"shimp",
			"shrimp",
			"cocktail",
		],
		recover_hunger = 180,
		price = 1800,
		inebriation = 0,
		str_name = 'a shrimp cocktail',
		vendors = [vendor_seafood, vendor_beachresort, vendor_countryclub],
		str_eat = "You pull out the prawns and pop ‘em into your mouth one after without removing their shell. You take vigorous swigs of the cocktail sauce straight "
				  "out of the glass to wash down the shards of crustacean getting lodged in the roof of your mouth.",
		str_desc = "A wavy glass of some shelled shrimp dipped in a weird, bitter ketchup that assaults your snout and mouth with unfortunate strength. Nothing is sacred."
	),
	EwFood(
		id_food = "halibut",
		alias = [
			"halibut",
		],
		recover_hunger = 270,
		price = 3000,
		inebriation = 0,
		str_name = 'a grilled halibut',
		vendors = [vendor_seafood, vendor_bazaar],
		str_eat = "You scarf down some delicious grilled halibut for the helluvit and it’s accompanying sides for the sidesuvit.",
		str_desc = "A grilled hunk of halibut, served with chipotle dirty rice and corn."
	),
	EwFood(
		id_food = "salmon",
		alias = [
			"salmon",
		],
		recover_hunger = 450,
		price = 5200,
		inebriation = 0,
		str_name = 'a wood fired salmon',
		vendors = [vendor_seafood, vendor_bazaar],
		str_eat = "You swallow the wood fired salmon without saving any of its smoky aftertaste! Aww man, so much for the extra 2 SlimeCoin…",
		str_desc = "A wood fired slice of salmon, served with a Dijon glaze and scalloped potatoes and broccoli on the side."
	),
	EwFood(
		id_food = "mahimahi",
		alias = [
			"mahimahi",
		],
		recover_hunger = 360,
		price = 4000,
		inebriation = 0,
		str_name = 'a sauteed mahi mahi',
		vendors = [vendor_seafood, vendor_bazaar],
		str_eat = "You gobble up the sauteed mahi mahi with lighting speed, reducing the proud fish into liquid in a matter of seconds.",
		str_desc = "A sauteed measurement of mahi mahi, with a lemon pepper crust and served with scalloped potatoes and spinach."
	),
	EwFood(
		id_food = "scallops",
		alias = [
			"scallops",
			"scl",
			"fish nuggies"
		],
		recover_hunger = 540,
		price = 6000,
		inebriation = 0,
		str_name = 'pan-seared scallops',
		vendors = [vendor_seafood, vendor_bazaar],
		str_eat = "You lean your head back, grab a few scallops, and try throwing them up into air and landing them in your mouth. This goes extremely poorly.",
		str_desc = "Some pan-seared scallops, served with goat cheese grits, sweet corn, and asparagus."
	),
	EwFood(
		id_food = "clamchowder",
		alias = [
			"clam",
			"chowder",
		],
		recover_hunger = 90,
		price = 1000,
		inebriation = 0,
		str_name = 'a cup of clam chowder',
		vendors = [vendor_seafood, vendor_bazaar],
		str_eat = "You scoop out a glob of the hearty chowder and clench your fist above your head, letting it drizzle down all over your face and into your eager mouth. You’re a fucking freak.",
		str_desc = "A bowl of New England clam chowder, served to you cold and runny in Arizona."
	),
	EwFood(
		id_food = "steaknlobster",
		alias = [
			"lobster",
			"lob",
			"snl",
			"lb"
		],
		recover_hunger = 720,
		price = 8000,
		inebriation = 0,
		str_name = 'a rock lobster tail and a sirloin steak',
		vendors = [vendor_seafood, vendor_bazaar],
		str_eat = "You discard the napkin immediately, along with the silverware trapped inside of it, opting to instead to eat the meal with your hands. "
				  "You pry the lobster from its shell first, ramming it into your mouth and taking a shot of melted butter to soften it up while you chew. "
				  "You continue onto the steak, carefully sliced against the grain, and smother it in half a bottle of A1 sauce and just start to suck on the two inch pieces "
				  "as if they were a jawbreaker or some other hard candy. You suck on the dead animal until it moistens to the point of liquefying, a solid hour and a half each. "
				  "You burp loudly. Man, what an unforgettable dinner!",
		str_desc = "A grilled 12oz sirloin steak and similarly sized rock lobster tail, served with scalloped potatoes, broccoli, asparagus, shallot herb butter "
				   "along side a portrait of the chef that was autographed and kissed with a vibrant red lipstick. What, does he think he’s better than you? "
				   "You break the portrait with your fist and your hand starts to bleed."
	),
	EwFood(
		id_food = "kingpincrab",
		alias = [
			"crab",
			"kingpin",
			"kp",
			"crb",
			"krb",
			"pin"
		],
		recover_hunger = 630,
		price = 7000,
		inebriation = 0,
		str_name = 'an Arizonian Kingpin Crab',
		vendors = [vendor_seafood, vendor_bazaar],
		str_eat = "You’re too weak to properly crack the mighty crabs’ carapaces, even with the proper crab carapace cracking crackers. After about 10 minutes of desperately trying to, "
				  "you just whip out whatever weapon you currently have quiped and start to viciously strike the crustaceans in a vain attempt to release their inner, delectable meat. "
				  "You just end up destroying the entire table you’re eating at.",
		str_desc = "Two imposing 1½ lb Arizonian Kingpin Crabs, steamed and split, served with a small side of melted butter. Their unique pink and purple carapaces that distinguish them are purely cosmetic, "
				   "but you’ll always think one color tastes better than the other. D’awww...",
	),
	EwFood(
		id_food = "champagne",
		alias = [
			"champagne",
		],
		recover_hunger = 99,
		price = 9999,
		inebriation = 99,
		str_name = 'a bottle of champagne',
		vendors = [vendor_seafood],
		str_eat = "You shake the bottle violently before popping off the cork and letting the geyser of pink alcohol blast your waiter in the face. Haha, what a fucking dumbass.",
		str_desc = "The bubbly, carbonated bright pink liquid contained inside this bottle is very reminiscent of of the alcohol in Disney’s The Great Mouse Detective, "
				   "otherwise known as most appealing liquid on Earth until you remember it’s not straight edge."
	),
	EwFood(
		id_food = "sparklingwater",
		alias = [
			"sparklingwater",
		],
		recover_hunger = 9,
		price = 100,
		inebriation = 0,
		str_name = 'a glass of sparkling water',
		vendors = [vendor_bar, vendor_seafood, vendor_countryclub, vendor_beachresort],
		str_eat = "You savor every bubble of this lightly carbonated bliss. Your eyes begin to tear up as you fondly regard your own ecstasy. ‘Ah, just like in Roma…’",
		str_desc = "It’s some water with bubbles in it. Snore!"
	),
	EwFood(
		id_food = "juviesroe",
		alias = [
			"roe",
		],
		recover_hunger = 99,
		price = 99999,
		inebriation = 0,
		str_name = 'a bowl of decadent Juvie’s Roe',
		vendors = [vendor_seafood, vendor_bazaar],
		str_eat = "You don’t really know how to eat caviar, so you just scoop some of the disgusting slop out of the tin with your bare hands and get crushed fish eggs all over your mouth "
				  "as you shovel it into your uncultured maw. It tastes, uh… high class? This was a waste of money.",
		str_desc = "A small tin of wild, matured Juvie’s roe. A highly sought after delicacy by the upper crust of the critical improshived juveniles of the city. "
				   "Considered by many to be the height of luxury, an utterly decadent show of unrivalled epicurean ecstasy. "
				   "Sure, some of the unwashed masses COULD describe the understated burst of flavor non-existent, reducing the whole dish to a weird, goopy mess, but you know better."

	),
	EwFood(
		id_food = "homefries",
		alias = [
			"fries",
		],
		recover_hunger = 15,
		price = 100,
		inebriation = 0,
		str_name = 'home fries',
		vendors = [vendor_diner, vendor_bazaar],
		str_eat = "You cram as many overcooked cubes of potato into your oversized maw as possible.You choke painfully on some of the tiny bits that that bypass your poor attempts at chewing. You hunger for more.",
		str_desc = "A greasy, over salted, crispy pile of miniature potato chunks, ranging from the average cubes to smaller irregularly shaped, condensed bits of pure fried potato skin. "
				   "With a calorie count well above your recommended daily consumption in just a handful, you could subsist on these preservative riddled species of spud for well over a week and still gain weight. "
				   "Too bad you can’t stop yourself from guzzling an entire plates worth in 5 minutes. Oops."
	),
	EwFood(
		id_food = "pancakes",
		alias = [
			"flapjacks",
		],
		recover_hunger = 105,
		price = 700,
		inebriation = 0,
		str_name = 'stack of three pancakes',
		vendors = [vendor_diner, vendor_bazaar],
		str_eat = "You drench your three flapjacks in a generous helping of maple syrup and slap a stick of butter on top for good measure. It’s a good thing you’ve drowned your pancakes in all this excess shit, "
				  "or you might have actually tasted them! The soggy, limp fried dough is so much more appetizing when all it’s innate flavor is overrun by pure sugary excess.",
		str_desc = "Pancakes are usually a pretty safe bet, no matter where you are. You can’t really mess up a pancake unless you’re specifically trying to burn it. Luckily, "
				   "the dedicated chefs in the kitchen are doing just that! Thank God, you almost got a decent meal in this city."
	),
	EwFood(
		id_food = "chickennwaffles",
		alias = [
			"belgium",
			"cnw",
		],
		recover_hunger = 135,
		price = 900,
		inebriation = 0,
		str_name = 'two chicken strips and a waffle',
		vendors = [vendor_diner, vendor_bazaar],
		str_eat = "You promptly seperate the two chicken strips and waffle on to separate plates, quarantining them off completely from one another. "
				  "You dip the chicken strips into some ketchup and drizzle some syrup onto the waffles, making sure to NEVER combine the two bitter rivals and to cleanse your palette before switching between them. "
				  "Ah, the life of a picky eater, it’s hard and no one understands.",
		str_desc = "Waffles are the perfect test subject. Whether it’s a good waffle or a bad waffle, they’re all going to hover around the same average quality. So, "
				   "whenever you’re in a new town and you wanna judge the quality of any given breakfast diner, order the waffle and rest easy knowing that even the worst waffle isn’t really that bad. "
				   "Oh, this waffle? It’s terrible. At least you have two chicken strips that were clearly frozen and only heated up a couple of minutes before you received them. "
				   "For all of the loss in quality and flavor, you can't fuck up microwaving something."
	),
	EwFood(
		id_food = "frenchtoast",
		alias = [
			"toast",
			"ft",
			"egg bread"
		],
		recover_hunger = 90,
		price = 600,
		inebriation = 0,
		str_name = 'four slices of french toast',
		vendors = [vendor_diner, vendor_bazaar],
		str_eat = "You brace untold misery, for your hopes and dreams to be smashed utterly and irreparably, and most importantly to have wasted 12 SlimeCoin on the worst meal of your life. "
				  "Every hair on your body stands upright, as if preparing for a betrayal fueled stroke. You bite into the toast, and "
				  "as soon as the sweet pastry touches your tongue you feel as though you finally resonate with the ending of critically acclaimed children’s movie Ratatouille. "
				  "The bread is fluffy, light, and pleasantly moist, the perfect distribution of cinnamon and nutmeg, mixed with light sprinkles of sugar and vanilla, "
				  "create a french toast that is sweet but not sickeningly so. You can’t believe you’re saying this, but… it’s perfect! Your compliments to the chef, you guess.",
		str_desc = "French toast is the hardest to perfect out of the legendary fried dough trio. Requiring even cursory amounts of knowledge or expertise in the kitchen proves "
				   "to be too much for the chefs of diners nationwide. And unlike both the pancake and the waffle, there is a huge difference between a good french toast and a bad french toast. "
				   "There is nothing more euphoric than biting into a fluffy, moist, and sweet piece of good french toast, while conversely there is nothing that invokes the image of pigs greedily "
				   "eating trash in their trough than the feeling of a sticky glob of undercooked dough slide down your throat from a bad french toast. You really have to be sure that the restaurant "
				   "you’re ordering french toast knows what they’re doing, or else your night is ruined. Now, take a wild guess if the chefs at the Smoker’s Cough know what they’re doing."
	),
	EwFood(
		id_food = "friedeggs",
		alias = [
			"eggs",
		],
		recover_hunger = 45,
		price = 300,
		inebriation = 0,
		str_name = 'two sunny side up eggs',
		vendors = [vendor_diner, vendor_bazaar],
		str_eat = "You isolate the yolks from your two fried eggs with surgical precision, leaving a clump of egg whites scraps and two perfectly contained yellow bubbles waiting to burst. "
				  "You salt and pepper them both thoroughly before eating one after another, first chewing on the slightly discolored egg whites and then bursting each egg yolk whole in your "
				  "mouth and letting the runny, golden goo to coat your insides.",
		str_desc = "Sure, you like your egg yolks runny, but given by their snotty, green discoloration, it’s pretty likely these eggs were severely undercooked. Oh well, salmonella here we come!"
	),
	EwFood(
		id_food = "eggsbenedict",
		alias = [
			"benedict",
			"benny",
		],
		recover_hunger = 75,
		price = 500,
		inebriation = 0,
		str_name = 'an eggs benedict',
		vendors = [vendor_diner, vendor_bazaar],
		str_eat = "Even though you’re pretty sure you know what an eggs benedict is, you aren’t sure you know how to eat it. You pick up the muffin and just take a bite out of it directly, "
				  "hollandaise sauce and egg yolk coat your nostrils and generally splatters all over your face. Who would eat something like this????",
		str_desc = "An English muffin topped off with some ham, a poached egg, and hollandaise sauce. It seems like the sort of food that’d you would enjoy, it’s customizable and leans itself "
				   "to quirky variants, it’s pretty easy to make, it has an egg on it… still, the food comes across as menacing. It’s thick sauce masks it’s ingredients, what secrets could it be "
				   "hiding? You guess there’s only one way to find out. Gulp!"
	),
	EwFood(
		id_food = "scrambledeggs",
		alias = [
			"scrambled",
		],
		recover_hunger = 60,
		price = 400,
		inebriation = 0,
		str_name = 'two scrambled eggs',
		vendors = [vendor_diner, vendor_bazaar],
		str_eat = "You attempt to strangle your ketchup bottle for the state mandated dollop of ketchup to be adequately mixed into your scrambled egg when tragedy strikes! The bottle is empty! "
				  "It blasts out specs of ketchup and a funny noise a few times before you throw it against the wall in ballistic anger. You are forced to eat the eggs… plain. DEAR GOD!!!!",
		str_desc = "Some scrambled eggs. Come on, you know what scrambled eggs are, right? Do I have to spell out everything for you? Do you want me to stay awake all night and come up with immature "
				   "jokes and puns for every one of these fucking things? Come on kid, get real."
	),
	EwFood(
		id_food = "omelette",
		alias = [
			"om",
		],
		recover_hunger = 120,
		price = 800,
		inebriation = 0,
		str_name = 'a western omelette',
		vendors = [vendor_diner, vendor_bazaar],
		str_eat = "You pour plenty of hot sauce all over your omelette and shove bite after bite into your slobbering mouth. The heat from the sauce and the bell peppers builds to a breaking point, "
				  "causing you to blackout. You wake up an indeterminate amount of time later, covered in dried tears and sweat and your abdomen feeling as though you’re pregnant with Satan. You love pain.",
		str_desc = "A delicious Denver omelette, stuffed with diced ham, onions, and green peppers. Looks great! Hm? Excuse me? What the fuck is a ‘western omelette’? Do people on the east coast "
				   "seriously call Denver omelettes that? Are you joking me? You ask anyone on the sensible half of the country what the name of the best omelette is and they’ll bark back the long "
				   "and storied history of John D. Omelette and his rough-and-tumble youth growing up in the mean streets of the great state of Colorado’s capital. Do they not know what Denver is? "
				   "Do they think everything past the Appalachians are uncharted wilderness? Man, fuck you guys. We know were New York is, we know where Boston is, we know where Cincinnati is, we know "
				   "our geography of the east coast like the back of our hand and it’s about time you start memorizing ours. Eat shit."
	),
	EwFood(
		id_food = "orangejuice",
		alias = [
			"oj",
			"juice",
		],
		recover_hunger = 9,
		price = 100,
		inebriation = 0,
		str_name = 'a glass of orange juice',
		vendors = [vendor_diner, vendor_bazaar],
		str_eat = "You swish around the decadent, pulpy orange juice in your mouth. This exacerbates your already poor dental hygiene, sending shockwaves of pain through your mouth as the "
				  "sugary liquid washes up against dozens of cavities all throughout your mouth. But, you don’t care. You’re in heaven.",
		str_desc = "A cavity creating, dental decaying, and enamel eroding glass of delicious orange juice. This vibrant citrus drink hits the spot any day of the week, any minute of the day, "
				   "and every second of your short, pathetic life. Coffee is a myth, water is a joke, soda is piss. #juiceprideworldwide"
	),
	EwFood(
		id_food = "milk",
		alias = [
			"cowjuice"
		],
		recover_hunger = 9,
		price = 100,
		inebriation = 0,
		str_name = 'a glass of milk',
		vendors = [vendor_diner, vendor_bazaar],
		str_eat = "You take a swig of a nice, cold glass of whole milk and your palette is instantly clear of any sugary or syrupy foods you may have been eating. You are left in total cow induced euphoria.",
		str_desc = "A simple glass of milk. No more, no less. "
	),
	EwFood(
		id_food = "steakneggs",
		alias = [
			"steak",
			"sne",
		],
		recover_hunger = 150,
		price = 1500,
		inebriation = 0,
		str_name = "two steak tips and two sunny side up eggs",
		vendors = [vendor_diner, vendor_bazaar],
		str_eat = "You break the yolk of your two fried eggs immediately, letting the yolk run and pool around the steak tips, acting as a dipping sauce. With each mouthwatering bite of juicy, "
				  "medium rare steak coated in delicious, runny yolk, you reach a higher level of christ consciousness. How does no one else but you do this?",
		str_desc = "The only actually filling meal they serve at the diner. Between the two medium rare steak tips and the perfectly cooked sunny side up eggs, you’ve got enough protein in this one "
				   "meal to grow an extra muscle."
	),
	EwFood(
		id_food = "doubledown",
		alias = [
			"double",
			"down",
		],
		recover_hunger = 80,
		price = 800,
		inebriation = 0,
		str_name = 'Double Down',
		vendors = [vendor_kfc],
		str_eat = "You chomp into the meaty pseudo-sandwich! The Colonol's Special Sauce oozes over your lips and fingers, making you feel absolutely filthy.",
		str_desc = "From between two crispy chicken filets oozes the Colonel's Special Sauce. Haha, nasty!"
	),
	EwFood(
		id_food = "familymeal",
		alias = [
			"family",
			"meal",
			"fm",
		],
		recover_hunger = 480,
		price = 4800,
		inebriation = 0,
		str_name = 'KFC Family Meal',
		vendors = [vendor_kfc],
		str_eat = "You feast on all manner of Southern homestyle delicacies out of this greasy fast food banquet! Your hands turn to blurs as you shovel handfuls of juicy fried calorie nuggets "
				  "into your biological furnace as possible, only slowly down to chug the mushy sides down the very same abyss. You reduce the dinner intend for 5+ in a manner of minutes, causing "
				  "frightened onlookers to scream and faint. You chew and chew until your jaw aches and tears stream down your cheeks.",
		str_desc = "A veritable menagerie of cheap crap and homestyle goodness. Various fried, dismembered limbs of a chicken, instant mashed potatoes and gravy, oily mac n' cheese, stale biscuits, "
				   "the list goes on and on. It’s enough to feed an army, or one you."
	),
	EwFood(
		id_food = "plutoniumchicken",
		alias = [
			"pluto",
			"plutonium",
		],
		recover_hunger = 160,
		price = 1600,
		inebriation = 0,
		str_name = 'whole plutonium-battered fried baby chicken',
		vendors = [vendor_kfc],
		str_eat = "You crunch into the remains of this once-adorable animal. It’s odd metallic taste makes your tongue tingle in a most unsettling way. You try and blow a bubble with it but "
				  "you just end up spitting baby chicken bones five feet in front of you.",
		str_desc = "It resembles a miniature cooked chicken, save for an extra wing or too, or an hyperrealistic green peep. It is encrusted with an odd greenish-brown coating, which tickles "
				   "your skin upon touch. You could pop a few of these tiny things into your mouth at a time and feel their soul exit their body as you grind them into crispy dust. May adversely affect sperm count."
	),
	EwFood(
		id_food = "giantdeepdish",
		alias = [
			"gdd",
			"deepdish",
		],
		recover_hunger = 300,
		price = 3000,
		inebriation = 0,
		str_name = 'giant deep-dish pizza',
		vendors = [vendor_pizzahut],
		str_eat = "You slurp down soupy slice after soupy slice of the sopping sauce-soaked pizza in a gruesome spectacle. Gnarly!!",
		str_desc = "This goopy, near liquid mass of cheap marinara and pre-grated mozzarella resembles a hearty soup more so than a pizza. It’s sauce and cheese acts as quicksand, "
				   "with anything placed on its surface sinking to the bottom, never to be seen again."
	),
	EwFood(
		id_food = "whackcalzone",
		alias = [
			"wc",
			"whack",
			"calzone",
		],
		recover_hunger = 210,
		price = 2100,
		inebriation = 0,
		str_name = 'Whack Calzone',
		vendors = [vendor_pizzahut],
		str_eat = "You chomp into the colossal Italian confection in a mad craze, searing hot grease pours out from the edges and melted cheese explodes in every direction. De-LISH!!",
		str_desc = "It is literally just an upside-down pizza on top of another pizza. Your base, carnal desires will be the end of you one of these days."
	),
	EwFood(
		id_food = "nachosupreme",
		alias = [
			"ns",
			"nacho",
			"nachos",
			"supreme",
		],
		recover_hunger = 110,
		price = 1100,
		inebriation = 0,
		str_name = 'Nacho Supreme',
		vendors = [vendor_tacobell],
		str_eat = "You shovel fistfuls of nacho detritus into your gaping maw. Your gums are savaged by the sharp edges of the crips corny chips.",
		str_desc = "A plate full of crisp tortilla chips onto which ground beef, sour cream, cheese, tomatoes, and various assorted bullshit has been dumped.",
	),
	EwFood(
		id_food = "energytaco",
		alias = [
			"et",
			"energy",
			"etaco",
		],
		recover_hunger = 90,
		price = 900,
		inebriation = 0,
		str_name = 'Energy Taco',
		vendors = [vendor_tacobell],
		str_eat = "Biting into this taco, your mouth is numbed by a sudden discharge of stored energy, accompanied by a worrisome flash of greenish light. You can't say for sure if it tasted good or not.",
		str_desc = "This resembles a normal taco, but where the cheese might normally be is a strange glowing green fluid. It occasionally sparks and crackles with limic energy."
	),
	EwFood(
		id_food = "mtndewsyrup",
		alias = [
			"syrup",
			"mdsyrup",
			"mds",
			"greensyrup",
		],
		recover_hunger = 100,
		price = 1000,
		inebriation = 0,
		str_name = 'cup of pure undiluted MTN DEW syrup',
		vendors = [vendor_mtndew],
		str_eat = "You pour the molasses-like liquid down your throat. It stings your teeth and clings to your esophagus on the way down, but you feel suddenly invigorated as your blood sugar skyrockets!!",
		str_desc = "This thick, viscous green fluid reeks with a sickly-sweet citrusy odor.",
	),
	EwFood(
		id_food = "bajablastsyrup",
		alias = [
			"bbsyrup",
			"bbs",
			"bluesyrup",
		],
		recover_hunger = 100,
		price = 1000,
		inebriation = 0,
		str_name = 'cup of pure undiluted MTN DEW Baja Blast syrup',
		vendors = [vendor_mtndew],
		str_eat = "You pour the molasses-like liquid down your throat. It stings your teeth and clings to your esophagus on the way down, but you feel suddenly invigorated as your blood sugar skyrockets!!",
		str_desc = "This thick, viscous blue fluid reeks with a sickly-sweet tropical odor."
	),
	EwFood(
		id_food = "coderedsyrup",
		alias = [
			"crsyrup",
			"crs",
			"redsyrup",
		],
		recover_hunger = 100,
		price = 1000,
		inebriation = 0,
		str_name = 'cup of pure undiluted MTN DEW Code Red syrup',
		vendors = [vendor_mtndew],
		str_eat = "You pour the molasses-like liquid down your throat. It stings your teeth and clings to your esophagus on the way down, but you feel suddenly invigorated as your blood sugar skyrockets!!",
		str_desc = "This thick, viscous red fluid reeks with a sickly-sweet cherry odor."
	),
	EwFood(
		id_food = "pitchblacksyrup",
		alias = [
			"pbsyrup",
			"pbs",
			"blacksyrup",
			"purplesyrup"
		],
		recover_hunger = 100,
		price = 1000,
		inebriation = 0,
		str_name = 'cup of pure undiluted MTN DEW Pitch Black syrup',
		vendors = [vendor_mtndew],
		str_eat = "You pour the molasses-like liquid down your throat. It stings your teeth and clings to your esophagus on the way down, but you feel suddenly invigorated as your blood sugar skyrockets!!",
		str_desc = "This thick, viscous purple fluid reeks with a sickly-sweet grapey odor."
	),
	EwFood(
		id_food = "whiteoutsyrup",
		alias = [
			"wosyrup",
			"wos",
			"whitesyrup",
		],
		recover_hunger = 100,
		price = 1000,
		inebriation = 0,
		str_name = 'cup of pure undiluted MTN DEW White Out syrup',
		vendors = [vendor_mtndew],
		str_eat = "You pour the molasses-like liquid down your throat. It stings your teeth and clings to your esophagus on the way down, but you feel suddenly invigorated as your blood sugar skyrockets!!",
		str_desc = "This thick, viscous pale fluid reeks with a sickly-sweet citrusy odor."
	),
	EwFood(
		id_food = "livewiresyrup",
		alias = [
			"lwsyrup",
			"lws",
			"orangesyrup",
		],
		recover_hunger = 100,
		price = 1000,
		inebriation = 0,
		str_name = 'cup of pure undiluted MTN DEW Livewire syrup',
		vendors = [vendor_mtndew],
		str_eat = "You pour the molasses-like liquid down your throat. It stings your teeth and clings to your esophagus on the way down, but you feel suddenly invigorated as your blood sugar skyrockets!!",
		str_desc = "This thick, viscous orange fluid reeks with a sickly-sweet orangey odor."
	),
	EwFood(
		id_food = "mexicanpizza",
		alias = [
			"mp",
			"mexican",
		],
		recover_hunger = 70,
		price = 700,
		inebriation = 0,
		str_name = 'Mexican pizza',
		vendors = [vendor_tacobell],
		str_eat = "You chomp right into the damp, haphazard mess of ethnic flavors and poor ingredients. The four sauces inexplicably just dumped on top drizzle down your chin and ruin your shirt. "
				  "You feel like a complete dumbass, because you are.",
		str_desc = "What the hell. A nauseating layer of refried beans and mushy, paste-like ground beef on top of and topped with a soggy, limp corn tortilla, finished with pre-grated, "
				   "processed cheese maxed out on preservatives, weeks-old diced tomatoes, and a mysterious dark red, viscous liquid referred to only as “Mexican Pizza Sauce.” Oh joy!"
	),
	EwFood(
		id_food = item_id_doublestuffedcrust,
		alias = [
			"dsc",
			"stuffed",
			"stuffedcrust",
			"double",
			"doub",
			"dou"
		],
		recover_hunger = 500,
		price = 5000,
		inebriation = 0,
		str_name = 'Original Double Stuffed Crust® pizza',
		vendors = [vendor_pizzahut],
		str_eat = "You gaze upon the unholy, excessive pile of dough, pepperoni, grease, marinara and cheese you imprudently ordered. Tepidly, you bring the first slice to your tongue, "
				  "letting the melted cheese drizzle unto your awaiting tongue. And, just as a beast would be reduced to a state of pure carnal hunger and lust after acquiring it’s first taste of flesh and blood, "
				  "you enter a state of sheer wilderness, stuffing each stuffed crust into your teeth and gums and tongue and throat. You scream at the top of your lungs. Sicknasty, dude!!",
		str_desc = "Nothing can articulate the sheer awesomeness of this pizza. Always thought to be theoretically possible and discussed in hushed tones in obscure circles on the fringe of acceptable dialogue, "
				   "but never achieved in practice, this heap of diary and dough can only truly be comprehended through several layers of abstraction. It is too big, too thick, too heavy and too deep. "
				   "To put it simply, however, it is a pizza. Specifically, an Original Stuffed Crust® pizza. But, everything is doubled. Every ingredient is doubled. The toppings are doubled, "
				   "the cheese is doubled, the pepperoni is doubled, the grease is doubled, the yeast is doubled and you fucking bet you could fit your whole forearm into the caverns they dare call a crust, "
				   "if it weren’t overflowing with double the molten, stretchy string cheese. And it doesn’t stop there, double the size, double the weight, "
				   "double the budget required to ward off lawsuits for double the colohestral, double the heart attacks. People die because of this pizza, "
				   "someone you know has or will die because of this item in your inventory right now. It’s made to order, piping hot and ready to be devoured by "
				   "whatever foolish egomaniac with enough hubris to challenge it’s supremacy. Bow down before it, beg and weep for your life and the life of the ones you love. "
				   "Chant it’s name, praise the harbinger of death you just acquired from Pizza Hut. Doubled Stuffed Crust. Doubled Stuffed Crust. DOUBLE STUFFED CRUST!! AAAAAAAAAH!!"
	),
	EwFood(
		id_food = "boxofchocolates",
		alias = [
			"box",
			"chocolates",
		],
		recover_hunger = 500,
		price = 2500,

		inebriation = 0,
		str_name = 'box of chocolates',
		#vendors = [vendor_tacobell, vendor_pizzahut, vendor_kfc, vendor_bar, vendor_diner, vendor_seafood],
		#This was a Valenslime's Day only item, you shouldn't be able to order it anymore.
		str_eat = "You pop open the lid of the heart-shaped box and shower yourself in warm sugary delicates! Your face and shirt is grazed numerous times by the melted confections, smearing brown all over you. Baby made a mess.",
		str_desc = "A huge heart-shaped box of assorted, partially melted chocolates and other sweet hors d'oeuvres. Sickeningly sweet literally and metaphorically.",
	),
	EwFood(
		id_food = item_id_pinkrowddishes,
		recover_hunger = 60,
		str_name = 'Pink Rowddishes',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Pink Rowddishes. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "The sweet-smelling tubers stain your hands pink.",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = item_id_sludgeberries,
		recover_hunger = 60,
		str_name = 'Sludgeberries',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Sludgeberries. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "The thick syrup covering the green and teal berries makes your hands sticky.",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = item_id_pulpgourds,
		recover_hunger = 60,
		str_name = 'Pulp Gourds',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Pulp Gourds. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "The easily malleable gourds form indents from even your lightest touch.",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = item_id_joybeans,
		recover_hunger = 60,
		str_name = 'Joybeans',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Joybeans. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "The sugary candy-like beans have a thick gel interior that rots your teeth.",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = item_id_brightshade,
		recover_hunger = 60,
		str_name = 'Brightshade',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Brightshade. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "The dangerously toxic chemicals that cover the flower bud burn your eyes and nose.",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = item_id_direapples,
		recover_hunger = 60,
		str_name = 'Dire Apples',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Dire Apples. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "The vicious acidity from from the cyan and orange apples makes your mouth contort in pain with every bite.",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = item_id_purplekilliflower,
		recover_hunger = 60,
		str_name = 'Purple Killiflower',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Purple Killiflower. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "The deep purple head has an extremely bitter aftertaste.",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = item_id_razornuts,
		recover_hunger = 60,
		str_name = 'Razornuts',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Razornuts. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "The sharp edges of the hard nut slice open your mouth so that you taste slight hints of copper from your blood every bite.",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = item_id_poketubers,
		recover_hunger = 60,
		str_name = 'Poke-tubers',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Poke-tubers. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "The lame, sad, lumpy roots barely support a bulbous crop that’s indiscernible taste is not complemented by it’s awkward texture.",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = item_id_suganmanuts,
		recover_hunger = 60,
		str_name = 'Suganma Nuts',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Suganmanuts. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "The difficult nuts infuriate you for reasons you don’t really underst-- HEY WAIT A SECOND!!",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = item_id_dankwheat,
		recover_hunger = 60,
		str_name = 'Dankwheat',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Dankwheat. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "The damp barley milled from this moist wheat causes hallucinations and intoxication once digested fully.",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = item_id_blacklimes,
		recover_hunger = 60,
		str_name = 'Black Limes',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Black Limes. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "The sour juice squeezed from just one of these small dark grey limes can flavor an entire production of Warheads hard candy.",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = item_id_phosphorpoppies,
		recover_hunger = 60,
		str_name = 'Phosphorpoppies',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Phosphorpoppies. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "The vivid and unnatural colors of this plant reveal it’s man made origin. Some say SlimeCorp designed the plant’s addictive and anxiety/paranoia inducing nature to keep juveniles weak and disenfranchised.",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = item_id_sourpotatoes,
		recover_hunger = 60,
		str_name = 'Sour Potatoes',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Sour Potatoes. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "The staple of many unhealthy juveniles’ diet. It’s revolting taste leaves much to be desired.",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = item_id_bloodcabbages,
		recover_hunger = 60,
		str_name = 'Blood Cabbages',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Blood Cabbages. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "The dripping mass of dark crimson leaves have become the staple special effects tool for aspiration amatuer filmmakers in the city for it’s uncanny resemblance to human blood.",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = item_id_pawpaw,
		recover_hunger = 60,
		str_name = 'Pawpaw',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Pawpaw. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "An American classic.",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = "pinkrowdatouille",
		recover_hunger = 1200,
		str_name = 'Pink Rowdatouille',
		acquisition = acquisition_milling,
		ingredients = item_id_pinkrowddishes,
		str_eat = "You gingerly nibble on the fancy vegetables. It’s nostalgic taste sends you right back to your childhood, and your first encounter with the law. You had to get sent to the New Los Angeles City aka Neo Milwaukee Juvenile Detention Center somehow, after all. It feels like it happened so long ago, and yet, you can remember it like it was yesterday.",
		str_desc = "Thinly sliced rounds of Pink Rowddish and other colorful vegetables are slow roasted and drizzled with special sauce. It seems simple enough, it can’t taste THAT good, can it?",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "sludgeberrypancakes",
		recover_hunger = 800,
		str_name = 'Sludgeberry Pancakes',
		acquisition = acquisition_milling,
		ingredients = item_id_sludgeberries,
		str_eat = "You pick up the stack of pancakes with your hands, holding and biting into them as if they were a hamburger. Thick syrup coats your hands and mouth, ready to be licked off after the main meal has concluded.",
		str_desc = "Fluffy flapjacks filled with assorted Sludgeberries and topped with a heaping helping of viscous syrup. You’ve died and washed up in the sewers. But, like, a nice part of the sewers. This express doesn’t really translate well into the setting.",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "pulpgourdpie",
		recover_hunger = 800,
		str_name = 'Pulp Gourd Pie',
		acquisition = acquisition_milling,
		ingredients = item_id_pulpgourds,
		str_eat = "You pick up a piece like it's a goddamn slice of pizza, demolishing it in a few barbaric bites. Eventually you get your fill of the crust and just start scraping out the delicious Pulp Gourd filling goop and slathering it all over your mouth and tongue like you're a fucking mindless pig at his trough.",
		str_desc = "A warm, freshly baked pie. It's still molten, still solidifying Pulp Gourd filling beckons you like a siren lures a sailor. So many holidays have been ruined because of your addiction to this cinnamon imbued delicacy, and so many more will be in the future.",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "joybeanpastemochi",
		recover_hunger = 800,
		str_name = 'Joybean Paste Mochi',
		acquisition = acquisition_milling,
		ingredients = item_id_joybeans,
		str_eat = "You pop the delicate confectionary into your mouth and start ravenously shredding it into barely digestible chewy chunks. Sweet paste is slathered across your mouth. Your teeth enamel is decimated, execution style.",
		str_desc = "A sickeningly sweet  Joy Bean paste filling encased in a small, round mochi covered in powdered sugar. It’s *proper* name is “Daifucku.”",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "brightshadeseeds",
		recover_hunger = 800,
		str_name = 'Brightshade Seeds',
		acquisition = acquisition_milling,
		ingredients = item_id_brightshade,
		str_eat = "You pop a few seeds into your mouth at a time, grinding them into dust with your molars and digesting their sweet, sweet single digit calories.",
		str_desc = "A bag of Brightshade seeds, unsalted and ready for ill-advised consumption.",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "direapplejuice",
		recover_hunger = 800,
		str_name = 'Dire Apple Juice',
		acquisition = acquisition_milling,
		ingredients = item_id_direapples,
		str_eat = "You slurp down the delicious sugary juice! Hell yeah!",
		str_desc = "A 99% juice-like substance that tastes vaguely like Dire Apples! It’s so ubiquitous that you guarantee that if you rummaged through every school kid’s lunch in the city, you’d be sent to jail.",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "purplekilliflowercrustpizza",
		recover_hunger = 1200,
		str_name = 'Purple Killiflower Crust Pizza',
		acquisition = acquisition_milling,
		ingredients = item_id_purplekilliflower,
		str_eat = "You take a hesitant nibble of the famously keto pizza slice before coming to the reality that sometimes healthy things CAN taste good! You shove the rest of the slice in your mouth, nearly choking. Deep inside of your body, you can feel your kidney begin to churn and convulse. That’s probably fine.",
		str_desc = "A deliciously dietary-accordant slice of Killiflower crusted pizza. Made by milling down Killiflower into fine crumbs, combining with various irradiated cheeses, and baking until even notorious ENDLSS WAR critic Arlo is impressed. Now THIS is how you lose weight!",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "razornutbutter",
		recover_hunger = 800,
		str_name = 'Razornut Butter',
		acquisition = acquisition_milling,
		ingredients = item_id_razornuts,
		str_eat = "You take a hefty spoonful of the thick mucilage, coating your mouth completely. It’ll take weeks to swallow the last of it.",
		str_desc = "A tub of chunky, creamy Razonut Butter. Co-star of countless childhood classics. You know it was invented by a Juvie, right?",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "jellyfilleddoughnut",
		recover_hunger = 800,
		str_name = 'Jelly-Filled Doughnut',
		acquisition = acquisition_milling,
		ingredients = item_id_poketubers,
		str_eat = "You chomp into the delicious jelly-filled doughnuOH GOD WHY THE FUCK DOES IT TASTE LIKE A TRADITIONAL JAPANESE ONIGIRI WITH A PICKLE PLUM FILLING WHO COULD HAVE PREDICTED THIS?!?!",
		str_desc = "These jelly-filled doughnuts seem appetizing enough, but you're no expert. You never really cared much for jelly-filled doughnuts. In fact, in most scenarios you'd pass them up in favor of another pastry or sugary snack.",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "yourfavoritefood",
		recover_hunger = 800,
		str_name = '***Your Favorite Food***',
		acquisition = acquisition_milling,
		ingredients = item_id_suganmanuts,
		str_eat = "***You bite into your favorite meal!! It’s taste is literally indescribable!! You feel like you’re going retarded, your mind is clearly breaking!! Uwahhh!!***",
		str_desc = "***Your favorite meal!! You could go on for hours about how great this food is!! But, you won’t, because no one appreciates it as much as you do.***",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "dankwheattoast",
		recover_hunger = 800,
		str_name = 'Dankwheat Toast',
		acquisition = acquisition_milling,
		ingredients = item_id_dankwheat,
		str_eat = "You take a bite out of the Dank Wheat Toast, and immediately you begin to start staggering around, clearly lost in some sort of unearned pleasure.",
		str_desc = "A burnt, slightly soggy slice of Dank Wheat Toast. What more do you want out of me?",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "blacklimesour",
		recover_hunger = 800,
		str_name = 'Black Lime Sour',
		acquisition = acquisition_milling,
		ingredients = item_id_blacklimes,
		str_eat = "You take a swig of the obscure southern delicacy. Its overwhelming acidity tricks your mouth into generating quarts of saliva, refreshing your mouth and destroying your taste buds. Nifty!",
		str_desc = "A small paper cup with nothing but crushed ice, the juice of a Black Lime, a little salt, and about a pound of cocaine.",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "phosphorpoppiesmuffin",
		recover_hunger = 800,
		str_name = 'Phosphorpoppies Muffin',
		acquisition = acquisition_milling,
		ingredients = item_id_phosphorpoppies,
		str_eat = "You remove the muffin head from the stump, before devouring the former and throwing the later as far away from you as humanly possible. Good riddance.",
		str_desc = "Oooh, muffins! Remember that? Gimme a thumbs up with you get this joke.",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "sourpotatofrenchfries",
		recover_hunger = 800,
		str_name = 'Sour Potato French Fries',
		acquisition = acquisition_milling,
		ingredients = item_id_sourpotatoes,
		str_eat = "You bite into the fluffy, acidic french fries, occasionally dipping in into a selection of various dipping sauces such as hot slime and sweet slime. You divorce the actual flavor of the crispy exterior from it’s sour innards with a technique not unlike the one used to get the last drop of toothpaste out of it’s tube. Your face convulses in pain.",
		str_desc = "Some gloriously thick cut Sour Potato french fries accompanied by an embarrassment of tasty slime-based dipping sauces. What else could a juvenile asked for?? Maybe some sugar and baking soda, this shit is unbelievably acidic.",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "bloodcabbagecoleslaw",
		recover_hunger = 800,
		str_name = 'Blood Cabbage Coleslaw',
		acquisition = acquisition_milling,
		ingredients = item_id_bloodcabbages,
		str_eat = "You drop the semi-solidified puck of red coleslaw into your eager maw, upon which the faux gelletain instantly loses it’s form and start to crumble into drop down your face. You manage to digest a cabbage shred.",
		str_desc = "A congealed dark crimson slab of myoglobin encasing sparse strands of Blood Cabbage. It jiggles when you shake the cup it’s stored in. Why the fuck would you mill this?",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "pawpawfood",
		recover_hunger = 800,
		str_name = 'Pawpaw Food',
		acquisition = acquisition_milling,
		ingredients = item_id_pawpaw,
		str_eat = "You slowly drink the bitter, flavorless mush. Its… uh… food?",
		str_desc = "An unappetizing pile of Pawpaw Gruel. It’s just Pawpaw milled into something halfway between puke and diarrhea. The staple of a traditional Juvenile diet. ",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "khaotickilliflowerfuckenergy",
		alias = [
			"kkfu"
		],
		recover_hunger = 1200,
		price = 12000,
		inebriation = 1000,
		vendors = [vendor_mtndew, vendor_vendingmachine],
		str_name = 'Khaotic Killiflower FUCK ENERGY Drink',
		str_eat = "You crack open a cold, refreshing can of Khaotic Killiflower flavored FUCK ENERGY. You throw your head back and begin to chug it, its viciously viscous consistency is almost enough to trigger your gag reflexes. But, you hold strong. Its bitter, low quality artificial Purple Killiflower flavorings remind you of discount children’s cough medicine. Nigh instantaneously, the chemicals infiltrate your central nervous system. You feel an intense heat, like your body is about to spontaneously combust. You become lightheaded, your body twitching and convulsing randomly. And then, suddenly, you are launched into a manic, hyper-awareness. You begin to process more information in a single nanosecond than people with a masters in theoretical physics analyze in a lifetime. Your left and right brain sever, they now operate completely separately from one another and twice as efficiently. Your pineal gland doubles, nay, triples in size. You have never felt more alive. You crush the can with your forehead, screaming.",
		str_desc = "A cold, refreshing can of Khaotic Killiflower flavored FUCK ENERGY. You can occasionally feel rumbles from inside it, the drink itself begging to be released from the thin metal sarcophagus that barely contains it. You flip it over to read the blurb on the back.\n\n\n*Make no mistake - FUCK ENERGY is not your grandma's run-of-the-mill pissy baby fucker fapper limp, lame liquid masquerading as a psychotic psychedelic or performance-enhancing elixir. FUCK ENERGY is the real deal. From the moment you bought this energy drink, your fate was sealed, cursed. Reality itself has been rewritten, and your destiny decided. Your body's natural limits and basic inhibitions will be completely and utterly pulverized, ground into dust to be scavenged by us to imbue into the next incarnation of the very instrument of your destruction. Every FUCK ENERGY is infused, steeped in the atomized souls of our unprepared consumers. You will contribute to this vicious cycle, at a near molecular level your very consciousness will be ripped apart and sold into slavery. Your new master? Us. Every drop of FUCK ENERGY has been rigorously tested to systematically attack you, shutting down entire bodily functions. Your organs will be forcefully transformed into top-of-the-line computer parts, hand picked by a cruel computer science major to maximize the fidelity of his foreign language visual erotica. Your brain will be overclocked, your heart pushed past all previous extremes, and without an internal fan to cool it down either. You will be a being of pure adrenaline and a martyr for dopamine. You will be consumed by the abstract idea of energy. But, it won't be abstract to you. You will understand energy more than any other living creature on this planet. Now go, open this quite literal Pandora's Box. Escaping your purpose is impossible. What are you waiting for? Are you scared? GET FUCKED.*",
	),
	EwFood(
		id_food = "rampagingrowddishfuckenergy",
		alias = [
			"rrfu"
		],
		recover_hunger = 1200,
		price = 12000,
		inebriation = 1000,
		vendors = [vendor_mtndew, vendor_vendingmachine],
		str_name = 'Rampaging Rowddish FUCK ENERGY Drink',
		str_eat = "You crack open a cold, refreshing can of Rampaging Rowddish flavored FUCK ENERGY. You throw your head back and begin to chug it, its viciously viscous consistency is almost enough to trigger your gag reflexes. But, you hold strong. Its sickeningly sweet artificial Pink Rowddish flavorings taste like if you mixed about 16 packs of Starburst FaveREDs into a blender. Nigh instantaneously, the chemicals infiltrate your central nervous system. You feel an intense heat, like your body is about to spontaneously combust. You become lightheaded, your body twitching and convulsing randomly. And then, suddenly, you are launched into a manic, hyper-awareness. You begin to process more information in a single nanosecond than people with a masters in theoretical physics analyze in a lifetime. Your left and right brain sever, they now operate completely separately from one another and twice as efficiently. Your pineal gland doubles, nay, triples in size. You have never felt more alive. You crush the can with your forehead, screaming.",
		str_desc = "A cold, refreshing can of Rampaging Rowddish flavored FUCK ENERGY. You can occasionally feel rumbles from inside it, the drink itself begging to be released from the thin metal sarcophagus that barely contains it. You flip it over to read the blurb on the back.\n\n\n*Make no mistake - FUCK ENERGY is not your grandma's run-of-the-mill pissy baby fucker fapper limp, lame liquid masquerading as a psychotic psychedelic or performance-enhancing elixir. FUCK ENERGY is the real deal. From the moment you bought this energy drink, your fate was sealed, cursed. Reality itself has been rewritten, and your destiny decided. Your body's natural limits and basic inhibitions will be completely and utterly pulverized, ground into dust to be scavenged by us to imbue into the next incarnation of the very instrument of your destruction. Every FUCK ENERGY is infused, steeped in the atomized souls of our unprepared consumers. You will contribute to this vicious cycle, at a near molecular level your very consciousness will be ripped apart and sold into slavery. Your new master? Us. Every drop of FUCK ENERGY has been rigorously tested to systematically attack you, shutting down entire bodily functions. Your organs will be forcefully transformed into top-of-the-line computer parts, hand picked by a cruel computer science major to maximize the fidelity of his foreign language visual erotica. Your brain will be overclocked, your heart pushed past all previous extremes, and without an internal fan to cool it down either. You will be a being of pure adrenaline and a martyr for dopamine. You will be consumed by the abstract idea of energy. But, it won't be abstract to you. You will understand energy more than any other living creature on this planet. Now go, open this quite literal Pandora's Box. Escaping your purpose is impossible. What are you waiting for? Are you scared? GET FUCKED.*",
	),
	EwFood(
		id_food = "direappleciderfuckenergy",
		alias = [
			"dacfu"
		],
		recover_hunger = 1200,
		price = 12000,
		inebriation = 1000,
		vendors = [vendor_mtndew, vendor_vendingmachine],
		str_name = 'Dire Apple Cider FUCK ENERGY Drink',
		str_eat = "You crack open a cold, refreshing can of Dire Apple Cider flavored FUCK ENERGY. You throw your head back and begin to chug it, its viciously viscous consistency is almost enough to trigger your gag reflexes. But, you hold strong. Its wickedly sour artificial Dire Apple flavorings, mixed with its thick consistency, makes it feel like you’re drinking applesauce mixed with a healthy heaping of malic acid. Nigh instantaneously, the chemicals infiltrate your central nervous system. You feel an intense heat, like your body is about to spontaneously combust. You become lightheaded, your body twitching and convulsing randomly. And then, suddenly, you are launched into a manic, hyper-awareness. You begin to process more information in a single nanosecond than people with a masters in theoretical physics analyze in a lifetime. Your left and right brain sever, they now operate completely separately from one another and twice as efficiently. Your pineal gland doubles, nay, triples in size. You have never felt more alive. You crush the can with your forehead, screaming.",
		str_desc = "A cold, refreshing can of Dire Apple Cider flavored FUCK ENERGY. You can occasionally feel rumbles from inside it, the drink itself begging to be released from the thin metal sarcophagus that barely contains it. You flip it over to read the blurb on the back.\n\n\n*Make no mistake - FUCK ENERGY is not your grandma's run-of-the-mill pissy baby fucker fapper limp, lame liquid masquerading as a psychotic psychedelic or performance-enhancing elixir. FUCK ENERGY is the real deal. From the moment you bought this energy drink, your fate was sealed, cursed. Reality itself has been rewritten, and your destiny decided. Your body's natural limits and basic inhibitions will be completely and utterly pulverized, ground into dust to be scavenged by us to imbue into the next incarnation of the very instrument of your destruction. Every FUCK ENERGY is infused, steeped in the atomized souls of our unprepared consumers. You will contribute to this vicious cycle, at a near molecular level your very consciousness will be ripped apart and sold into slavery. Your new master? Us. Every drop of FUCK ENERGY has been rigorously tested to systematically attack you, shutting down entire bodily functions. Your organs will be forcefully transformed into top-of-the-line computer parts, hand picked by a cruel computer science major to maximize the fidelity of his foreign language visual erotica. Your brain will be overclocked, your heart pushed past all previous extremes, and without an internal fan to cool it down either. You will be a being of pure adrenaline and a martyr for dopamine. You will be consumed by the abstract idea of energy. But, it won't be abstract to you. You will understand energy more than any other living creature on this planet. Now go, open this quite literal Pandora's Box. Escaping your purpose is impossible. What are you waiting for? Are you scared? GET FUCKED.*",
	),
	EwFood(
		id_food = "ultimateurinefuckenergy",
		alias = [
			"uufu"
		],
		recover_hunger = 1200,
		price = 12000,
		inebriation = 1000,
		vendors = [vendor_mtndew, vendor_vendingmachine],
		str_name = 'Ultimate Urine FUCK ENERGY Drink',
		str_eat = "You crack open a cold, refreshing can of Ultimate Urine flavored FUCK ENERGY. You throw your head back and begin to chug it, its viciously viscous consistency is almost enough to trigger your gag reflexes. But, you hold strong. It literally just tastes like piss. You’re almost positive you’re literally drinking pee right now. It’s not even carbonated. Nigh instantaneously, the chemicals infiltrate your central nervous system. You feel an intense heat, like your body is about to spontaneously combust. You become lightheaded, your body twitching and convulsing randomly. And then, suddenly, you are launched into a manic, hyper-awareness. You begin to process more information in a single nanosecond than people with a masters in theoretical physics analyze in a lifetime. Your left and right brain sever, they now operate completely separately from one another and twice as efficiently. Your pineal gland doubles, nay, triples in size. You have never felt more alive. You crush the can with your forehead, screaming.",
		str_desc = "A cold, refreshing can of Ultimate Urine flavored FUCK ENERGY. You can occasionally feel rumbles from inside it, the drink itself begging to be released from the thin metal sarcophagus that barely contains it. You flip it over to read the blurb on the back.\n\n\n*Make no mistake - FUCK ENERGY is not your grandma's run-of-the-mill pissy baby fucker fapper limp, lame liquid masquerading as a psychotic psychedelic or performance-enhancing elixir. FUCK ENERGY is the real deal. From the moment you bought this energy drink, your fate was sealed, cursed. Reality itself has been rewritten, and your destiny decided. Your body's natural limits and basic inhibitions will be completely and utterly pulverized, ground into dust to be scavenged by us to imbue into the next incarnation of the very instrument of your destruction. Every FUCK ENERGY is infused, steeped in the atomized souls of our unprepared consumers. You will contribute to this vicious cycle, at a near molecular level your very consciousness will be ripped apart and sold into slavery. Your new master? Us. Every drop of FUCK ENERGY has been rigorously tested to systematically attack you, shutting down entire bodily functions. Your organs will be forcefully transformed into top-of-the-line computer parts, hand picked by a cruel computer science major to maximize the fidelity of his foreign language visual erotica. Your brain will be overclocked, your heart pushed past all previous extremes, and without an internal fan to cool it down either. You will be a being of pure adrenaline and a martyr for dopamine. You will be consumed by the abstract idea of energy. But, it won't be abstract to you. You will understand energy more than any otherr living creature on this planet. Now go, open this quite literal Pandora's Box. Escaping your purpose is impossible. What are you waiting for? Are you scared? GET FUCKED.*",
	),
	EwFood(
		id_food = "superwaterfuckenergy",
		alias = [
			"swfu"
		],
		recover_hunger = 1200,
		price = 12000,
		inebriation = 1000,
		vendors = [vendor_mtndew, vendor_vendingmachine],
		str_name = 'Super Water FUCK ENERGY Drink',
		str_eat = "You crack open a cold, refreshing can of Super Water flavored FUCK ENERGY. You throw your head back and begin to chug it, its viciously viscous consistency is almost enough to trigger your gag reflexes. But, you hold strong. Its extremely potent artificial water flavorings overwhelm your senses, temporarily shutting off your brain from the sheer amount of information being sent to it from your overloaded taste buds. You probably are literally retarded now. Nigh instanously, the chemicals infiltrate your central nervous system. You feel an intense heat, like your body is about to spontaneously combust. You become lightheaded, your body twitching and convulsing randomly. And then, suddenly, you are launched into a manic, hyper-awareness. You begin to process more information in a single nanosecond than people with a masters in theoretical physics analyze in a lifetime. Your left and right brain sever, they now operate completely separately from one another and twice as efficiently. Your pineal gland doubles, nay, triples in size. You have never felt more alive. You crush the can with your forehead, screaming.",
		str_desc = "A cold, refreshing can of Super Water flavored FUCK ENERGY. You can occasionally feel rumbles from inside it, the drink itself begging to be released from the thin metal sarcophagus that barely contains it. You flip it over to read the blurb on the back.\n\n\n*Make no mistake - FUCK ENERGY is not your grandma's run-of-the-mill pissy baby fucker fapper limp, lame liquid masquerading as a psychotic psycadellic or performance-enhancing elixir. FUCK ENERGY is the real deal. From the moment you bought this energy drink, your fate was sealed, cursed. Reality itself has been rewritten, and your destiny decided. Your body's natural limits and basic inhibitions will be completely and utterly pulverized, ground into dust to be scavenged by us to imbue into the next incarnation of the very instrument of your destruction. Every FUCK ENERGY is infused, steeped in the atomized souls of our unprepared consumers. You will contribute to this vicious cycle, at a near molecular level your very consciousness will be ripped apart and sold into slavery. Your new master? Us. Every drop of FUCK ENERGY has been rigorously tested to systematically attack you, shutting down entire bodily functions. Your organs will be forcefully transformed into top-of-the-line computer parts, hand picked by a cruel computer science major to maximize the fidelity of his foreign language visual erotica. Your brain will be overclocked, your heart pushed past all previous extremes, and without an internal fan to cool it down either. You will be a being of pure adrenaline and a martyr for dopamine. You will be consumed by the abstract idea of energy. But, it won't be abstract to you. You will understand energy more than any other living creature on this planet. Now go, open this quite literal Pandora's Box. Escaping your purpose is impossible. What are you waiting for? Are you scared? GET FUCKED.*",
	),
	EwFood(
		id_food = item_id_quadruplestuffedcrust,
		alias = [
			"qsc",
			"quadruple",
			"quadruplestuffed"
		],
		recover_hunger = 1000,
		str_name = "Original Quadruple Stuffed Crust® Pizza",
		str_eat = "You gaze upon the unholy, excessive pile of dough, pepperoni, grease, marinara and cheese you "
				  "imprudently smelted. Tepidly, you bring the first slice to your tongue, letting the melted "
				  "cheese drizzle unto your awaiting tongue. And, just as a beast would be reduced to a state of pure "
				  "carnal hunger and lust after acquiring it’s first taste of flesh and blood, you enter a state of "
				  "sheer wilderness, stuffing each stuffed crust into your teeth and gums and tongue and throat. You "
				  "scream at the top of your lungs. Sicknasty, dude!!",
		str_desc = "Nothing can articulate the sheer awesomeness of this pizza. Always thought to be theoretically "
				   "possible and discussed in hushed tones in obscure circles on the fringe of acceptable dialogue, but "
				   "never achieved in practice, this heap of diary and dough can only truly be comprehended through "
				   "several layers of abstraction. It is too big, too thick, too heavy and too deep. To put it simply, "
				   "however, it is a pizza. Specifically, an Original Stuffed Crust® pizza. But, everything is quadrupled. "
				   "Every ingredient is quadrupled. The toppings are quadrupled, the cheese is quadrupled, the pepperoni "
				   "is quadrupled, the grease is quadrupled, the yeast is quadrupled and you fucking bet you could fit "
				   "your whole forearm into the caverns they dare call a crust, if it weren’t overflowing with quadruple "
				   "the molten, stretchy string cheese. And it doesn’t stop there, quadruple the size, quadruple the weight, "
				   "quadruple the budget required to ward off lawsuits for quadruple the colohestral, quadruple the heart "
				   "attacks. People die because of this pizza, someone you know has or will die because of this item in your "
				   "inventory right now. It’s made to order, piping hot and ready to be devoured by whatever foolish egomaniac "
				   "with enough hubris to challenge it’s supremacy. Bow down before it, beg and weep for your life and the "
				   "life of the ones you love. Chant it’s name, praise the harbinger of death you just acquired from Pizza "
				   "Hut. Quadruple Stuffed Crust. Quadruple Stuffed Crust. QUADRUPLE STUFFED CRUST!! AAAAAAAAAAAAAAAAAAH!!",
		acquisition = acquisition_smelting
	),
	EwFood(
		id_food = item_id_monstersoup,
		alias = [
			"soup",
			"meatsoup",
			"stew",
			"meatstew",
			"monstersoup",
			"monster soup"
		],
		recover_hunger = 2000,
		str_name = "Homemade Monster Soup",
		str_eat = "You gaze upon the large bowl of monster soup and slurp it down, your throat scratched by the copious ammounts "
		"of bone shards that permiate the rich broth. Meaty and homely, just like grandma made it.",
		str_desc = "A large bowl of soup covered with the saran wrap that prevents you from smelling the wonderous mix of"
		"soft meat and crackling bones, full of nutrients and carcinogens in equal ammounts.",
		acquisition = acquisition_smelting
	),
	EwFood(
		id_food = item_id_octuplestuffedcrust,
		alias = [
			"osc",
			"octuple",
			"octuplestuffed"
		],
		recover_hunger = 2000,
		str_name = "Original Octuple Stuffed Crust® Pizza",
		str_eat = "You gaze upon the unholy, excessive pile of dough, pepperoni, grease, marinara and cheese you "
				  "imprudently smelted. Tepidly, you bring the first slice to your tongue, letting the melted "
				  "cheese drizzle unto your awaiting tongue. And, just as a beast would be reduced to a state of pure "
				  "carnal hunger and lust after acquiring it’s first taste of flesh and blood, you enter a state of "
				  "sheer wilderness, stuffing each stuffed crust into your teeth and gums and tongue and throat. You "
				  "scream at the top of your lungs. Sicknasty, dude!!",
		str_desc = "Nothing can articulate the sheer awesomeness of this pizza. Always thought to be theoretically "
				   "possible and discussed in hushed tones in obscure circles on the fringe of acceptable dialogue, but "
				   "never achieved in practice, this heap of diary and dough can only truly be comprehended through "
				   "several layers of abstraction. It is too big, too thick, too heavy and too deep. To put it simply, "
				   "however, it is a pizza. Specifically, an Original Stuffed Crust® pizza. But, everything is octupled. "
				   "Every ingredient is octupled. The toppings are octupled, the cheese is octupled, the pepperoni "
				   "is octupled, the grease is octupled, the yeast is octupled and you fucking bet you could fit "
				   "your whole forearm into the caverns they dare call a crust, if it weren’t overflowing with octuple "
				   "the molten, stretchy string cheese. And it doesn’t stop there, octuple the size, octuple the weight, "
				   "octuple the budget required to ward off lawsuits for octuple the colohestral, octuple the heart "
				   "attacks. People die because of this pizza, someone you know has or will die because of this item in your "
				   "inventory right now. It’s made to order, piping hot and ready to be devoured by whatever foolish egomaniac "
				   "with enough hubris to challenge it’s supremacy. Bow down before it, beg and weep for your life and the "
				   "life of the ones you love. Chant it’s name, praise the harbinger of death you just acquired from Pizza "
				   "Hut. Octuple Stuffed Crust. Octuple Stuffed Crust. OCTUPLE STUFFED CRUST!! *AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH!!*",
		acquisition = acquisition_smelting
	),
	EwFood(
		id_food = item_id_sexdecuplestuffedcrust,
		alias = [
			"sdsc",
			"sexdecuple",
			"sexdecuplestuffed"
		],
		recover_hunger = 4000,
		str_name = "Original Sexdecuple Stuffed Crust® Pizza",
		str_eat = "You gaze upon the unholy, excessive pile of dough, pepperoni, grease, marinara and cheese you "
				  "imprudently smelted. Something is… wrong. You can’t really put your finger on it, but you start feeling a strange sensation starting into this pizza. "
				  "Tepidly, you bring the first slice to your tongue, letting the melted "
				  "cheese drizzle unto your awaiting tongue. And, just as a beast would be reduced to a state of pure "
				  "carnal hunger and lust after acquiring it’s first taste of flesh and blood, you enter a state of "
				  "sheer wilderness, stuffing each stuffed crust into your teeth and gums and tongue and throat. You "
				  "scream at the top of your lungs. Sicknasty, dude!!",
		str_desc = "Nothing can articulate the sheer frightening presence of this pizza. Something is… wrong. You can’t really put your finger on it, "
				   "but you start feeling a strange sensation starting into this pizza. Always thought to be theoretically "
				   "possible and discussed in hushed tones in obscure circles on the fringe of acceptable dialogue, but "
				   "never achieved in practice, this heap of diary and dough can only truly be comprehended through "
				   "several layers of abstraction. It is too big, too thick, too heavy and too deep. To put it simply, "
				   "however, it is a pizza. Specifically, an Original Stuffed Crust® pizza. But, everything is sexdecupled. "
				   "Every ingredient is sexdecupled. The toppings are sexdecupled, the cheese is sexdecupled, the pepperoni "
				   "is sexdecupled, the grease is sexdecupled, the yeast is sexdecupled and you fucking bet you could fit "
				   "your whole forearm into the caverns they dare call a crust, if it weren’t overflowing with sexdecuple "
				   "the molten, stretchy string cheese. And it doesn’t stop there, sexdecuple the size, sexdecuple the weight, "
				   "sexdecuple the budget required to ward off lawsuits for sexdecuple the colohestral, sexdecuple the heart "
				   "attacks. People die because of this pizza, someone you know has or will die because of this item in your "
				   "inventory right now. It’s made to order, piping hot and ready to be devoured by whatever foolish egomaniac "
				   "with enough hubris to challenge it’s supremacy. Bow down before it, beg and weep for your life and the "
				   "life of the ones you love. Chant it’s name, praise the harbinger of death you just acquired from Pizza "
				   "Hut. sexdecuple Stuffed Crust. sexdecuple Stuffed Crust. SEXDECUPLE STUFFED CRUST!! **AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH!!**",
		acquisition = acquisition_smelting
	),
	EwFood(
		id_food = item_id_duotrigintuplestuffedcrust,
		alias = [
			"dtsc",
			"duotrigintuple",
			"duotrigintuplestuffed"
		],
		recover_hunger = 8000,
		str_name = "Original Duotrigintuple Stuffed Crust® Pizza",
		str_eat = "You gaze upon the unholy, excessive pile of dough, pepperoni, grease, marinara and cheese you "
				  "imprudently smelted. It was funny at first, but now this pizza is seriously starting to creep you out. Looking at it for too long gives you a headache, "
				  "and you can feel a cold shiver run up your spine. But, you smelted it. You might as well eat it. Tepidly, you bring the first slice to your tongue, letting the melted "
				  "cheese drizzle unto your awaiting tongue. And… the taste is surprisingly mild. In fact, it doesn’t really taste like anything. "
				  "For all the bottled oregano, store-bought marinara, and grease this thing is soaked in, it just sort of tastes like… nothing. This is concerning. You are concerned.",
		str_desc = "Nothing can articulate the sheer frightening presence of this pizza. It was funny at first, but now this pizza "
				   "is seriously starting to creep you out. Looking at it for too long gives you a headache, and you can feel a cold shiver run up your spine. You can’t really put your finger on it, "
				   "but you start feeling a strange sensation starting into this pizza. Always thought to be theoretically "
				   "possible and discussed in hushed tones in obscure circles on the fringe of acceptable dialogue, but "
				   "never achieved in practice, this heap of diary and dough can only truly be comprehended through "
				   "several layers of abstraction. It is too big, too thick, too heavy and too deep. To put it simply, "
				   "however, it is a pizza. Specifically, an Original Stuffed Crust® pizza. But, everything is duotrigintupled. "
				   "Every ingredient is duotrigintupled. The toppings are duotrigintupled, the cheese is duotrigintupled, the pepperoni "
				   "is duotrigintupled, the grease is duotrigintupled, the yeast is duotrigintupled and you fucking bet you could fit "
				   "your whole forearm into the caverns they dare call a crust, if it weren’t overflowing with duotrigintuple "
				   "the molten, stretchy string cheese. And it doesn’t stop there, duotrigintuple the size, duotrigintuple the weight, "
				   "duotrigintuple the budget required to ward off lawsuits for duotrigintuple the colohestral, duotrigintuple the heart "
				   "attacks. People die because of this pizza, someone you know has or will die because of this item in your "
				   "inventory right now. It’s made to order, piping hot and ready to be devoured by whatever foolish egomaniac "
				   "with enough hubris to challenge it’s supremacy. Bow down before it, beg and weep for your life and the "
				   "life of the ones you love. Chant it’s name, praise the harbinger of death you just acquired from Pizza "
				   "Hut. Duotrigintuple Stuffed Crust. Duotrigintuple Stuffed Crust. DUOTRIGINTUPLE STUFFED CRUST!! ***AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH!!***",
		acquisition = acquisition_smelting
	),
	EwFood(
		id_food = item_id_quattuorsexagintuplestuffedcrust,
		alias = [
			"qssc",
			"quattuorsexagintuple",
			"quattuorsexagintuplestuffed"
		],
		recover_hunger = 16000,
		str_name = "Original Quattuorsexagintuple Stuffed Crust® Pizza",
		str_eat = "You gaze upon the unholy mountain of red, white, and yellow that vaguely forms the shape of a pizza. "
				  "Rather, you try to. It is hard to look at directly. Like a mirage obscured by heatwaves, it subtly "
				  "changes shape, as if its true dimensions are imperceivable to the naked eye. It radiates a menacing aura. "
				  "You don’t even really want to eat it, but you feel compelled by forces you can’t really articulate. "
				  "You take a bite and… it’s disgusting. You want to spit it out, but, you can’t. It tastes like death. "
				  "You eat and eat, your body refusing to stop as you  devour the entire pizza. You cry the entire time.",
		str_desc = "Nothing can articulate the truly terrifying nature of this pizza. And so, you won’t even try to. "
				   "All that you can describe is the feeling you get being in its presence, which to say the very least "
				   "is not good. You feel cold and sweaty, like you’re perpetually falling. You know you should drop "
				   "this thing and run away as fast as possible, but… you’ve worked so hard for this. You’re in the end game. "
				   "Your thoughts of absconding are quickly overwhelmed by its name echoing in your mind. Duotrigintuple "
				   "Stuffed Crust. Duotrigintuple Stuffed Crust. DUOTRIGINTUPLE STUFFED CRUST.",
		acquisition = acquisition_smelting
	),
	EwFood(
		id_food = item_id_forbiddenstuffedcrust,
		alias = [
			"fsc",
			"forbiddenstuffedcrust",
		],
		recover_hunger = 340282366920938463463374607431768211455,
		str_name = "The Forbidden Stuffed Crust Pizza",
		str_eat = forbiddenstuffedcrust_eat,
		str_desc = forbiddenstuffedcrust_desc,
		acquisition = acquisition_smelting
	),
	EwFood(
		id_food = item_id_dinoslimemeat,
		alias = [
			"meat",
			"mutton",
			"monstermeat",
			"ssm"
		],
		recover_hunger = 500,
		str_name = 'Dinoslime Meat',
		str_eat = "You bite into the raw meat of dead Dinoslime. It feels like you're biting into raw sewage at certain points, but hey, food is food.",
		str_desc = "The meat of a Dinoslime. It's best to probably cook it before consumption, if only you knew how.",
	),
	EwFood(
		id_food = item_id_dinoslimesteak,
		alias = [
			"cookedmeat",
			"sss"
		],
		recover_hunger = 2500,
		str_name = 'Dinoslime Steak',
		str_eat = "You savour every last bite of your meal, and all the doubt you might have had about sacrificing your sticks washes away.",
		str_desc = "Through a stroke of genius, a faggot was sacrificed, and fire was made. The result is the meat of a savage beast, seared to perfection.",
		acquisition = acquisition_smelting
	),
	EwFood(
		id_food = item_id_paradoxchocs,
		alias = [
			"chocs",
		],
		recover_hunger = 120,
	price = 100,
		str_name = 'Paradox Chocs',
		str_eat = "You eat the Paradox Chocs. They don't taste all that good, but that's part of their charm, you think.",
		str_desc = "A bag of chocolates. Almost all of them are shaped like the head of Paradox Crocs. Every bag also comes with a Koff head, a Seani head, and an ~~Ackro~~ Obama head.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_twixten,
		alias = [
			"twix",
		],
		recover_hunger = 150,
	price = 100,
		str_name = 'Twixten',
		str_eat = "You sink your teeth into the Twixten, working your way down the blade, and finally giving a huge bite into the hilt. *CRUNCH*",
		str_desc = "A chocolate bar. It's shaped like a katana.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_snipercannon,
		alias = [
			"sniper",
			"cannon",
		],
		recover_hunger = 100,
		price = 100,
		str_name = 'Sniper Cannon',
		str_eat = "You take a bite out of your Sniper Cannon bar.",
		str_desc = "A chocolate bar with wafers on the inside. It's shaped like a bulky, rectangular version of the cannon found on the arm of the Unnerving Fighting Operator. On the back of the wrapper, there's some text that reads: 'We at Slimy Persuits had only the best intentions in our initial run of the [REDACTED] bar. We hope this rebranding will allow you to continue to enjoy our products without having to fear of blatant racism.'",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_slimybears,
		alias = [
			"bears",
		],
		recover_hunger = 80,
		price = 100,
		str_name = 'Slimy Bears',
		str_eat = "You stash a fistfull of Slimy Bears right into your gullet, chewing them thoroughly.",
		str_desc = "A packet of Slimy Bears. They come in a variety of colors, like purple, pink, green, and... yellow? Somehow this weirds you out a bit...",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_n8heads,
		alias = [
			"n8s",
		],
		recover_hunger = 60,
		price = 100,
		str_name = 'N8heads',
		str_eat = "You chew on a N8head. It stopped tasting good long before you were done sinking your teeth into it, but you felt committed enough to finish what you started. Fuckin shill.",
		str_desc = "A N8heads packet. They're bars of sour taffy, each with his signature shades imprinted onto them.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_turstwerthers,
		alias = [
			"turst",
		],
		recover_hunger = 70,
		price = 100,
		str_name = 'Turstwerthers',
		str_eat = "You shatter the Turstwerthers in your mouth, and the gooey caramel seeps out with every bite. Simply delight!",
		str_desc = "A bag of Turstwerthers. They're hard caramels, shaped like elephant tusks.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_candybungis,
		alias = [
			"bungis",
		],
		recover_hunger = 100,
		price = 1000,
		str_name = 'Candy (Bungis)',
		str_eat = "You eat through the Candy (Bungis). Rather than imprint the temporary tattoo, you just shove the whole thing into your mouth and chew through it.",
		str_desc = "A rolled up fruit snack. An layer of ink it has allows you to imprint an image of Sky (Bungis) onto your tongue.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_licoricelobsters,
		alias = [
			"licorice",
		],
		recover_hunger = 150,
		price = 1000,
		str_name = 'Licorice Lobsters',
		str_eat = "You chomp on the Licorice Lobsters. Their slight bittersweetness fills you with memories of days gone by.",
		str_desc = "Yup. They're lobsters.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_chocolateslimecorpbadges,
		alias = [
			"badges",
		],
		recover_hunger = 200,
		price = 1000,
		str_name = 'Chocolate Slimecorp Badges',
		str_eat = "You eat the Chocolate Slimecorp Badges. They taste surprisingly good. Maybe they're home-made?",
		str_desc = "A plastic bag of chocolates, all resembling that infamous logo. Snapping them in half reveals a thin layer of graham cracker on the inside.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_poudrinpops,
		alias = [
			"pops",
		],
		recover_hunger = 100,
		price = 1000,
		str_name = 'Poudrin Pops',
		str_eat = "You crush the poudrin pops with your teeth alone. You don't gain any slime, but they do taste amazing.",
		str_desc = "Hard, green candy, meant to resemble Slime Poudrins. They're placed atop plastic rings, meant to be worn on your finger as you lick away.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_atms,
		alias = [
			"ATm's",
		],
		recover_hunger = 130,
		price = 1000,
		str_name = "ATm's",
		str_eat = "You snack on the packet of ATm's. The hard shell pairs nicely with the milk chocolate on the inside.",
		str_desc = "A packet of ATm's. They're all small, spherical chocolates with the @ symbol on them.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_seanis,
		alias = [
			"seanies",
		],
		recover_hunger = 90,
		price = 1000,
		str_name = 'Seanis',
		str_eat = "You chomp on the Seanis, slicing them in twain over and over. By the time you're finished with them, you've developed three cavities.",
		str_desc = "A packet of hard candies. They're small tablets, colored in fuchsia, purple, and seafoam green.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_bustahfingers,
		alias = [
			"bustah",
		],
		recover_hunger = 300,
		price = 10000,
		str_name = 'Bustahfingers',
		str_eat = "You chomp on each half of the Bustahfingers heartily. The thick layer of chocolate is complimented perfectly by the core of peanut butter inside.",
		str_desc = "A high quality candy bar, shaped like two nunchuks bonded together by a thin section of chocolate in the middle.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_marsbar,
		alias = [
			"mars",
		],
		recover_hunger = 300,
		price = 10000,
		str_name = 'Mars Bar',
		str_eat = "You take a bite out of the mars bar. Shockingly, the nicotine on the inside pairs well with the creamy sweetness of the white chocolate shell.",
		str_desc = "A small cylindrical candy bar, unsurprisingly shaped like a cigarette. What is surprising, however, is that it contains tiny traces of nicotine on the inside.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_juvieranchers,
		alias = [
			"ranchers",
		],
		recover_hunger = 30,
		price = 10000,
		str_name = 'Juvie Ranchers',
		str_eat = "You suck on the Juvie Ranchers. The Dire Apple ones are particularly sour.",
		str_desc = "A bag of hard candies, all flavored after the various crops of the city.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_swedishbassedgods,
		alias = [
			"bassedgods",
		],
		recover_hunger = 100,
		price = 10000,
		str_name = 'Swedish Bassed Gods',
		str_eat = "You chew through the Swedish Bassed Gods. Despite their unassuming appearance, they taste amazing. Truly a snack worthy of praise. Or would it be 'appraisal', in this case? Ah, forget it.",
		str_desc = "A packet of gummies shaped like the Bassed God. On the back of the packet, there's an advertisement for the Fishing Guild.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food=item_id_endlesswarheads,
		alias=[
			"warheads",
		],
		recover_hunger=250,
		price=10000,
		str_name='Endless Warheads',
		str_eat="You chew through the Endless Warheads. Combining different colored ones inside your mouth sets off a burst of flavor. Sick!!",
		str_desc="A bag of sour candies coated in sugar. They're all multicolored, and shaped like the familiar obelisk it gets its name from.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_chutzpahcherries,
		alias = [
			"cherries",
		],
		recover_hunger = 250,
		price = 10000,
		str_name = 'Chutzpah Cherries',
		str_eat = "You gobble up the Chutzpah Cherries. Who knew euthanasia could taste this good!",
		str_desc = "A small box of dark red gummies, each one bearing the face of a slimeoid.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_slimesours,
		alias = [
			"sours",
		],
		recover_hunger = 100,
		price = 100000,
		str_name = 'Slime Sours',
		str_eat = "You pop a few Slime Sours into your maw. They bubble in your mouth a bit, almost like they're carbonated or something. Luckily they taste excellent, and seemingly have no connection with the death raining from above.",
		str_desc = "A small plastic bag of gumdrops, each as green as slime itself. Apparently they're made entirely by hand.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_munchies,
		alias = [
			"munchys",
		],
		recover_hunger = 350,
		price = 100000,
		str_name = 'Munchies',
		str_eat = "You gorge yourself on the Munchies. What seemed like such a basic snack item reveals itself to be incredibly addictive. Before you know it, the bag is empty, leaving you to reflect on your gluttony.",
		str_desc = "A bag of crackers, with a thin layer of cream in the middle. They're all shaped like jester hats.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_magickspatchkids,
		alias = [
			"magicks",
		],
		recover_hunger = 100,
		price = 100000,
		str_name = 'Magicks Patch Kids',
		str_eat = "You munch on the Magicks Patch Kids. Sour. Sweet. !dab.",
		str_desc = "People are rather split on these. Some find them too sour, while others claim it to have an 'acquired taste'.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_krakel,
		alias = [
			"krak",
		],
		recover_hunger = 320,
		price = 100000,
		str_name = 'Krakel',
		str_eat = "You take a large bite out of the Krakel bar. The rice lining the interior gives it a nice texture, and offsets the bitterness of the dark chocolate a bit.",
		str_desc = "A thick slab of dark chocolate. An engraving on the back reads 'SLURP SLIME, BUSTERS'. Go figure.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_strauberryshortcakes,
		alias = [
			"shortcakes",
		],
		recover_hunger = 250,
		price = 100000,
		str_name = 'Strauberry Shortcakes',
		str_eat = "You toss the shortcakes into your mouth one at a time, savoring every bite. Even though they're manufactured, somehow you feel like a lot of love went into making them. Maybe it's just because of all the sugar.",
		str_desc = "A packet containing two small pastries. An anchor symbol made of pink frosting is drawn onto both of them.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_n3crunch,
		alias = [
			"crunch",
		],
		recover_hunger = 250,
		price = 100000,
		str_name = 'N3 Crunch',
		str_eat = "You bite through the N3 Crunch bar. It's just your basic chocolate bar, with no outstanding appeal other than the engraving on the front.",
		str_desc = "A chocolate bar popular with fans of Slimecorp. Each bar has an engraving of N3 on it. You try not to think about what people would do with these things behind closed doors.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = "sourpussbread",
		alias = [
			"bowserbread",
			"spb",
			"sourpuss"
		],
		recover_hunger = 100,
		price = 1000,
		str_name = 'Sourpuss Bread',
		str_eat = "You chomp through the loaf of sourpuss bread. Somehow you feel like it would taste better if it was toasted.",
		str_desc = "A loaf of bread. The likeness of some reptile is planted on the bag containing it. Apparently it's from 'Bowser', but who the fuck that is, you've got no clue.",
		vendors = [vendor_pizzahut]
	),
	EwFood(
		id_food = item_id_seaweedjoint,
		alias = [
			"joint",
			"weed",
			"blunt",
			"doobie",
		],
		recover_hunger = 0,
		str_name = 'Seaweed Joint',
		str_eat = "You light up your Seaweed and begin to smoke it. Congratulations! You're now high. You catch fish twice as often, but food is half as effective. This lasts for 10 minutes.",
		str_desc = "A joint made up of dankwheat and seaweed bartered with Captain Albert Alexander. Wait a minute, does that make the good Captain your drug dealer? Hell yeah.",
		acquisition = acquisition_smelting
	),
	EwFood(
		id_food="brawldenbagel",
		alias=[
			"bagel",
			"bdbagel",
			"brawlbagel"
		],
		recover_hunger=111-1, # ;)
		price=1001,
		str_name='Brawlden Bagel',
		str_eat="You attempt to cut the bagel with the shitty plastic butter-knife the waitress gave you, but it snaps in two almost immediately. Looks like you won’t be having any slime cream cheese on your meal today. You crunch as hard as you can into the absolute BRICK of Juvish bread and in the process nearly snap your jaw in two. You begin to chew it only to realize it's fucking sludgeberry. Who puts sludgeberries a bagel? You’re just too furious to finish this distinctly non-keto bagel of burden, so you find the nearest Juvie and chuck it at their skull.",
		str_desc="Despite the rampant crime-rates of their home district, Brawlden Bagels are a staple of NLACakaNM’s brunch cuisine. Of course, they’re all so stale that most people just use them as brass knuckles, but nonetheless they can be downright irresistible with a large enough smattering of slime cream cheese. That shit has to be, like, an inch thick, though.",
		vendors=[vendor_greencakecafe]
	),
	EwFood(
		id_food="greeneye",
		alias=[
			"redeye",
			"espresso",
			"caffeine"
		],
		recover_hunger=150,
		price=1500,
		str_name='Green Eye',
		str_eat="You bring the small cup to your lips, only to be greeted by a very suspicious smell. You think nothing of it and down the drink in one gulp… This was a mistake. That smell was slime vapor because it turns out the coffee was still fucking boiling when the waitress poured it for you. It may have burned all the skin in your mouth off, sure, but it also burned the nerve-endings on your tongue, so it only hurt for a moment. At the very least, you feel energized and in the mood to put pen to paper and write.",
		str_desc="Coffee topped off with a nice rejuvenating shot of slime to stop the ol’ adenosine from pumping. It’s even served in a miniature cup so you can shotgun it without issue!",
		vendors=[vendor_greencakecafe]
	),
	EwFood(
		id_food="pcpastry",
		alias=[
			"pcp",
			"pastry",
			"procrastinatorspastry"
		],
		recover_hunger=90,
		price=900,
		str_name='PCPastry',
		str_eat="You aren’t certain about this pastry’s quality because you were a bit iffy on last week’s. You give it a try and are pleasantly surprised! The ingredients seem to be more in harmony this week, and generally it just has a better texture. All the people you know seem to still be under the assumption that they’re always gonna be spicy and hard to eat, but that hasn’t really been the case for a few months. After finishing it, you come to the conclusion that, while you wouldn’t go so far as to call yourself a PCPastries-head, you’d probably purchase one again as long as they keep up the quality.",
		str_desc="A sweet treat that is somewhat notorious in town. Of course, everybody has their favorite and least favorite ingredients, but is it actually really worth the trek to the cafe to eat the new one every single week?",
		vendors=[vendor_greencakecafe]
	),
	EwFood(
		id_food="fuckuccino",
		alias=[
			"frappuccino",
			"cappuccino",
			"sourpuss"
		],
		recover_hunger=300,
		price=3000,
		str_name='Fuckuccino',
		str_eat="You let it cool off for a few seconds before taking a sip, only to be disgusted by how bitter it is. You figured this would be the case, so you unload one of the sugar packets into the mug. Nope, the bitterness remains. You pour another. It's still not sweet enough. You continue this cycle until you’ve poured all 12 sugar packets into the coffee. Eventually it becomes sweet enough to tolerate. Truly, the young slimeboi’s ambrosia.",
		str_desc="A wonderful cup of joe mixed with a healthy dose of Fuck Energy ™ Cream. It comes with several packets of sugar, in case the 500 milligrams of caffeine isn’t enough for you.",
		vendors=[vendor_greencakecafe]
	),
	EwFood(
		id_food="goolongtea",
		alias=[
			"tea",
			"oolong",
			"goolong"
		],
		recover_hunger=310,
		price=3100,
		str_name='Goolong Tea',
		str_eat="Finally, after months of purely fast food and various carcinogens, a beverage that won’t take a year off of your lifespan. You sip the oriental tea with newfound vigor. You begin to recall back to before the slime, before the poudrins, before the FUCK Energy. You snap back to reality when you realize that you were so out of it that you spilled the rest of it all over your clothes. Shit.",
		str_desc="Restorative, piping-hot tea made with the goolong herb grown in the far eastern lands of *Nuvada*. Even if it is “good” for you, at least it’s served in a styrofoam cup so it can still hurt the environment in some way. The zarf is bright green. If you don’t know what that means then look it up, pussy.",
		vendors=[vendor_greencakecafe]
	),
	EwFood(
		id_food="3tart",
		alias=[
			"tart",
			"3tard",
		],
		recover_hunger=33,
		price=333,
		str_name='3tart',
		str_eat="You bite into the 3tart, and yeah, the initial mouthfeel is pretty crummy, but you decide to stick with it because you already invested some slime in the thing anyways. As you chew it more and more you begin to grow less wary of it. By the time you swallow, you’re actually somewhat fond of the thing, even if it was relatively new. Man, if only 3tards could follow this kind of arc.",
		str_desc="A petite shortbread tart served with three random fruits on the top. The quality of these can vary to say the least. Most of the time, they’re so brittle that they don’t stick around long enough for you to really decide whether it had any merit to it, and other times they have such little flavor that they seem to lurk for minutes on end until you can finally remember to swallow them. But very occasionally, you find a tart that suits your fancy excellently and you’re able to cherish the taste.",
		vendors=[vendor_greencakecafe]
	),
	EwFood(
		id_food = "direapplefrickenergy",
		alias = [
			"juice",
			"appyjuice",
			"frickenergy",
		],
		recover_hunger=10,
		price=1,
		str_name = "Dire Apple FRICK Energy",
		str_eat = "*siiiiiip*, Ahhh, that's the stuff. You drink through the entire juice box in one go.",
		str_desc = "A small rectangular box of apple juice. Suitable for children, and perhaps small slimeoids.",
		vendors=[vendor_greencakecafe, vendor_beachresort, vendor_bar, vendor_pizzahut, vendor_kfc, vendor_tacobell]
	)
]

# A map of id_food to EwFood objects.
food_map = {}

# A list of food names
food_names = []

# list of crops you're able to !reap
vegetable_list = []
