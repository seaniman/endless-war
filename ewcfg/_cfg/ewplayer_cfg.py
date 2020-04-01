
# Player related config

# combatant ids to differentiate players and NPCs in combat
combatant_type_player = "player"

# Life states. How the player is living (or deading) in the database
life_state_corpse = 0
life_state_juvenile = 1
life_state_enlisted = 2
life_state_shambler = 3
life_state_executive = 6
life_state_lucky = 7
life_state_grandfoe = 8
life_state_kingpin = 10
life_state_observer = 20
slimeoid_state_dead = 4

# Role names. All lower case with no spaces.
role_juvenile = "juveniles"
role_juvenile_pvp = "juvenilewanted"
role_juvenile_active = "juvenileotp"
role_rowdyfucker = "rowdyfucker"
role_rowdyfuckers = "rowdys"
role_rowdyfuckers_pvp = "rowdywanted"
role_rowdyfuckers_active = "rowdyotp"
role_copkiller = "copkiller"
role_copkillers = "killers"
role_copkillers_pvp = "killerwanted"
role_copkillers_active = "killerotp"
role_corpse = "corpse"
role_corpse_pvp = "corpsewanted"
role_corpse_active = "corpseotp"
role_shambler = "shambler"
role_kingpin = "kingpin"
role_grandfoe = "grandfoe"
role_slimecorp = "slimecorp"
role_deathfurnace = "deathfurnace"
role_donor = "terezigang"
role_tutorial = "newintown"
role_slimernalia = "kingpinofslimernalia"
role_gellphone = "gellphone"

faction_roles = [
	role_juvenile,
	role_juvenile_pvp,
	role_juvenile_active,
	role_rowdyfucker,
	role_rowdyfuckers,
	role_rowdyfuckers_pvp,
	role_rowdyfuckers_active,
	role_copkiller,
	role_copkillers,
	role_copkillers_pvp,
	role_copkillers_active,
	role_corpse,
	role_corpse_pvp,
	role_corpse_active,
	role_kingpin,
	role_grandfoe,
	role_slimecorp,
	role_tutorial,
	role_shambler,
	]

role_to_pvp_role = {
	role_juvenile : role_juvenile_pvp,
	role_rowdyfuckers : role_rowdyfuckers_pvp,
	role_copkillers : role_copkillers_pvp,
	role_corpse : role_corpse_pvp
	}

role_to_active_role = {
	role_juvenile : role_juvenile_active,
	role_rowdyfuckers : role_rowdyfuckers_active,
	role_copkillers : role_copkillers_active,
	role_corpse : role_corpse_active
	}

misc_roles = {
	role_slimernalia,
	role_gellphone
}

# used for checking if a user has the donor role
role_donor_proper = "Terezi Gang"

# used for checking if a user has the gellphone role
role_gellphone_proper = "Gellphone"


