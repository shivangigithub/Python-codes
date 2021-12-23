#Peak element
#An element is called a peak element if its value is not smaller than the value of its adjacent elements
List = [3,14,5,9,1]
Max = 0
for i in List:
	if i > Max:
		Max = i
print Max
