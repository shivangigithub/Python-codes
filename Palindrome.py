#Check if given string is palindrome or not
Str="ACTCAA"
Str2 = ""
count = (len(Str)/2)+1
for i in Str:
	Str1 = Str[0:count]
	break

for i in range(len(Str)-1,(len(Str)/2)-1,-1):
	Str2 = Str2+Str[i]
if (Str1 == Str2):
	print "It is a palindrome"
else:
	print "It is not a palindrome"