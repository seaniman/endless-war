
mutation_id_spontaneouscombustion = "spontaneouscombustion"
mutation_id_thickerthanblood = "thickerthanblood"
mutation_id_graveyardswift = "graveyardswift" #TODO
mutation_id_fungalfeaster = "fungalfeaster"
mutation_id_sharptoother = "sharptoother"
mutation_id_openarms = "openarms" #TODO
mutation_id_2ndamendment = "2ndamendment"
mutation_id_panicattacks = "panicattacks" #TODO
mutation_id_twobirdswithonekidneystone = "2birds1stone" #TODO
mutation_id_shellshock = "shellshock" #TODO
mutation_id_bleedingheart = "bleedingheart"
mutation_id_paranoia = "paranoia" #TODO
mutation_id_cloakandstagger = "cloakandstagger" #TODO
mutation_id_nosferatu = "nosferatu"
mutation_id_organicfursuit = "organicfursuit"
mutation_id_lightasafeather = "lightasafeather"
mutation_id_whitenationalist = "whitenationalist"
mutation_id_spoiledappetite = "spoiledappetite"
mutation_id_bigbones = "bigbones"
mutation_id_fatchance = "fatchance"
mutation_id_fastmetabolism = "fastmetabolism"
mutation_id_bingeeater = "bingeeater"
mutation_id_lonewolf = "lonewolf"
mutation_id_quantumlegs = "quantumlegs"
mutation_id_chameleonskin = "chameleonskin"
mutation_id_patriot = "patriot"
mutation_id_socialanimal = "socialanimal"
mutation_id_corpseparty = "corpseparty" #TODO
mutation_id_threesashroud = "threesashroud"
mutation_id_aposematicstench = "aposematicstench"
mutation_id_paintrain = "paintrain" #TODO
mutation_id_lucky = "lucky"
mutation_id_dressedtokill = "dressedtokill"
mutation_id_keensmell = "keensmell"
mutation_id_enlargedbladder = "enlargedbladder"
mutation_id_dumpsterdiver = "dumpsterdiver"
mutation_id_trashmouth = "trashmouth"
mutation_id_webbedfeet = "webbedfeet"

mutation_milestones = [5,10,15,20,25,30,35,40,45,50]

mutations = [
	EwMutationFlavor(
		id_mutation = mutation_id_spontaneouscombustion,
		str_describe_self = "On the surface you look calm and ready, probably unrelated to your onset of **Spontaneous Combustion**.",
		str_describe_other = "On the surface they look calm and ready, probably unrelated to their onset of **Spontaneous Combustion**.",
		str_acquire = "Deep inside your chest you feel a slight burning sensation. You suddenly convulse for a few moments, before… returning basically to normal. Huh, that’s weird. Oh well, I guess nothing happened. You have developed the mutation **Spontaneous Combustion**.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_thickerthanblood,
		str_describe_self = "Unnatural amounts of blood rush through your body, causing grotesquely large veins to bulge out of your head and arms frequently, due to **Thicker Than Blood**.",
		str_describe_other = "Unnatural amounts of blood rush through their body, causing grotesquely large veins to bulge out of their head and arms frequently, due to **Thicker Than Blood**.",
		str_acquire = "Your face swells with unnatural amounts of blood, developing hideously grotesque, bulging veins in the process. You begin to foam at the mouth, gnashing your teeth and longing for the thrill of the hunt. You have developed the mutation **Thicker Than Blood**. On a fatal blow, immediately receive the opponent’s remaining slime. Its effects are diminished on hunted enemies, however.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_fungalfeaster,
		str_describe_self = "Tiny mushrooms and other fungi sprout from the top of your head and shoulders due to **Fungal Feaster**.",
		str_describe_other = "Tiny mushrooms and other fungi sprout from the top of their head and shoulders due to **Fungal Feaster**.",
		str_acquire = "Your saliva thickens, pouring out of your mouth with no regulation. A plethora of funguses begin to grow from your skin, causing you to itch uncontrollably. You feel an intense hunger for the flesh of another juvenile. You have developed the mutation **Fungal Feaster**. On a fatal blow, restore all hunger.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_sharptoother,
		str_describe_self = "Your inhuman hand-eye-teeth coordination is the stuff of legends due to **Sharptoother**.",
		str_describe_other = "Their inhuman hand-eye-teeth coordination is the stuff of legends due to **Sharptoother**.",
		str_acquire = "Your pupils dilate, a cacophony of previously imperceivable noises floods into your head. Your canines pop out of your skull, making room for monstrously oversized saber-tooth replacements. Your fingers twitch frequently, begging to pull a trigger, any trigger. You have developed the mutation **Sharptoother**. Halved miss chance.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_2ndamendment,
		str_describe_self = "A spare pair of arms extend from your monstrously large shoulders due to **2nd Amendment**.",
		str_describe_other = "A spare pair of arms extend from their monstrously large shoulders due to **2nd Amendment**.",
		str_acquire = "You feel an intense, sharp pain in the back of your shoulders. Skin tears and muscles rip as you grow a brand new set of arms, ready, willing, prepared to fight. You have developed the mutation **2nd Amendment**. Extra equippable gun slot.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_bleedingheart,
		str_describe_self = "Your heartbeat’s rhythm is sporadic and will randomly change intensity due to **Bleeding Heart**.",
		str_describe_other = "Their heartbeat’s rhythm is sporadic and will randomly change intensity due to **Bleeding Heart**.",
		str_acquire = "To say you experience “heart palpitations” is a gross understatement. Your heart feels like it explodes and reforms over and over for the express amusement of some cruel god’s sick sense of humor. You begin to cough up blood and basically continue to do so for the rest of your life. You have developed the mutation **Bleeding Heart**. Upon being hit, none of your slime is splattered onto the street. It is all stored as bleed damage.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_nosferatu,
		str_describe_self = "Your freakishly huge, hooked schnoz and pointed ears give you a ghoulish appearance due to **Noseferatu**.",
		str_describe_other = "Their freakishly huge, hooked schnoz and pointed ears give them a ghoulish appearance due to **Noseferatu**.",
		str_acquire = "The bridge of your nose nearly triples in size. You recoil as the heat of nearby lights sear your skin, forcing you to seek cover under the shadows of dark, secluded alleyways. Your freakish appearance make you a social outcast, filling you with a deep resentment which evolves into unbridled rage. You will have your revenge. You have developed the mutation **Noseferatu**. At night, upon successful hit, all of the target’s slime is splattered onto the street. None of it is stored as bleed damage.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_organicfursuit,
		str_describe_self = "Your shedding is a constant source of embarrassment due to **Organic Fursuit**.",
		str_describe_other = "Their shedding is a constant source of embarrassment due to **Organic Fursuit**.",
		str_acquire = "An acute tingling sensation shoots through your body, causing you to start scratching uncontrollably. You fly past puberty and begin growing frankly alarming amounts of hair all over your body. Your fingernails harden and twist into claws. You gain a distinct appreciation for anthropomorphic characters in media, even going to the trouble of creating an account on an erotic furry roleplay forum. Oh, the horror!! You have developed the mutation **Organic Fursuit**. Double damage dealt, 1/10th damage taken and movement speed every 31st night.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_lightasafeather,
		str_describe_self = "Your anorexic, frail physique causes even light breezes to blow you off course due to **Light As A Feather**.",
		str_describe_other = "Their anorexic, frail physique causes even light breezes to blow them off course due to **Light As A Feather**.",
		str_acquire = "Your body fat begins to dissolve right before your eyes, turning into a foul-smelling liquid that drenches the floor beneath you. You quickly pass conventionally attractive weights and turn into a hideous near-skeleton. The only thing resting between your bones and your skin is a thin layer of muscles that resemble lunch meat slices. You have developed the mutation **Light As A Feather**. Double movement speed while weather is windy.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_whitenationalist,
		str_describe_self = "Your bleached white, peeling skin is surely the envy of lesser races due to **White Nationalist**.",
		str_describe_other = "Their bleached white, peeling skin is surely the envy of lesser races due to **White Nationalist**.",
		str_acquire = "Every pore on your skin suddenly feels like it’s being punctured by a rusty needle. Your skin’s pigment rapidly desaturates to the point of pure #ffffff whiteness. You suddenly love country music, too. Wow, that was a really stupid joke. You have developed the mutation **White Nationalist**. Scavenge bonus and cannot be scouted while weather is snowy.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_spoiledappetite,
		str_describe_self = "Your frequent, unholy belches could incapacitate a Megaslime due to **Spoiled Appetite**.",
		str_describe_other = "Their frequent, unholy belches could incapacitate a Megaslime due to **Spoiled Appetite**.",
		str_acquire = "You become inexplicably tired, you develop bags under your eyes and can barely keep them open without fidgeting. Stenches begin to secrete from your body, which only worsens as your stomach lets out a deep, guttural growl that sounds like a dying animal being raped by an already dead animal. Which is to say, not pleasant. You are overcome with a singular thought. “What the hell, I’ll just eat some trash.” You have developed the mutation **Spoiled Appetite**. You can now eat spoiled food.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_bigbones,
		str_describe_self = "You can often be seen consuming enough calories to power a small country due to **Big Bones**.",
		str_describe_other = "They can often be seen consuming enough calories to power a small country due to **Big Bones**.",
		str_acquire = "Your can actively feel your brain being squeezed and your heart being nearly crushed by your rib cage as every bone in your body doubles in size. Your body fat doubles in density, requiring great strength and energy for even simple movements. You have developed the mutation **Big Bones**. Double food carrying capacity.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_fatchance,
		str_describe_self = "Your impressive girth provides ample amounts of armor against attacks due to **Fat Chance**.",
		str_describe_other = "Their impressive girth provides ample amounts of armor against attacks due to **Fat Chance**.",
		str_acquire = "Your body begins to swell, providing you with easily hundreds of extra pounds nigh instantaneously. Walking becomes difficult, breathing even more so. Your fat solidifies into a brick-like consistency, turning you into a living fortress. You only have slightly increased mobility than a regular fortress, however. You have developed the mutation **Fat Chance**. Take 25% less damage when above 50% hunger.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_fastmetabolism,
		str_describe_self = "Fierce boiling and sizzling can be heard from deep inside your stomach due to **Fast Metabolism**.",
		str_describe_other = "Fierce boiling and sizzling can be heard from deep inside their stomach due to **Fast Metabolism**.",
		str_acquire = "An intense heat is felt in the pit of your stomach, which wails in pain as it’s dissolved from the inside out. Your gastric acid roars to an unthinkably destructive fever pitch, ready to completely annihilate whatever poor calories may enter your body before instantly turning them into pure leg muscle. You have developed the mutation **Fast Metabolism**. Doubled movement speed at below 50% hunger.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_bingeeater,
		str_describe_self = "You’re always one criticism away from devouring several large pizzas due to **Binge Eater**.",
		str_describe_other = "They’re always one criticism away from devouring several large pizzas due to **Binge Eater**.",
		str_acquire = "Your mouth begins to mimic chewing over and over again, opening and closing all on it’s own. You’re suddenly able to smell the food being carried by passersby for sometimes hours after they’ve left your sight. Your mouth dries and you sweat profusely even just being in the same room as food. Even now, just thinking about food, you begin to tremble. You can barely contain yourself. You don’t need it. You don’t need it. You don’t need it. You don’t need it... You need it. You have developed the mutation **Binge Eater**. Upon eating food, the restored hunger is multiplied by the number of dishes you’ve consumed in the past 5 seconds.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_lonewolf,
		str_describe_self = "You stand out from the crowd, mostly because you stay far away from them due to **Lone Wolf**.",
		str_describe_other = "They stand out from the crowd, mostly because they stay far away from them due to **Lone Wolf**.",
		str_acquire = "Your eyes squint and a growl escapes your mouth. You begin fostering an unfounded resentment against your fellow juveniles, letting it bubble into a burning hatred in your chest. You snarl and grimace as people pass beside you on the street. All you want to do is be alone, no one understands you anyway. You have developed the mutation **Lone Wolf**. 20% capping discount and 50% damage buff when in a district alone.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_quantumlegs,
		str_describe_self = "You’ve got nothing of note below the belt due to **Quantum Legs**.",
		str_describe_other = "They’ve got nothing of note below the belt due to **Quantum Legs**.",
		str_acquire = "Before you can even register it’s happening, your legs simply evaporate into a light mist that dissolves into the atmosphere. You ungracefully fall to the ground in pure shock, horror, and unrivaled agony. You are now literally half the person you used to be. What the hell are you supposed to do now? You scramble to try and find someone that can help you, moving to a nearby phone booth. Wait… how did you just do that? You have developed the mutation **Quantum Legs**. You can now use the !tp command, allowing you to teleport to a district up to two locations away from you instantly, with a cooldown of 3 hours.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_chameleonskin,
		str_describe_self = "Your skin quickly adjusts and camouflages you in your current surroundings due to **Chameleon Skin**.",
		str_describe_other = "Their skin quickly adjusts and camouflages them in their current surroundings due to **Chameleon Skin**.",
		str_acquire = "You feel a scraping sensation all over your body, like you’re being sunburned and skinned alive at the same exact time. You begin to change hue rapidly, flipping through a thousand different colors, patterns, and textures. Every individual minor change in value across your entire body feels like you’re being dismembered. This transpires for several agonizing seconds before your body settles on a perfect recreation of your current surroundings. For all intents and purposes, you are transparent. You have developed the mutation **Chameleon Skin**. While offline, you can move and scout other districts and cannot be scouted.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_patriot,
		str_describe_self = "You beam with intense pride over your faction’s sophisticated culture and history due to **Patriot**.",
		str_describe_other = "They beam with intense pride over their faction’s sophisticated culture and history due to **Patriot**.",
		str_acquire = "Your brain’s wrinkles begin to smooth themselves out, and you are suddenly susceptible to being swayed by propaganda. Suddenly, your faction’s achievements flash before your eyes. All of the glorious victories it has won, all of its sophisticated culture and history compels you to action. You have developed the mutation **Patriot**. 20% capture discount.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_socialanimal,
		str_describe_self = "Your charming charisma and dashing good looks make you the life of the party due to **Social Animal**.",
		str_describe_other = "Their charming charisma and dashing good looks make them the life of the party due to **Social Animal**.",
		str_acquire = "You begin to jitter and shake with unusual vim and vigor. Your heart triples in size and you can’t help but let a toothy grin span from ear to ear as a bizarre energy envelopes you. As long as you’re with your friends, you feel like you can take on the world!! You have developed the mutation **Social Animal**. Your damage increases by 10% for every ally in your district.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_threesashroud,
		str_describe_self = "You tend to blend into the crowd due to **Three’s A Shroud**.",
		str_describe_other = "They tend to blend into the crowd due to **Three’s A Shroud**.",
		str_acquire = "A distinct sense of loneliness pervades your entire body. You’re reduced to the verge of tears without really knowing why. You suddenly feel very conscious of how utterly useless you are. You want to fade away so badly, you’d give anything just to be invisible. Everyone would like it better that way. You have developed the mutation **Three’s A Shroud**. Cannot be scouted if there are more than 3 allies in your district.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_aposematicstench,
		str_describe_self = "A putrid stench permeates around you all hours of the day due to **Aposematic Stench**.",
		str_describe_other = "A putrid stench permeates around them all hours of the day due to **Aposematic Stench**.",
		str_acquire = "Your eyes water as you begin secreting pheromones into the air from every indecent nook and cranny on your body. You smell so unbelievably terrible that even you are not immune from frequent coughs and wheezes when you catch a particularly bad whiff. You have developed the mutation **Aposematic Stench**. For every 5 levels you gain, you appear as 1 more person when being scouted.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_lucky,
		str_describe_self = "You are extremely fortunate due to **Lucky**.",
		str_describe_other = "They are extremely fortunate due to **Lucky**.",
		str_acquire = "Just as you level up, you are struck by lightning. You struggle to stand at first, but after the initial shock wears off you quickly dust the cartoonish soot from your clothes and begin walking again. Then, you’re struck again. You stand up again. This happens a few more times before you’re forced by the astronomically low odds of you being alive to conclude you are a statistical anomaly and thus normal concepts of fortune do not apply to you. You have developed the mutation **Lucky**. Drastically increased chance to unearth slime poudrins and odds of winning slime casino games.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_dressedtokill,
		str_describe_self = "You’re fabulously accompanied by a wide range of luxurious cosmetics due to **Dressed to Kill**.",
		str_describe_other = "They’re fabulously accompanied by a wide range of luxurious cosmetics due to **Dressed to Kill**.",
		str_acquire = "You are rocked by a complete fundamental change in your brain’s chemistry. Practically every cell in your body is reworked to apply this, the most ambitious mutation yet. You gain an appreciation for French haute couture. You have developed the mutation **Dressed to Kill**. Damage bonus if all available cosmetic slots are filled.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_keensmell,
		str_describe_self = "You have an uncanny ability to track and identify scents due to **Keen Smell**.",
		str_describe_other = "They have an uncanny ability to track and identify scents due to **Keen Smell**.",
		str_acquire = "You can feel your facial muscles being ripped as your skull elongates your mouth and nose, molding them into an uncanny snout. Your nostrils painfully stretch and elongate to allow for a broad range of olfactory sensations you could only have dreamed of experiencing before. Your nose twitches and you begin to growl as you pick up the scent of a nearby enemy gangster. You have developed the mutation **Keen Smell**. You can now use the !sniff command, allowing you to meticulously list every single player in the targeted district.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_dumpsterdiver,
		str_describe_self = "You are exceptionally good at picking up trash due to **Dumpster Diver**.",
		str_describe_other = "They are exceptionally good at picking up trash due to **Dumpster Diver**.",
		str_acquire = "A cold rush overtakes you, fogging your mind and causing a temporary lapse in vision. When your mind clears again and you snap back to reality, you notice so many tiny details you hadn’t before. All the loose change scattered on the floor, all the pebbles on the sidewalk, every unimportant object you would have normally glanced over now assaults your senses. You have an uncontrollable desire to pick them all up. You have developed the mutation **Dumpster Diver**. 10 times chance to get items while scavenging.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_trashmouth,
		str_describe_self = "You have the mouth of a sailor and the vocabulary of a fourteen year old due to **Trash Mouth**.",
		str_describe_other = "They have the mouth of a sailor and the vocabulary of a fourteen year old due to **Trash Mouth**.",
		str_acquire = "You drop down onto your knees, your inhibitions wash away as a new lust overtakes you. You begin shoveling literally everything you can pry off the floor into your mouth with such supernatural vigor that a nearby priest spontaneously dies. You have developed the mutation **Trash Mouth**. Reach maximum power scavenges faster.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_webbedfeet,
		str_describe_self = "Your toes are connected by a thin layer of skin due to **Webbed Feet**.",
		str_describe_other = "Their toes are connected by a thin layer of skin due to **Webbed Feet**.",
		str_acquire = "Your feet grow a thin layer of skin, allowing you to swim through piles of slime, soaking up their precious nutrients easily. You have developed the mutation **Webbed Feet**. Your scavenging power increases the more slime there is in a district.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_enlargedbladder,
		str_describe_self = "You have an enlarged bladder due to **Enlarged Bladder**.",
		str_describe_other = "They have an enlarged bladder due to **Enlarged Bladder**.",
		str_acquire = "You feel some mild sensation near your kidney, but you don’t really notice it. You have developed the mutation **Enlarged Bladder**. You may now, finally, piss.",
		),
	]

mutations_map = {}

mutation_ids = set()
