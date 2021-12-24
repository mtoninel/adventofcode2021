#!usr/bin/env python


# Import input file
with open('./depths.txt') as file:
    depths = file.readlines()

# Convert character list into int
depths = list(map(int, depths))
    
# PUZZLE 1
# Loop through and count
counter = 0
for i in range(1,len(depths)):
    curr_depth = depths[i]
    prev_depth = depths[i-1]
    if curr_depth > prev_depth:
        counter = counter + 1

print(counter)    

# PUZZLE 2
# Three-measurement sliding windows
window = 3
counter = 0
for i in range(len(depths)-window+1): # Stop on last possible window
    value = sum(depths[i:i+window])
    next_value = sum(depths[i+1:i+1+window]) # Both windows at once
    if next_value > value:
        counter = counter + 1

print(counter)
