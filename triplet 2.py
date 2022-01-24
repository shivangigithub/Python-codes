##triplet.py
# Given an array arr of size n and an integer X. 
# Find if there's a triplet in the array which sums up to the 
# given integer X.
List = [1,3,45,6,10,8,2,4]
givensum = 13
dict = {}
for i in range(0,len(List),1):
	dict[List[i]] = ""
	# print (dict)

# for i in range(0,len(List)-1,1):
for i in range(0,len(List),1):
	for j in range(i+1,len(List),1):
		Sum = List[i] + List[j]
		# print	(Sum)
		find = givensum - Sum
		# print ("find is " , find)
		if find in dict.keys() and find != List[j] and find != List[i]:
			print ("triplet is " , find,List[i],List[j])