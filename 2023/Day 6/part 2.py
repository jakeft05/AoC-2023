with open("input.txt","r") as file:
  data = file.read()

methods=0
time = data.split("Time:")[1].split("\n")[0].replace(" ","")
distance = data.split("Distance:")[1].replace(" ","")

for i in range(0,int(time)):
  travelled = i * (int(time)-i)
  if travelled > int(distance):
    methods += 1

print(str(methods))
