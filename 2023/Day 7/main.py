with open("input.txt","r") as file:
  data = file.read()
data = data.split("\n")
map = data[0]

directions = {}
for line in data:
  if " = " in line:
    directions[line.split(" = ")[0]] = line.split("(")[1].split(")")[0].split(", ")

position = "AAA"
command = 0
count = 0

while position != "ZZZ":
  if command != len(map):
    if map[command] == "R":
      position = directions[position][1]
    elif map[command] == "L":
      position = directions[position][0]
    command += 1
    count += 1
  else:
    command = 0
    
print(str(count))