#Written by Shiven Desai
#This program sorts a tuple by the total of the nested lists

input_tup = ([2, 20], [44, 1], [3, 13])

#Define a function to get the total of a sublist
def sublist_total(sublist):
    return sum(sublist)

#Use the sorted() function to sort the tuple by sublist total
sorted_tup = sorted(input_tup, key=sublist_total)

#Print the sorted tuple
print("The sorted tuple is:", sorted_tup)
