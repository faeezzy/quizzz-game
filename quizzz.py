print("Welcome to my beauty quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play!")
score = 0

answer = input("What does the use of sunscreen help prevent? ")
if answer.lower() == "Sunburn":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Try again.")

answer = input("What does toner help with? ")
if answer.lower() == "Pores":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Try again.")

answer = input("What does the use of mask? ")
if answer.lower() == "Hydration":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Try again.")

answer = input("What does the facial wash help with? ")
if answer.lower() == "Cleansing":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Try again.")

answer = input("What is a ph balance? ")
if answer.lower() == "Neutral":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Try again.")

answer = input("What does moisturizer help with? ")
if answer.lower() == "Hydration":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Try again.")

answer = input("What does exfoliation remove from the skin? ")
if answer.lower() == "Dead cells":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Try again.")

answer = input("What does sunscreen protect your skin from? ")
if answer.lower() == "UV rays":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Try again.")

answer = input("What is the main benefit of using a facial serum? ")
if answer.lower() == "Nourishment":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Try again.")

answer = input("What does sunscreen protect your skin from? ")
if answer.lower() == "UV rays":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Try again.")

print("You got " + str(score) + " queations correct!")
print("You got " + str(score / 10 * 100) + '%')
