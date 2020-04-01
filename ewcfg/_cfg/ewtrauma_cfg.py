injury_weights = {
	status_injury_head_id : 1,
	status_injury_torso_id : 5,
	status_injury_arms_id : 2,
	status_injury_legs_id : 2
}


# Places you might get !shot
hitzones = [
	EwHitzone(
		name = "head",
		aliases = [
			"neck",
			"jaw",
			"face",
			"nose",
		],
		id_injury = status_injury_head_id,
	),
	EwHitzone(
		name = "torso",
		aliases = [
			"upper back",
			"obliques",
			"solar plexus",
			"trapezius",
			"chest",
			"gut",
			"abdomen",
			"lower back",
		],
		id_injury = status_injury_torso_id,
	),
	EwHitzone(
		name = "leg",
		aliases = [
			"foot",
			"kneecap",
			"Achilles' tendon",
			"ankle",
			"thigh",
			"calf",
		],
		id_injury = status_injury_legs_id,
	),
	EwHitzone(
		name = "arm",
		aliases = [
			"hand",
			"wrist",
			"shoulder",
			"elbow",
		],
		id_injury = status_injury_arms_id,
	),
]

hitzone_list = []
hitzone_map = {}

trauma_id_suicide = "suicide"
trauma_id_betrayal = "betrayal"
trauma_id_environment = "environment"

trauma_class_slimegain = "slimegain"
trauma_class_damage = "damage"

trauma_class_sapregeneration = "sapgen"
trauma_class_accuracy = "accuracy"
trauma_class_bleeding = "bleeding"
trauma_class_movespeed = "movespeed"
trauma_class_hunger = "hunger"

