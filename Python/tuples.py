# Date:27/08/2024
# tuples
# packing
# unpacking
# edit tuples
# add two tuples
# loop in tuples

# Tuples:
# ordered list,
# unchangeable
# duplicate value allowed

# packing
name=('Ravi','ram','rahul')
print(type(name))
# single value tuple
name=('ram')
name1=('ram',)
print('name : ',type(name),'name1 : ',type(name1))

# packing
name=('Ravi','ram','rahul')
print(name)
# unpacking
(a,b,c)=name
print(a)
print(b)
print(c)

print('\n ***** edit tuples\n')
name=('Ravi','ram','rahul')
print('before edit : ',name)
name1=list(name)
name1[0]='aditya'
name=tuple(name1)
print('after edit : ', name)

print('\n ***** add two tuples\n')
name=('ravi','ram','rahul')
name1=('aditya','sumit')
name2=name+name1
print(name2)


print('\n ***** using loop print value\n')
for x in name2:
    print(x)

print('\n **** using loop print only index\n')
for i in range(len(name)):
    print(i)