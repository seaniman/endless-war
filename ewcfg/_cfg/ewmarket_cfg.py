#Stockmarket related config

# Market delta
max_iw_swing = 30

# stock ids
stock_kfc = "kfc"
stock_pizzahut = "pizzahut"
stock_tacobell = "tacobell"

# default stock rates
default_stock_market_rate = 1000
default_stock_exchange_rate = 1000000


# list of stock ids
stocks = [
	stock_kfc,
	stock_pizzahut,
	stock_tacobell,
]

# Stock names
stock_names = {
	stock_kfc : "Kentucky Fried Chicken",
	stock_pizzahut : "Pizza Hut",
	stock_tacobell : "Taco Bell",
}

#  Stock emotes
stock_emotes = {
	stock_kfc : emote_kfc,
	stock_pizzahut : emote_pizzahut,
	stock_tacobell : emote_tacobell
}

# trading
trade_state_proposed = 0
trade_state_ongoing = 1
trade_state_complete = 2

