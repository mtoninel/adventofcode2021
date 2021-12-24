# PUZZLE 1
# Determine the submarine position
with open('./position_input.txt') as file:
    pos = file.readlines()

    # Iterate through file
    fdepth = 0
    fpos = 0

    for i in range(len(pos)):

        direction = pos[i].split(' ')[0]
        value = int(pos[i].split(' ')[1])

        if direction == 'forward':
            fpos = fpos + value
        elif direction == 'up':
            fdepth = fdepth - value
        elif direction == 'down':
            fdepth = fdepth + value
            
print(fdepth * fpos)

# PUZZLE 2
# Insert aim, which is based on up or down
with open('./position_input.txt') as file:
    pos = file.readlines()
    
    fdepth = 0
    fpos = 0
    aim = 0

    for i in range(len(pos)):

        direction = pos[i].split(' ')[0]
        value = int(pos[i].split(' ')[1])

        if direction == 'up':
            aim = aim - value
        elif direction == 'down':
            aim = aim + value
        elif direction == 'forward':
            fpos = fpos + value
            fdepth = fdepth + (aim * value)

print(fdepth * fpos)
