import file_read as fr
import gui
import scoring
import csv_export

# get years
ask_parent_path = input("Type your parent folder >> ")
parent_path = ask_parent_path
print(fr.file_read_c.return_years(parent_path))


# get all the files
ask_year = int(input("Type your year >> "))
target_year = fr.file_read_c.find_year_path(parent_path,ask_year,"WakaNats")
files_list = fr.file_read_c.return_files(target_year)

# find specific keyword only
ask_keyword = input("filter keyword >> ")
filtered_files_list = []
for file in files_list:
    if ask_keyword in file.lower():
        filtered_files_list.append(file)
    else:
        continue
print(len(filtered_files_list), ask_keyword, "found")



