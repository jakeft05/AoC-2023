with open("input.txt", "r") as file:
  data = file.read().split("\n")

total = 0
dataPos = 0
for i in range(0,4):
  data.insert(0,"NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")
  data.append("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")
  
for line in data:
  data[dataPos] = "NNNNN" + line + "NNNNN"
  dataPos += 1

#print(data)
dataPos = 0

for line in data:
  linePos = 0
  print(line)
  for letter in line:
    if letter == "A":
      # RIGHT
      if line[linePos+1] == "M" and line[linePos+2] == "A" and line[linePos+3] == "S":
        total += 1
      # LEFT
      if line[linePos-1] == "M" and line[linePos-2] == "A" and line[linePos-3] == "S":
        total += 1
      # UP
      if data[dataPos-1][linePos] == "M" and data[dataPos-2][linePos] == "A" and data[dataPos-3][linePos] == "S":
        total += 1
      # DOWN
      if data[dataPos+1][linePos] == "M" and data[dataPos+2][linePos] == "A" and data[dataPos+3][linePos] == "S":
        total += 1
      # UP RIGHT
      if data[dataPos-1][linePos+1] == "M" and data[dataPos-2][linePos+2] == "A" and data[dataPos-3][linePos+3] == "S":
        total += 1
      # UP LEFT
      if data[dataPos-1][linePos-1] == "M" and data[dataPos-2][linePos-2] == "A" and data[dataPos-3][linePos-3] == "S":
        total += 1
      # DOWN RIGHT
      if data[dataPos+1][linePos+1] == "M" and data[dataPos+2][linePos+2] == "A" and data[dataPos+3][linePos+3] == "S":
        total += 1
      # DOWN LEFT
      if data[dataPos+1][linePos-1] == "M" and data[dataPos+2][linePos-2] == "A" and data[dataPos+3][linePos-3] == "S":
        total += 1
    linePos += 1
  dataPos += 1

print(str(total))