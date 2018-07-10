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

lang_names = dict()
with open("../data/nouns/lang_codes.csv", "r") as f:
	for line in f:
		line_arr = line.strip().split(",")
		lang_names[line_arr[1]] = line_arr[0]

count = 0
for lang in sorted(chains.keys()):

	count+=1
	nav_id = "\"n"+str(count)+"\""

	with open("../ai/chain_blend.svg", "r") as f:
		data = "".join(f.readlines())
		for i in range(len(chains[lang])):
			links = chains[lang][i]

			# change opacity on spiral
			# print("\"l"+str(i+1)+"\" opacity=\"0.4\"")
			# print(data)
			# print("\"l"+str(i+1)+"\" opacity=\"0.4\"" in data)
			data = data.replace(
				"\"w"+str(i+1)+"\" opacity=\".4\"", 
				"\"w"+str(i+1)+"\" opacity=\""+str(min(links*0.25, 1))+"\"")

			# change opacity of nav dots
			# print(nav_id+" opacity=\"0.5\"", nav_id+" opacity=\"1.0\"")
			data = data.replace(
				nav_id+" opacity=\"0.5\"",
				nav_id+" opacity=\"1.0\"")

			# add language name
			data = data.replace(
				"id=\"language\">Language",
				"id=\"language\">"+lang_names[lang]+" ("+lang+")")			

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