#find pair of numbers with given sum using dict
List = [1,2,3,6,4,9,4,2,10,30,11,7]
givensum = 16
dict = {}
for i in range(0,len(List),1):
	dict[List[i]] = ""

for key in dict:
	find = givensum - key
	if find in dict.keys():
		print ("pairs are " , find, key)
