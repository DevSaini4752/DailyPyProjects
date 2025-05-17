"""Here we will make a function which will add a task to the list, and it will
be saved in  a JSON file in a "list" form and whenever needed, it will be used
accordingly"""

#Importing Modules
import json

# Function
# mtd -> Manage task and data
def mtd(**tasks):
    data = {}
    try:
        with open("data.json", "r") as file_op:
            data = json.load(file_op)

    # Just to don't raise error during an empty file
    except json.JSONDecodeError:
        pass
    except FileNotFoundError:
        pass

    #Keeping this out of the first try part because if
    # an exception is there in try  then it would  end
    # after  that  execution, and  this  operation  is
    # compulsory to be executed
    for tskkey, tskval in tasks.items():
        data[tskkey] = tskval


    with open("data.json", "w") as file_wr:
        json.dump(data, file_wr, indent=4)

if __name__ == "__main__":
    mtd(Jerry = "Software engineer", Shishipanda="Jee", )

