#Written by Shiven Desai
#This program finds the sum of all integer numbers in a given tuple

test_tup = ([17, 28], [93, 11], [20, 17])

#Initialize variable
sum = 0

#Iterate through the nested tuple using nested loops
for sublist in test_tup:
    for num in sublist:
        #Check if the current element is an integer
        if isinstance(num, int):
            #If it is, add it to the sum
            sum += num

#Print the sum
print("The sum of all integer numbers in the tuple is:", sum)
