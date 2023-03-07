#Written by Shiven Desai
#This program finds the sum of a given tuple

test_tup = (15, 20, 123, 47, 26, 81)

#Initialize variables
i = 0
sum = 0

#Iterate through the tuple using a while loop
while i < len(test_tup):
    # Add each element to the sum
    sum += test_tup[i]
    #Increment the index variable
    i += 1

#Print the sum
print("The sum of the tuple is:", sum)
