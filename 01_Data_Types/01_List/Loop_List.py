# Loop through a list using a for loop- it Print all items in the list, one by one
mylist = ["apple", "banana", "kiwi", "grapes"]
for x in mylist:
    print(x)        # Ooutput:  apple
                    #           banana
                    #           kiwi
                    #           grapes

# Loop through list using index numbers- example below is [0, 1, 2].
# Use the range() and len() functions to create a suitable iterable.
mylist = ["apple", "banana", "kiwi", "grapes"]
for i in range(len(mylist)) :
    print(mylist[i])        # Ooutput:  apple
                            #           banana
                            #           kiwi
                            #           grapes

# Loop through a list using a while loop. Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.
# Remember to increase the index by 1 after each iteration.
mylist = ["apple", "banana", "kiwi"]
i = 0
while i < len(mylist) :
    print(mylist[i])
    i += 1                  # Ooutput:  apple
                            #           banana
                            #           kiwi

# Loop through a list using list comprehension
mylist = ["apple", "banana", "kiwi"]
[print(x) for x in mylist]      # Ooutput:  apple
                                #           banana
                                #           kiwi