#Substring
x="This is a longass string and we can choose to extract the substrings from this"
sub1= x[0:10]
sub2= x[10:20]
sub3= x[20:31]
sub4= x[31:44]
sub5= x[44:56]
sub6= x[56:79]
print(sub1+sub2+sub3+sub4+sub5+sub6)

#Calculate the length
x="calculate the length of the string"
y= len(x)
print (y)

#Splitting
x="This,String@needs,to,be,splitted"
y=x.split("@")
print(y)

#Joining
a=['String','is','joined']
b=",".join(a)
print(b)
