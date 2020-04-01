
# Stats related config

# Leaderboard score categories
leaderboard_slimes = "SLIMIEST"
leaderboard_slimecoin = "SLIMECOIN BARONS"
leaderboard_ghosts = "ANTI-SLIMIEST"
leaderboard_podrins = "PODRIN LORDS"
leaderboard_bounty = "MOST WANTED"
leaderboard_kingpins = "KINGPINS' COFFERS"
leaderboard_districts = "DISTRICTS CONTROLLED"
leaderboard_donated = "LOYALEST CONSUMERS"
#SLIMERNALIA
leaderboard_slimernalia = "MOST FESTIVE"
#INTERMISSION2
leaderboard_degradation = "MOST DEGRADED"
leaderboard_shamblers_killed = "MOST SHAMBLER KILLS"


# leaderboard entry types
entry_type_player = "player"
entry_type_districts = "districts"

# district control channel topic text
control_topic_killers = "Currently controlled by the killers."
control_topic_rowdys = "Currently controlled by the rowdys."
control_topic_neutral = "Currently controlled by no one."

control_topics = {
	faction_killers: control_topic_killers,
	faction_rowdys: control_topic_rowdys,
	"": control_topic_neutral  # no faction
}

# district control actors
actor_decay = "decay"

# degradation strings
channel_topic_degraded = "(Closed indefinitely)"
str_zone_degraded = "{poi} has been degraded too far to keep operating."

# The highest and lowest level your weaponskill may be on revive. All skills over this level reset to these.
weaponskill_max_onrevive = 6
weaponskill_min_onrevive = 0

# User statistics we track
stat_max_slimes = 'max_slimes'
stat_lifetime_slimes = 'lifetime_slimes'
stat_lifetime_slimeloss = 'lifetime_slime_loss'
stat_lifetime_slimesdecayed = 'lifetime_slimes_decayed'
stat_slimesmined = 'slimes_mined'
stat_max_slimesmined = 'max_slimes_mined'
stat_lifetime_slimesmined = 'lifetime_slimes_mined'
stat_slimesfromkills = 'slimes_from_kills'
stat_max_slimesfromkills = 'max_slimes_from_kills'
stat_lifetime_slimesfromkills = 'lifetime_slimes_from_kills'
stat_slimesfarmed = 'slimes_farmed'
stat_max_slimesfarmed = 'max_slimes_farmed'
stat_lifetime_slimesfarmed = 'lifetime_slimes_farmed'
stat_slimesscavenged = 'slimes_scavenged'
stat_max_slimesscavenged = 'max_slimes_scavenged'
stat_lifetime_slimesscavenged = 'lifetime_slimes_scavenged'
stat_lifetime_slimeshaunted = 'lifetime_slimes_haunted'
stat_max_level = 'max_level'
stat_max_ghost_level = 'max_ghost_level'
stat_max_hitsurvived = 'max_hit_survived'
stat_max_hitdealt = 'max_hit_dealt'
stat_max_hauntinflicted = 'max_haunt_inflicted'
stat_kills = 'kills'
stat_max_kills = 'max_kills'
stat_biggest_kill = 'biggest_kill'
stat_lifetime_kills = 'lifetime_kills'
stat_lifetime_ganks = 'lifetime_ganks'
stat_lifetime_takedowns = 'lifetime_takedowns'
stat_max_wepskill = 'max_wep_skill'
stat_max_slimecoin = 'max_slime_coins'
stat_lifetime_slimecoin = 'lifetime_slime_coins'
stat_slimecoin_spent_on_revives = 'slimecoins_spent_on_revives'
stat_biggest_casino_win = 'biggest_casino_win'
stat_biggest_casino_loss = 'biggest_casino_loss'
stat_lifetime_casino_winnings = 'lifetime_casino_winnings'
stat_lifetime_casino_losses = 'lifetime_casino_losses'
stat_total_slimecoin_invested = 'total_slimecoin_invested'
stat_total_slimecoin_withdrawn = 'total_slimecoin_withdrawn'
stat_total_slimecoin_from_recycling = 'total_slimecoin_from_recycling'
stat_total_slimecoin_from_swearing = 'total_slimecoin_from_swearing'
stat_bounty_collected = 'bounty_collected'
stat_max_bounty = 'max_bounty'
stat_ghostbusts = 'ghostbusts'
stat_biggest_bust_level = 'biggest_bust_level'
stat_lifetime_ghostbusts = 'lifetime_ghostbusts'
stat_max_ghostbusts = 'max_ghostbusts'
stat_max_poudrins = 'max_poudrins'
stat_poudrins_looted = 'poudrins_looted'
stat_lifetime_poudrins = 'lifetime_poudrins'
stat_lifetime_damagedealt = 'lifetime_damage_dealt'
stat_lifetime_selfdamage = 'lifetime_self_damage'
stat_lifetime_deaths = 'lifetime_deaths'
#Track revolver trigger pulls survived?
stat_lifetime_spins_survived = 'lifetime_spins_survived'
stat_max_spins_survived = 'max_spins_survived'
stat_capture_points_contributed = 'capture_points_contributed'
stat_pve_kills = 'pve_kills'
stat_max_pve_kills = 'max_pve_kills'
stat_lifetime_pve_kills = 'lifetime_pve_kills'
stat_lifetime_pve_takedowns = 'lifetime_pve_takedowns'
stat_lifetime_pve_ganks = 'lifetime_pve_ganks'
stat_lifetime_pve_deaths = 'lifetime_pve_deaths'
stat_capture_points_contributed = 'capture_points_contributed'
stat_shamblers_killed = 'shamblers_killed'

stat_revolver_kills = 'revolver_kills'
stat_dual_pistols_kills = 'dual_pistols_kills'
stat_shotgun_kills = 'shotgun_kills'
stat_rifle_kills = 'rifle_kills'
stat_smg_kills = 'smg_kills'
stat_minigun_kills = 'miningun_kills'
stat_bat_kills = 'bat_kills'
stat_brassknuckles_kills = 'brassknuckles_kills'
stat_katana_kills = 'katana_kills'
stat_broadsword_kills = 'broadsword_kills'
stat_nunchucks_kills = 'nunchucks_kills'
stat_scythe_kills = 'scythe_kills'
stat_yoyo_kills = 'yoyo_kills'
stat_knives_kills = 'knives_kills'
stat_molotov_kills = 'molotov_kills'
stat_grenade_kills = 'grenade_kills'
stat_garrote_kills = 'garrote_kills'
stat_pickaxe_kills = 'pickaxe_kills'
stat_fishingrod_kills = 'fishingrod_kills'
stat_bass_kills = 'bass_kills'
stat_bow_kills = 'bow_kills'
stat_umbrella_kills = 'umbrella_kills'
stat_dclaw_kills = 'dclaw_kills'

# Categories of events that change your slime total, for statistics tracking
source_mining = 0
source_damage = 1
source_killing = 2
source_self_damage = 3
source_busting = 4
source_haunter = 5
source_haunted = 6
source_spending = 7
source_decay = 8
source_ghostification = 9
source_bleeding = 10
source_scavenging = 11
source_farming = 12
source_fishing = 13
source_squeeze = 14
source_weather = 15
source_crush = 16
source_casino = 17
source_slimeoid_betting = 18

# Categories of events that change your slimecoin total, for statistics tracking
coinsource_spending = 0
coinsource_donation = 1
coinsource_bounty = 2
coinsource_revival = 3
coinsource_casino = 4
coinsource_transfer = 5
coinsource_invest = 6
coinsource_withdraw = 7
coinsource_recycle = 8
coinsource_swearjar = 9

# Causes of death, for statistics tracking
cause_killing = 0
cause_mining = 1
cause_grandfoe = 2
cause_donation = 3
cause_busted = 4
cause_suicide = 5
cause_leftserver = 6
cause_drowning = 7
cause_falling = 8
cause_bleeding = 9
cause_burning = 10
cause_killing_enemy = 11
cause_weather = 12
cause_cliff = 13
cause_backfire = 14
cause_praying = 15

# List of user statistics that reset to 0 on death
stats_clear_on_death = [
	stat_slimesmined,
	stat_slimesfromkills,
	stat_kills,
	stat_pve_kills,
	stat_ghostbusts,
	stat_slimesfarmed,
	stat_slimesscavenged
]
