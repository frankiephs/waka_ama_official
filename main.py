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
target_year_path = fr.file_read_c.find_year_path(parent_path,ask_year,"WakaNats")
files_list = fr.file_read_c.return_files(target_year_path)

# find specific keyword only
ask_keyword = input("filter keyword >> ")
filtered_files_list = []
for file in files_list:
    if ask_keyword in file.lower():
        filtered_files_list.append(file)
    else:
        continue
print(len(filtered_files_list), ask_keyword, "found")

# get contents
filtered_files_contents = []
for i in filtered_files_list:
    filepath = f"{target_year_path}/{i}"
    file_contents = fr.file_read_c.return_content(filepath,i)
    filtered_files_contents.append(file_contents)
    


# score the files



