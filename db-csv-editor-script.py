import csv
import os


# file_directory = "C:/Users/raddo/Desktop/RAM TIREX/Websites/bricksneakers/"
# file_path = os.path.join(file_directory, old_db_filename)


# ================================

old_db_filename = "wc-customers.csv"
new_db_filename = "wc-customers.csv"

# Get the absolute path of the directory containing the script
script_directory = os.path.dirname(os.path.abspath(__file__))
print(script_directory)

relative_file_path = os.path.join(script_directory, old_db_filename)

print("Relative path of the file:", relative_file_path)

# ================================


# count = 0

# with open(file_path, 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for row in csv_reader:
#         # Access individual values using index
#         count += 1

#         # if row[0] != " ":
#             # print(row)



#         if count > 10:
#             break
