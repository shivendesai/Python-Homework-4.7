#Written by Shiven Desai
#This program finds the largest number in a given tuple

test_tup = (15, 20, 123, 47, 26, 81)

#Initialize variable
largest_num = test_tup[0]

#Iterate through the tuple using a for loop
for num in test_tup:
    #Check if the current number is larger than the largest number so far
    if num > largest_num:
        #If it is, update the largest number
        largest_num = num

#Print the largest number
print("The largest number in the tuple is:", largest_num)
