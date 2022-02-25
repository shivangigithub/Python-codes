#A code to make matrix of gene expression data of 20000 genes from 10000 patient samples downloaded from TCGA
import glob
path = "/Users/apple/Desktop/Python-tasks/Python-Phd-programs/TCGA/dir/*/*"
f2 = open("out.txt","w")
f3=open("filename.txt","r").read().split("\n")
mfile = f3
dict={}
for filename in glob.glob(path):
	# print (filename)
	splitfilename  = filename.split("/")
	splitfilename2 = splitfilename[9].split(".")
	# print (splitfilename2[0])
	f1=open("{0}".format(filename),"r").read().split("\n")
	List = f1
	for line in List:
		# print ("***********")
		splitline = line.split("\t")
		key = splitline[0]
		value = splitline[1]
		if key in dict:
			fetchvalue = dict.get(key)
			value = fetchvalue + "\t" + value
			dict[key]=value
		else:
			dict[key]=value
	for line2 in mfile:
		# print ("###########")
		splitmline = line2.split("\t")
		if splitmline[1] == splitfilename2[0]:
			# print (splitmline[1])
			f2.write(splitmline[5])
			f2.write("\t")
f2.write("\n")
for key in dict:
	# print (key,dict[key])
	f2.write(key)
	f2.write("\t")
	f2.write(dict[key])
	f2.write("\n")

