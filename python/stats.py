lang = []
lang_names = dict()
lang_fam = dict()

with open("../data/nouns/lang_codes.csv", "r") as f:

	for line in f:
		splitted = line.strip().split(",")
		lang.append(splitted[1])
		lang_names[splitted[1]] = splitted[0]
		lang_fam[splitted[1]] = splitted[2]

en_500 = []
en_1000 = []
en_1500 = []

with open("../data/nouns/500/translate_en.csv", "r") as f:
	for line in f:
		en_500.append(line.strip().lower())

with open("../data/nouns/1000/translate_en.csv", "r") as f:
	for line in f:
		en_1000.append(line.strip().lower())

with open("../data/nouns/1500/translate_en.csv", "r") as f:
	for line in f:
		en_1500.append(line.strip().lower())

stats_500 = dict()
for l in lang:

	count = 0
	temp_arr = []

	with open("../data/nouns/500/translate_en_" + l + "_en.csv", "r") as f:
		for line in f:
			temp_arr.append(line.strip().lower())

	if len(temp_arr) != 500:
		print(l + "_500_"+str(len(temp_arr)))

	for i in range(len(temp_arr)):
		if temp_arr[i] != en_500[i] and "(PL)" not in en_500[i]:
			count += 1

	stats_500[l] = count

stats_1000 = dict()
for l in lang:

	count = 0
	temp_arr = []

	with open("../data/nouns/1000/translate_en_" + l + "_en.csv", "r") as f:
		for line in f:
			temp_arr.append(line.strip().lower())

	# print(str(len(temp_arr)))
	if len(temp_arr) != 500:
		print(l + "_1000_"+str(len(temp_arr)))

	for i in range(len(temp_arr)):
		if temp_arr[i] != en_1000[i] and "(PL)" not in en_1000[i]:
			count += 1

	stats_1000[l] = count

stats_1500 = dict()
for l in lang:

	count = 0
	temp_arr = []

	with open("../data/nouns/1500/translate_en_" + l + "_en.csv", "r") as f:
		for line in f:
			temp_arr.append(line.strip().lower())

	if len(temp_arr) != 500:
		print(l + "_1500_"+str(len(temp_arr)))

	for i in range(len(temp_arr)):
		if temp_arr[i] != en_1500[i] and "(PL)" not in en_1500[i]:
			count += 1

	stats_1500[l] = count

with open("../data/nouns/stats.csv", "w") as f:

	# f.write("lang,lang_code,500_score,1000_score\n")
	for l in stats_500:
		doublecombo = str(stats_500[l] + stats_1000[l] + stats_1500[l])
		combo = str(stats_500[l] + stats_1000[l])
		solo = str(stats_500[l])

		f.write(lang_names[l] + "," + l + "," + solo + "," +
				combo + "," + doublecombo + "," + lang_fam[l] + "\n")
