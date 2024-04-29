def listLength(playerPosition):
    if playerPosition == "Striker":
        return len(strikerArr)
    elif playerPosition == "Midfielder":
        return len(midfielderArr)
    elif playerPosition == "Defender":
        return len(defenderArr)
    elif playerPosition == "Goalkeeper":
        return len(goalkeeperArr)

def appendPlayersList(playerName, playerPosition):
    new_row = []
    listLengthnew = listLength(playerPosition) - 1
    for x in range(listLengthnew):
        if playerPosition == "Striker":
            floatie = input("Enter the Player's " + strikerArrNaming[x] + ", separated by commas, no spaces.")
            new_row.append(floatie)
        elif playerPosition == "Midfielder":
            floatie = input("Enter the Player's " + midfielderArrNaming[x] + ", separated by commas, no spaces.")
            new_row.append(floatie)
        elif playerPosition == "Defender":
            floatie = input("Enter the Player's " + defenderArrNaming[x] + ", separated by commas, no spaces.")
            new_row.append(floatie)
        elif playerPosition == "Goalkeeper":
            floatie = input("Enter the Player's " + goalkeeperArrNaming[x] + ", separated by commas, no spaces.")
            new_row.append(floatie)
    new_row.insert(0, playerPosition)
    new_row.insert(0, playerName)
    print(new_row)
    data_list.append(new_row)
    saveList(file_path, data_list)
    print("Player data saved!")

def playerRemove(playerName, playerPosition):
    try:
        with open(file_path, 'r') as file:
            line_number = 0
            for line in file:
                line_number += 1
                parts = line.strip().split(',')
                if parts[0] == playerName and parts[1] == playerPosition:
                    return line_number - 1
    except Exception as e:
        print(f"An error occurred: {e}")
    return -1

def positionFinder(playerPostion):
    playerPosition = str(playerPostion)
    print(playerPosition)
    if playerPosition == "a":
        return "Striker"
    elif playerPosition == "b":
        return "Midfielder"
    elif playerPosition == "c":
        return "Defender"
    elif playerPosition == "d":
        return "Goalkeeper"
    else:
        return "None"

def readList(file_path):
    with open(file_path, 'r') as file:
        return [line.strip().split(',') for line in file]


def saveList(file_path, data_list):
    with open(file_path, 'w') as file:
        for row in data_list:
            file.write(','.join(map(str, row)) + '\n')


def editList(file_path):
    data_list = readList(file_path)

    print("Current list:")
    for row_idx, row in enumerate(data_list, start=1):
        print(f"{row_idx}. {row}")

    while True:
        action = input("\nEnter 'a' to add a row, 'r' to remove a row, 'q' to quit: ").lower()

        if action == 'a':
            new_row = input("Enter the new row (name, value1, value2, value3): ").split(',')
            data_list.append(new_row)
        elif action == 'r':
            row_to_remove = int(input("Enter the index of the row to remove: ")) - 1
            if 0 <= row_to_remove < len(data_list):
                del data_list[row_to_remove]
            else:
                print("Invalid index.")
        elif action == 'q':
            saveList(file_path, data_list)
            print("List saved. Exiting.")
            break
        else:
            print("Invalid action. Please try again.")

file_path = "Data.txt"
data_list = readList(file_path)
strikerArr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
midfielderArr = [0, 0, 0, 0, 0, 0, 0, 0, 0]
defenderArr = [0, 0, 0, 0, 0, 0, 0]
goalkeeperArr = [0, 0, 0, 0, 0, 0, 0]
strikerArrNaming = ["Goals Scored", "Shots On Target", "Shot Accuracy", "Conversion Rate", "Assists", "Chances Created", "Dribbles Completed", "Duels Won", "Distance Covered", "Offsides"]
midfielderArrNaming = ["Pass Acc", "Assists", "Tackles Won", "Interceptions", "Duels Won", "Distance Covered", "Dribbles Completed", "Shots Taken", "Offsides"]
defenderArrNaming = ["Tackles Won", "Interceptions", "Clearances", "Blocks", "Passing Accuracy", "Distance Covered", "Offsides"]
goalkeeperArrNaming = ["Save Percentage", "Clean Sheets", "Goals Conceded", "Distribution Accuracy", "Crosses Claimed", "Penalty Saves", "Errors Leading To Goal"]
strikerArrWeighting =  [0.25, 0.25, 0.15, 0.1, 0.1, 0.1, 0.05, 0.05, 0.05, -0.1]
midfielderArrWeighting =  [0.15, 0.3, 0.1, 0.1, 0.05, 0.1, 0.05, 0.2, -0.05]
defenderArrWeighting =  [0.25, 0.25, 0.15, 0.1, 0.15, 0.15, -0.05]
goalkeeperArrWeighting =  [0.4, 0.3, -0.15, 0.2, 0.2, 0.2, -0.15]

while True:
    userdecision1 = input("What would you like to do? \na) Add a new player \nc) Change player data \nf) Find best player for position \nr) remove player from list \ns) Save and Exit \n==> ")
    if userdecision1 == "a":
        playerAppend = input("Enter the name of the player you wish to add: ")
        playerPosition = str(input("Enter their position \na) Striker \nb) Midfielder \nc) Defender \nd) Goalkeeper \n ==> "))
        playerPosition = playerPosition.lower()
        playerPosition = positionFinder(playerPosition)
        playerAppend = playerAppend.upper()
        print(playerAppend)
        print(playerPosition)
        if (playerAppend not in file_path):
            appendPlayersList(playerAppend, playerPosition)
        elif (playerPosition == "None"):
            print("Entered invalid position. Try again!")
        elif (playerAppend in file_path) and (playerPosition in file_path):
            print("Player already in file! Try again.")
        else:
            print("Something went wrong! Try again.")
    if userdecision1 == "c":
        print("no!")
    if userdecision1 == "r":
        playerAppend = input("Enter the name of the player you wish to remove: ")
        playerAppend = playerAppend.upper()
        playerPosition = str(input("Enter their position \na) Striker \nb) Midfielder \nc) Defender \nd) Goalkeeper \n ==> "))
        playerPosition = playerPosition.lower()
        playerPosition = positionFinder(playerPosition)
        row_to_remove = playerRemove(playerAppend, playerPosition)
        if 0 <= row_to_remove < listLength(playerPosition):
            del data_list[row_to_remove]
            saveList(file_path, data_list)
        else:
            print("Invalid index.")
    if userdecision1 == "s":
        saveList(file_path, data_list)
        print("List saved. Exiting.")
        break

