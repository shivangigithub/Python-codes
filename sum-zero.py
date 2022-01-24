##print subarray with sum zero
# List = [6, 4, 5, -7, -3, -4, -1]
List = [8,2,5,-1,-4,-2,5,9]
# List = [6, -3, -2, -1, 5, -5, -2,9,-7,6, -3, -1, -1, -1]
Sum1=0
for i in range(0,len(List)-1,1):
	subarray= []
	Sum1 = List[i] + List[i+1]
	subarray.extend([List[i],List[i+1]])
	if Sum1 == 0:
		pass
		print ("subarray-wid-sum zero " ,subarray)
	for j in range(i+2,len(List),1):
		if Sum1 != 0:
			Sum2 = Sum1 + List[j]
			Sum1 = Sum2
			subarray.append([List[j]])
			if Sum2 == 0:
				print ("Subarray with sum zero is" , subarray)