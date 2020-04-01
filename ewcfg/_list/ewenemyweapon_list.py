
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