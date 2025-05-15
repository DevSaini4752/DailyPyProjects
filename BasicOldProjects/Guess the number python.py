print("The Guessing Game")
print("Lets Gooooooo!!!!!")
import random
num1 = random.randint(1,10)
num2 = random.randint(40,50)
numfinal = random.randint(num1,num2)
chance = 1
while chance <= 5:
  userinput = int(input("Guess the number between "+ str(num1) + " and " +  str(num2) + " :"))
  if userinput == numfinal: 
    print("The correct answer is:",numfinal, "You gussesd it correctly , wah bethe wah kya tukka tha")
    break
  else:
    print("Wrong answer, Try again")
    chance = chance + 1

print ("Thank You For choosing me, I hope you enjoyed the game.")
print("The number was: " + str(numfinal))