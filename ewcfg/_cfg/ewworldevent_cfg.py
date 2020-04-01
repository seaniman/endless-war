event_type_slimeglob = "slimeglob"
event_type_slimefrenzy = "slimefrenzy"
event_type_poudrinfrenzy = "poudrinfrenzy"
event_type_minecollapse = "minecollapse"
event_type_minesweeper = "minesweeper"
event_type_pokemine = "pokemine"
event_type_bubblebreaker = "bubblebreaker"

world_events = [
	EwEventDef(
		event_type = event_type_slimeglob,
		str_event_start = "You mined an extra big glob of slime! {}".format(emote_slime1),
	),
	EwEventDef(
		event_type = event_type_slimefrenzy,
		str_event_start = "You hit a dense vein of slime! Double slimegain for the next 30 seconds.",
		str_event_end = "The double slime vein dried up.",
	),
	EwEventDef(
		event_type = event_type_poudrinfrenzy,
		str_event_start = "You hit a dense vein of poudrins! Guaranteed poudrin on every {} for the next 5 seconds.".format(cmd_mine),
		str_event_end = "The poudrin vein dried up.",
	),
	EwEventDef(
		event_type = event_type_minecollapse,
		str_event_start = "The mineshaft starts collapsing around you. Get out of there quickly! ({cmd} {captcha})",
	),
	EwEventDef(
		event_type = event_type_minesweeper,
		str_event_start = "You notice the wall bulging slightly and you can dig into it. ({} coordinates, {} coordinates)".format(cmd_mine, cmd_flag),
		str_event_end = "The wall collapses.",
	),
	EwEventDef(
		event_type = event_type_pokemine,
		str_event_start = "You notice the wall bulging slightly and you can dig into it. ({} coordinates, {} coordinates)".format(cmd_mine, cmd_flag),
		str_event_end = "The wall collapses.",
	),
	EwEventDef(
		event_type = event_type_bubblebreaker,
		str_event_start = "You notice the wall bulging slightly and you can dig into it.({} column number)".format(cmd_mine),
		str_event_end = "The wall collapses.",
	),

]

event_type_to_def = {}

for event in world_events:
	event_type_to_def[event.event_type] = event

grid_type_by_mining_event = {
	event_type_minesweeper: mine_grid_type_minesweeper,
	event_type_pokemine: mine_grid_type_pokemine,
	event_type_bubblebreaker: mine_grid_type_bubblebreaker,
}