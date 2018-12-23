from Himalaya.input import *
from Himalaya.data_modules import *


# class Entity:
#
#     def __init__(self, name, classification, residence):
#         self.name = name
#         self.classification = classification
#         self.residence = residence
#         self.relationship = {}


def entity_new():  # Function: Create new entity entry

    with Database(database_name) as db:

        while True:

            print("\n=== Create New Entity ===\n")

            info_tuple = entity_info_collect()
            print("Adding entity information into database...")
            cursor = db.cursor
            cursor.execute("INSERT INTO entities (entity_name, tax_classification, entity_residence) "
                           "VALUES (?, ?, ?)", info_tuple)
            print("{} record updated".format(cursor.rowcount))
            cursor.connection.commit()

            # Asking for recurring updates
            continue_add = input_select("\nAdd another entity (Y/N)?: ", "Y", "N")
            if continue_add.upper() == "N":
                break
            else:
                continue


def entity_get_id(e_name):

        with Database(database_name) as db:

            select_sql = "SELECT entity_id FROM entities WHERE entity_name = ? "
            entity_id = db.query(select_sql, (e_name, )).fetchone()[0]
            return entity_id


def entity_info():  # Function: retrieve entity information

    print("\n=== Entity Info Query/Update ===\n")

    while True:

        e_name = entity_select("Please select the entity to query / update")

        if e_name.upper() == "RETURN":
            break

        else:
            with Database(database_name) as db:

                record = db.query("SELECT entity_name,tax_classification, entity_residence "
                                  "FROM entities WHERE entity_name = ?", (e_name,)).fetchone()

                print("Legal Name: {}".format(record[0]))
                print("US Tax Classification: {}".format(record[1]))
                print("Tax Residence: {}".format(record[2]))

                # Sub-function: update entity information
                update_confirmation = input_select("Update information (Y/N)?: ", "Y", "N")

                if update_confirmation.upper() == "Y":
                    print("\n === Update === \n")

                    info_tuple = entity_info_collect()
                    update_tuple = (*info_tuple, e_name)
                    cursor = db.cursor
                    cursor.execute("UPDATE entities SET entity_name = ?, tax_classification = ?, entity_residence = ? "
                                   "WHERE entity_name = ?", update_tuple)
                    cursor.connection.commit()
                    print("Record updated")
                    break
                else:
                    continue


def entity_remove():

    print("\n=== Entity Record Removal ====\n")

    while True:

        e_name = entity_select("Please indicate the entity to remove")

        if e_name.upper() == "RETURN":
            break
        else:
            with Database(database_name) as db:

                db.query("DELETE FROM entities WHERE entity_name = ?", (e_name, ))
                print("Record removed for {}".format(e_name))
            break
