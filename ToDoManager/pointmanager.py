"""The point manager will be used to manage points.
It will take  some arguments, and depending on the
argument, it will add or deduct points.

The point manager will take 2 args, one will be for
how  many  points to  be added or deducted and the
time will be taken by manager on itself through time
module. 2nd would be for what purpose was it deducted.."""

#importing module
import json
import datetime

# Function for the purpose
def point_manger(points, purpose):
    live_time = datetime.datetime.now()
    with open("data.json", "r") as file:
        data = json.load(file)
        data["total_points"] += points
        history = data["PoiHis"]
        history[f"{live_time}"] = [f"{points}", f"{purpose}"]

    with open("data.json", "w") as file:
        json.dump(data, file)

point_manger(2, "Initializing")
