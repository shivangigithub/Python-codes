#The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.
#Accessing Values in Tuples
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print "tup1[0]: ", tup1[0];
print "tup2[1:5]: ", tup2[1:5];
# tup1[2] = 5
# print tup1,"\n";

#Updating Tuples
#Tuples are immutable which means you cannot update or change the values of tuple elements.
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');
# Following action is not valid for tuples
# tup1[0] = 100;
# So let's create a new tuple as follows
tup3 = tup1 + tup2;
print tup3;

#Delete Tuple Elements; not possible
# tup = ('physics', 'chemistry', 1997, 2000);
# print tup;
# del tup;
# print "After deleting tup : ";
# print tup;

#Indexing, Slicing, and Matrixes
#Because tuples are sequences, indexing and slicing work the same way for tuples as they do for strings.

#Python tuple method cmp() compares elements of two tuples.
#cmp(tuple1, tuple2)
tuple1, tuple2 = (456, 'xyz'), (123, 'abc')
print "compare is " , cmp(tuple1, tuple2)
print cmp(tuple2, tuple1)
tuple3 = tuple2 + (786,);
print cmp(tuple2, tuple3)

#Python tuple method len() returns the number of elements in the tuple.
#len(tuple)
tuple1, tuple2 = (123, 'xyz', 'zara'), (456, 'abc')
print "First tuple length : ", len(tuple1)
print "Second tuple length : ", len(tuple2)

#Python tuple method max() returns the elements from the tuple with maximum value.
#max(tuple)
tuple1, tuple2 = (123000, 'xyz', 'zara', 'abc'), (456, 700, 200)
print "Max value element : ", max(tuple1)
print "Max value element : ", max(tuple2)

#Python tuple method min() returns the elements from the tuple with minimum value.
#min(tuple)
tuple1, tuple2 = (123000, 'xyz', 'zara', 'abc'), (456, 700, 200)
print "min value element : ", min(tuple1)
print "min value element : ", min(tuple2)

#Python tuple method tuple() converts a list of items into tuples
#tuple( seq )
aList = [123, 'xyz', 'zara', 'abc']
aTuple = tuple(aList)
print "Tuple elements : ", aTuple
listt = list (tup1)
print listt,"\n"
listt[1] = 5
print listt,"\n"
print tup1,"\n"



