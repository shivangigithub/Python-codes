import os, glob
path1 = "/media/shivangiagarwal/510c2bd7-16e1-4416-afa8-8f0854a24c61/shivangi/PrCa-SNVs/VAF/master-vcf/*"
path2 = "/media/shivangiagarwal/510c2bd7-16e1-4416-afa8-8f0854a24c61/shivangi/PrCa-SNVs/VAF/excel-vcf/*"
# path2 = "/home/shivangiagarwal/Documents/optimizing/2018-559_v2_c3387_2021-06-22-10-34-39-399_ds.f960a12ba1264c838fcf2807fd399030/SNVs/*.txt"
for file in glob.glob(path1):
	print (file)
	splitFileName1 = file.split("/")
	splitFileName1a = splitFileName1[8].split("--")
	# print ("AAAA"+splitFileName1a[0])
	# out = splitFileName1a[0]+"-hard-filtered-3.vcf"
	# print (out)
	# f1 = open("{0}".format(file),"r").read().split("\n")
	# f4 = open(out,"w")
	# # f4 = open("{0}.out".format(file),"w")
	# list1 = f1
	for file2 in glob.glob(path2):
		print (file2)
		splitFileName2 = file2.split("/")
		splitFileName2a = splitFileName2[8].split("-SP")
		# print ("BB"+splitFileName2a[0])
		if splitFileName1a[0] in splitFileName2a[0]:
			# print ("YES")
			f1 = open("{0}".format(file),"r").read().split("\n")
			list1 = f1
			f2 = open("{0}".format(file2),"r").read().split("\n")
			list2 = f2
			out = splitFileName2a[0]+"-VAF.vcf"
			f4 = open(out,"w")
			for line in list1:
				# print (line)
				splitline = line.split("\t")
				string1 = splitline[0]+splitline[1]+splitline[3]+splitline[4]
				# print (string1)
				splitline4 = splitline[9].split(":")
				for line2 in list2:
					# print (line2)
					if line2.startswith("chr"):
						# print (line2)
						splitline2 = line2.split(":")
						string2 = splitline2[0]+splitline2[1]
						splitline3 = string2.split("\t")
						string3 = splitline3[0]+splitline3[1]+splitline3[2]
						# print (string3)
						if string1 in string3:
							# print ("YES")
							f4.write(line2+"\t"+splitline4[3])
							f4.write("\n")
							# print (line2+"\t"+splitline4[3])
							break
			break