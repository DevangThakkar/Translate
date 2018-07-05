# shittiest code I've ever written. Sorry.

lang = []
lang_names = dict()
lang_fam = dict()

with open("../data/nouns/lang_codes.csv", "r") as f:

	for line in f:
		splitted = line.strip().split(",")
		lang.append(splitted[1])
		lang_names[splitted[1]] = splitted[0]
		lang_fam[splitted[1]] = splitted[2]

en =[]
en_500 = []
en_1000 = []
en_1500 = []

with open("../data/nouns/500/translate_en.csv", "r") as f:
	for line in f:
		line = (line.replace(" (PL)", "")
					.replace(",", "")
					.replace("\n", "")
					.replace("=-", ""))
		en_500.append(line.strip().lower())
		en.append(line.strip().lower())

with open("../data/nouns/1000/translate_en.csv", "r") as f:
	for line in f:
		line = (line.replace(" (PL)", "")
					.replace(",", "")
					.replace("\n", "")
					.replace("=-", ""))
		en_1000.append(line.strip().lower())
		en.append(line.strip().lower())

with open("../data/nouns/1500/translate_en.csv", "r") as f:
	for line in f:
		line = (line.replace(" (PL)", "")
					.replace(",", "")
					.replace("\n", "")
					.replace("=-", ""))
		en_1500.append(line.strip().lower())
		en.append(line.strip().lower())

def count_stats(num, en_array, lang_names, mega):

	for l in lang_names:

		if l not in mega:
			mega[l] = []
		with open("../data/nouns/" + str(num) + "/translate_en_" + l + "_en.csv", "r") as f:
			for line in f:
				line = line.replace(" (PL)", "") \
							.replace(",", "") \
							.replace("\n", "") \
							.replace("=-", "")
				mega[l].append(line.strip().lower())

	return mega

mega = dict()
mega = count_stats(500, en_500, lang_names, mega)
mega = count_stats(1000, en_1000, lang_names, mega)
# mega = count_stats(1500, en_1500, lang_names, mega)

stats = [[0 for l in lang] for l in lang]

lang_ordered = []
lang_ordered_indices = []
i = 0
for lang in mega:
	lang_ordered.append(lang)
	lang_ordered_indices.append(i)
	i += 1

for lang in lang_ordered_indices:
	for lang1 in lang_ordered_indices:
		count = 0
		for i in range(len(mega[lang_ordered[lang]])):
			if mega[lang_ordered[lang]][i] == en[i]:
				pass
			else:
				if mega[lang_ordered[lang1]][i] == mega[lang_ordered[lang]][i]:
					count += 1
		if lang == lang1:
			count = 0
		stats[lang][lang1] = count

with open("../data/nouns/pairwise_stats.tsv", "w") as f:
	f.write("-\t")
	for lang in lang_ordered_indices:
		f.write(lang_ordered[lang] + "\t")
	f.write("\n")

	for lang in lang_ordered_indices:
		f.write(lang_ordered[lang] + "\t")
		# print(stats[lang])
		for count in stats[lang]:
			f.write(str(count) + "\t")
		f.write("\n")

with open("../data/nouns/pairwise_dig_50_stats.tsv", "w") as f:
	f.write("-\t-\t")
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

	for lang in lang_ordered_indices:

		for i in fams:

			if lang_ordered[lang] in fams[i]:
				f.write(i + "\t")
				break

	f.write("\n-\t-\t")

	for lang in lang_ordered_indices:
		f.write(lang_ordered[lang] + "\t")
	f.write("\n")

	for lang in lang_ordered_indices:

		for i in fams:

			if lang_ordered[lang] in fams[i]:
				f.write(i + "\t")
				break

		f.write(lang_ordered[lang] + "\t")
		# print(stats[lang])
		for count in stats[lang]:
			f.write(str(int(count/50)) + "\t")
		f.write("\n")

with open("../data/nouns/pairwise_words.tsv", "w") as f:
	f.write("en\t")
	for word in en:
		f.write(word+"\t")
	f.write("\n")	
	
	for lang in mega:
		f.write(lang + "\t")
		for word in mega[lang]:
			f.write(word + "\t")
		f.write("\n")
