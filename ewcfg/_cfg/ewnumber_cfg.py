
# Set values here for whatever things need values


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

# Limits message length
discord_message_length_limit = 2000

# Update intervals
update_hookstillactive = 60 * 60 * 3
update_twitch = 60
update_pvp = 60
update_market = 900 #15 min


# Slime costs/values
slimes_onrevive = 20
slimes_onrevive_everyone = 20
slimes_toenlist = 0
slimes_perspar_base = 0
slimes_hauntratio = 400
slimes_hauntmax = 20000
slimes_perslot = 100
slimes_perpachinko = 500
slimecoin_exchangerate = 1
slimes_permill = 50000
slimes_invein = 4000
slimes_pertile = 50
slimes_tomanifest = -100000
slimes_cliffdrop = 200000
slimes_item_drop = 10000
slimes_shambler = 1000000


# Explain better ~ Seani
tv_set_slime = 5000000
tv_set_level = 100
