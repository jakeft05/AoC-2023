with open("input.txt", "r") as file:
  data = file.read()

safeFloors = 0

for report in data.split("\n"):
  levels = report.split(" ")
  safe = True

  # Increasing
  if int(levels[0]) < int(levels[1]):
    previous = int(levels[0]) - 1
    for level in levels:
      if int(level) <= previous + 3 and int(level) > previous and safe is True:
        previous = int(level)
      else:
        safe = False

  # Decreasing  
  elif int(levels[0]) > int(levels[1]):
    previous = int(levels[0]) + 1
    for level in levels:
      if int(level) >= previous - 3 and int(level) < previous and safe is True:
        previous = int(level)
      else:
        safe = False

  else:
    safe = False

  if safe is True:
    safeFloors += 1

print(str(safeFloors))