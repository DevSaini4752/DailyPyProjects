"""Here the taskremover() function will allow us
to remove a task from the task list (data.json)"""

#Importing Modules
import json
import colours as c

# Function
def tskrem(*tasks):
    try:
        with open("data.json", "r") as file_in:
            data = json.load(file_in)
            # Will remove the task given
            for task in tasks:
                del data[task]

        #Updating the data in data,json
        with open("data.json", "w") as file_out:
            json.dump(data, file_out, indent=4)

    # Just to don't raise error during an empty file
    except json.JSONDecodeError:
        msg = f"{c.red}No task in inventory!!!{c.end}"
        print(msg)
    # If no file is there
    except FileNotFoundError:
        msg = f"{c.red}No task in inventory!!!{c.end}"
        print(msg)
    # If a task does not exist
    except KeyError as er:
        msg = f"{c.red}{er} : Task not found!!! Recheck the name of the task{c.end}"
        print(msg)

if __name__ == "__main__":
    tskrem("Chy", "Doggo")