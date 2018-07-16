# the aim of this script is to create minimal chain with only words in English
# and store it in a single file accessible by javascript. Output format is
# <lang>\t<word number>\t<element 1>\t<element 2>\t<element 3>...

from os import listdir

mypath = "../data/nouns/chains/"
files = listdir(mypath)

chain = ""

for item in files:

	count = 0
	with open(mypath+item, "r") as f:

		for line in f:
			count += 1
			line_arr = line.strip().split(",")
			line_arr = [x.strip() for x in line_arr if x != ""]

			if len(line_arr) > 3:
				len_chain = int(len(line_arr)/2)-1
				short_name = item.replace("chain_", "").replace(".csv", "")
				chain += (short_name+"\t"+str(count))
				for i in range(2*int(len(line_arr)/2)):
					if i%2 == 0:
						chain += ("\t"+line_arr[i])
				chain += "\n"


with open("../data/nouns/minimal_chain.tsv", "w") as f:
	f.write(chain)		