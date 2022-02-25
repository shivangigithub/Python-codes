#A code to calculate enrichment of active molecules in a docking method
import os
f1=open("39_actives_ids.txt").read().split("\n")
f2=open("docking_350_actives_decoys_2.csv").read().split("\n")
array1=f1
array2=f2
count = 0
TP = 0
percent = int((10 * len(array2))/100)
# print (percent)
i=0
total_actives = 6
TNFP=20
list = "ZINCDDDDD"
# ids = `cut -f1 39_actives_ids.txt`
# print (f1)
for i in range(0,len(array2),i+percent):
	# print (i)
	# splitline = array2[i].split(",")
	# print (splitline[0])
	# ids = splitline[0]
	for j in range (i,i+percent,1):
		# print ("j is " , j)
		splitline = array2[j].split(",")
		# print (splitline[0])
		os.system('grep splitline[0] 39_actives_ids.txt')
		for line2 in array1:
			count = 0 
			if line2 == splitline[0]:
				# print (line2)
				count += 1
				# print ("count is " , count)
				TP = count + TP
				# print ("TP is ", TP)
	FN = total_actives-TP
	se = TP/(TP+FN)
	FP = (i+percent)-TP
	TN = (TNFP)-FP
	sp = TN/(TN+FP)
	Nsp = 1-sp
	#EF = se/Nsp;
	FE1=TP/(i+percent)
	#print FE1,"\n";
	FE2=total_actives/TNFP
		#print FE2,"\n";
	EF=FE1/FE2
	#% = ((i+p)/l)*100;
	a = i+percent
	b = len(array2)/100
	c = (a/b)
	# print (c)
	# per = round( c )
	# print (percent, "\t", i+percent, "\t", TP)
	print (c, i+percent, TP,FN,TP+FN, se, FP, TNFP, TN, sp, Nsp, EF)

				# n=@match;
				# print "n=n,\t", @match,"\n";
				# TP=TP+n;	
				# print "TP is " , TP
		# match=grep(/splitline[0]/,list);
		# print (match)

	# if splitline[0]=="ZINC01543843":
	# 	print ("y")
	# print (len(array2))
	# percent = 
	# print ()
	# print (splitline[1])
	# if line == splitline[0]:
	# 	print ("Y",line)