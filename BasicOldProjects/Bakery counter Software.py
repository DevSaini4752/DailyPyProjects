#Key Requirements:
#1. Input daily stock updates.
#2. Check current stock levels.
#3. Alert when stock is below the minimum threshold.
#4. Allow for manual stock adjustment.


#Client Scenario:

#Client: A small bakery owner

#Problem: The bakery wants a simple inventory management system to track the daily stock of ingredients. The owner wants to ensure that they don't run out of essential ingredients and receive alerts when stocks are low.

#Details:
#The bakery uses ingredients like flour, sugar, eggs, and butter.
#Each ingredient has a minimum threshold. If stock falls below this threshold, the system should alert the owner.
#The owner wants to add new stock daily and see the current inventory.
#The system should allow checking the stock of any ingredient and updating quantities after daily usage.
#A simple text-based interface is sufficient.
#Key Requirements:
#1. Input daily stock updates.
#2. Check current stock levels.
#3. Alert when stock is below the minimum threshold.
#4. Allow for manual stock adjustment.
#Your task is to develop a program that meets these requirements.

def additem(item,quantity,date,price):
    n = [item]
    items.append(n)
    quan = {item:quantity}
    itemquantity.update(quan)
    dt = {item:date}
    itemdate.update(dt)
    pri = {item:price}
    itemprice.update(pri)
    
def changequantity(key,changedquantity):
    itemquantity[key] = changedquantity
    
def changeprice(key, newprice):
    itemprice[key] = newprice
    
def changedate(key, newdate):
    itemdate[key] = newdate
items = ["Donut", "Bread", "Milk", "Cream"]

while True:
    try:
        print("\n")
        donutq = int(input("kindly put the quantity of donut : "))
        breadq = int(input("Kindly put the quatnity of bread : "))
        milkq = int(input("Kindly put the quatity of milk in litre : "))
        creamq = int(input("Kindly put the quatity of cream in litre : "))
        break
    
    except:
          print("Kindy put integers in the place of quantity")

    
itemquantity = { 
"Donut" : donutq,
"Bread" : breadq,
"Milk" : milkq,
"Cream" : creamq 
}




while True:
    try:
        print("\n")
        donutd = (input("kindly put the date of order of donut (dd/mm/yyyy) : "))
        breadd = (input("Kindly put the date of orde of bread (dd/mm/yyyy) : "))
        milkd = (input("Kindly put the date of order of milk (dd/mm/yyyy) : "))
        creamd = (input("Kindly put the date of order of cream (dd/mm/yyyy) : "))
        break
    
    except:
          print("Error, Try again")

    
itemdate = { 
"Donut" : donutd,
"Bread" : breadd,
"Milk" : milkd,
"Cream" : creamd 
}


while True:
    try:
        print("\n")
        donutp = int(input("kindly put the price of donut : "))
        breadp = int(input("Kindly put the price of bread : "))
        milkp = int(input("Kindly put the price of milk : "))
        creamp = int(input("Kindly put the price of cream : "))
        break
    
    except:
          print("Kindy put integers in the place of quantity")

    
itemprice = { 
"Donut" : donutp,
"Bread" : breadp,
"Milk" : milkp,
"Cream" : creamp 
}

while True:
    try:
        print("a. Update list")
        print("b. Start sale")
        
        
        request = input("So what do you want to do : ")
        if request == "a" :
            print("a. add item")
            print("b. change date")
            print("c. change price")
            print("d. change quantity")
            request2 = input("kindly choose the option : ")
            if request2 == "a":
                a = input("Kindly enter item name : ")
                b = input("Kindly enter item quatity : ")
                c = input("Kindly enter item date of order : ")
                d = input("Kindly enter item price : ")
                additem(a,b,c,d)
                print("The list of items is : ", items)
                print("Item's quantity : ", itemquantity)
                print("Item's date", itemdate)
                print("Item's price",itemprice)
                
            elif request2 == "b":
                quan3 = input("Of which item do you want to change date of order : ")
                quan4 = input("What should be the new order of date : ")
                changedate(quan3,quan4)
                print("Updated list : ", itemdate)
                
            elif request2 == "c":
                quan2 = input("Of which item do you want to update price : ")
                quan3 = input("What should be the new price : ")
                changeprice(quan2, quan3)
                print(itemprice)
                
            
            elif request2 == "d":
                quan0 = input("Of which item\'s quantity do you want to change : ")
                quan1 = input("What should be the new quantity : ")
                changequantity(quan0,quan1)
                print("This is the new data : ", itemquantity)
                
        elif request == "b":
            do = int(itemquantity["Donut"])
            br = int(itemquantity["Bread"])
            mi = int(itemquantity["Milk"])
            cr = int(itemquantity["Cream"])
            no_0 = (do + br + mi + cr)
            for x in range(no_0):
                print("Order", x)
                no_001 = input("Enter the Item name (write quit if want to leave) : ")
                no_002 = input("Enter the item quantity : ")
                if no_001 == "quit":
                    no_0 = 0
                    break
                changequantity(no_001, (int(itemquantity[no_001]) - (int(no_002))))
                print(f"{no_001} left : {itemquantity[no_001]}") 
                if (int(itemquantity[no_001]) <= 10):
                       print(f"{no_001} is in less amount {itemquantity[no_001]}")
                
            
    except ValueError:
            print("Kindly dont put invalid input")
        
