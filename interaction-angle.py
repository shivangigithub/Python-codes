# python3 interaction-angle.py  > interaction-angle.txt 
import re,glob
import math 
f1=open("Receptor_3ert1.pdb").read().split("\n")
path="/Users/apple/Desktop/Python-tasks/Python-Phd-programs/PL/All_ligands_3ert/*.pdb"
List=f1
N=[]
H=[]
for file in glob.glob(path):
	print (file)
	splitfilename = file.split("/")
	f2=open("{0}".format(file),"r").read().split("\n")
	List2=f2
	for line in List2:
		print (line)
		if line.startswith("HET"):
			line = re.sub(" +", " ", line)
			splitline1 = line.split(" ")
			if splitline1[10] == "N":
				print ("YESSSSSSSS")
				N.append(splitline1[5])
				N.append(splitline1[6])
				N.append(splitline1[7])
				N.append(splitline1[1])
				N.append(splitline1[2])
				# print (N)
			if splitline1[10] == "H":
				# x2=splitline1[5]
				# y2=splitline1[6]
				# z2=splitline1[7]
				H.append(splitline1[5])
				H.append(splitline1[6])
				H.append(splitline1[7])
				H.append(splitline1[1])
				H.append(splitline1[2])
				# print (H)
				print ("***********")
				for i in range (0,len(List),1):
					print ("i " , i )
					List[i] = re.sub(" +", " ", List[i])
					# print (N)
					if List[i].startswith("ATOM"):
						splitline2 = List[i].split(" ")
						# if splitline2[0] == "ATOM":
						if splitline2[11] == "O":
							print ("oxygen is " , splitline2[11])
							x3=float(splitline2[6])
							y3=float(splitline2[7])
							z3=float(splitline2[8])
							for j in range(0,len(N),5):
								# print ("jjjjjjjjj")
								# print (N[j])
								x1= float(N[j])
								y1 =float(N[j+1])
								z1 = float(N[j+2])
								# print (x1,x3,y1,y3,z1,z3)
								dist5 = math.sqrt((float(x3)-float(x1))*(float(x3)-float(x1))+(float(y3)-float(y1))*(float(y3)-float(y1))+(float(z3)-float(z1))*(float(z3)-float(z1)))
								# print (dist5)
								# print (splitfilename[8],splitline2[1],splitline2[2],splitline2[3],splitline2[5],N[j+3],N[j+4],dist5)
								if (dist5 <= 3.2):
									# print (splitfilename[8],splitline2[1],splitline2[2],splitline2[3],splitline2[5],N[j+4],N[j+3],dist5)
									pass
									print ("distance")
									for k in range(0,len(H),5):
										x2 = float(H[k])
										y2 = float(H[k+1])
										z2 = float(H[k+2])
										print ("see " , x2,y2,z2)
										BA= (x1-x2, y1-y2, z1-z2)
										BC= (x3-x2, y3-y2, z3-z2)
										BABC=((x1-x2) * (x3-x2) + (y1-y2) * (y3-y2) + (z1-z2) * (z3-z2))
										vBA= math.sqrt ((x1-x2) * (x1-x2) + (y1-y2) * (y1-y2) + (z1-z2) * (z1-z2))
										vBC= math.sqrt ((x3-x2) * (x3-x2) + (y3-y2) * (y3-y2) + (z3-z2) * (z3-z2))
										cosangle = (BABC/(vBA *vBC))
										angle = math.acos (cosangle)
										deg = math.degrees(angle)
										# print (deg)
										if((deg>=90) and (deg<=180)):
											print (splitfilename[8],splitline2[1],splitline2[2],splitline2[3],splitline2[5],N[j+4],N[j+3],H[k+3],H[k+4],dist5,deg)
											print ("###########")
	# break
	N=[]
	H=[]