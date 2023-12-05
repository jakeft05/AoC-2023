with open("input.txt","r") as file:
  data = file.read()
data = data.split("\n")
games = {}
count = 0

for game in data:
  gameID = str(game.split(":")[0].split("Game ")[1])
  games[gameID] = {"commands":[],"minimums":{"blue":0,"green":0,"red":0}}
  games[gameID]["commands"] = game.split(":")[1].split(";")
  for command in games[gameID]["commands"]:
    for colour in games[gameID]["minimums"]:
      if colour in command:
        rawCommand = command.split(" "+colour)[0].split(" ")
        number = rawCommand[len(rawCommand)-1]
        if int(number) > games[gameID]["minimums"][colour]:
          games[gameID]["minimums"][colour] = int(number)
  count += int(games[gameID]["minimums"]["blue"]*games[gameID]["minimums"]["green"]*games[gameID]["minimums"]["red"])
print(str(count))