transport_lines = [
	EwTransportLine( # ferry line from wreckington to vagrant's corner
		id_line = transport_line_ferry_wt_to_vc,
		alias = [
			"vagrantscornerferry",
			"vagrantsferry",
			"vcferry",
			"ferrytovagrantscorner",
			"ferrytovagrants",
			"ferrytovc"
			],
		first_stop = poi_id_wt_port,
		last_stop = poi_id_vc_port,
		next_line = transport_line_ferry_vc_to_wt,
		str_name = "The ferry line towards Vagrant's Corner",
		schedule = {
			poi_id_wt_port : [60, poi_id_slimesea],
			poi_id_slimesea : [120, poi_id_vc_port]
			}

		),
	EwTransportLine( # ferry line from vagrant's corner to wreckington
		id_line = transport_line_ferry_vc_to_wt,
		alias = [
			"wreckingtonferry",
			"wreckferry",
			"wtferry",
			"ferrytowreckington",
			"ferrytowreck",
			"ferrytowt"
			],
		first_stop = poi_id_vc_port,
		last_stop = poi_id_wt_port,
		next_line = transport_line_ferry_wt_to_vc,
		str_name = "The ferry line towards Wreckington",
		schedule = {
			poi_id_vc_port : [60, poi_id_slimesea],
			poi_id_slimesea : [120, poi_id_wt_port]
			}

		),
	EwTransportLine( # yellow subway line from south sleezeborough to arsonbrook
		id_line = transport_line_subway_yellow_northbound,
		alias = [
			"northyellowline",
			"northyellow",
			"yellownorth",
			"yellowtoarsonbrook",
			"yellowtoarson",
			"yellowtoab"
			],
		first_stop = poi_id_ssb_subway_station,
		last_stop = poi_id_ab_subway_station,
		next_line = transport_line_subway_yellow_southbound,
		str_name = "The yellow subway line towards Arsonbrook",
		schedule = {
			poi_id_ssb_subway_station : [20, poi_id_kb_subway_station],
			poi_id_kb_subway_station : [20, poi_id_dt_subway_station],
			poi_id_dt_subway_station : [20, poi_id_sb_subway_station],
			poi_id_sb_subway_station : [20, poi_id_ab_subway_station]
			}

		),
	EwTransportLine( # yellow subway line from arsonbrook to south sleezeborough
		id_line = transport_line_subway_yellow_southbound,
		alias = [
			"southyellowline",
			"southyellow",
			"yellowsouth",
			"yellowtosouthsleezeborough",
			"yellowtosouthsleeze",
			"yellowtossb"
			],
		first_stop = poi_id_ab_subway_station,
		last_stop = poi_id_ssb_subway_station,
		next_line = transport_line_subway_yellow_northbound,
		str_name = "The yellow subway line towards South Sleezeborough",
		schedule = {
			poi_id_ab_subway_station : [20, poi_id_sb_subway_station],
			poi_id_sb_subway_station : [20, poi_id_dt_subway_station],
			poi_id_dt_subway_station : [20, poi_id_kb_subway_station],
			poi_id_kb_subway_station : [20, poi_id_ssb_subway_station]
			}

		),
	EwTransportLine( # red subway line from cratersville to toxington
		id_line = transport_line_subway_red_northbound,
		alias = [
			"northredline",
			"northred",
			"rednorth",
			"redtotoxington",
			"redtotox",
			"redtott"
			],
		first_stop = poi_id_cv_subway_station,
		last_stop = poi_id_tt_subway_station,
		next_line = transport_line_subway_red_southbound,
		str_name = "The red subway line towards Toxington",
		schedule = {
			poi_id_cv_subway_station : [20, poi_id_wt_subway_station],
			poi_id_wt_subway_station : [20, poi_id_rr_subway_station],
			poi_id_rr_subway_station : [20, poi_id_dt_subway_station],
			poi_id_dt_subway_station : [20, poi_id_ck_subway_station],
			poi_id_ck_subway_station : [20, poi_id_gd_subway_station],
			poi_id_gd_subway_station : [20, poi_id_ah_subway_station],
			poi_id_ah_subway_station : [20, poi_id_tt_subway_station]
			}

		),
	EwTransportLine( # red subway line from toxington to cratersville
		id_line = transport_line_subway_red_southbound,
		alias = [
			"southredline",
			"southred",
			"redsouth",
			"redtocratersville",
			"redtocraters",
			"redtocv"
			],
		first_stop = poi_id_tt_subway_station,
		last_stop = poi_id_cv_subway_station,
		next_line = transport_line_subway_red_northbound,
		str_name = "The red subway line towards Cratersville",
		schedule = {
			poi_id_tt_subway_station : [20, poi_id_ah_subway_station],
			poi_id_ah_subway_station : [20, poi_id_gd_subway_station],
			poi_id_gd_subway_station : [20, poi_id_ck_subway_station],
			poi_id_ck_subway_station : [20, poi_id_dt_subway_station],
			poi_id_dt_subway_station : [20, poi_id_rr_subway_station],
			poi_id_rr_subway_station : [20, poi_id_wt_subway_station],
			poi_id_wt_subway_station : [20, poi_id_cv_subway_station]
			}

		),
	EwTransportLine( # green subway line from smogsburg to west glocksbury
		id_line = transport_line_subway_green_eastbound,
		alias = [
			"greeneastline",
			"greeneast",
			"eastgreen",
			"greentosmogsburg",
			"greentosmogs",
			"greentosb"
			],
		first_stop = poi_id_wgb_subway_station,
		last_stop = poi_id_sb_subway_station,
		next_line = transport_line_subway_green_westbound,
		str_name = "The green subway line towards Smogsburg",
		schedule = {
			poi_id_wgb_subway_station : [20, poi_id_jp_subway_station],
			poi_id_jp_subway_station : [20, poi_id_nsb_subway_station],
			poi_id_nsb_subway_station : [20, poi_id_kb_subway_station],
			poi_id_kb_subway_station : [20, poi_id_dt_subway_station],
			poi_id_dt_subway_station : [20, poi_id_sb_subway_station]
			}

		),
	EwTransportLine( # green subway line from west glocksbury to smogsburg
		id_line = transport_line_subway_green_westbound,
		alias = [
			"greenwestline",
			"greenwest",
			"westgreen",
			"greentowestglocksbury",
			"greentowestglocks",
			"greentowgb"
			],
		first_stop = poi_id_sb_subway_station,
		last_stop = poi_id_wgb_subway_station,
		next_line = transport_line_subway_green_eastbound,
		str_name = "The green subway line towards West Glocksbury",
		schedule = {
			poi_id_sb_subway_station : [20, poi_id_dt_subway_station],
			poi_id_dt_subway_station : [20, poi_id_kb_subway_station],
			poi_id_kb_subway_station : [20, poi_id_gb_subway_station],
			poi_id_gb_subway_station : [20, poi_id_wgb_subway_station]
			}

		),
	EwTransportLine( # blue subway line from downtown to assault flats beach
		id_line = transport_line_subway_blue_eastbound,
		alias = [
			"blueeastline",
			"blueeast",
			"eastblue",
			"bluetoassaultflatsbeach",
			"bluetoassaultflats",
			"bluetobeach",
			"bluetoafb"
			],
		first_stop = poi_id_dt_subway_station,
		last_stop = poi_id_afb_subway_station,
		next_line = transport_line_subway_blue_westbound,
		str_name = "The blue subway line towards Assault Flats Beach",
		schedule = {
			poi_id_dt_subway_station : [20, poi_id_gld_subway_station],
			poi_id_gld_subway_station : [20, poi_id_jr_subway_station],
			poi_id_jr_subway_station : [20, poi_id_vc_subway_station],
			poi_id_vc_subway_station : [20, poi_id_afb_subway_station]
			}

		),
	EwTransportLine( # blue subway line from assault flats beach to downtown
		id_line = transport_line_subway_blue_westbound,
		alias = [
			"bluewestline",
			"bluewest",
			"westblue",
			"bluetodowntown",
			"bluetodt"
			],
		first_stop = poi_id_afb_subway_station,
		last_stop = poi_id_dt_subway_station,
		next_line = transport_line_subway_blue_eastbound,
		str_name = "The blue subway line towards Downtown NLACakaNM",
		schedule = {
			poi_id_afb_subway_station : [20, poi_id_vc_subway_station],
			poi_id_vc_subway_station : [20, poi_id_jr_subway_station],
			poi_id_jr_subway_station : [20, poi_id_gld_subway_station],
			poi_id_gld_subway_station : [20, poi_id_dt_subway_station]
			}

		),
	# EwTransportLine( # white subway line from downtown to juvies row
	# 	id_line = transport_line_subway_white_eastbound,
	# 	alias = [
	# 		"whiteeastline",
	# 		"whiteeast",
	# 		"eastwhite",
	# 		"whitetojuviesrow",
	# 		"whitetojuvies",
	# 		"whitetojr"
	# 	    ],
	# 	first_stop = poi_id_underworld_subway_station,
	# 	last_stop = poi_id_jr_subway_station,
	# 	next_line = transport_line_subway_white_westbound,
	# 	str_name = "The white subway line towards Juvie's Row",
	# 	schedule = {
	# 		poi_id_underworld_subway_station : [20, poi_id_dt_subway_station],
	# 		poi_id_dt_subway_station : [20, poi_id_rr_subway_station],
	# 		poi_id_rr_subway_station : [20, poi_id_jr_subway_station]
	# 	    }
	# 	),
	# EwTransportLine( # white subway line from juvies row to downtown
	# 	id_line = transport_line_subway_white_westbound,
	# 	alias = [
	# 		"whitewestline",
	# 		"whitewest",
	# 		"westwhite",
	# 		"whitetounderworld",
	# 		"whitetouw"
	# 	    ],
	# 	first_stop = poi_id_jr_subway_station,
	# 	last_stop = poi_id_underworld_subway_station,
	# 	next_line = transport_line_subway_white_eastbound,
	# 	str_name = "The white subway line towards The Underworld",
	# 	schedule = {
	# 		poi_id_jr_subway_station : [20, poi_id_rr_subway_station],
	# 		poi_id_rr_subway_station : [20, poi_id_dt_subway_station],
	# 		poi_id_dt_subway_station : [20, poi_id_underworld_subway_station],
	# 	    }
	# 	),
	EwTransportLine( # blimp line from dreadford to assault flats beach
		id_line = transport_line_blimp_df_to_afb,
		alias = [
			"assaultflatsbeachblimp",
			"assaultflatsblimp",
			"beachblimp",
			"afbblimp",
			"blimptoassaultflatsbeach",
			"blimptoassaultflats",
			"blimptobeach",
			"blimptoafb"
			],
		first_stop = poi_id_df_blimp_tower,
		last_stop = poi_id_afb_blimp_tower,
		next_line = transport_line_blimp_afb_to_df,
		str_name = "The blimp line towards Assault Flats Beach",
		schedule = {
			poi_id_df_blimp_tower : [60, poi_id_jaywalkerplain],
			poi_id_jaywalkerplain : [40, poi_id_northsleezeborough],
			poi_id_northsleezeborough : [40, poi_id_krakbay],
			poi_id_krakbay : [40, poi_id_downtown],
			poi_id_downtown : [40, poi_id_greenlightdistrict],
			poi_id_greenlightdistrict : [40, poi_id_vagrantscorner],
			poi_id_vagrantscorner : [40, poi_id_afb_blimp_tower]
			}

		),
	EwTransportLine( # blimp line from assault flats beach to dreadford
		id_line = transport_line_blimp_afb_to_df,
		alias = [
			"dreadfordblimp",
			"dreadblimp",
			"dfblimp",
			"blimptodreadford",
			"blimptodread",
			"blimptodf"
			],
		first_stop = poi_id_afb_blimp_tower,
		last_stop = poi_id_df_blimp_tower,
		next_line = transport_line_blimp_df_to_afb,
		str_name = "The blimp line towards Dreadford",
		schedule = {
			poi_id_afb_blimp_tower : [60, poi_id_vagrantscorner],
			poi_id_vagrantscorner : [40, poi_id_greenlightdistrict],
			poi_id_greenlightdistrict : [40, poi_id_downtown],
			poi_id_downtown : [40, poi_id_krakbay],
			poi_id_krakbay : [40, poi_id_northsleezeborough],
			poi_id_northsleezeborough : [40, poi_id_jaywalkerplain],
			poi_id_jaywalkerplain : [40, poi_id_df_blimp_tower]
			}

		)
]

id_to_transport_line = {}