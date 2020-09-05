#List and its default method

list1=["Maths","English",2000,52]
print(list1)

#append
list1.append("Science")
print(list1)

#insert
list1.insert(1,5400)
print(list1)

#extend
list2=[5,9,25,"Hindi"]
list1.extend(list2)
print(list1)

#pop
list1.pop(6)
print(list1)

#sum
list3=[1,2,3,4,5,6]
print("Sum of list3= ",sum(list3))



#Dictionary and its default functions

Dict={1:'LetsUpgrade',2:'python',3:'Dhirendra',4:'Book'}
print(Dict)

#get()
print(Dict.get(1))

#pop()
pe=Dict.pop(2)
print("Value associated to popped key is: ",pe)
print(Dict)

#copy()
new=Dict.copy()
print("new: ",new)

#keys()
print("Keys of Dict are : ",Dict.keys())

#clear()
new.clear()
print("new: ",new)


#Sets and its default functions

set1={"Letsupgrade","python","book","jupyter"}
print(set1)

#add()
set1.add("Anaconda")
print(set1)

#intersection()
set2={"English","Maths","Anaconda","Science","Letsupgrade"}
print(set2)
i=set1.intersection(set2)
print("Intersection of set1 and set2 are :",i)

#remove()
set1.remove("book")
print(set1)

#union()
u=set1.union(set2)
print("union of set1 and set2 are :",u)

#update()
set1.update(set2)
print("After update Set1 elements are :",set1)


#Tuple and its Default methods

tup=(1,3,7,8,5,4,6,8,5)
print(tup)

#count()
co=tup.count(5)
print(co)

#index()
itp=tup.index(8)
print("index of 8 is ",itp)


#Strings and its default functions

string1="LetsUPgrade python Course BATCH7 python"
print(string1)

#split()
sp=string1.split()
print(sp)

#lower()
l=string1.lower()
print(l)

#count()
cn=string1.count("python")
print(cn)

#upper()
upr=string1.upper()
print(upr)

#isalnum()
string2="Lets123"
check=string2.isalnum()
print(check)