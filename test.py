import pandas as pd
import os
import re

name_dict = {
            'Name': ['a','b','c','d'],
            'Score': [90,80,95,20]
}
def validate_phone_no(phone_no):

        regex = re.compile(r"""( #regex for any country phone numbers
        \+
        (\d{1,3} | \(\d{1,3}\))?    #countrycode
        (\s | - | \.)?                  #seprator
        (\d{1,3} | \(\d{1,3}\))       #areacode
        (\s | - | \.)?                  #seperator
        (\d{3,4})                         #first 3 digits
        (\s | - | \.)?                  #seperator
        (\d{4})                         #last 4 digits
        )""", re.VERBOSE | re.DOTALL)
        try:
            if regex.search(phone_no):
                return phone_no
        except Exception:
            return None

a=validate_phone_no("+1 650 513 0514")
print(a)


# df = pd.DataFrame(name_dict)
# print(df.append({"Name": 'k', 'Score': 10}, ignore_index=True))

# class BMS:
#     fieldnames = ["Donor ID",
#                     "Date",
#                     "First Name",
#                     "Last Name",
#                     "Blood Group",
#                     "Age",
#                     "Gender",
#                     "Phone Number"]
#
#     def __init__(self,
#                  first_name: str,
#                  last_name: str,
#                  blood_group,
#                  age: int,
#                  gender ,
#                  phone_no=None):
#         self.donor_id = 1122
#         self.date = "12-08-2022"
#         self.first_name = first_name
#         self.last_name = last_name
#         self.blood_group = blood_group
#         self.age = age
#         self.gender = gender
#         self.phone_no = phone_no
#         self.filename = None
#
# a = BMS('john', 'cena', 'A+', 23, 'male')

# a = dict(zip(BMS.fieldnames, [x for x in a.__dict__.values()]))
# print(a)
#
#
#
# print(1+ (2, 3))

