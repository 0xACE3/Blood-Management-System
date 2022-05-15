import sys

from texts import *
from database import BMS
import os
import re


def main():

    print(main_text + menu_text)
    response = input("\n>>>  ")
    if response.lower() == "q" :
        sys.exit()
    if response.isdecimal():
        if response.strip() == "1":
            filename = input(option_oneNote + filename_text)

            if not re.search(r'(?<=[a-zA-Z\d_.])(\.csv)', filename):
                filename = f'{filename}.csv'

            if os.path.exists(filename):
                add_data()

            else:
                BMS.create_csv(filename)
                add_data()

        if response.strip() == "2":
            BMS.show_all_data()
            back = input("\nEnter 0 to go back: ")
            if back.strip() == "0": main()
            else : sys.exit()

        if response.strip() == "3":
            delete_row()

        if response.strip() == "4":
            update_data()

    else:
        print(main_else_text)


def add_data():
    flag = True
    while flag:

        name = input(name_text)
        blood_type = input(blood_type_text)
        age = int(input(age_text))
        sex = input(gender_text)
        phone_number = input(phoneNo_text)

        try:
            data = BMS(name.lower().strip(),
                       blood_type,
                       age,
                       sex.lower().strip(),
                       phone_number.strip())
            data.insert_data()
        except PermissionError:
            print(perm_error_text)
        except AssertionError:
            print(assert_err_text)

        new_entry = input("Another entry? (y/n): ")
        if new_entry.lower().strip() == "y":
            continue

        elif new_entry.lower().strip() == "n":
            flag = False

        else:
            print(add_else_text)
            continue

    return main()


def update_data():
    print(f'Current Field Names: {BMS.fieldnames}')
    while True:

        row = int(input(row_text))
        field_name = input(fieldname_text)
        replacement = input(replacement_text)

        BMS.update_row(row, field_name.strip(), replacement)
        repl_again = input("\nAnother replacement? (y/n): ")
        if repl_again.lower().strip() == "y":
            continue

        elif repl_again.lower().strip() == "n":
            break

        else:
            print(add_else_text)
            continue

    return main()


def delete_row():
    print(f'Current Field Names: {BMS.fieldnames}')
    while True:
        fdname = input(fieldname_text)
        value = input(value_text)

        if fdname == BMS.fieldnames[5]:
            value = int(value)
            
        del_row = BMS.delete_row(fdname, value)
        del_again = input("\nWant to delete another row? (y/n): ")

        if del_again.lower().strip() == "y":
            continue

        elif del_again.lower().strip() == "n":
            break

        else:
            print(add_else_text)
            continue

    return main()


if __name__ == "__main__":
    main()
