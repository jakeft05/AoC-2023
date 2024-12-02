with open("input.txt", "r") as file:
  data = file.read()

list1 = []
list2 = []
similarity = 0

for line in data.split("\n"):
  list1.append(int(line.split("   ")[0]))
  list2.append(int(line.split("   ")[1]))

for i in list1:
  similarity += i*list2.count(i)

print(str(similarity))