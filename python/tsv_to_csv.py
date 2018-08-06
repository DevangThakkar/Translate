data = ""
with open("../../Website/devangthakkar.github.io/design/assets/minimal_chain.tsv", "r") as f:
	for line in f:
		data += line.replace('\t', ',')

with open("../../Website/devangthakkar.github.io/design/assets/minimal_chain.csv", "w") as f:
	f.write(data)