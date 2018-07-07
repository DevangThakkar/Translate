# The aim of this script is to count the number of elements in the chain for
# each word in each language. The resulting output is a 103x1000 matrix with
# the number of elements in the chain in the corresponding cell.
from os import listdir

mypath = "../data/nouns/chains/"
files = listdir(mypath)

for f in files:
	
