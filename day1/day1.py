
f = open("day1inputs.txt", "r")

numbers: dict = {
    'one': "1",
    'two': "2",
    'three': "3",
    'four': '4',
    'five': '5',
    'six':'6',
    'seven':'7',    
    'eight':'8',
    'nine':'9'
}

sum = 0

for line in f:
    numbers = []
    for char in line:
        if char.isnumeric():
            numbers.append(char) 
        else:
            numbers.append(char)
    sum += int(numbers[0]+numbers[-1])

print(sum)