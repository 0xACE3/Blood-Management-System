"""This is a Blood Bank Management System
Donor ID, Date, Name, Blood group, Gender, age: 18-75, address, phone number, blood bank, 350-450ml of blood drawn
blood type: A+, A-, B+, B-, AB+, AB-, O+, O-
"""
import time
import csv
from rgbprint import *
import pandas as pd

csvfile = 'data.csv'


class BMS:
    fieldnames = ["Donor ID",
                  "First Name",
                  "Last Name",
                  "Blood Group",
                  "Date",
                  "Age",
                  "Gender",
                  "Phone Number"]
    __epoch = 1650000000
    __blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

    def __init__(self,
                 name: str,
                 blood_group: str,
                 age: int,
                 gender: str,
                 phone_no: str):
        # validation of correct input
        assert 60 >= age >= 18, f"Age {age} should be between 18 and 60 years to be eligible."
        assert gender.lower() == "male" or gender.lower() == "female", f"Gender {gender} does not exist."
        assert blood_group in BMS.__blood_groups, f"{blood_group} is a wrong blood type."
        assert 9 <= len(phone_no) <= 11, f"{phone_no} is not a real phone number."

        self.__first_name = name.split()[0].title()
        self.__last_name = name.split()[1].title()

        self.name = f"{self.__first_name} {self.__last_name}"
        self.gender = gender
        self.age = age
        self.blood_group = blood_group
        self.phone_no = phone_no
        self.__date = time.strftime(f"%d-%m-%y")
        self.donor_id = BMS.__unique_id()

    @classmethod
    def __unique_id(cls) -> int:
        id = int(time.time() - cls.__epoch)
        id <<= 2
        return id

    @staticmethod
    def create_csv(file):
        csvfile = file
        with open(csvfile, 'w', newline="") as f:
            writer = csv.DictWriter(f, fieldnames=BMS.fieldnames)
            writer.writeheader()

    def insert_data(self):
        with open(csvfile, "a", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=BMS.fieldnames)
            writer.writerow({BMS.fieldnames[0]: self.donor_id,
                             BMS.fieldnames[1]: self.__first_name,
                             BMS.fieldnames[2]: self.__last_name,
                             BMS.fieldnames[3]: self.blood_group,
                             BMS.fieldnames[4]: self.__date,
                             BMS.fieldnames[5]: self.age,
                             BMS.fieldnames[6]: self.gender,
                             BMS.fieldnames[7]: self.phone_no,
                             })

    @staticmethod
    def show_all_data():

        with open(csvfile, newline='') as f:
            reader = csv.reader(f)
            print("\n\n" + f"{Fore.GREEN}+ {Fore.RED}Blood {Fore.WHITE}Management {Fore.CYAN}System {Fore.GREEN}+{Fore.RESET}".center(195, f"—") + "\n\n")
            id = 0
            for row in reader:
                print(
                    '{color}{id:<5} {color1}{:<12} {color2}{:<15} {color2}{:<12} {color3}{:^15} {color4}{:^15} {color5}{:<8} {color6}{:<10} {color7}{:^10}'.format(
                        *row,
                        id=id,
                        color=Fore.WHITE,
                        color1=Fore.GREEN,
                        color2=Fore.LIGHT_YELLOW,
                        color3=Fore.LIGHT_RED,
                        color4=Fore.CYAN,
                        color5=Fore.LIGHT_MAGENTA,
                        color6=Fore.YELLOW,
                        color7=Fore.LIGHT_GRAY))
                id += 1
    @staticmethod
    def update_row(row: int, fieldname: str, replacement):
        df = pd.read_csv(csvfile)
        df.loc[row, fieldname] = replacement
        df.to_csv(csvfile, index=False)
        print(df)
    @staticmethod
    def delete_row(fname, value):
        df = pd.read_csv(csvfile)
        df.set_index(fname, inplace=True)
        df = df.drop(value)
        df.to_csv(csvfile, index=False)
        print(df)



