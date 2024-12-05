with open("input.txt", "r") as file:
  data = file.read()

result = 0
active = True

for line in data.split("\n"):
  for section in line.split("mul("):
    if active:
      subsection = section.split(")")[0]
      numbers = subsection.split(",")
      if len(numbers) == 2 and numbers[0].isnumeric() and numbers[1].isnumeric():
        result += (int(numbers[0])*int(numbers[1]))
    if "do()" in section:
      active = True
    if "don't()" in section:
      active = False

print(str(result))
    