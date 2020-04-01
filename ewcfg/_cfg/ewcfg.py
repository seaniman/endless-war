
# Global configuration options.

version = "v3.26i2"

dir_msgqueue = 'msgqueue'

# lists of all the discord server objects served by bot, identified by the server id
server_list = {}

"""
	store a server in a dictionary
"""
def update_server_list(server):
	server_list[server.id] = server


client_ref = None

def get_client():
	global client_ref
	return client_ref

"""
	save the discord client of this bot
"""
def set_client(cl):
	global client_ref
	client_ref = cl

	return client_ref
