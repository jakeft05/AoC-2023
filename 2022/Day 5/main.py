import json

stacks={1:["W","R","F"],2:["T","H","M","C","D","V","W","P"],3:["P","M","Z","N","L"],4:["J","C","H","R"],5:["C","P","G","H","Q","T","B"],6:["G","C","W","L","F","Z"],7:["W","V","L","Q","Z","J","G","C"],8:["P","N","R","F","W","T","V","C"],9:["J","W","H","G","R","S","V"]}

#stacks={1:["Z","N"],2:["M","C","D"],3:["P"]}

with open("input.txt","r") as file:
  data=file.read()
data = data.replace("\n","")
lines = data.split("move ")
lines.pop(0)
for line in lines:
  count = int(line.split(" from ")[0])
  start = int(line.split(" from ")[1].split(" to ")[0])
  end = int((line.split(" from ")[1].split(" to ")[1]))
  for X in range(0,count):
    stacks[end].append(stacks[start][len(stacks[start])-1])
    stacks[start].pop(len(stacks[start])-1)
for i in stacks:
    print(stacks[i][len(stacks[i])-1])