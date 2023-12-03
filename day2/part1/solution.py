# The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

limits = {
    'red': 12,
    'green': 13,
    'blue': 14
}

f = open("/Users/kaito/Desktop/code/practice/advent-of-code/2023/day2/part1/inputs.txt", "r")

answer = 0

for i, line in enumerate(f.readlines()):
    currentGameId = i+1
    impossible = False
    transformedLine = line[line.find(':') + 2:]
    sets = transformedLine.split(';')
    for s in sets:
        for pick in s.strip().split(', '):
        
            number, color = pick.split(' ')
            if (int(number) > limits[color]):
                impossible = True
                break
        if(impossible):
            break

    if (not impossible):
        answer += currentGameId


print(answer)



    
