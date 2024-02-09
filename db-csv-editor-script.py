import csv
import os
import re
import random


fake_names = '''
Carol	MacLeod
Chloe	Rees
Julian	Dickens
Max	Pullman
Jack	Newman
Harry	Hodges
Alexandra	Taylor
Austin	Oliver
Tim	Hudson
Brandon	Ferguson
Lauren	Davidson
Yvonne	Rees
Jack	King
Piers	Robertson
Jessica	Quinn
Kevin	Gill
Mary	Robertson
Sally	Murray
Ella	Rampling
Yvonne	Lewis'''.split(" ")[0]

fake_names = re.split("\t|\n", fake_names)[1:]

print(fake_names)


script_directory = os.path.dirname(os.path.abspath(__file__))

# this database is only for testing, it is not a real db
old_db_filename = "wc-customers.csv"
old_rel_file_path = os.path.join(script_directory, old_db_filename)
new_db_filename = "db-test.csv"
new_rel_file_path = os.path.join(script_directory, new_db_filename)

output_file = open(new_rel_file_path, "w")


# count = 0  # for testing

with open(old_rel_file_path, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)

    has_empty_header = True
    for row in csv_reader:
        if has_empty_header:
            has_empty_header = False
            output_file.write("Customer ID,First Name,Last Name,Email,Accepts Email Marketing,Default Address Company,Default Address Address1,Default Address Address2,Default Address City,Default Address Province Code,Default Address Country Code,Default Address Zip,Default Address Phone,Phone,Accepts SMS Marketing,Total Spent,Total Orders,Note,Tax Exempt,Tags\n")
#                   Customer ID
#                   First Name
#                   Last Name
#                   Email
#                   Accepts Email Marketing
#                   Default Address Company
#                   Default Address Address1
#                   Default Address Address2
#                   Default Address City
#                   Default Address Province Code
#                   Default Address Country Code
#                   Default Address Zip
#                   Default Address Phone
#                   Phone
#                   Accepts SMS Marketing
#                   Total Spent
#                   Total Orders
#                   Note
#                   Tax Exempt
#                   Tags

        # name correction
        name = row[0].split(" ")
        first_name = name[0]
        last_name = " ".join(name[1:])
        email = row[4]

        # for testing
        # max_len = len(fake_names)-1
        # first_name = fake_names[random.randint(0, max_len)]
        # last_name = fake_names[random.randint(0, max_len)]
        # email = f"{last_name.lower()}.{first_name.lower()}@clienteditor.csv"


        # changing the order will change the resulting file, remember to match the header line
        output_file.write(" ,")  # Customer ID
        output_file.write(f"{first_name},")  # First name
        output_file.write(f"{last_name},")  # Last name
        output_file.write(f"{email},")  # Email
        output_file.write("yes,")  # Accepts Email Marketing
        output_file.write(",")  # Default Address Company
        output_file.write(",")  # Default Address Address1
        output_file.write(",")  # Default Address Address2
        output_file.write(f"{row[9]},")  # Default Address City
        output_file.write(f"{row[10]},")  # Default Address Province Code
        output_file.write(f"{row[8]},")  # Default Address Country Code
        output_file.write(f"{row[11]},")  # Default Address Zip
        output_file.write(",")  # Default Address Phone
        output_file.write(",")  # Phone
        output_file.write("yes,")  # Accepts SMS Marketing
        output_file.write(f"{row[6]},")  # Total Spent
        output_file.write(f"{row[5]},")  # Total Orders
        output_file.write(",")  # Note
        output_file.write("no,")  # Tax Exempt
        output_file.write(f'"Last Active {row[2]},Sign Up {row[3]}",')  # Tags

        output_file.write("\n")
        
        # count += 1  # for testing
        # if count > 9:
        #     break

output_file.close()
