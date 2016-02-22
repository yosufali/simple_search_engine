
#time_step and page
def compute_ranks(graph):
	d = 0.8 # damping factor
	numloops = 10 # bo. of time we'll go through the relaxation. Determines accuracy of ranks

	ranks = {} #
	npages = len(graph)
	for page in graph:
		ranks[page] = 1.0 / npages

	#relaxation
	for i in range(0, numloops):
		newranks = {}
		for page in graph:
			newrank = (1 - d) / npages
			for node in graph:
				if page in graph[node]: # if page is in the list of urls node points to, we'll add to new rank, based on the rank of this node
					newrank = newrank + d * (ranks[node] / len(graph[node])) # decrease value of a link on a page if there are lots links on that page
			newranks[page] = newrank
		ranks = newranks
	return ranks
