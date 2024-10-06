name = 'Adeel'

name1 = 'adeel sohail'
print (name)

print (len(name))

print(name[0:])

print(name[1:])

print(name[-1:]) #reverse slices index always start with -1 instead of 0 start point

print(name[-10000:]) #what if wrong index is given

print(name[:9888]) #what if wrong index is given

print(name[555555:9885888888]) #what if wrong index is given . Nothing will be printed

print(name1.capitalize()) #Capitilising only first character

print(name1.startswith('a'))