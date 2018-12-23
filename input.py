# This doc provides supplemental modules for general usage
from Himalaya.data_modules import *
from Himalaya import entity


def entity_list():  # Function: retrieve list of entity name as a dictionary

    with Database(database_name) as db:

        sql = str("SELECT entity_id, entity_name FROM entities ORDER BY entity_name")
        temp_record = db.query(sql).fetchall()
        temp_dict = {}
        temp_counter = 0
        for i in temp_record:
            temp_counter += 1
            temp_dict[str(temp_counter)] = i[1]
        return temp_dict


def percent_input(prompt):
    while True:
        percentage = float(input("{} (0-100): ".format(prompt))) / 100
        if 1 >= percentage >= 0:
            right_percent = percentage
            break
        else:
            print("{} is not a valid percentage".format(percentage * 100))
    return right_percent


def input_select(prompt, *args):  # Function: to confirm if input is either Y or N.

    while True:
        selection = str(input(prompt))
        if selection.upper() in [*args]:
            break
        else:
            print("{} is not a valid selection".format(selection))
    return selection


def entity_select(prompt):

    e_list = entity_list()

    while True:
        entity_input = str(input("{}\n(Commands: \"List\", \"Return\"):".format(prompt)))
        if entity_input.upper() == "LIST":
            for i in e_list:
                print('[{}] {}'.format(i, e_list[i]))
            continue
        elif entity_input in list(e_list.keys()):
            e_name = e_list[entity_input]
            break
        elif (entity_input in e_list.values()) or (entity_input.upper() == "RETURN"):
            e_name = entity_input
            break
        else:
            print("No such entity or invalid command")
            new_entity = input_select("Would you like to create a new entity (Y/N)", "Y", "N")
            if new_entity.upper() == "Y":
                entity.entity_new()
            continue
    return e_name


def entity_info_collect():  # Collect entity information

    entity_class = {"1": "Corporation",
                    "2": "Partnership",
                    "3": "Disregarded Entity"}

    while True:  # Entity information entering loop

        e_name = str(input("Please enter the entity's legal name: "))
        if e_name == "":
            print("Entity name cannot be empty")
            continue

        print("Please select the entity's US entity tax classification: ".format(e_name))
        for i in entity_class:
            print("[{}]: {}". format(i, entity_class[i]))

        while True:
            select_classification = str(input("Classification (1/2/3): "))
            if select_classification in list(entity_class.keys()):
                e_form = entity_class[select_classification]
                break
            else:
                print("{} is not a valid selection".format(select_classification))

        e_residence = str(input("Please enter the entity's tax residence: "))
        # To add residence info validation

        # Entity information review
        print("\n=== Review ===")
        print("Legal Name: {}\n"
              "US Tax Classification: {}\n"
              "Tax Residence: {}\n".format(e_name, e_form, e_residence))

        entity_info_confirm = input_select("Confirm? (Y/N): ", "Y", "N")
        if entity_info_confirm.upper() == "Y":
            break
        else:
            print("\n=== re-entering information ===\n")
            continue

    info_tuple = (e_name, e_form, e_residence)
    return info_tuple
