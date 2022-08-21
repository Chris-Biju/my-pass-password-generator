import random

# list setup
letterLst = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
             "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

letterLstUpper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                  "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

specialCharacterLst = ["!", "@", "#", "$", "%", "^", "&",
                       "*", "(", ")", "-", "_", "/", "?", ".", "~", "`", ":", ";"]

numberLst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def passwordGeneration():
    # function setup
    password = ""
    num = 1
    # user input
    secureMode = input("Would you like to turn on secure mode (how many characters you want, upper and lowercase letters, special characters, and numbers.) or just answer all the questions? For secure mode just type Y otherwise type N  ")
    length = input(
        "How many characters would you like the password to be? Limit 49 characters. ")
    if secureMode == "N":
        cases = input(
            " Would you like to have both upper and lowercase letters? Y/N ")
        specialCharacters = input(
            "would you like to have special characters in your password Y/N ")
        numbers = input(
            "Would like numbers in your password Y/N "
        )
    else:
        # setting up the generator using user input
        specialCharacters = "Y"
        cases = "Y"
        numbers = "Y"

    if specialCharacters == "Y":
        num += 1
    if cases == "Y":
        num += 1
    if numbers == "Y":
        num += 1
    # generating the password
    for i in range(int(length)):
        character = random.randint(1, num)
        if character == 1:
            lowerLetter = random.randint(1, 26)
            password += letterLst[lowerLetter-1]
        elif character == 2:
            upperLetter = random.randint(0, 26)
            password += letterLstUpper[upperLetter-1]
        elif character == 3:
            symbols = random.randint(1, 19)
            password += specialCharacterLst[symbols]
        elif character == 4:
            nums = random.randint(0, 10)
    print(password)
    # RUNNING THE FUNCTION/mainloop


welcome = input("Welcome to MyPass password generator!, Press enter to begin")


while True:
    passwordGeneration()
    again = input(
        "If you want a new password click the enter key, if you want to quit press Q")
    if again == "Q":
        break
