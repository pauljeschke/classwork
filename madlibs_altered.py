counter = 0
prompt = ['a proper noun:', 'a verb:', 'a number:', 'a verb ending in -ing:', 'a plural noun:', 'a noun:', 'a verb ending in -ing:', 'an adjective:', 'an adjective:', 'a verb ending in -ing:', 'an adjective:', 'a verb:', 'a plural noun:']
response = []
print("\nHello! Welcome to Paul Jeschke's Madlib Extravaganza. You will provide responses to a series of prompts requesting verbs, nouns, and adjectives of varying specificity. Complete the prompts and enjoy an all-original madlib created by your very own Accounting Manager.\n")
# This while code provides the loop that populates our madlibs list of variables from user inputs
while counter < 13:
  print(f"#{str(counter + 1)} Provide {prompt[counter]}")
  response.append(input())
  counter += 1
print(f"\nRyan lost a bet with {response[0]}! Now he has to teach Arcadia employees how to {response[1]} in {response[2]} weeks. You have been selected as one of the lucky few to take Ryan's {response[3]} class. Do you have what it takes to succeed? Will you achieve the highest {response[4]}? Or will you be a rogue {response[5]}, ready to send this house of cards {response[6]} to the ground? You will encounter super  {response[7]} coffee, {response[8]} mornings, {response[9]} priorities, and {response[10]} ultraviolet computer monitor light. Whether you succeed or {response[11]}, and toward what goal, is all in your {response[12]}.")