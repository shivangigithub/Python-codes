##leader.py
#Given an array A of positive integers. 
#Find the leaders in the array. 
# An element of array is leader if it is greater than or equal to all 
# the elements to its right side. The rightmost element is always a leader. 
List = [11,2,1,5,2,1]
leader = List[len(List)-1]
# print leader
for i in range (len(List)-1,-1,-1):
	# print List[i]
	if (List[i]) > leader:
		leader = List[i]
	print leader
