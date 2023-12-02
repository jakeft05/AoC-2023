with open("input.txt","r") as file:
  data = file.read()
data = data.split("\n")

sum = 0
words = {
  "one":{"no.":"1","cache":""},
  "two":{"no.":"2","cache":""},
  "three":{"no.":"3","cache":""},
  "four":{"no.":"4","cache":""},
  "five":{"no.":"5","cache":""},
  "six":{"no.":"6","cache":""},
  "seven":{"no.":"7","cache":""},
  "eight":{"no.":"8","cache":""},
  "nine":{"no.":"9","cache":""}
}

for line in data:
  numbers = []
  cache = ""
  for character in line:
    
    if character.isnumeric():
      numbers.append(character)
      cache = ""
      
    else:
      valid = False
      for word in words:

        if (cache + character) == word[0:len(cache)+1]:
          if (cache + character) == word:
            numbers.append(words[word]["no."])
            cache = character
          elif word[len(cache)] == character:
            cache = cache + character
          valid = True
      if valid == False:
        if cache != "":
          for word in words:
            if cache[len(cache)-1] == word[0] and character == word[1]:
              cache = cache[len(cache)-1] + character
              valid = True
        if valid == False:
          cache = character

  value = numbers[0] + numbers[len(numbers)-1]
  sum += int(value)
print("\nTotal: " + str(sum))