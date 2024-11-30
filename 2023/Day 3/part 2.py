with open("input.txt","r") as file:
  data = file.read()
data = data.split("\n")

count = 0
cogs = {}

for line in data:
  data[data.index(line)] = ".."+line+".."
  cogs[".."+line+".."] = {}

for line in data:
  accumulator = ""
  part = False
  startPos = 0
  endPos = 0
  position = -1
  
  for character in line:
    position += 1
    if character.isnumeric():
      if accumulator == "":
        accumulator = character
        startPos = position
      else:
        accumulator = accumulator + character
    elif accumulator != ".":
      if accumulator != "":
        endPos = position
        if line[startPos-1] == "*":
          if startPos-1 not in cogs[line]:
            cogs[line][startPos-1] = [accumulator]
          else:
            cogs[line][startPos-1].append(accumulator)
        elif line[endPos] == "*":
          if endPos not in cogs[line]:
            cogs[line][endPos] = [accumulator]
          else:
            cogs[line][endPos].append(accumulator)
        else:
          if data.index(line) != 0:
            for i, place in enumerate(data[data.index(line)-1][startPos-1:endPos+1]):
              if place == "*":
                if i not in cogs[data[data.index(line)-1]]:
                  cogs[data[data.index(line)-1]][i] = [accumulator]
                else:
                  cogs[data[data.index(line)-1]][i].append(accumulator)
          if data.index(line) != len(data)-1:
            for i, place in enumerate(data[data.index(line)+1][startPos-1:endPos+1]):
              if place == "*":
                if i not in cogs[data[data.index(line)+1]]:
                  cogs[data[data.index(line)+1]][i] = [accumulator]
                else:
                  cogs[data[data.index(line)+1]][i].append(accumulator)

        accumulator = ""
        part = False
        startPos = 0
        endPos = 0

for cog in cogs:
  for gear in cogs[cog]:
    gearRatio=1
    if len(cogs[cog][gear]) == 2:
      count += int(cogs[cog][gear][0]) * int(cogs[cog][gear][1])
    
print("Total: " + str(count))
            