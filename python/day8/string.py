name = "jasii"
print(name)
print("length is ", len(name))
print("first character is ", name[0])
print("last character is ", name[-1])
print("upper case is ", name.upper())
print("lower case is ", name.lower())
print("first 3 characters are", name[:3])
print("last 3 characters are", name[-3:])
print("reversed string is", name[::-1])
c=0
for ch in name:
    if ch == 'i':
        c=c+1

print("number of i is ", c)
print('si' in name)
new = name.replace('i', 'e')
print(new)
