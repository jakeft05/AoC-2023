with open("input.txt","r") as file:
  data = file.read()

methods=[]
times = data.split("Time:")[1].split("\n")[0].split(" ")

while "" in times:
  times.remove("")
distances = data.split("Distance:")[1].split(" ")
while "" in distances:
  distances.remove("")

for race, time in enumerate(times):
  methods.append(0)
  for i in range(0,int(time)):
    travelled = i * (int(time)-i)
    if travelled > int(distances[race]):
      methods[race] += 1

count = 1
for method in methods:
  count = count * method

print(str(count))
    