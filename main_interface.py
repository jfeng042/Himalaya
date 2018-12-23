from Himalaya.entity import *

print("\n**** Himalaya Program Test v1.0 ****")

available_command = {"1": "New Entity",
                     "2": "Entity Information Query/Update",
                     "3": "Remove Entity",
                     "4": "Database Settings",
                     "5": "Quit"}

create_database()

while True:

    print("\n=== Main Interface ===\n")
    print("Please select from the following commands:")

    for command in available_command:
        print("[{}]: {}".format(command, available_command[command]))

    selected_command = str(input("Select Command: "))

    if selected_command.upper() == "1" or selected_command == available_command["1"].upper():
        entity_new()
    elif selected_command.upper() == "2" or selected_command == available_command["2"].upper():
        entity_info()
    elif selected_command.upper() == "3" or selected_command == available_command["3"].upper():
        entity_remove()
    elif selected_command.upper() == "4" or selected_command == available_command["4"].upper():
        print("To be developed")
    elif selected_command.upper() == "5" or selected_command == available_command["5"].upper():
        break
    else:
        print("Invalid command")








