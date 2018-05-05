import os
import csv

path_1 = "C:\\Users\\mattm\\python-challenge\\PyBoss\\Resources\\raw_data\\employee_data1.csv"
path_2 = "C:\\Users\\mattm\\python-challenge\\PyBoss\\Resources\\raw_data\\employee_data2.csv"

new_employee_data = []

with open(path_1) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        names = row["Name"].split(" ")
        first_names = names[0]
        last_names = names[1]

        dates = row["DOB"].split("-")
        month = dates[1]
        day = dates[2]
        year = dates[0]
        DOB_new = month + "/" + day + "/" + year

        SSN_old = row["SSN"].split("-")
        SSN_new = "***-***-" + SSN_old[2]

        state = row["State"]
        state_abbrev = {
            'Alabama': 'AL',
            'Alaska': 'AK',
            'Arizona': 'AZ',
            'Arkansas': 'AR',
            'California': 'CA',
            'Colorado': 'CO',
            'Connecticut': 'CT',
            'Delaware': 'DE',
            'Florida': 'FL',
            'Georgia': 'GA',
            'Hawaii': 'HI',
            'Idaho': 'ID',
            'Illinois': 'IL',
            'Indiana': 'IN',
            'Iowa': 'IA',
            'Kansas': 'KS',
            'Kentucky': 'KY',
            'Louisiana': 'LA',
            'Maine': 'ME',
            'Maryland': 'MD',
            'Massachusetts': 'MA',
            'Michigan': 'MI',
            'Minnesota': 'MN',
            'Mississippi': 'MS',
            'Missouri': 'MO',
            'Montana': 'MT',
            'Nebraska': 'NE',
            'Nevada': 'NV',
            'New Hampshire': 'NH',
            'New Jersey': 'NJ',
            'New Mexico': 'NM',
            'New York': 'NY',
            'North Carolina': 'NC',
            'North Dakota': 'ND',
            'Ohio': 'OH',
            'Oklahoma': 'OK',
            'Oregon': 'OR',
            'Pennsylvania': 'PA',
            'Rhode Island': 'RI',
            'South Carolina': 'SC',
            'South Dakota': 'SD',
            'Tennessee': 'TN',
            'Texas': 'TX',
            'Utah': 'UT',
            'Vermont': 'VT',
            'Virginia': 'VA',
            'Washington': 'WA',
            'West Virginia': 'WV',
            'Wisconsin': 'WI',
            'Wyoming': 'WY',
        }
        for key, value in state_abbrev.items():
            if state == key:
                State_new = value

        new_employee_data.append(
            {   "Emp ID": row["Emp ID"],
                "First Name": first_names,
                "Last Name": last_names,
                "DOB": DOB_new,
                "SSN": SSN_new,
                "State": State_new
            }
        )

_, filename = os.path.split(path_1)

csvpath = "C:\\Users\\mattm\\python-challenge\\PyBoss\\output\\new_data.csv"
with open(csvpath, "w") as csvfile:
    fieldnames = ["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(new_employee_data)