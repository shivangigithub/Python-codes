##swapping variable with and without using temp variable
var1 = "Tom"
var2 = "Jerry"
print ("Original " , var1, var2)

temp = var1
var1 = var2
var2 = temp

print ("After swapping " , var1, var2)

var1, var2 = (var2 , var1)
print ("After swapping " , var1, var2)
##without using temp variable
a = 5
b = 4
a = a + b ##9
b = a - b ##5
a = a - b ##4
print ("After swapping " , a, b)
