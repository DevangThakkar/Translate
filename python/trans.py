from googletrans import Translator
import sys

trans = Translator()
arr = []

with open("../data/nouns/1500/translate_"+sys.argv[1]+".csv", "r") as f:
	i = 0
	for line in f:

		if i < 20:
			i += 1
			arr.append(line.strip())

		if i == 20:
			i = 0
			t = trans.translate(arr, src=sys.argv[2], dest=sys.argv[3])

			fname = "../data/nouns/1500/translate_"+sys.argv[1]+"_"+sys.argv[3]+".csv"
			with open(fname, "a") as out:
				for translation in t:
					out.write(translation.text+"\n")

			arr = []
