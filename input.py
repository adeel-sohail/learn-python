
#so here we are having a little problem we are getting an input but the input is always considered as string
a = input("Enter a number 1: ") # for example input is 2

b = input("Enter a number 2: ") # for example input is 3

Sum = a + b

print(Sum) # should be 5 but will print 23

# So now we will convert it to int

a = int(input("Enter a number 1: ")) # for example input is 2

b = int(input("Enter a number 2: "))

Sum = a + b

print(Sum)