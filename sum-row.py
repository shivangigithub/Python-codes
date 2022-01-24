##sum and average of row elements
file = open ("sum.txt","r").read().split("\n")
array =file
# print type(array)
# array.append(file)
for i in range(len(array)):
	Sum =0
	# count =0
	# print "*************"
	# print array[i]
	splitline = array[i].split("\t")
	for j in range(0,len(splitline),1):
		# print j
		# print "#####"
		# print splitline[j]
		# print type(splitline[j])
		Sum += int(splitline[j])
		# count = count + 1
		# print len(splitline)
	average = Sum/len(splitline)
	print "sum of row elements is " , Sum
	print "average of row elements is " , average
