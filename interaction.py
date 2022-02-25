import re,glob
import math 
# f1=open("Receptor_2fsz8228.pdb").read().split("\n")
# path="/Users/apple/Desktop/Python-tasks/Python-Phd-programs/PL/All_ligands_2fsz/*.pdb"
f1=open("Receptor_3ert1.pdb").read().split("\n")
path="/Users/apple/Desktop/Python-tasks/Python-Phd-programs/PL/All_ligands_3ert/*.pdb"
List=f1
for file in glob.glob(path):
	# print (file)
	splitfilename = file.split("/")
	f2=open("{0}".format(file),"r").read().split("\n")
	List2=f2
	for line in List2:
		if line.startswith("HET"):
			# print (line)
			line = re.sub(" +", " ", line)
			splitline1 = line.split(" ")
			if splitline1[10] == "N" or splitline1[10] == "N1+":
				x1=splitline1[5]
				y1=splitline1[6]
				z1=splitline1[7]
				# print (x1,y1,z1)
				for i in range (0,len(List),1):
					List[i] = re.sub(" +", " ", List[i])
					if List[i].startswith("ATOM"):
						splitline2 = List[i].split(" ")
						# if splitline2[0] == "ATOM":
						if splitline2[11] == "O":
							x2=splitline2[6]
							y2=splitline2[7]
							z2=splitline2[8]
							# print (x1,x2,y1,y2,z1,z2)
							# dist1 =((float(x2)-float(x1))*(float(x2)-float(x1)))
							# dist2 =((float(y2)-float(y1))*(float(y2)-float(y1)))
							# dist3 =((float(z2)-float(z1))*(float(z2)-float(z1)))
							# dist4 = ((float(x2)-float(x1))*(float(x2)-float(x1))+(float(y2)-float(y1))*(float(y2)-float(y1))+(float(z2)-float(z1))*(float(z2)-float(z1)))# print (dist)
							dist5 = math.sqrt((float(x2)-float(x1))*(float(x2)-float(x1))+(float(y2)-float(y1))*(float(y2)-float(y1))+(float(z2)-float(z1))*(float(z2)-float(z1)))
							# print (dist5)
							if (dist5 <= 3.2):
								print (splitfilename[8],splitline2[1],splitline2[2],splitline2[3],splitline2[5],splitline1[2],splitline1[1],dist5)
			if splitline1[10] == "O":
				x1=splitline1[5]
				y1=splitline1[6]
				z1=splitline1[7]
				# print (x1,y1,z1)
				for i in range (0,len(List),1):
					List[i] = re.sub(" +", " ", List[i])
					if List[i].startswith("ATOM"):
						splitline2 = List[i].split(" ")
						if splitline2[11] == "N" or splitline2[11] == "N1+" :
							x2=splitline2[6]
							y2=splitline2[7]
							z2=splitline2[8]
							# print (x1,x2,y1,y2,z1,z2)
							dist5 = math.sqrt((float(x2)-float(x1))*(float(x2)-float(x1))+(float(y2)-float(y1))*(float(y2)-float(y1))+(float(z2)-float(z1))*(float(z2)-float(z1)))# print (dist)
							if (dist5 <= 3.2):
								print (splitfilename[8],splitline2[1],splitline2[2],splitline2[3],splitline2[5],splitline1[2],splitline1[1],dist5)
			
