#Traffic Light System

color=input("enter the traffic color (red/yellow/green):").lower()

match color:
    case "red":
        print("stop the vehicle")
    case "yellow":
        print("start the vehicle")
    case "green":
        print("go to best ride")
    case _:
        print("default")
