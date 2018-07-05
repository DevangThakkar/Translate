with open("../data/nouns/pairwise_dig_50_stats.tsv", "r") as f:
	flag = True

	fams = {"Afroasiatic":["am", "ar", "ha", "iw", "mt", "so"],
			"Albanian":["sq"],
			"Armenian":["hy"],
			"Austroasiatic":["km", "vi"],
			"Austronesian":["ceb", "tl", "haw", "id", "jw", "mg", "ms", "mi", "sm", "su"],
			"Baltic":["lv", "lt"],
			"Basque":["eu"],
			"Celtic":["ga", "gd", "cy"],
			"Dravidian":["ta", "te", "kn", "ml"],
			"Esperanto":["eo"],
			"Germanic":["af", "da", "nl", "fy", "de", "is", "lb", "no", "sv", "yi"],
			"Hellenic":["el"],
			"Iberian":["ka"],
			"Indic":["bn", "gu", "hi", "mr", "ne", "pa", "sd", "si", "ur"],
			"Iranian":["ku", "ps", "fa", "tg"],
			"Japonic":["ja"],
			"Korean":["ko"],
			"Kra-Dai":["lo", "th"],
			"Mongolic":["mn"],
			"Niger-Congo":["ny", "ig", "st", "sn", "sw", "xh", "yo", "zu"],
			"Romance":["ca", "co", "fr", "gl", "ht", "it", "la", "pt", "ro", "es"],
			"Sino-Tibetan":["zh-CN", "zh-TW", "hmn", "my"],
			"Slavic":["be", "bs", "bg", "hr", "cs", "mk", "pl", "ru", "sr", "sk", "sl", "uk"],
			"Turkic":["az", "kk", "ky", "tr", "uz"],
			"Uralic":["et", "fi", "hu"]}

	fam_list = ["Afroasiatic", "Albanian", "Armenian", "Austroasiatic",
				"Austronesian", "Baltic", "Basque", "Celtic", "Dravidian",
				"Esperanto", "Germanic", "Hellenic", "Iberian", "Indic",
				"Iranian", "Japonic", "Korean", "Kra-Dai", "Mongolic",
				"Niger-Congo", "Romance", "Sino-Tibetan", "Slavic",
				"Turkic", "Uralic"]

	lang = []

	fam_count = [[0 for fam in fams] for fam in fams]

	for line in f:

		if flag:

			# print(line)
			flag = False
			node_names = line.strip().replace("-,", "").split("\t")
			print(node_names)
			continue

		else:
			line_arr = line.strip().split("\t")
			for i in range(len(line_arr)):
				if i == 0 or i == 1:
					continue
				else:
					if line_arr[i] != 0:
						second_fam = ""
						for fam in fams:
							if node_names[i] in fams[fam]:
								second_fam = fam
								break
						# print
						fam_count[fam_list.index(line_arr[0])][fam_list.index(second_fam)] += int(line_arr[i])

# for i in range(len(fam_list)):
# 	for j in range(len(fam_list)):
# 		if fam_list[i][j] == 0:

print(fam_count)

for i in range(len(fam_list)):
	for j in range(len(fam_list)):
		if fam_count[i][j] != 0:
			print("[\""+fam_list[i]+"\",\""+fam_list[j]+"\","+str(fam_count[i][j])+"],")