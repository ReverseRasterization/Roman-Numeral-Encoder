#Import the os module
import os

#Roman numeral dictionary
romanNumerals = {
  "M" : 1000,
  "D" : 500,
  "C" : 100,
  "L" : 50,
  "X" : 10,
  "V" : 5,
  "I" : 1
}

#Function used to check if an integer is valid
def isValid(numbers):
  #Attempt to convert it to an int
  try:
    _ = int(numbers)
    return True
  except:
    return False

#Main loop
while True:
  #Ask the user for a number
  user_input = input("Please type a number:\n> ")

  #Data validation
  while not isValid(user_input):
    #Display invalid input
    print("\nINVALID INPUT, PLEASE TYPE A NUMBER")

    #Ask the user for a number
    user_input = input("\nPlease type a number:\n> ")

  #Convert the user input to an integer
  oldUser_input = int(user_input)
  user_input = oldUser_input
  
  #Setup variable for roman numeral iteration process
  result = ""

  #Iterate through the roman numerals
  for rn in romanNumerals:
    #Variable
    rnVal = romanNumerals[rn]

    #Get how many times the value of the roman numeral can go into the user input number
    repeatNum = user_input // rnVal

    #Check if the value of the roman numeral can go into the user input number
    if repeatNum > 0:
      #Get how much is left over
      user_input = user_input % rnVal

      #Add to the result
      result += rn*repeatNum

      #Make sure that user_input isnt 0
      if user_input == 0:
        break
  
  #Display result
  print(f"\n{str(oldUser_input)} converted into roman numerals is {result}")

  #Ask the user if they want to run the program again
  doAgain = input("\nWould you like to run the program again? (Y/N)\n> ").lower()

  #Data validation
  while doAgain != "y" and doAgain != "n":
    #Display invalid answer
    print("\nINVALID ANSWER")

    #Ask the user if they want to run the program again
    doAgain = input("\nWould you like to run the program again? (Y/N)\n> ").lower()

  #Check the users answer 
  if doAgain == "y":
    os.system('clear')
  else:
    print("\nGoodbye!")
    break
