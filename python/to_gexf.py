import networkx as nx

G = nx.Graph()

color = {1:"gray",
			2:"red",
			3:"blue",
			4:"yellow",
			5:"green",
			6:"purple",
			7:"pink",
			8:"orange"}

with open("../data/nouns/interaction.tsv", "r") as f:
	flag = True
	for line in f:
		# print(i)
		if flag:
			# print(line)
			flag = False
			node_names = line.strip().replace("_\t", "").split("\t")
			for i in range(len(node_names)):
				G.add_node(node_names[i], id=i, lang=node_names[i],fam="")
			# for n in G:
			# 	print(n)
			# 	print(G.node[n])
			continue
		else:
			line = line.strip()

			if "\t" in line:
				line_arr = line.split("\t")
			else:
				line_arr = []
				continue

			for i in range(len(line_arr)):
				if i == 0:
					G.node[line_arr[1]]["fam"] = line_arr[0]
					continue
				if i == 1:
					continue	
				else:
					if int(line_arr[i]) != 0:
						G.add_edge(line_arr[1], node_names[i])
						G[line_arr[1]][node_names[i]]['weight'] = int(line_arr[i])
						G[line_arr[1]][node_names[i]]['color'] = color[int(line_arr[i])]
						# print(G[line_arr[1]][node_names[i]]['color'])

nx.write_gexf(G, "../data/nouns/interaction.gexf")