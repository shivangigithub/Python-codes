#A code to match coding gene symbols from other file containg gene symbols in multi columns
f1=open("coding.txt").read().split("\n")
f2=open("uniq-gene-symbols.txt").read().split("\n")
List1 = f1
List2 = f2
dict={}
for i in range(0,len(List1),1):
	splitline = List1[i].split("\t")
	split2 = splitline[1].split(",")
	dict[splitline[0]]=""
	# print (dict)
	for j in range(0,len(split2),1):
		dict[split2[j]]=""
	# print (dict)
for line in List2:
	if line in dict:
		print (line)


