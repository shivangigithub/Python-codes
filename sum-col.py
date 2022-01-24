##sum and average of row elements
file = open ("sum.txt","r").read().split("\n")
array =file
Sum = len(array[0].split("\t")) *[0]
# print type(Sum)
for i in range(len(array)):
	count =0
	# Sum.append(0)
	# print "*************"
	# print array[i]
	splitline = array[i].split("\t")
	for j in range(0,len(splitline),1):
		# print j
		# Sum.append(j)
		print "#####"
		print len(splitline)
		# print type(splitline[j])
		# if j == 1:
			# print splitline[j]
		Sum[j] += int(splitline[j])
		# count = count + 1
		# average = Sum/count
print "sum of column elements is " , Sum
	# print "average of row elements is " , average
