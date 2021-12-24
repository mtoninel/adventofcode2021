# PUZZLE 1
# Calculate submarine power consumption by multiplying gamma and epsilon rates extracted from input binaries. The idea is that since values are either 0 or 1, and we have to know which one is the most represented, the trick is to do the mean for each list and if it is more than 0.5 then there are more 1s. 

# When will we upload to py3?
from __future__ import division

# Read input
with open('./binary_input.txt') as file:
    binaries = file.readlines()

    gamma = []
    epsilon = []

    for i in range(len(binaries[0])-1): # -1 to avoid newline char!!

        count = 0

        for x in binaries: # Iterate trough length of list (rows)
            count = count +  int(x[i]) # keep count of total

        value = count/len(binaries)
        
        if value > 0.5:
            gamma.append('1')
            epsilon.append('0')

        else:
            gamma.append('0')
            epsilon.append('1')

# Collapse lists and convert binary to decimal with int()
gamma = int(''.join(gamma), 2)
epsilon = int(''.join(epsilon), 2)

power = gamma * epsilon

file.close()

print(power)


# PUZZLE 2
# Define a recursive strategy to calculate O2 and C02 ratings
# count bits
def bit_counter(array, index):
    zeroes, ones = 0, 0
    for line in array:
        if line[index] == "0":
            zeroes += 1
        if line[index] == "1":
            ones += 1
    return zeroes, ones

# functions to define which values are more or less represented per bit   
def most(zeroes, ones):
    if ones >= zeroes:
        return '1'
    else:
        return '0'

def least(zeroes, ones):
    if ones >= zeroes:
        return '0'
    else:
        return '1'

# main
def recursive_search(array, idx, mode):
    if len(array) == 1:
        return array[0] # stop at one
    else:
        zeroes, ones = bit_counter(array, idx)
        if mode == 'O2':
            col = most(zeroes, ones)
        elif mode == 'CO2':
            col = least(zeroes, ones)

        fresh_array = [] # empty array to append with new values based on idx
        for item in array:
            if item[idx] == col:
                fresh_array.append(item)
        idx += 1
        return recursive_search(fresh_array, idx, mode) # recursion

binaries = []
with open("./binary_input.txt", 'r+') as in_file:
    for line in in_file:
        binaries.append(line.strip('\n'))       

O2 = recursive_search(binaries, 0, 'O2')
CO2 = recursive_search(binaries, 0, 'CO2')

# Convert to decimal and multiply
print(int(O2, 2) * int(CO2, 2))
