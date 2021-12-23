#Find subarray with sum zero
# List = [8,2,5,-4,-7,-3,-1,9]#8,2,5,-4,-7,-3,-1
List = [8,2,-10,-4,-7,7,4,9]

Sum = List[0]+List[1]
array =[List[0],List[1]]
for i in range(2,len(List),1):
	Sum = Sum + List[i]
	# print (Sum)
	array.append(List[i])
	if Sum == 0:
		print ("subarray with sum zero " , array)