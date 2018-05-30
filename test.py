from iota import Iota

# Generate a random seed.
api = Iota('http://localhost:14265')

#print nodeinfo
print(api.get_node_info())