# Snake water gun
# 0 = snake
# 1 = water
# 2 = gun
# Possible result (computer - user)
#C = 0, U = 0 (Snake vs Snake)
#C = 1, U = 0 (Water vs Snake)
#C = 2, U = 0 (Gun vs Snake)

#C = 0, U = 1 (Snake vs Water)
#C = 1, U = 1 (Water vs Water)
#C = 2, U = 1 (Gun vs Water)

#C = 0, U = 2 (Snake vs Gun)
#C = 1, U = 2 (Water vs Gun)
#C = 2, U = 2 (Gun vs Gun)

# c-u=0 (draw)
# c-u=1(user wins)
# c-u=-1(computer wins)
# c-u=-2(user wins)
# c-u=2(computer wins)

import os
import random
from time import sleep as delay # Importing for user freindly ui
# Showing the rule
print("""0 = snake
1 = water
2 = gun""")
# Time for delay
a = 300/1000 
i = 0
result = 0
# Scores
scorec = 0
scoreu = 0
#creating options for computer
options = [0,1,2]
while True:
    try:
        #Asking user and computer for a no. 
        user = int(input("Kindly enter no. : "))
        delay(a)
        comp = random.choice(options)
        delay(a)
        #Giving all the conditions to work accordingly
        if user != 0 and user != 1 and user != 2:
            raise ValueError
            # raising error to tell user for a correct input
        elif (comp - user) == 0:
             delay(a)
             print("Ohhh ! Its a same")
             
        elif (comp-user)==1 or (comp-user)==-2:
             delay(a)
             print("Ohh ! A point goes to you")
             scoreu=scoreu+1
             result = result + 1
        elif (comp - user)==-1 or (comp-user)==2:
             delay(a)
             print("Ohh shit ! a point goes to computer")
             scorec=scorec+1
             result=result-1
        i=i+1
        if i == 3:
            print("So the game is over, lets see the result")
            delay(a)
            break
         
              
    except ValueError:
        delay(a)
        print("Kindly enter a no. according to above instruction")
   
# Printing the result     
if result == 0:
        delay(a)
        result_data = "It's a draw !"
        print("Ohh its a draw, I hope you enjoyed the game")
        
elif result > 0:
        delay(a)
        result_data = 'User won !'
        print("Yeah boy ! you won ")

elif result < 0:
        delay(a)
        result_data = 'Computer won !'
        print("What the hell ! bro, you lost")
        
print(f"""Computer : {scorec}
You : {scoreu}""")

# Saving data
data = open("snake_water_gun_record.txt","a")
import time
# Get the current date
current_date = time.strftime("%Y-%m-%d")
# Saving the result
data.write("\n")
data.write(f'''\nMatch -  {current_date}
Computer : {scorec}
User : {scoreu}
Result = {result_data}''')
data.close()
xyz = open("snake_water_gun_record.txt","r")
print(xyz.read())
xyz.close()