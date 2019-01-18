the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This first kine of for-loop goes through a loop
for number in the_count:
    print(f"This is count {number}")
    
# Same as above
for fruit in fruits:
    print(f"A type of fruites: {fruit}")

# Also, we can go through mixed lists too
# notice we have to use {} since we do not know what's in it
for i in change:
    print(f"I got {i}")

# We can also build lists, first starts with an empty one
elements = []

# Then use the range function to do the 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list")
    # append is a function that lists understand
    elements.append(i)

# elements = list(range(0, 6))

# Now, we can print them out
for i in elements:
    print(f"Element was: {i}")


