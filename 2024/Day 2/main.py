with open("input.txt", "r") as file:
  data = file.read()

safeFloors = 0

for report in data.split("\n"):
  levels = report.split(" ")
  safe = True
  dampened = 0

  # Increasing
  if int(levels[0]) < int(levels[len(levels)-1]):
    previous = int(levels[0]) - 1
    prePrevious = int(levels[0]) - 2
    for level in levels:
      if int(level) <= previous + 3 and int(level) > previous and safe is True:
        prePrevious = previous
        previous = int(level)
      else:
        if int(level) <= prePrevious + 3 and int(level) > prePrevious and safe is True:
          dampened += 1
          prePrevious = previous
          previous = int(level)

  # Decreasing  
  elif int(levels[0]) > int(levels[len(levels)-1]):
    previous = int(levels[0]) + 1
    prePrevious = int(levels[0]) + 2
    for level in levels:
      if int(level) >= previous - 3 and int(level) < previous and safe is True:
        prePrevious = previous
        previous = int(level)
      else:
        if int(level) >= prePrevious - 3 and int(level) > prePrevious and safe is True:
          dampened += 1
          prePrevious = previous
          previous = int(level)

  else:
    safe = False

  if dampened > 1:
    safe = False
    
  if safe is True:
    safeFloors += 1

print(str(safeFloors))