
quadrant_flushed = "flushed"
quadrant_pale = "pale"
quadrant_caliginous = "caliginous"
quadrant_ashen = "ashen"

quadrant_ids = [
	quadrant_flushed,
	quadrant_pale,
	quadrant_caliginous,
	quadrant_ashen
	]

quadrants_map = {}

quadrants = [
	EwQuadrantFlavor(
		id_quadrant = quadrant_flushed,

		aliases = ["heart", "hearts", "matesprit", "matespritship"],

		resp_add_onesided = "You have developed flushed feelings for {}.",

		resp_add_relationship = "You have entered into a matespritship with {}.",

		resp_view_onesided = "{} has a one-sided red crush on {}.",

		resp_view_onesided_self = "You have a one-sided red crush on {}.",

		resp_view_relationship = "{} is in a matespritship with {}. " + emote_hearts,

		resp_view_relationship_self = "You are in a matespritship with {}. " + emote_hearts
		),

	EwQuadrantFlavor(
		id_quadrant = quadrant_pale,

		aliases = ["diamond", "diamonds", "moirail", "moiraillegiance"],

		resp_add_onesided = "You have developed pale feelings for {}.",

		resp_add_relationship = "You have entered into a moiraillegiance with {}.",

		resp_view_onesided = "{} has a one-sided pale crush on {}.",

		resp_view_onesided_self = "You have a one-sided pale crush on {}.",

		resp_view_relationship = "{} is in a moiraillegiance with {}. " + emote_diamonds,

		resp_view_relationship_self = "You are in a moiraillegiance with {}. " + emote_diamonds
		),

	EwQuadrantFlavor(
		id_quadrant = quadrant_caliginous,

		aliases = ["spade", "spades", "kismesis", "kismesissitude"],

		resp_add_onesided = "You have developed caliginous feelings for {}.",

		resp_add_relationship = "You have entered into a kismesissitude with {}.",

		resp_view_onesided = "{} has a one-sided black crush on {}.",

		resp_view_onesided_self = "You have a one-sided black crush on {}.",

		resp_view_relationship = "{} is in a kismesissitude with {}. " + emote_spades,

		resp_view_relationship_self = "You are in a kismesissitude with {}. " + emote_spades
		),

	EwQuadrantFlavor(
		id_quadrant = quadrant_ashen,

		aliases = ["club", "clubs", "auspistice", "auspisticism"],

		resp_add_onesided = "You have developed ashen feelings for {}.",

		resp_add_relationship = "You have entered into an auspisticism with {}.",

		resp_view_onesided = "{} has a one-sided ashen crush on {}.",

		resp_view_onesided_self = "You have a one-sided ashen crush on {}.",

		resp_view_relationship = "{} is in an auspisticism with {}. " + emote_clubs,

		resp_view_relationship_self = "You are in an auspisticism with {}. " + emote_clubs
		)

]