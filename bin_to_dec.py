# Luke Reissmueller
# CECS 229 - Programming Assignment 1
# 9/18/2020

# binary string to decimal function
def bin_to_dec(x):  # Returns decimal equivalent
    x = list(x)  # Convert binary string to list
    y = 0
    for i in range(len(x)):  # Cuts down list and checks whether bit is 1.
        if x.pop() == '1':  # If current bit is 1, compound assignment operator
            y += 2**i  # --adds to decimal conversion with a 2^index value.
    return y

print(bin_to_dec('10111'))  # Test, returns 23