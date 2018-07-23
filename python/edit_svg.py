# The aim of this script is to modify and create individual svgs for different
# languages

import re

# open file with language name to code mapping and store it in a dict
# lang_names[<lang code>] = <language name>
lang_names = dict()
with open("../data/nouns/lang_codes.csv", "r") as f:
	for line in f:
		line_arr = line.strip().split(",")
		lang_names[line_arr[1]] = line_arr[0]

# open chain stats file and store data in a dict
# file contains the number of chains for each word (,) for each language (\n)
# chains[<language name + lang code] = <array of counts for each word>
chains = dict()
with open("../data/nouns/chain_stats.csv", "r") as f:
	for line in f:
		line_arr = line.strip().split(",")
		fname = line_arr[0]
		line_arr = [int(x.strip()) for x in line_arr if
			(x != "" and "." not in x)]
		lang_code = fname.replace("chain_", "").replace(".csv", "")
		lang_full = lang_names[lang_code] + " [" + lang_code + "]" 
		chains[lang_full] = line_arr

# reinit final file
with open("../ai/chain_blend_final.svg", "w") as f:
	f.write("")

# read and write the chain blend start file into final file
start = ""
with open("../ai/chain_blend_start.svg", "r") as f:
	start = "".join(f.readlines())

with open("../ai/chain_blend_final.svg", "w") as f:
	f.write(start)

count = 0
for lang in sorted(chains.keys()):

	count+=1
	nav_id = "\'n"+str(count)+"\'"

	with open("../ai/chain_blend.svg", "r") as f:
		data = "".join(f.readlines())
		for i in range(len(chains[lang])):
			links = chains[lang][i]

			# change opacity on spiral
			opacity = ["0.0", ".2", ".4", ".6", ".8"]
			colors = ["#ffffff", "#f44bf9", "#bf37b5", "#7c157c", "#490056"]
			data = data.replace(
				"\'w"+str(i+1)+"\' opacity=\'.4\'", 
				"\'w"+str(i+1)+"\' opacity=\'"+opacity[min(links, 4)]+"\' "+
				"fill="+"\'"+colors[min(links, 4)]+"\'")

			# change opacity of nav dots
			data = data.replace(
				nav_id+" opacity=\'0.51\'",
				nav_id+" opacity=\'1.0\'")

			# add language name
			data = data.replace(
				"id=\'language\'>Language",
				"id=\'language\'>"+lang)

	name = "../ai/automated/chain_"+lang.split(" [")[1].replace("]", "")+".svg"
	with open(name, "w") as f:
		f.write("<g id=\'Layer_"+str(count)+"\' opacity=\'0.0\'>\n")
		f.write(data)

	mod_data = ""
	with open(name, "r") as f:
		for line in f:
			if "opacity=\'0.0\' fill" in line:
				continue
			if "opacity=\'0.51\'" in line:
				continue
			mod_data += line

	with open("../ai/chain_blend_final.svg", "a") as f:
		mod_data = mod_data.replace("\n\t", "\n").replace("\n\t", "\n")
		mod_data = mod_data.replace("\n\n", "\n").replace("\n\n", "\n")
		mod_data = mod_data.replace("\n\n", "\n").replace("\n\n", "\n")
		mod_data = mod_data.replace("\n\n", "\n").replace("\n\n", "\n")
		f.write(mod_data)
		f.write("</g>\n")

with open("../ai/chain_blend_final.svg", "a") as f:
	f.write("</svg>")