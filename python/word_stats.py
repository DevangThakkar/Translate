#  Obtain the number of languages a word matches with

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

def count_stats(num, en_array, lang):
	stats = dict()
	for i in range(len(en_array)):

		count = 0
		temp_arr = []
		for l in lang:
			with open("../data/nouns/" + str(num) + "/translate_en_" + l + "_en.csv", "r") as f:
				temp = 0
				for line in f:
					if en_array[i] == "tobacco" and line.strip().lower() == "tobacco":
						print(line)
					if temp == i:
						temp_arr.append(line.strip().lower())
						break
					temp += 1

		if len(temp_arr) != 103:
			print(str(i) + "_" + str(num) + "_"+str(len(temp_arr)))

		stats[en_array[i]] = temp_arr.count(en_array[i])

	with open("../data/nouns/word_stats.csv", "a") as f:
		for word in stats:
			f.write(word + "," + str(stats[word]) + "\n")

count_stats(500, en_500, lang)
count_stats(1000, en_1000, lang)
count_stats(1500, en_1500, lang)