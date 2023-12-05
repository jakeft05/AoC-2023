with open("input.txt","r") as file:
  data = file.read()
data = data.split("\n")

check=[]

count = 0

for line in data:
  data[data.index(line)] = ".."+line+".."

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
        if not line[startPos-1].isalnum() and line[startPos-1] != ".":
          part = True
        elif not line[endPos].isalnum() and line[endPos] != ".":
          part = True
        else:
          if data.index(line) != 0:
            for place in data[data.index(line)-1][startPos-1:endPos+1]:
              if not place.isalnum() and place != ".":
                part = True
          if data.index(line) != len(data)-1:
            for place in data[data.index(line)+1][startPos-1:endPos+1]:
              if not place.isalnum() and place != ".":
                part = True

        if part == True:
          count += int(accumulator)
        accumulator = ""
        part = False
        startPos = 0
        endPos = 0

print("Total: " + str(count))
