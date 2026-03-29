# 5. Match Case In Python

color = input("Enter color of Traffic Light: ")

match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Reday")
    case "green":
        print("Go")
    case _:
        print("Wrong color")