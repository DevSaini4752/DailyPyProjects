import sys
def table(n):
    for i in range(1, 11):  # Start from 1 instead of 0
        print(n, "x", i, "=", int(n) * i)  # Adjust the calculation accordingly


name = input("Enter your name: ")
print("\n")
print("note: Kindly enter number/integer as your age other wise later it will give error")
print("\n")
age = input("Hi " + name + " Enter your age: ")
print("\n")
print("a. Green")
print("b. Blue")
print("c. Red")
print("d. Yellow")
print("e. Purple")
print("\n")
color = input(name + " Kindly choose your favorite color option: ")
print("\n")
while True :
    if color == "a":
      print("\n")
      print("Hmmm 🤔🤔🤔, I think you are a nature lover")
      break 
    elif color == "b":
      print("\n")
      print("Hmmm 🤔🤔🤔, I think you are calm, peaceful and trust worthy person")
      break 
    elif color == "c":
      print("\n")
      print("Hmmm 🤔🤔🤔, I guess, you are person who is very passionate and loves to work hard")
      break
    elif color == "d":
      print("\n")
      print("Hmmm 🤔🤔🤔, Likly you are very creative and a good communicator")
      break
    elif color == "e":
      print("\n")
      print("Hmmm 🤔🤔🤔, I think you are a very different kind of person, who is difficult to understand")
      break
    else:
      print("\n")
      print("Invalid option, please choose from the options given above")
      color = input(name + " Kindly choose your favorite color option: ")
print("\n")
print("\n")
print("a. I want to know about myself")
print("b. I want to play some games")
print("c. I want gain some knowledge")
print ("d. I want to use calculator") 
print("\n")
request = input("How can I help you " + name + " ?, please choose from the options given above : ")
print("\n")
while True:
  if request == "a":
    print("\n")
    realage = int(age)
    print("a. Know whether you can drive or not")
    print("b. Know are you capable of voting")
    print("c. Want to know your lucky number ")
    print("d. exit")
    print("\n")
    requesta = input("Okay!, So what do you want to know about yourself ?, please choose the option : ")
    while True:
      if requesta == "a":
        if realage >= 18:
          print("\n")
          print("You can drive")
          break
        else:
          print("\n")
          print("You cannot drive")
          break
      elif requesta == "b":
        if realage >= 18:
          print("\n")
          print("You can vote")
        else:
          print("\n")
          print("You cannot vote")
          break
      elif requesta == "c":
        print("\n")
        import random
        luckynumber = random.randint(1,1000)
        print("Your lucky number is " + str(luckynumber))
        break
      elif requesta == "d":
        print("\n")
        print("Okay, Thank you for using me")
        sys.exit()
  
      else:
        print("\n")
        requesta == input("Kindly put a valid option :")
    
  elif request == "b":
    print("\n")
    print("Ohh, I have some games for you")
    print("\n")
    print("a. Guess the number")
    print("b. Mental ability questions ")
    print("c. exit")
    requestb = input("Which game do you want to play? :")
    print("\n")
    if requestb == "a":
      print("\n")
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
          print("\n")
          print("The correct answer is:",numfinal, "You gussesd it correctly ")
          break
        elif chance == 3:
          print("\n")
          print("You have only two chance left")
        else:
          print("\n")
          print("Wrong answer, Try again")
          chance = chance + 1

      print ("Thank You For choosing me, I hope you enjoyed the game.")
      print("The number was: " + str(numfinal))
      

    elif requestb == "b":
      mat = """Mental Ability Questions - 
      1. A man starts walking north and covers a distance of 5 km. Then he turns to his right and walks 3 km. Finally, he turns to his right again and walks 5 km. How far is he from his starting point?


2. If 4 cats can catch 4 mice in 4 minutes, how many cats are needed to catch 100 mice in 100 minutes?


3. A clock shows the time as 3:15. What is the angle between the hour hand and the minute hand?






---

Answers:

1. 3 km.


2. 4 cats.


3. 7.5 degrees."""
      
      print("\n")
      print(mat)
      break
    elif requestb == "c":
      print("\n")
      print("Okay, Thank you for using me")
      sys.exit()
    else:
      print("\n")
      requestb = input("Kindly put a valid option :")

  
    
  elif request == "c":
    print("\n")
    print("Oh oh oh, So it's study time guys")
    print("\n")
    print("a. Science")
    print("b. History")
    print("c. Maths")
    print("d. exit")
    print("\n")
    learning = input("So, what do you want to learn?, Choose from following options :")
    print("\n")
    while True :
      if learning == "a":
        print("\n")
        print("a. Science facts")
        print("b. Science Theories")
        print("c. exit")
        print("\n")
        sciencelearn = input("So, what do you want to learn about science?, Choose from following options :")
        print("\n")
        while True:
          if sciencelearn == "a":
            print("""Science Facts -
              1. The gender of the turtles in the sea are determined by the temperature, thats why due to global warming their sex ratio is disbalancing.
            2. You can know about your health condition by your snot color
            3. Our immune system has world largest library
            4. Your eyes don't get spectacles due to screen""")
          elif sciencelearn == "b":
            print("\n")
            print("Ohh, so you have intrest complex topics.")
            print("\n")
            print("a. Theory of simulation")
            print("b. Theory of relativity")
            print("c. exit")
            print("\n")
            theory = input("Kindly write the option you want to learn about : ")
          
          
            if theory == "a":
              print("\n")
              print("""Simulation theory tells that every thing in the universe
              is simulated by computer, and we are the players of it. Ultimatly
              it tells that actually we all are simulated by someone else.""")
              break
            elif theory == "b":
              print("\n")
              print("""The theory of relativity usually encompasses two interrelated
            physics theories by Albert Einstein: special relativity and general
            relativity, proposed and published in 1905 and 1915, respectively. Special
            relativity applies to all physical phenomena in the absence of gravity""")
            elif theory == "c":
              print("\n")
              print("Okay, Thank you for using me")
              sys.exit()
              
            else:
              print("\n")
              theory = input("Kindly write the option you want to learn about : ")
              
          elif sciencelearn == "c":
              print("\n")
              print("Okay, Thank you for using me")
              sys.exit()  
            
          else:
              print("\n")
              print("Kindly choose a valid option")
              theory = input("Kindly write the option you want to learn about")
            
      elif learning == "b":
        print("\n")
        print("a. Know about WW2")
        print("b. Know about cold war between USA and USSR")
        print("c. exit")
    
        print("\n")
        learnhistory = input("So, what do you want to learn about history?, Choose from following options :") 
        print("\n")
        while True:
          if learnhistory == "a":
            print("\n")
            print("""World War II or the Second World War, often abbreviated as WWII or WW2, was a global war that lasted from 1939 to 1945. It involved the vast majority of the world's countries—including all of the great powers—forming two opposing military alliances: the Allies and the Axis powers.""")
          elif learnhistory == "b":
            print("\n")
            print("""The Cold War was a global conflict that took place between 1947 and 1991, during which the United States and the Soviet Union (USSR) clashed on the one hand and the European Union and the United Kingdom on the other. The Cold War was the deadliest conflict in history, with more than 100 million people killed and more than 16 million injured.""")
          elif learnhistory == "c":
            print("\n")
            print("Okay, Thank you for using me")
            sys.exit()
          
          else:
            print("\n")
            print("Kindly choose a valid option")
            learnhistory = input("So, what do you want to learn about history?, Choose from following options :")
      elif learning == "c":
        print("\n")
        print("Oh oh oh!, its maths time")
        print("\n")
        print("a. Tables")
        print("b. exit")
        print("\n")
        learnmaths = input("So, what do you want to learn about maths?, Choose from following options :")
        print("\n")
        while True:
          if learnmaths == "a":
            xyz = input("Which number table do you want to learn :")
            table(xyz)
          elif learnmaths == "b":
            print("\n")
            print("Okay, Thank you for using me")
            sys.exit()
          else:
            print("\n")
            print("Kindly choose a valid option")
            learnmaths = input("So, what do you want to learn about maths?, Choose from following options :")
      elif learning == "d":
        print("\n")
        print("Okay, Thank you for using me")
        sys.exit()
  elif request == "d":
    print("\n")
    print("So here is your calculator")
    print("\n")
    no_1 = input("Enter your first number :")
    no_2 = input("Enter your second number :")
    print("\n")
    print("a. Addition")
    print("b. Subtraction")
    print("c. Multiplication")
    print("d. Division")
    print("e. exit")
    print("\n")
    operation = input("Kindly choose the operation you want to perform :")
    print("\n")
    while True:
      if operation == "a":
        print("\n")
        print("The sum of the two numbers is :",int(no_1) + int(no_2))
        break
      elif operation == "b":
        print("\n")
        print("The difference of the two numbers is :",int(no_1) - int(no_2))
        break 
      elif operation == "c":
        print("\n")
        print("The product of the two numbers is :",int(no_1) * int(no_2))
        break
      elif operation == "d":
        print("\n")
        print("The quotient of the two numbers is :",int(no_1) / int(no_2))
        break
      elif operation == "e":
        print("\n")
        print("Okay, Thank you for using me")
        sys.exit()
      else:
        print("\n")
        print("Kindly choose a valid option")
        operation = input("Kindly choose the operation you want to perform :")
                                                                       
  else:
    print("\n")
    print("Invalid option, please choose from the options given above")
    print("\n")
    request = input("How can I help you " + name + " ?, please choose from the options given above : ")