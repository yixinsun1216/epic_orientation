for i in range(10):
	print(i)

j = 1
while j < 10:
	j+=1
	print(j)

greeting = "hello"
if "h" in greeting:
	print("hi")
elif "y" in greeting:
	print("ugh why")
else: 
	print("not a greeting")


list_object = ["hi", 2, True, greeting]

for j in range(len(list_object)):
	if type(list_object[j]) is int:
		list_object[j] = list_object[j]+10

print(list_object)


tupleobj = (1,2,3,4)
newlist = []
for j in range(len(tupleobj)):
	newlist.append(tupleobj[j]+10)

print(tuple(newlist))