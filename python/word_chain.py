# the aim of this script is to see how far a word goes on multiple translations
# for example, ((en->it->en)country)->nation, then, we find out the result for
# ((en->it->en)nation) until a word is repeated


from googletrans import Translator
import sys
from time import sleep

trans = Translator()

en = []

# sys.argv[1] is the pointer to the word file
with open("../data/nouns/" + sys.argv[1] + "/translate_en.csv", "r") as f:
	for line in f:
		en.append(line.strip().lower())

# other lang
lang = sys.argv[2].strip()

# we have a limit to the number of wirds we can translate at once - we shall
# use sys.argv 3,4

en = en[int(sys.argv[3]):int(sys.argv[4])]

for word in en:
	chain = [word]
	while True:
		if len(chain) == 1:
			src = "en"
			dest = lang

		t = trans.translate(word, src=src, dest=dest)

		# print(word, t.text, src, dest)
		temp = src
		src = dest
		dest = temp
		word = t.text

		translated = t.text.lower()

		if translated in chain:
			chain.append(translated)
			break
		if translated not in chain:
			chain.append(translated)

	fname = "../data/nouns/chains/chain_" + lang + ".csv"
	with open(fname, "a") as out:
		for link in chain:
			out.write(link + ", ")
		out.write("\n")
	chain = []