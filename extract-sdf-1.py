#A code to fetch coordinates of desired set of molecules from a databse sdf file 
f1 = open("10000.txt").read().split("\n")
f2 = open ("id.txt").read().split("\n")
f4 = open ("combined-sdf.txt","w")
array1=f1
array2=f2
# array3=f3
dict={}
for i in range (0,len(array1),1):
	if (array1[i] == "$$$$"):
		# print (array1[i])
		a=i+1
		for j in range (0,len(array2),1):
			# print (array2[j])
			if array2[j] in dict:
				pass
			else:
				if array2[j] == array1[a]:
					dict[array2[j]]=1
					for k in range(a,a+30000,1):
						# print ("k is " , k)
						f4.write(array1[k])
						f4.write("\n")
						if array1[k] == "M  END":
						# if array1[k] == "$$$$":
							break


