"""This is a Blood Bank Management System
Donor ID, Date, Name, Blood group, Gender, age: 18-75, address, phone number, blood bank, 350-450ml of blood drawn
blood type: A+, A-, B+, B-, AB+, AB-, O+, O-
"""
from uuid import uuid4
from typing import Optional

from supported import BLOOD_GROUP_LITERAL, GENERAL_LITERAL
from colored.Fore import Fore

import os
import re
import time
import pandas as pd


class BMS:
    fieldnames = ["Donor ID",
                    "Date",
                    "First Name",
                    "Last Name",
                    "Blood Group",
                    "Age",
                    "Gender",
                    "Phone Number"]

    def __init__(self,
                 first_name: str,
                 last_name: str,
                 blood_group: BLOOD_GROUP_LITERAL,
                 age: int,
                 gender: GENERAL_LITERAL,
                 phone_no: Optional[str] = None):

        # validation of correct input
        assert 60 >= age >= 18, f"Age {age} should be between 18 and 60 years to be eligible."

        self.donor_id = uuid4().fields[1]
        self.date = time.strftime(f"%d-%m-%y")
        self.first_name = first_name
        self.last_name = last_name
        self.blood_group = blood_group
        self.age = age
        self.gender = gender
        self.phone_no = validate_phone_no(phone_no) or None
        self.filename = None

    def save_to_csv(self, data_frame: pd.DataFrame,
                    filename="bms_data.csv"):

        self.filename = filename
        if not os.path.exists("./data"):
            os.mkdir('./data')

        data_frame.to_csv(f"./data/{self.filename}")

    def insert_data(self):
        df = pd.read_csv(f"./data/{self.filename}")
        data_frame = dict(zip(BMS.fieldnames, [x for x in self.__dict__.values()]))
        df.append(data_frame, ignore_index=True)

    def show_all_data(self):
        df = pd.read_csv(f"./data/{self.filename}")
        print(df)

    def update_full_row(self, row_index: int, *replacement):
        df = pd.read_csv(f"./data/{self.filename}")
        df.loc[row_index, [x for x in self.__dict__.keys()]] = replacement
        print(df)

    def delete_row(self, row_id: int):
        df = pd.read_csv(f"./data/{self.filename}")
        df = df.drop(row_id)
        print(df)

    @staticmethod
    def validate_phone_no(phone_no):

        regex = re.compile(r"""( #regex for any country phone numbers
        \+
        (\d{1,3} | \(\d{1,3}\))?        #countrycode
        (\s | - | \.)?                  #seprator
        (\d{1,3} | \(\d{1,3}\))         #areacode
        (\s | - | \.)?                  #seperator
        (\d{3,4})                       #first 3 digits
        (\s | - | \.)?                  #seperator
        (\d{4})                         #last 4 digits
        )""", re.VERBOSE | re.DOTALL)

        try:
            if regex.search(phone_no):
                return phone_no
        except Exception as e:
            return None

