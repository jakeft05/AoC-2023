with open("input.txt","r") as file:
  input = file.read()
rawData = input.split("\n")
data = {}
for line in rawData:
  data[line] = 1

count = 0

for position, line in enumerate(data):
  reward = 0
  winNo = line.split(" | ")[0].split(": ")[1].split(" ")
  myNo = line.split(" | ")[1].split(" ")
  for number in myNo:
    if number.isnumeric() and number in winNo:
      reward += 1
  for i in range(0, data[line]):
    for i in range(1,1+reward):
      data[rawData[position+i]] += 1

for line in data:
  count += data[line]

print("Total: " + str(count))