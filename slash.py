# Get two integers from the user
x = int(input())  # First integer
y = int(input())  # Second integer

# Perform integer division (floor division) of x by y and assign to x
# This effectively sets x to the largest whole number less than or equal to x/y
x = x // y

# Perform integer division (floor division) of y by x and assign to y
# Because x is now a fraction of its original value, this will always result in 0
# This is because y/x will be a very small fraction, which is truncated to 0 when using integer division
y = y // x

# Print the result
# Because of the above operation, this will always print 0
print(y)

