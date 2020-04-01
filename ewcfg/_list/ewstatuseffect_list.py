
status_effect_list = [
	EwStatusEffectDef(
		id_status = status_burning_id,
		time_expire = time_expire_burn,
		str_acquire = '{name_player}\'s body is engulfed in flames.',
		str_describe = 'They are burning.',
		str_describe_self = 'You are burning.'
	),
	EwStatusEffectDef(
		id_status = status_ghostbust_id,
		time_expire = 86400,
		str_describe_self = 'The coleslaw in your stomach allows you to bust ghosts.'
	),
	EwStatusEffectDef(
		id_status = status_strangled_id,
		time_expire = 5,
		str_describe = 'They are being strangled.'
	),
	EwStatusEffectDef(
		id_status = status_stunned_id,
		str_describe = 'They are stunned.'
	),
	EwStatusEffectDef(
		id_status = status_repelled_id,
		time_expire = time_expire_repel_base,
		str_acquire = 'You spray yourself with the FUCK ENERGY Body Spray.',
		str_describe = 'They smell like shit, much to the displeasure of slime beasts.',
		str_describe_self = 'You smell like shit, much to the displeasure of slime beasts.'
	),
	EwStatusEffectDef(
		id_status = status_repelaftereffects_id,
		time_expire = 2,
		str_acquire = 'You try and shake off the body spray, but its stench still lingers, if only for a brief moment.',
		str_describe = 'Their surroundings give off a slightly foul odor.',
		str_describe_self = 'Your surroundings give off a slightly foul odor.'
	),
	EwStatusEffectDef(
		id_status = status_high_id,
		time_expire = time_expire_high,
		str_describe = "They are as high as a kite.",
		str_describe_self = "You are as high as a kite."
	),
	EwStatusEffectDef(
		id_status = status_evasive_id,
		time_expire = 10,
		str_describe = "They have assumed an evasive stance.",
		str_describe_self = "You have assumed an evasive stance.",
		miss_mod = 0.25
	),
	EwStatusEffectDef(
		id_status = status_taunted_id,
		time_expire = 10,
		str_describe = "They are fuming with rage.",
		str_describe_self = "You are fuming with rage.",
		miss_mod_self = 0.25
	),
	EwStatusEffectDef(
		id_status = status_aiming_id,
		time_expire = 10,
		str_describe = "They are taking careful aim.",
		str_describe_self = "You are taking careful aim.",
		miss_mod_self = -0.1,
		crit_mod_self = 0.2
	),
	EwStatusEffectDef(
		id_status = status_sapfatigue_id,
		time_expire = 60,
		str_describe = "They are suffering from sap fatigue.",
		str_describe_self = "You are suffering from sap fatigue.",
	),
	EwStatusEffectDef(
		id_status = status_rerollfatigue_id,
	),
	EwStatusEffectDef(
		id_status = status_injury_head_id,
		str_describe = "Their head looks {severity}",
		str_describe_self = "Your head looks {severity}",
		miss_mod_self = 0.05,
		crit_mod_self = -0.1,
		miss_mod = -0.01,
		crit_mod = 0.01,
	),
	EwStatusEffectDef(
		id_status = status_injury_torso_id,
		str_describe = "Their torso looks {severity}",
		str_describe_self = "Your torso looks {severity}",
	),
	EwStatusEffectDef(
		id_status = status_injury_arms_id,
		str_describe = "Their arms look {severity}",
		str_describe_self = "Your arms look {severity}",
		miss_mod_self = 0.05,
		crit_mod_self = -0.1,
	),
	EwStatusEffectDef(
		id_status = status_injury_legs_id,
		str_describe = "Their legs look {severity}",
		str_describe_self = "Your legs look {severity}",
		miss_mod = -0.06,
		crit_mod = 0.03,
	),

]

status_effects_def_map = {}