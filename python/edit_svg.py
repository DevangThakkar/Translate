# The aim of this script is to modify and create individual svgs for different
# languages

import re

chains = dict()
with open("../data/nouns/chain_stats.csv", "r") as f:
	for line in f:
		line_arr = line.strip().split(",")
		fname = line_arr[0]
		line_arr = [int(x.strip()) for x in line_arr if
			(x != "" and "." not in x)]
		chains[fname.replace("chain_", "").replace(".csv", "")] = line_arr

for lang in chains:
	with open("../ai/chain_blend.svg", "r") as f:
		data = "".join(f.readlines())
		# print(data)
		for i in range(len(chains[lang])):
			links = chains[lang][i]
			data = data.replace(
				"\"l"+str(i+1)+"\" opacity=\"0.4\"", 
				"\"l"+str(i+1)+"\" opacity=\""+str(min(links*0.25, 1))+"\"")

	with open("../ai/automated/chain_"+lang+".svg", "w") as f:
		f.write(data)

	mod_data = ""
	with open("../ai/automated/chain_"+lang+".svg", "r") as f:
		for line in f:
			# print(line)
			# print("opacity=\"0.0\"" in line)
			if "opacity=\"0.0\"" in line:
				pass
			else:
				mod_data += line

	with open("../ai/automated/chain_"+lang+".svg", "w") as f:
		mod_data = mod_data.replace("\n\t", "\n").replace("\n\t", "\n")
		mod_data = mod_data.replace("\n\n", "\n").replace("\n\n", "\n")
		mod_data = mod_data.replace("\n\n", "\n").replace("\n\n", "\n")
		mod_data = mod_data.replace("\n\n", "\n").replace("\n\n", "\n")
		f.write(mod_data)